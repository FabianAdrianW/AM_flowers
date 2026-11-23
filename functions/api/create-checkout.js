// Cloudflare Pages Function: POST /api/create-checkout
// Tworzy sesję Stripe Checkout. Ceny liczone wyłącznie po stronie serwera z data/products.json.
// Zmienna środowiskowa: STRIPE_SECRET_KEY (najpierw sk_test_…, po testach klucz produkcyjny).
import catalog from "../../data/products.json";

const json = (status, body) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });

export async function onRequestPost({ request, env }) {
  const key = env.STRIPE_SECRET_KEY;
  if (!key) return json(503, { error: "Płatności online nie są jeszcze skonfigurowane." });

  let body;
  try { body = await request.json(); } catch { return json(400, { error: "Nieprawidłowe dane." }); }
  const items = Array.isArray(body.items) ? body.items.slice(0, 30) : [];
  const c = body.customer || {};
  if (!items.length) return json(400, { error: "Koszyk jest pusty." });
  const phone = String(c.telefon || "").replace(/\D/g, "");
  if (phone.length < 9) return json(400, { error: "Brak numeru telefonu." });

  const form = new URLSearchParams();
  const summary = [];
  let i = 0;
  const line = (name, amount, qty, desc) => {
    form.append(`line_items[${i}][quantity]`, String(qty));
    form.append(`line_items[${i}][price_data][currency]`, "pln");
    form.append(`line_items[${i}][price_data][unit_amount]`, String(Math.round(amount * 100)));
    form.append(`line_items[${i}][price_data][product_data][name]`, name);
    if (desc) form.append(`line_items[${i}][price_data][product_data][description]`, desc);
    i++;
  };
  for (const it of items) {
    const p = catalog.products.find((x) => x.id === it.id);
    if (!p) return json(400, { error: "Nieznany produkt." });
    if (p.from) return json(400, { error: "Ta pozycja jest wyceniana indywidualnie." });
    const size = catalog.sizes.find((s) => s.id === it.size) || catalog.sizes.find((s) => s.id === "M");
    const qty = Math.max(1, Math.min(20, parseInt(it.q, 10) || 1));
    const price = p.price + (p.cat === "bukiety" ? size.delta : 0);
    const card = String(it.card || "").slice(0, 160);
    line(`${p.name} (${size.name})`, price, qty, card ? `Bilecik: ${card}` : "");
    summary.push(`${qty}x ${p.name} ${size.id}${card ? ` [bilecik: ${card}]` : ""}`);
  }
  const delivery = c.odbior === "Dostawa";
  if (delivery) line("Dostawa", catalog.delivery_fee || 0, 1);

  const origin = new URL(request.url).origin;
  const cut = (s) => String(s || "").slice(0, 490);
  form.append("mode", "payment");
  form.append("locale", "pl");
  ["blik", "card", "p24"].forEach((m, k) => form.append(`payment_method_types[${k}]`, m));
  form.append("success_url", `${origin}/sukces.html?session_id={CHECKOUT_SESSION_ID}`);
  form.append("cancel_url", `${origin}/sklep.html?anulowano=1`);
  const meta = { zamowienie: summary.join(" | "), imie: c.imie, telefon: phone, termin: c.kiedy, odbior: c.odbior, adres: delivery ? c.adres : "", uwagi: c.uwagi };
  for (const [k, v] of Object.entries(meta)) form.append(`metadata[${k}]`, cut(v));
  form.append("payment_intent_data[description]", cut(`AM Flowers: ${summary.join(", ")}`));

  const r = await fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/x-www-form-urlencoded" },
    body: form,
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.url) { console.error(j); return json(502, { error: "Nie udało się utworzyć płatności." }); }
  return json(200, { url: j.url });
}
