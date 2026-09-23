-- ONEHART — Supabase schema
-- Shopify owns products, variants, inventory, customers, checkout and orders.
-- Supabase only records checkout sessions started from this site (for
-- conversion / abandoned-bag tracking), which Shopify does not expose to a headless storefront.
-- Run once in Supabase → SQL Editor.

create table if not exists public.checkout_sessions (
  id              uuid primary key default gen_random_uuid(),
  created_at      timestamptz not null default now(),
  shopify_cart_id text not null unique,
  checkout_url    text not null,
  lines           jsonb not null,           -- [{ handle, size, quantity }]
  item_count      integer not null check (item_count > 0),
  subtotal        numeric(12, 2),
  currency        text,
  user_agent      text
);

create index if not exists checkout_sessions_created_at_idx
  on public.checkout_sessions (created_at desc);

-- RLS on with no policies: the anon/public key can neither read nor write.
-- Only the server (service role key in /api/checkout) inserts rows.
alter table public.checkout_sessions enable row level security;
