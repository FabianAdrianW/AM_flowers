// Cloudflare Pages Function: POST /api/order
// Przyjmuje zamówienie ze sklepu (form-urlencoded) i przekazuje je jako JSON
// do backendu formularzy (zmienna ORDER_WEBHOOK_URL, np. własny backend, n8n albo Make).
// Bez ORDER_WEBHOOK_URL zwraca 503, a sklep otwiera SMS z gotową treścią zamówienia.
export async function onRequestPost({ request, env }) {
  const hook = env.ORDER_WEBHOOK_URL;
  if (!hook) return new Response("Not configured", { status: 503 });
  let data;
  try { data = Object.fromEntries(await request.formData()); } catch { return new Response("Bad request", { status: 400 }); }
  if (data.www) return new Response("OK", { status: 200 }); // honeypot
  delete data.www;
  const payload = { source: "amflowers.pl/sklep", received: new Date().toISOString(), ...data };
  const r = await fetch(hook, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...(env.ORDER_WEBHOOK_TOKEN ? { Authorization: `Bearer ${env.ORDER_WEBHOOK_TOKEN}` } : {}) },
    body: JSON.stringify(payload),
  });
  return new Response(r.ok ? "OK" : "Upstream error", { status: r.ok ? 200 : 502 });
}
