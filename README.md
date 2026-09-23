# ONEHART

Storefront for ONEHART — elevated streetwear, Drop 001 "After Dark".

## Running locally

The site is a single self-contained page. Because it loads local assets, serve it
over HTTP rather than opening the file directly:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Structure

| Path | Purpose |
| --- | --- |
| `index.html` | The entire site — hero, rack, Drop 001 grid, PDP, bag, footer |
| `support.js` | Runtime that renders the page |
| `image-slot.js` | Drag-and-drop image placeholder component |
| `brand/wordmark-v3.png` | ONEHART wordmark (header, hero reveal, footer) |
| `brand/tile-bg.jpg` | Product tile backdrop |
| `tees/tee-1…6.png` | The six garment cutouts |
| `uploads/` | Hero background video |

## Products

Defined in the `catalog()` method inside `index.html`:
name, price in rupees, and image path.

| # | Piece | Price |
| --- | --- | --- |
| 01 | Positive Poison | ₹999 |
| 02 | Scream | ₹899 |
| 03 | Cowboy | ₹949 |
| 04 | Rawr | ₹899 |
| 05 | Lunatic | ₹999 |
| 06 | All We Need Is Money | ₹949 |

## Checkout (Shopify)

Bag → **Checkout** redirects straight to Shopify's hosted checkout using a cart
permalink: `https://z91v0v-vs.myshopify.com/cart/<variantId>:<qty>,...`.
No API token or environment variables are needed.

Variant IDs live in `variants()` in `index.html` (same order as `catalog()`, keyed by
S/M/L/XL). If you add a product or size in Shopify, add its variant ID there.

`api/checkout.js` (Storefront API version) is kept for later but is no longer called.

## Supabase (optional)

`supabase/schema.sql` creates one table, `checkout_sessions`, written server-side
with the service role key. Products, customers and orders stay in Shopify.

## Environment variables

See `.env.example`. Locally: copy to `.env.local` and run `npx vercel dev`
(checkout needs the `/api` route, so a plain static server won't work for it).

## Contact

Footer: +91 99940 13477 (tel:), onehart.clothing@gmail.com (mailto:),
Instagram https://www.instagram.com/onehart.clothing/

## Deploying

Vercel: import the repo, no build command, output directory = root.
Add the env vars in Project Settings → Environment Variables, then redeploy.
