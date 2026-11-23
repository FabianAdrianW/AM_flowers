// Cloudflare Pages Function: POST /api/order
// Przyjmuje zamówienie ze sklepu (form-urlencoded) i przekazuje je jako JSON
// do backendu formularzy (zmienna ORDER_WEBHOOK_URL, np. własny backend, n8n albo Make).
// Bez ORDER_WEBHOOK_URL zwraca 503, a sklep otwiera SMS z gotową treścią zamówienia.
const cors = (env, req) => {
  const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
  const origin = req.headers.get("Origin") || "";
  return allowed.includes(origin) ? { "Access-Control-Allow-Origin": origin, "Vary": "Origin" } : {};
};
// ALLOWED_ORIGINS: np. "https://kwiaciarniamalgorzata.pl" (szybkie zamówienie ze strony Kwiaciarni Małgorzata)
export function onRequestOptions({ request, env }) {
  return new Response(null, { status: 204, headers: { ...cors(env, request), "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type" } });
}

export async function onRequestPost({ request, env }) {
  const h = cors(env, request);
  const hook = env.ORDER_WEBHOOK_URL;
  if (!hook) return new Response("Not configured", { status: 503, headers: h });
  let data;
  try { data = Object.fromEntries(await request.formData()); } catch { return new Response("Bad request", { status: 400 }); }
  if (data.www) return new Response("OK", { status: 200, headers: h }); // honeypot
  delete data.www;
  const payload = { source: data["form-name"] === "zamowienie" ? "kwiaciarnia-malgorzata/szybkie-zamowienie" : "amflowers.pl/sklep", received: new Date().toISOString(), ...data };
  const r = await fetch(hook, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...(env.ORDER_WEBHOOK_TOKEN ? { Authorization: `Bearer ${env.ORDER_WEBHOOK_TOKEN}` } : {}) },
    body: JSON.stringify(payload),
  });
  return new Response(r.ok ? "OK" : "Upstream error", { status: r.ok ? 200 : 502, headers: h });
}
