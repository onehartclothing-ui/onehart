// Vercel serverless function: turns the bag into a Shopify cart and returns its checkout URL.
// Credentials are read from environment variables and never reach the browser.

const API_VERSION = '2026-07';
const SIZES = ['S', 'M', 'L', 'XL'];
const HANDLE_RE = /^[a-z0-9][a-z0-9-]{0,99}$/;

const PRODUCT_QUERY = `query Variants($handle: String!) {
  product(handle: $handle) {
    variants(first: 100) {
      nodes { id availableForSale selectedOptions { name value } }
    }
  }
}`;

const CART_CREATE = `mutation CartCreate($input: CartInput!) {
  cartCreate(input: $input) {
    cart { id checkoutUrl totalQuantity cost { subtotalAmount { amount currencyCode } } }
    userErrors { field message }
  }
}`;

async function storefront(domain, token, query, variables) {
  const res = await fetch(`https://${domain}/api/${API_VERSION}/graphql.json`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Shopify-Storefront-Access-Token': token },
    body: JSON.stringify({ query, variables })
  });
  if (!res.ok) throw new Error(`Shopify responded ${res.status}`);
  const json = await res.json();
  if (json.errors && json.errors.length) throw new Error(json.errors.map((e) => e.message).join('; '));
  return json.data;
}

function validate(body) {
  const lines = body && Array.isArray(body.lines) ? body.lines : null;
  if (!lines || lines.length === 0 || lines.length > 50) return null;
  for (const l of lines) {
    if (!l || typeof l.handle !== 'string' || !HANDLE_RE.test(l.handle)) return null;
    if (!SIZES.includes(l.size)) return null;
    if (!Number.isInteger(l.quantity) || l.quantity < 1 || l.quantity > 20) return null;
  }
  return lines;
}

async function logSession(cart, lines, userAgent) {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) return;
  const sub = cart.cost && cart.cost.subtotalAmount;
  try {
    await fetch(`${url.replace(/\/$/, '')}/rest/v1/checkout_sessions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        apikey: key,
        Authorization: `Bearer ${key}`,
        Prefer: 'return=minimal'
      },
      body: JSON.stringify({
        shopify_cart_id: cart.id,
        checkout_url: cart.checkoutUrl,
        lines,
        item_count: cart.totalQuantity,
        subtotal: sub ? Number(sub.amount) : null,
        currency: sub ? sub.currencyCode : null,
        user_agent: userAgent ? String(userAgent).slice(0, 300) : null
      }),
      signal: AbortSignal.timeout(2500)
    });
  } catch (e) {
    console.error('Supabase log failed:', e.message);
  }
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed.' });
  }

  const domain = process.env.SHOPIFY_STORE_DOMAIN;
  const token = process.env.SHOPIFY_STOREFRONT_ACCESS_TOKEN;
  if (!domain || !token) {
    console.error('Missing SHOPIFY_STORE_DOMAIN or SHOPIFY_STOREFRONT_ACCESS_TOKEN');
    return res.status(503).json({ error: 'Checkout is not configured yet.' });
  }

  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = null; } }
  const lines = validate(body);
  if (!lines) return res.status(400).json({ error: 'Your bag looks invalid. Please refresh and try again.' });

  try {
    const handles = [...new Set(lines.map((l) => l.handle))];
    const products = {};
    await Promise.all(handles.map(async (h) => {
      const data = await storefront(domain, token, PRODUCT_QUERY, { handle: h });
      products[h] = data.product;
    }));

    const merged = new Map();
    for (const l of lines) {
      const product = products[l.handle];
      if (!product) return res.status(409).json({ error: `A piece in your bag is no longer available (${l.handle}).` });
      const variant = product.variants.nodes.find((v) =>
        v.selectedOptions.some((o) => /size/i.test(o.name) && o.value.trim().toUpperCase() === l.size));
      if (!variant) return res.status(409).json({ error: `Size ${l.size} isn't available for ${l.handle}.` });
      if (!variant.availableForSale) return res.status(409).json({ error: `Size ${l.size} of ${l.handle} is sold out.` });
      merged.set(variant.id, (merged.get(variant.id) || 0) + l.quantity);
    }

    const data = await storefront(domain, token, CART_CREATE, {
      input: { lines: [...merged].map(([merchandiseId, quantity]) => ({ merchandiseId, quantity })) }
    });
    const { cart, userErrors } = data.cartCreate;
    if (userErrors && userErrors.length) return res.status(409).json({ error: userErrors[0].message });
    if (!cart || !cart.checkoutUrl) throw new Error('No checkout URL returned');

    await logSession(cart, lines, req.headers['user-agent']);
    return res.status(200).json({ checkoutUrl: cart.checkoutUrl });
  } catch (e) {
    console.error('Checkout error:', e.message);
    return res.status(502).json({ error: 'Checkout is unavailable right now. Please try again.' });
  }
}
