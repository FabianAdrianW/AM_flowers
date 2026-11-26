# AM Flowers, Oława

Strona i sklep AM Flowers (dawniej Kwiaciarnia Małgorzata): mama i córka, pracownia przy ul. J. Iwaszkiewicza 137B, sklep online i kwiatomat 24/7 przy Intermarché (ul. ks. prał. F. Kutrowskiego 29).

Statyczny HTML/CSS/JS bez kroku budowania + dwie funkcje Cloudflare Pages.

## Co jest w repo

| Plik / folder | Co to |
|---|---|
| `index.html` | Strona główna: hero z wideo, historia, sklep, kalendarz okazji, oferta (5 usług + nietypowe zamówienia), kwiatomat 24/7, śluby i pamięć, dla firm, pytania, kontakt |
| `sklep.html` | Sklep przeniesiony z repo Kwiaciarni Małgorzata w stylu AM Flowers: kategorie, karta produktu, koszyk, zamówienie |
| `sukces.html` | Strona po udanej płatności |
| `regulamin.html`, `polityka-prywatnosci.html` | Projekty dokumentów z polami TODO, do sprawdzenia przez prawnika |
| `data/products.json` | Katalog i ceny. **Jedyne źródło cen** dla sklepu i płatności |
| `functions/api/create-checkout.js` | Płatność Stripe Checkout (BLIK, karta, Przelewy24), ceny liczone na serwerze |
| `functions/api/order.js` | Zamówienia ze sklepu: przekazuje je do backendu formularzy (`ORDER_WEBHOOK_URL`) |
| `swipe/` | Suwak przejścia do wpięcia na stronie Kwiaciarni Małgorzata |
| `przejscie-demo.html` | Podgląd suwaka w hero strony Małgorzaty |
| `css/`, `js/`, `img/`, `video/`, `fonts/`, `logo/` | Style, skrypty, zdjęcia WebP, wideo H.264 bez dźwięku, fonty OFL, logo SVG 1:1 z plików klientki |
| `brand/` | Brand book v2 (HTML, PDF), moodboard, `brandbook.config.json`, strategia, prompty Google Flow, skrypty budujące |
| `DESIGN.md` | Reguły wyglądu i decyzje |

## Wdrożenie: Cloudflare Pages

1. Cloudflare, *Workers & Pages → Create → Pages → Connect to Git*, wybierz to repo. Build command: pusty, output directory: `/`.
2. *Settings → Variables and secrets*:
   - `STRIPE_SECRET_KEY`: najpierw `sk_test_…`, po testach klucz produkcyjny. W Stripe włącz **BLIK** i **Przelewy24**.
   - `ORDER_WEBHOOK_URL` (+ opcjonalnie `ORDER_WEBHOOK_TOKEN`): adres backendu formularzy, który wyśle zamówienie e-mailem lub SMS-em.
   - `ALLOWED_ORIGINS`: domena strony Kwiaciarni Małgorzata (np. `https://kwiaciarniamalgorzata.pl`), żeby jej szybkie zamówienie też trafiało do `/api/order`.
   Bez tych zmiennych sklep działa dalej: płatność online przełącza się na płatność przy odbiorze, a zamówienie otwiera SMS z gotową treścią na 570 740 729.
3. *Custom domains*: podłącz `amflowers.pl` (domena i konto Stripe na klienta).

Lokalnie: `npx wrangler pages dev .` (funkcje) albo `python3 -m http.server` (sama strona).

## Suwak na stronie Kwiaciarni Małgorzata
```html
<link rel="stylesheet" href="https://amflowers.pl/swipe/am-swipe.css">
<div class="am-swipe" data-href="https://amflowers.pl/" data-asset-base="https://amflowers.pl/"></div>
<script src="https://amflowers.pl/swipe/am-swipe.js" defer></script>
```

## Edycja oferty
Ceny i produkty: `data/products.json`. Zdjęcie do `img/` (WebP, proporcja 4:5), ścieżka w `img`, opcjonalne drugie zdjęcie w `alt`. Pozycje z `"from": true` mają cenę „od” i są płatne przy odbiorze.

## Do uzupełnienia
- Adres potwierdzony: ul. Iwaszkiewicza 137B.
- Godziny otwarcia, e-mail, przypisanie telefonów (505 308 258 / 570 740 729).
- Ceny, dopłaty za wielkość, koszt i strefa dostawy (robocze).
- Pełna nazwa spółki AM Flowers, NIP, KRS w regulaminie i polityce prywatności.
- Rok 2021 i imię córki w sekcji „Historia”.
- Kwiatomat: sposób płatności, prawdziwe zdjęcie.
- Zgoda na zdjęcia z Facebooka (produkty p01–p16).
- Oferta (sekcje „Oferta”, „Dla firm”, „Pytania”): potwierdzić z AM Flowers, które usługi faktycznie prowadzą (abonament dla firm, kosze prezentowe, rośliny i kwiaty trwałe, dekoracje sal) i czy zamówienie „na dziś” jest możliwe.
- Po wdrożeniu: Google Business Profile, Search Console.
