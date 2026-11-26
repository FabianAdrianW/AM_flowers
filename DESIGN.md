# AM Flowers: DESIGN.md (v1, 2026-11-23)

Źródło prawdy: `brandbook.config.json`. Ten plik zbiera reguły wyglądu i decyzje dla strony AM Flowers oraz suwaka na stronie Kwiaciarni Małgorzata.

## Kierunek
Premium, ale ciepło. Papier i złoto jak na wizytówce, szmaragd do głębi. Rękodzieło florystki ważniejsze niż blichtr. Wszystko wynika ze **splotu**: litery A i M krzyżują się jak dwie łodygi (mama i córka).

## Kolor
| Token | Hex | Rola |
|---|---|---|
| `--emerald` | #0F2A24 | hero, kurtyna suwaka, stopka, sekcje premium |
| `--emerald-deep` | #0A1E19 | gradient kurtyny, cienie |
| `--gold` | #C9A45C | ornamenty, linie, przyciski na szmaragdzie |
| `--gold-text` | #7A5A22 | złoty tekst i linki na papierze |
| `--gold-grad` | gradient | tylko monogram, ornamenty, uchwyt suwaka |
| `--paper` | #FBF8F2 | tło jasnych sekcji |
| `--ink` | #1C1A17 | tekst |
| `--muted` | #5E6B63 | tekst pomocniczy |
| `--ivory` | #F4EEE3 | tekst na szmaragdzie |
| `--blush` | #E2C6C0 | akcent na szmaragdzie (rzadko) |

Zasada kontrastu: złoto #C9A45C nigdy jako tekst na papierze (2.8:1). Na papierze tekst złoty = `--gold-text` (6.0:1).

## Typografia
- Cormorant Garamond 400/500 + kursywa: display, h1–h3. Kursywa tylko na jedno słowo-akcent.
- Jost 400/500: tekst 16 px, etykiety 11–12 px wersalikami z odstępem .18em.
- Logo: tylko oryginalne pliki SVG z `logo/` (przerysowane 1:1 z plików klientki). Napisów z logo nie składamy żadnym fontem.
- Hostowane lokalnie, latin + latin-ext, `font-display: swap`.

## Motyw
- Podwójny narożnik (2 linie 1 px, odstęp 4–6 px): ramki zdjęć i kart. Hover: narożniki dosuwają się do rogów, zdjęcie przybliża się o 3%.
- Przerywnik z rombem: separator sekcji (poziomo na stronie).
- Okrąg z gwiazdą: favicon, loader, znacznik „24/7”, punkt na suwaku.

## Hasło
- Zapis wizualny: `Dwa pokolenia,` + kursywa `<span class="am">AM</span>iłość do kwiatów ta sama.`
- `aria-label` i `<title>`/meta: „Dwa pokolenia, AMiłość do kwiatów ta sama.”

## Struktura strony AM Flowers (propozycja)
1. Hero (szmaragd, zdjęcie #1, hasło, CTA „Zamów bukiet” + „Znajdź kwiatomat”).
2. Nasza historia: mama i córka, zdjęcie #5 (tradycja → nowoczesność), linia „dawniej Kwiaciarnia Małgorzata”.
3. Sklep: bestsellery (packshoty #7, #8), link do pełnego sklepu.
4. Kwiatomat 24/7: zdjęcie #6 (docelowo prawdziwe), adres, mapa, znacznik gwiazdy.
5. Okazje: śluby (#9), pamięć (#11).
6. Pracownia: ręce (#4), adres, godziny, oba telefony.
7. Stopka szmaragdowa z wspólnym znakiem.

## Suwak przejścia (strona Kwiaciarni Małgorzata → AM Flowers)
- Spoczynek: złota szyna 1 px, uchwyt 56 px z monogramem AM, etykieta „Kwiaciarnia Małgorzata rośnie. Przeciągnij →”.
- Przeciąganie (pointer events, palec i mysz): za uchwytem odsłania się szmaragd, dwie złote linie podążają.
- Próg 60%: linie splatają się w podwójny narożnik i domykają ekran (900 ms, `cubic-bezier(.22,1,.36,1)`).
- Otwarcie: kurtyna rozsuwa się od środka, logo i hasło AM Flowers, potem nawigacja do amflowers.pl.
- Klawiatura: uchwyt jako `role="slider"` z `aria-valuenow`; Enter/Spacja i strzałka w prawo uruchamiają przejście.
- `prefers-reduced-motion`: bez animacji, zwykłe przejście. Obok zawsze zwykły link „AM Flowers”.
- Poniżej 60% puszczenie uchwytu wraca go na start (spring 400 ms).

## Ruch
ease-out 300–900 ms, nic się nie odbija i nie kołysze. Wejścia sekcji: opacity + 12 px. Linie ornamentów rysują się (stroke-dashoffset).

## Zdjęcia
Prompty #1–#11 w `01_intake.md`. Jeden świat: szmaragd albo papier, ciepłe światło z lewej góry, szmaragdowa wstążka w każdym kadrze, bez tekstu i twarzy. Mama i córka tylko na prawdziwych zdjęciach.

## TODO
Imię córki, rok założenia Kwiaciarni Małgorzata, przypisanie telefonów, e-mail, domena, ceny, godziny pracowni, prawdziwe zdjęcie kwiatomatu.
