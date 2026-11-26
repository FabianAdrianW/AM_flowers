# AM Flowers: intake + paleta + prompty Google Flow (v1.1, 2026-11-23)

## Decyzje (Fabian, 2026-11-23)
- Dwie strony: **Kwiaciarnia Małgorzata** zostaje klasyczna (bez sklepu i kwiatomatu, z małym podpisem „AM Flowers” pod logo). **AM Flowers** to nowa strona premium: sklep internetowy, kwiatomaty, historia przejścia „z tradycji w XXI wiek”.
- Wejście: **przeciągany suwak** w hero strony Małgorzaty. Złoty uchwyt z monogramem AM, przeciągnięcie w prawo (palcem na mobile, klik też działa). Wjeżdża szmaragdowa kurtyna, złote podwójne linie rozsuwają się jak narożniki z wizytówki, otwiera się AM Flowers.
- Paleta: **A „Szmaragd i złoto”, wierna wizytówce** (patrz niżej).
- Brand book: **LITE**.
- Telefony: oba. 505 308 258 (wizytówka) i 570 740 729 (strona). Przypisanie do potwierdzenia.

## Materiały z wizytówki (S)
- Monogram „AM” pismem kaligraficznym, pod nim „flowers” kursywą. Złoto z gradientem: ciemniejsze końce kresek, jasny środek.
- Ornamenty art deco: podwójne linie w narożnikach (kształt L), pionowe przerywniki z podwójnym zakończeniem i rombem, okrąg z ośmioramienną gwiazdą (środek wizytówki).
- Tło: biały papier. Wszystko w jednym kolorze (złoto).
- Dane: ul. J. Iwaszkiewicza 137B, Oława · 505 308 258 · FB: Kwiaciarnia „Małgorzata” · IG: @malgorzatakwiaciarnia.

## Paleta (D, kontrast WCAG zmierzony)
Zasada wierności: jak na wizytówce, **papier + złoto** to podstawa. Szmaragd daje głębię (hero, kurtyna, stopka, sekcje premium). Róż tylko jako kolor kwiatów, na szmaragdzie.

| Token | Nazwa | Hex | Rola |
|---|---|---|---|
| `--paper` | Papier wizytówki | #FBF8F2 | główne tło jasnych sekcji, karty |
| `--emerald` | Szmaragd | #0F2A24 | hero, kurtyna swipe, stopka, sekcje premium |
| `--emerald-deep` | Głęboki szmaragd | #0A1E19 | cienie, gradient kurtyny |
| `--gold` | Złoto | #C9A45C | ornamenty, linie, monogram, akcent na szmaragdzie |
| `--gold-text` | Złoto do tekstu | #7A5A22 | złoty tekst i linki na jasnym tle |
| `--ink` | Atrament | #1C1A17 | tekst na papierze |
| `--muted` | Szałwia | #5E6B63 | tekst pomocniczy na papierze |
| `--blush` | Puder | #E2C6C0 | drobne akcenty na szmaragdzie (np. słowo „flowers”) |
| `--ivory` | Kość słoniowa | #F4EEE3 | tekst na szmaragdzie |

**Gradient złota** (z monogramu): `linear-gradient(120deg, #A0722F 0%, #C99A4B 30%, #F4D98E 52%, #B07E36 70%, #E0BA6C 100%)` (zmierzony z pliku logo). Tylko na monogramie, ornamentach i uchwycie suwaka, nigdy na tekście ciągłym.

| Para | Kontrast | Użycie |
|---|---|---|
| ink / paper | 16.4:1 | tekst |
| gold-text / paper | 6.0:1 | tekst, linki |
| muted / paper | 5.3:1 | tekst pomocniczy |
| gold / paper | 2.8:1 | **tylko ornamenty**, nie tekst |
| ivory / emerald | 13.2:1 | tekst na ciemnym |
| gold / emerald | 6.5:1 | nagłówki, przyciski na ciemnym |
| blush / emerald | 9.5:1 | akcent |
| emerald / gold | 6.5:1 | tekst na złotym przycisku |

## Motyw graficzny (z logo, wraca wszędzie)
- **Podwójny narożnik** (2 linie 1.5 px, odstęp 6 px): ramki kart, zdjęć, hover (narożniki dosuwają się do rogów), przejście swipe.
- **Przerywnik z rombem**: separator sekcji, etykiety.
- **Okrąg z gwiazdą**: favicon, loader, znacznik „czynne 24/7” przy kwiatomacie, punkt na suwaku.

## Typografia (propozycja, OFL)
- Nagłówki: **Cormorant Garamond** (300–500, kursywa do akcentów), pasuje do kaligrafii monogramu.
- Tekst: **Jost**. Etykiety: wersaliki, tracking .16–.2em.
- Logo: oba pliki Fabiana przerysowane do wektora 1:1 (kształt liter bez zmian). Pliki w `logo/`.

## Świat zdjęć (dusza marki, hipoteza)
- Metafora: **splot** (litery A i M krzyżują się jak dwie łodygi: mama i córka). Szczegóły w `03_strategy.md`.
- Światło: miękkie, kierunkowe z lewej góry, ciepłe. Tło: szmaragdowy aksamit/len albo papier #FBF8F2.
- Stały rekwizyt w każdym kadrze: **szmaragdowa satynowa wstążka**.
- Kwiaty: róże ogrodowe, piwonie, jaskry w odcieniach kości słoniowej, pudru i szampana + zieleń eukaliptusa.
- Bez twarzy, bez tekstu i logo w obrazie. Osoby fikcyjne (adnotacja „Sceny ilustracyjne”).

---

## Prompty Google Flow

Wspólny dopisek do każdego promptu (wklej na końcu):
```
Photorealistic editorial floral photography, soft directional warm light from upper left, palette of deep emerald green (#0F2A24), champagne gold (#C9A45C), warm ivory paper (#FBF8F2) and blush pink petals, one emerald satin ribbon visible, real textures, shallow depth of field, no text, no letters, no logos, no watermark.
```

### 1. Hero AM Flowers (16:9, desktop)
```
Lush luxury hand-tied bouquet of ivory garden roses, blush peonies, champagne ranunculus and silver eucalyptus, placed on the right side of the frame against a deep emerald green velvet backdrop, emerald satin ribbon loosely tied around the stems, thin brushed gold line running vertically in the background, generous empty dark space on the left third for headline text, moody high-end still life. Aspect ratio 16:9.
```
### 2. Hero mobile (9:16)
```
Same luxury bouquet of ivory garden roses, blush peonies and champagne ranunculus seen from slightly above, positioned in the top half of the frame, deep emerald green velvet backdrop fading darker toward the bottom, emerald satin ribbon trailing down, empty dark space in the lower half for text. Aspect ratio 9:16.
```
### 3. Tło kurtyny swipe (16:9)
```
Close-up of deep emerald green silk fabric with soft flowing folds, subtle sheen, a single thin polished gold line crossing diagonally, minimal and elegant, almost abstract, dark and rich, room for overlay graphics. Aspect ratio 16:9.
```
### 4. Historia: pracownia (4:5)
```
Close-up of a florist's hands (no face visible) arranging a bouquet of ivory roses and blush peonies on an old oak workbench, warm ivory wrapping paper, vintage brass scissors, emerald satin ribbon spool, deep emerald wall behind, warm window light from the left, calm craftsmanship moment. Aspect ratio 4:5.
```
### 5. Historia: tradycja → nowoczesność (3:2)
```
Split composition on one oak table: on the left a simple hand-tied bouquet wrapped in kraft paper with twine, on the right a refined luxury bouquet in ivory paper with an emerald satin ribbon and a small gold detail, both in the same warm window light, symbolising growth from tradition to modern elegance. Aspect ratio 3:2.
```
### 6. Kwiatomat 24/7 (4:5)
*Najlepiej zastąpić prawdziwym zdjęciem kwiatomatu z Intermarché. To kadr zastępczy.*
```
Modern premium flower vending machine with illuminated glass compartments, each holding a wrapped bouquet in ivory paper with emerald ribbon, machine body in deep emerald green with thin gold trim, standing in a clean bright shopping center entrance in the evening, soft glow from the compartments, nobody around, no text, no brand names, no screens with writing. Aspect ratio 4:5.
```
### 7. Sklep: packshot bukietu (4:5, seria)
```
Product photo of a single hand-tied bouquet of [ROSES/PEONIES/MIXED SEASONAL FLOWERS] in [COLOR] tones, wrapped in warm ivory paper and tied with an emerald satin ribbon, centered on a seamless warm ivory background (#FBF8F2), soft shadow below, consistent catalog lighting from upper left, clean and premium. Aspect ratio 4:5.
```
### 8. Sklep: flowerbox (1:1)
```
Round deep emerald green hatbox with a thin gold rim, filled densely with ivory and blush roses, lid leaning beside it, on a warm ivory seamless background, soft shadow, premium gift product photo. Aspect ratio 1:1.
```
### 9. Śluby i dekoracje (3:2)
```
Elegant wedding table setting with a low centrepiece of ivory roses, blush peonies and eucalyptus, emerald linen tablecloth, gold cutlery, tall ivory candles, warm evening light, a bridal bouquet with emerald satin ribbon resting at the edge of the table, no people. Aspect ratio 3:2.
```
### 10. Opakowanie / detal marki (3:2)
```
Flat lay on warm ivory paper: a deep emerald gift bag and an emerald tissue-wrapped bouquet, a small ivory gift card with only a thin gold double-line art deco corner border and no writing, a few loose blush petals, gold scissors, soft daylight. Aspect ratio 3:2.
```

### 11. Pamięć: wieniec (4:5)
```
Elegant funeral wreath of ivory roses, white lisianthus and silver eucalyptus lying on deep emerald velvet, a thin emerald satin ribbon with a narrow gold edge, soft calm light from upper left, quiet and respectful mood, no candles with text, no people. Aspect ratio 4:5.
```

### Wideo (Flow / Veo, 8 s, pętla)
**V1. Hero w ruchu**
```
Slow cinematic push-in on a luxury bouquet of ivory roses and blush peonies against a deep emerald velvet backdrop, petals moving very gently as if in a light breeze, soft shimmer of warm light passing across, emerald satin ribbon swaying slightly, seamless loop, no text.
```
**V2. Przejście (tło dla kurtyny)**
```
Deep emerald silk fabric slowly unfolding and rippling, thin gold light reflections sliding across the folds from left to right, elegant and calm, seamless loop, no text.
```

---

## Odpowiedzi robocze (Fabian, 2026-11-23; lista pytań do klientki później)
1. AM = A (córka, imię do potwierdzenia) + Małgorzata (mama). Firma przechodzi z mamy na mamę i córkę.
2. AM Flowers od 2021 (H). Rok założenia Kwiaciarni Małgorzata: do potwierdzenia.
3. Mama i córka na stronie później, gdy będą zdjęcia.
4. Kwiatomat 24/7: przy Intermarché, ul. ks. prał. F. Kutrowskiego 29, Oława. Na razie jeden.
5. Oba telefony do kwiaciarni (H).
6. Domena: amflowers.pl (H).
7. Logo: dwa pliki od Fabiana (monogram, wspólny znak).
8. Hasło: „Dwa pokolenia, AMiłość do kwiatów ta sama.” (zaakceptowane), przejście: „Kwiaciarnia Małgorzata rośnie. AMiłość do kwiatów zostaje.”
