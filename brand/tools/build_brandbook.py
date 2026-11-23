"""AM Flowers brand book LITE -> one self-contained responsive HTML (print = A4)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_moodboard import FONTS, LOGO, icon, frame, ROOT, SYMBOLS

VERSION = 'v2'
AM = '<span class="am">AM</span>'


def table(head, rows, cls=''):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def req(rows):
    return table(['Wymaganie', 'Konsekwencja wykonawcza'], rows, 'req')


def copy(label, text):
    return f'<div class="copy"><b>{label}</b><p>{text}</p></div>'


CH = []


def ch(num, kicker, title, lead, body):
    CH.append((num, kicker, title))
    return (f'<section class="ch" id="c{num}"><div class="kick"><span>{num}</span>{kicker}</div>'
            f'<h2>{title}</h2><p class="lead">{lead}</p>{body}</section>')


S = []

S.append(ch('01', 'Istota / Zdanie marki', f'Ta sam{AM}iłość do kwiatów.',
  'Kwiaciarnia Małgorzata nie znika, tylko rośnie. AM Flowers to ta sama pracownia i te same bukiety, a do tego zamówienie z telefonu i kwiaty o północy.',
  '<p class="big">Tradycja mamy, nowoczesność córki, jedne ręce do kwiatów.</p>'
  + table(['Poziom', 'Definicja marki', 'Konsekwencja wykonawcza'], [
    ['Cel istnienia', 'Kwiaty od Małgorzaty pod ręką wtedy, kiedy są potrzebne, także w nocy i online', 'sklep i kwiatomat 24/7 widoczne na pierwszym ekranie'],
    ['Misja', 'Mama i córka układają kwiaty jak przez lata, a podają je po nowemu', 'każda nowość pokazana obok rąk florystki'],
    ['Wizja', 'Kwiaciarnia w Oławie, której nie trzeba szukać: w telefonie, przy sklepie, za rogiem', 'jeden znak na stronie, kwiatomacie i torbach'],
    ['Obietnica', 'Ta samAMiłość do kwiatów. Teraz w dwóch pokoleniach.', 'hasło w hero, na bileciku i na kwiatomacie'],
    ['Rola marki', 'Następczyni, nie konkurentka', 'przez pierwszy rok przy logo: „dawniej Kwiaciarnia Małgorzata”'],
  ])
  + '<h3>Zdanie marki jako filtr</h3><p>Każdy tekst, zdjęcie i animacja ma potwierdzać, że klient kupuje dalej u Małgorzaty, tylko wygodniej. Element, który tego nie potwierdza, wypada.</p>'
  + '<h3>Zapis hasła</h3><p>„Ta sam<b class="g">AM</b>iłość” łączy słowo „sama” z „AMiłość”: litera A jest wspólna. „AM” zawsze w złocie, reszta w kolorze tekstu. W kodzie strony i w opisach dla wyszukiwarek pełny zapis: „Ta sama AMiłość do kwiatów”.</p>'))

S.append(ch('01a', 'Archetyp / Dusza marki', 'Twórca z sercem Kochanka',
  'Archetyp ustala ton, zdjęcia, kolor i ruch. Główny daje wiarygodność, wspierający daje styl.',
  table(['', 'Archetyp', 'Uzasadnienie'], [
    ['Główny', '<b>Twórca</b>', 'rękodzieło florystki, detal, jakość bukietu (S)'],
    ['Wspierający', '<b>Kochanek</b>', 'premium, zmysły, piękno, złoto i aksamit (D)'],
    ['Cień', 'dystans, perfekcjonizm · powierzchowność, „drogo na pokaz”', 'ręce przy pracy w ważnych kadrach, widoczne ceny, ciepły język'],
  ])
  + table(['Archetyp →', 'Konsekwencja'], [
    ['Ton', 'spokojny, ciepły, konkretny; forma „Ty”'],
    ['Zdjęcia', 'ręce przy pracy, detal płatków, wstążka, światło z lewej góry'],
    ['Kolor', 'szmaragd, złoto, papier; róż tylko w kwiatach'],
    ['Typografia', 'szeryf Cormorant z kursywą do akcentów, Jost do tekstu'],
    ['Ruch', 'powolny i płynny: linie się rysują, narożniki domykają, nic nie skacze'],
    ['Słowa zakazane', 'luksusowy, ekskluzywny, najlepszy, unikalny, wyjątkowy, „z pasją”, „dla wymagających”'],
  ])
  + '<h3>Dusza: splot</h3><div class="soul"><img src="' + LOGO['mono'] + '" alt="Monogram AM"><div>'
  + '<p>Litery A i M w monogramie krzyżują się jak dwie łodygi: mama i córka, jedna marka. Ten splot wraca w trzech miejscach.</p><ul>'
  + '<li><b>Rekwizyt:</b> szmaragdowa satynowa wstążka w każdym kadrze.</li>'
  + '<li><b>Ruch:</b> w przejściu ze strony Małgorzaty dwie złote linie splatają się i otwierają AM Flowers.</li>'
  + '<li><b>Motyw:</b> podwójna złota linia z wizytówki: narożniki, przerywnik z rombem, okrąg z gwiazdą.</li></ul>'
  + '<p class="note">Test duszy: zasłoń logo na trzech zrzutach strony i jednym zdjęciu. Szmaragd, złota podwójna linia i wstążka mają wystarczyć, żeby poznać markę.</p></div></div>'))

S.append(ch('02', 'Klient / Konteksty', 'Pięć sytuacji, w których ktoś szuka kwiatów',
  'Klient nie kupuje „produktu florystycznego”. Ma okazję, mało czasu albo ważny dzień. Każdy kontekst ma swój kanał i swój ton.',
  table(['Kontekst', 'Znaczenie', 'Kanał', 'Ton'], [
    ['OKAZJA', 'urodziny, rocznica, podziękowanie: szybko i pewnie', 'sklep online, pracownia', 'radosny, konkretny'],
    ['OSTATNIA CHWILA', 'wieczór, niedziela, zapomniana rocznica', 'kwiatomat 24/7', 'krótki, uspokajający'],
    ['ŚLUB', 'wiązanka, dekoracje sali i kościoła', 'rozmowa z florystką', 'ciepły, uważny'],
    ['PAMIĘĆ', 'wieńce, wiązanki, Wszystkich Świętych', 'telefon, pracownia', 'cichy, z taktem'],
    ['STAŁY KLIENT', 'zna Małgorzatę i ma zobaczyć, że to ona', 'pracownia, Facebook', 'osobisty, bez nowomowy'],
  ])
  + '<h3>Perspektywy oceny</h3>'
  + req([['Mama (Małgorzata): klienci nie mogą poczuć, że ktoś przejął jej miejsce', 'imię Małgorzaty i adres pracowni widoczne na każdej stronie'],
         ['Córka: marka ma wyglądać na XXI wiek', 'sklep, płatność BLIK, kwiatomat, animacje na stronie'],
         ['Klient: ma szybko wiedzieć, co kupuje i jak to odbierze', 'cena i sposób odbioru przy każdym bukiecie']])))

S.append(ch('03', 'Pozycja / Rynek', 'Pracownia z kwiatomatem',
  'W Oławie konkurują lokalne kwiaciarnie, ogólnopolskie poczty kwiatowe, markety i stacje paliw oraz kwiatomaty. AM Flowers bierze od każdej grupy to, co robi dobrze.',
  table(['Grupa', 'Obietnica', 'Co przenieść (funkcja)', 'Czego unikać'], [
    ['Lokalne pracownie (np. Kwiaciarnia Ewa, Oława)', 'osobiste podejście, śluby', 'rozmowa z florystką, projekt bukietu', 'strona bez cen i bez zamawiania'],
    ['Poczty kwiatowe online', 'zamówienie w 2 minuty, dostawa', 'prosta ścieżka zakupu, płatność online', 'anonimowe zdjęcia stockowe, brak twarzy'],
    ['Markety i stacje paliw', 'tanio i zawsze', 'dostępność bez godzin otwarcia', 'jakość „z wiadra”'],
    ['Kwiatomaty innych firm', '24/7', 'kwiaty o każdej porze', 'automat bez marki i bez historii'],
  ])
  + '<p><b>Pozycja AM Flowers:</b> jedyna w okolicy pracownia, która ma własny kwiatomat 24/7, sklep online i historię dwóch pokoleń. Rzemiosło jak u lokalnej florystki, wygoda jak w poczcie kwiatowej. <span class="tag">D</span></p>'
  + '<p class="note">Rynek: kwiatomaty szybko przybywają w całej Polsce, więc sam automat przestaje wyróżniać. Wyróżnia to, kto układa bukiety w środku. <span class="tag">E</span></p>'))

S.append(ch('04', 'Oferta', 'Co sprzedajemy i jak to odebrać',
  'Oferta jest ułożona według okazji, a nie według gatunków kwiatów. Ceny są widoczne.',
  table(['Linia', 'Co', 'Odbiór', 'Status'], [
    ['Bukiety', 'gotowe bukiety S/M/L, sezonowe', 'pracownia · dostawa · kwiatomat', 'ceny do potwierdzenia'],
    ['Flowerboxy', 'kompozycje w szmaragdowym pudełku', 'pracownia · dostawa', 'H'],
    ['Kwiatomat 24/7', 'gotowe bukiety w szybkach', 'Intermarché, ul. ks. prał. F. Kutrowskiego 29, Oława', 'S'],
    ['Śluby i dekoracje', 'wiązanki, butonierki, sale, kościoły', 'na zamówienie', 'S'],
    ['Pamięć', 'wieńce, wiązanki, stroiki', 'na zamówienie', 'S'],
  ])
  + '<p class="note">Kontakt: ul. J. Iwaszkiewicza 137B, Oława · 505 308 258 · 570 740 729 (oba numery do kwiaciarni, przypisanie do potwierdzenia) · FB Kwiaciarnia „Małgorzata” · IG @malgorzatakwiaciarnia · domena robocza amflowers.pl</p>'))

S.append(ch('05', 'Komunikacja / Tone of voice', 'Mówimy jak florystka przy ladzie',
  'Ciepło, krótko i konkretnie. Forma „Ty”. Żadnych przymiotników zastępujących fakty.',
  '<div class="yn"><div><b>Tak</b><ul><li>ciepło</li><li>konkretnie</li><li>spokojnie</li></ul></div><div><b>Nie</b><ul><li>przesłodzenie</li><li>korpo-nowomowa</li><li>pośpiech i krzyk promocji</li></ul></div></div>'
  + '<p><b>Reguła języka:</b> okazja → bukiet → jak odebrać → jedno działanie.</p>'
  + table(['Zamiast', 'Piszemy'], [
    ['Ekskluzywne kompozycje dla wymagających', 'Bukiety układane ręcznie w pracowni na Iwaszkiewicza'],
    ['Oferujemy szeroki asortyment', 'Róże, piwonie, sezonowe kwiaty. Zobacz, co mamy dziś'],
    ['Z pasją tworzymy wyjątkowe chwile', 'Ułożymy bukiet na Twoją okazję'],
    ['Zapraszamy do kontaktu', 'Zadzwoń: 505 308 258'],
    ['Innowacyjne rozwiązanie sprzedażowe', 'Kwiatomat przy Intermarché. Czynny całą dobę'],
  ])
  + '<h3>Gotowe komunikaty</h3><div class="copies">'
  + copy('Hasło', 'Ta samAMiłość do kwiatów. Teraz w dwóch pokoleniach.')
  + copy('Hasło przejścia', 'Kwiaciarnia Małgorzata rośnie. AMiłość do kwiatów zostaje.')
  + copy('Krótko (1 zdanie)', 'AM Flowers to Kwiaciarnia Małgorzata w nowej odsłonie: mama i córka, pracownia w Oławie, sklep online i kwiatomat 24/7.')
  + copy('Średnio (3 zdania)', 'Od lat układamy bukiety w pracowni przy Iwaszkiewicza. Teraz robimy to we dwie: mama i córka. Bukiet zamówisz online, odbierzesz w pracowni albo w kwiatomacie przy Intermarché, czynnym całą dobę.')
  + copy('Bio do social', 'Kwiaciarnia Małgorzata, teraz AM Flowers · Mama i córka · Oława · Sklep online · Kwiatomat 24/7 przy Intermarché')
  + copy('Odpowiedź na opinię', 'Dziękujemy, że wpadłaś do nas na Iwaszkiewicza! Cieszymy się, że bukiet się spodobał. Do zobaczenia, Małgorzata i A.')
  + copy('Stopka e-mail', 'AM Flowers · Kwiaciarnia Małgorzata<br>ul. J. Iwaszkiewicza 137B, Oława · 505 308 258<br>Kwiatomat 24/7: Intermarché, ul. ks. prał. F. Kutrowskiego 29')
  + '</div>'))

S.append(ch('06', 'Logotyp', 'Monogram, który już znają',
  'Logo nie zmienia się. Oba znaki są przerysowane do wektora z oryginalnych plików 1:1: kształt liter, kaligrafia i proporcje zostają takie, jak je dostaliśmy.',
  '<div class="logos"><div class="lg"><img src="' + LOGO['gold'] + '" alt="Logo złote na papierze"><small>Złoty gradient na papierze · podstawowa</small></div>'
  + '<div class="lg dark"><img src="' + LOGO['gold'] + '" alt="Logo złote na szmaragdzie"><small>Złoty gradient na szmaragdzie</small></div>'
  + '<div class="lg dark"><img src="' + LOGO['ivory'] + '" alt="Logo jasne"><small>Jasna · na zdjęciach</small></div>'
  + '<div class="lg"><img src="' + LOGO['mono'] + '" alt="Monogram"><small>Sam monogram · favicon, pieczątka, uchwyt suwaka</small></div>'
  + '<div class="lg wide"><img src="' + LOGO['lockup'] + '" alt="Wspólny znak"><small>Wspólny znak · strona Małgorzaty, faza przejściowa</small></div><div class="lg wide dark"><img src="' + LOGO['lockup_dark'] + '" alt="Wspólny znak na szmaragdzie"><small>Wspólny znak na szmaragdzie</small></div></div>'
  + req([['Pole ochronne', 'wolne miejsce wokół logo = wysokość litery „f” w „flowers”'],
         ['Minimalny rozmiar', 'pełne logo 28 mm / 96 px szerokości; poniżej tylko monogram (min. 24 px)'],
         ['Kolor', 'gradient złota tylko na papierze i szmaragdzie; na zdjęciach wersja jasna'],
         ['Zakazy', 'nie obracać, nie rozciągać, nie dodawać cieni ani obrysów, nie przepisywać napisów z logo innym krojem']])))

S.append(ch('07', 'Paleta / Kontrast', 'Papier i złoto, szmaragd do głębi',
  'Jak na wizytówce: podstawą są papier i złoto. Szmaragd daje głębię, puder pojawia się tylko w kwiatach.',
  '<div class="pal">' + ''.join(
    f'<div class="sw"><div class="chip" style="background:{v}"></div><b>{n}</b><span>{h}</span><small>{r}</small></div>' for n, v, h, r in [
      ('Szmaragd', '#0F2A24', '#0F2A24', 'hero, kurtyna, stopka'),
      ('Złoto', 'linear-gradient(120deg,#A0722F,#C99A4B 30%,#F4D98E 52%,#B07E36 70%,#E0BA6C)', '#C9A45C', 'ornamenty, monogram'),
      ('Złoto do tekstu', '#7A5A22', '#7A5A22', 'linki i etykiety na papierze'),
      ('Papier', '#FBF8F2', '#FBF8F2', 'tło, karty'),
      ('Atrament', '#1C1A17', '#1C1A17', 'tekst'),
      ('Szałwia', '#5E6B63', '#5E6B63', 'tekst pomocniczy'),
      ('Kość słoniowa', '#F4EEE3', '#F4EEE3', 'tekst na szmaragdzie'),
      ('Puder', '#E2C6C0', '#E2C6C0', 'akcent na szmaragdzie'),
    ]) + '</div>'
  + table(['Para', 'Kontrast', 'AA', 'Użycie'], [
    ['atrament / papier', '16.4:1', '✓', 'tekst'],
    ['złoto do tekstu / papier', '6.0:1', '✓', 'tekst, linki'],
    ['szałwia / papier', '5.3:1', '✓', 'tekst pomocniczy'],
    ['złoto / papier', '2.8:1', '✗', 'tylko ornamenty i duże logo'],
    ['kość słoniowa / szmaragd', '13.2:1', '✓', 'tekst na ciemnym'],
    ['złoto / szmaragd', '6.5:1', '✓', 'nagłówki, przyciski'],
    ['puder / szmaragd', '9.5:1', '✓', 'akcent'],
    ['szmaragd / złoto', '6.5:1', '✓', 'tekst na złotym przycisku'],
  ])))

S.append(ch('08', 'Kroje / Hierarchia', 'Kaligrafia w logo, spokój w tekście',
  'Dwa kroje na licencji SIL Open Font License, hostowane lokalnie z polskimi znakami.',
  '<div class="types"><div><span class="d1">Ta sam<i class="g">AM</i>iłość</span><small>Cormorant Garamond 400 · display 56–72 px · kursywa do akcentów</small></div>'
  + '<div><span class="d2">Bukiety z pracowni</span><small>Cormorant Garamond 500 · h2 32–40 px</small></div>'
  + '<div><span class="d3">Zamów online i odbierz w pracowni albo w kwiatomacie.</span><small>Jost 400 · tekst 16 px · interlinia 1.6</small></div>'
  + '<div><span class="d4">Kwiatomat · czynny 24/7</span><small>Jost 500 · etykieta 11–12 px · wersaliki · odstęp .18em</small></div></div>'
  + req([['Logo i jego napisy', 'tylko jako oryginalny plik SVG, nigdy składane z fontu'],
         ['Nagłówki', 'Cormorant, max 2 linie, kursywa na jedno słowo-akcent'],
         ['Tekst', 'Jost 16 px, max 68 znaków w linii'],
         ['Liczby i ceny', 'Jost 500, cyfry tabelaryczne']])))

S.append(ch('09', 'Art direction', 'Jeden świat zdjęć',
  'Szmaragdowy aksamit albo papier, ciepłe światło z lewej góry, kwiaty w kości słoniowej, pudrze i szampanie. W każdym kadrze szmaragdowa wstążka.',
  '<div class="grid4">' + frame(1, 'Hero', 'Bukiet na aksamicie') + frame(4, 'Pracownia', 'Ręce florystki') + frame(6, 'Kwiatomat', '24/7') + frame(7, 'Sklep', 'Packshot') + '</div>'
  + table(['Kadr', 'Zadanie', 'Sygnał', 'Test'], [
    ['#1 Hero', 'otworzyć stronę AM Flowers', 'premium, ale ciepło', 'czy widać bukiet i miejsce na hasło?'],
    ['#4 Pracownia', 'pokazać, że układa człowiek', 'rękodzieło', 'czy widać ręce i wstążkę?'],
    ['#5 Tradycja → nowoczesność', 'opowiedzieć przejście', 'ciągłość', 'czy oba bukiety są w tym samym świetle?'],
    ['#6 Kwiatomat', 'wyjaśnić 24/7', 'wygoda', 'czy wiadomo, że to automat z kwiatami?'],
    ['#7 Packshot', 'sprzedać w sklepie', 'jakość, cena', 'czy wszystkie zdjęcia w sklepie mają to samo tło?'],
  ])
  + req([['Światło', 'miękkie, kierunkowe z lewej góry, ciepłe'],
         ['Rekwizyt', 'szmaragdowa satynowa wstążka w każdym kadrze'],
         ['Ludzie', 'tylko ręce; mama i córka dopiero na prawdziwych zdjęciach, nie generowane'],
         ['Zakazy', 'tekst i logo w obrazie, stock z uśmiechniętymi modelkami, czerwone róże w celofanie']])
  + '<p class="note">Prompty Google Flow (#1–#11, 2 wideo) są w pliku 01_intake.md. Sceny generowane są ilustracyjne i nie przedstawiają prawdziwych osób.</p>'))

S.append(ch('10', 'Środowisko cyfrowe', 'Dwie strony i jeden suwak',
  'Strona Kwiaciarni Małgorzata zostaje klasyczna. AM Flowers to osobna strona premium, do której prowadzi przeciągany suwak.',
  table(['Strona', 'Rola', 'Zawartość'], [
    ['Kwiaciarnia Małgorzata', 'dla stałych klientów, bez zmian w nawykach', 'galeria, śluby, opinie, kontakt; mały podpis „AM Flowers” pod logo; suwak do AM Flowers'],
    ['AM Flowers (amflowers.pl)', 'nowa marka, sprzedaż', 'hero z hasłem, nasza historia, sklep, kwiatomat 24/7, śluby, pamięć, kontakt'],
  ])
  + '<h3>Suwak przejścia</h3><ol class="steps">'
  + '<li><b>Spoczynek.</b> W hero strony Małgorzaty cienka złota szyna z okrągłym uchwytem (monogram AM). Etykieta: „Kwiaciarnia Małgorzata rośnie. Przeciągnij →”.</li>'
  + '<li><b>Przeciąganie.</b> Za uchwytem odsłania się szmaragd, a dwie złote linie biegną za nim. Na mobile palcem, na desktopie myszą; klik i Enter też uruchamiają przejście.</li>'
  + '<li><b>Splot.</b> Po przekroczeniu 60% linie splatają się w podwójny narożnik i domykają ekran (ok. 900 ms).</li>'
  + '<li><b>Otwarcie.</b> Kurtyna rozsuwa się od środka, pojawia się logo AM Flowers i hasło „Ta samAMiłość do kwiatów”.</li>'
  + '<li><b>Dostępność.</b> Przy <code>prefers-reduced-motion</code> bez animacji, zwykłe przejście. Zawsze jest też zwykły link „AM Flowers”.</li></ol>'
  + req([['Ruch', 'ease-out, 600–900 ms; nic się nie odbija i nie kołysze'],
         ['Hover na kartach', 'złote narożniki dosuwają się do rogów zdjęcia, zdjęcie przybliża się o 3%'],
         ['Separatory', 'przerywnik z rombem zamiast linii poziomej'],
         ['Social', 'kwadraty 1:1 i pion 4:5: zdjęcie + złoty narożnik + monogram w rogu; bez tekstu na zdjęciu poza hasłem']])))

S.append(ch('11', 'Materiały drukowane', 'Mało, ale porządnie',
  'Druk powtarza wizytówkę: biały papier, złoto, podwójne narożniki. Szmaragd na opakowaniach.',
  table(['Materiał', 'Wykonanie', 'Priorytet'], [
    ['Wizytówka', 'obecna, nowy nakład z adresem kwiatomatu na rewersie', 'wysoki'],
    ['Bilecik do bukietu', 'papier kremowy, złoty narożnik, miejsce na dedykację', 'wysoki'],
    ['Naklejka na kwiatomat', 'szmaragd, monogram, „Czynne 24/7”, numer telefonu', 'wysoki'],
    ['Wstążka', 'szmaragdowa satyna, opcjonalnie złoty nadruk „AM flowers”', 'średni'],
    ['Torba / pudełko', 'szmaragd, złoty monogram (hot-stamping)', 'średni'],
    ['Tabliczka w pracowni', '„Kwiaciarnia Małgorzata · AM Flowers” wspólnym znakiem', 'średni'],
  ])))

S.append(ch('12', 'Tokeny / Wdrożenie', 'Jedno źródło prawdy dla strony',
  'Strona czyta tokeny z brandbook.config.json. Zmiana koloru albo hasła w tym pliku zmienia stronę.',
  '<pre><code>:root{\n  --emerald:#0F2A24; --emerald-deep:#0A1E19;\n  --gold:#C9A45C; --gold-text:#7A5A22;\n  --gold-grad:linear-gradient(120deg,#A0722F,#C99A4B 30%,#F4D98E 52%,#B07E36 70%,#E0BA6C);\n  --paper:#FBF8F2; --ink:#1C1A17; --muted:#5E6B63;\n  --ivory:#F4EEE3; --blush:#E2C6C0; --line:rgba(122,90,34,.28);\n  --font-display:"Cormorant Garamond",Georgia,serif;\n  --font-body:"Jost",system-ui,sans-serif;\n  --radius:2px; --ease:cubic-bezier(.22,1,.36,1);\n}</code></pre>'
  + req([['Kolejność prac', '1) zdjęcia z Flow, 2) moodboard v2, 3) strona AM Flowers, 4) suwak na stronie Małgorzaty'],
         ['Do potwierdzenia z klientką', 'imię córki, rok założenia, przypisanie telefonów, domena, ceny, godziny pracowni'],
         ['Pliki', 'logo/*.svg · brandbook.config.json · design.md · 01_intake.md · 03_strategy.md']])))

CSS = """
:root{--emerald:#0F2A24;--emerald-deep:#0A1E19;--gold:#C9A45C;--gold-text:#7A5A22;--paper:#FBF8F2;--ink:#1C1A17;--muted:#5E6B63;--blush:#E2C6C0;--ivory:#F4EEE3;--line:rgba(122,90,34,.25)}
*{box-sizing:border-box;margin:0}
html{background:var(--paper);scroll-behavior:smooth}
body{font-family:'Jost',system-ui,sans-serif;color:var(--ink);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.am,.g{color:#A0722F;font-weight:500;font-style:normal}
.wrap{display:grid;grid-template-columns:240px minmax(0,1fr);max-width:1240px;margin:0 auto}
nav.toc{position:sticky;top:0;height:100vh;padding:40px 24px;border-right:1px solid var(--line);overflow:auto}
nav.toc img{width:96px;margin-bottom:28px}
nav.toc a{display:flex;gap:10px;padding:6px 0;color:var(--muted);text-decoration:none;font-size:13.5px;line-height:1.35}
nav.toc a span{color:var(--gold-text);font-size:11px;letter-spacing:.12em;min-width:26px;padding-top:2px}
nav.toc a:hover{color:var(--ink)}
main{padding:0 56px 80px}
.cover{min-height:100vh;background:var(--emerald);color:var(--ivory);display:flex;flex-direction:column;justify-content:space-between;padding:48px 56px;margin:0 -56px;position:relative;overflow:hidden}
.cover:before,.cover:after{content:"";position:absolute;width:90px;height:90px;border:solid var(--gold);border-width:1px 0 0 1px;top:24px;left:24px}
.cover:after{top:auto;left:auto;bottom:24px;right:24px;border-width:0 1px 1px 0}
.cover .over{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);display:flex;justify-content:space-between}
.cover .mid{display:flex;flex-direction:column;align-items:center;gap:28px;text-align:center}
.cover .mid img{width:min(320px,60%)}
.cover h1{font-family:'Cormorant',serif;font-weight:400;font-size:clamp(34px,5vw,58px);line-height:1.05}
.cover h1 em{display:block;color:var(--blush)}
.cover .sub{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(244,238,227,.65)}
.ch{padding:72px 0 24px;border-bottom:1px solid var(--line)}
.kick{display:flex;align-items:center;gap:12px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-text);margin-bottom:14px}
.kick span{font-family:'Cormorant',serif;font-size:26px;letter-spacing:0;color:var(--gold)}
.kick:after{content:"";flex:1;height:1px;background:var(--line)}
h2{font-family:'Cormorant',serif;font-weight:500;font-size:clamp(30px,3.6vw,42px);line-height:1.08;margin-bottom:14px}
h3{font-family:'Cormorant',serif;font-weight:500;font-size:24px;margin:30px 0 10px}
.lead{font-size:18px;color:var(--muted);max-width:68ch;margin-bottom:24px}
p{max-width:72ch;margin-bottom:12px}
.big{font-family:'Cormorant',serif;font-style:italic;font-size:28px;line-height:1.25;color:var(--emerald);border-left:1px solid var(--gold);padding-left:18px;margin:8px 0 26px}
.tw{overflow-x:auto;margin:16px 0}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th{text-align:left;font-weight:500;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-text);padding:8px 12px;border-bottom:1px solid var(--gold)}
td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
table.req td:first-child{font-weight:500;width:38%}
.note{font-size:14px;color:var(--muted)}
.tag{display:inline-block;font-size:10px;letter-spacing:.1em;border:1px solid var(--line);padding:0 6px;border-radius:10px;color:var(--gold-text)}
.soul{display:grid;grid-template-columns:180px 1fr;gap:28px;align-items:start;background:#fff;border:1px solid var(--line);padding:24px;border-radius:2px}
.soul img{width:100%}
.soul ul{padding-left:18px;margin-bottom:12px}
.yn{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
.yn>div{border:1px solid var(--line);padding:16px 20px;border-radius:2px;background:#fff}
.yn b{font-family:'Cormorant',serif;font-size:22px;font-weight:500}
.yn ul{padding-left:18px}
.copies{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.copy{background:#fff;border:1px solid var(--line);border-radius:2px;padding:14px 18px}
.copy b{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-text);font-weight:500}
.copy p{margin:6px 0 0;font-size:15px}
.logos{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:8px 0 20px}
.lg{border:1px solid var(--line);border-radius:2px;padding:22px 16px 12px;display:flex;flex-direction:column;align-items:center;gap:12px;background:#fff}
.lg img{height:110px;max-width:100%;object-fit:contain}
.lg.dark{background:var(--emerald);border-color:var(--emerald)}
.lg.dark small{color:rgba(244,238,227,.7)}
.lg.wide{grid-column:span 4}.lg.wide img{height:150px}
.lg small{font-size:12px;color:var(--muted);text-align:center}
.pal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:8px 0 12px}
.sw{display:flex;flex-direction:column;font-size:13px;color:var(--muted)}
.sw .chip{height:72px;border-radius:2px;border:1px solid rgba(0,0,0,.08);margin-bottom:8px}
.sw b{font-family:'Cormorant',serif;font-weight:500;font-size:20px;color:var(--ink)}
.sw small{font-size:12px}
.types>div{padding:16px 0;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:4px}
.types small{font-size:12px;color:var(--muted);letter-spacing:.04em}
.d1{font-family:'Cormorant',serif;font-size:clamp(40px,5vw,64px);line-height:1}
.d2{font-family:'Cormorant',serif;font-weight:500;font-size:36px;line-height:1.1}
.d3{font-size:16px}
.d4{font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-text)}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:8px 0}
.grid4 .fr{aspect-ratio:4/5}
.fr{position:relative;overflow:hidden;border-radius:2px;background:var(--emerald)}
.fr>img{width:100%;height:100%;object-fit:cover;display:block}
.ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:radial-gradient(120% 90% at 30% 20%,#1A3D35 0%,var(--emerald) 55%,var(--emerald-deep) 100%);color:rgba(244,238,227,.55);font-size:10px;letter-spacing:.14em;text-transform:uppercase;text-align:center;line-height:1.5}
.ph-star{width:28px}
.cn{position:absolute;width:18px;height:18px;border:solid var(--gold);border-width:1px 0 0 1px}
.cn:after{content:"";position:absolute;inset:4px 0 0 4px;border:solid var(--gold);border-width:1px 0 0 1px}
.cn.tl{top:8px;left:8px}.cn.br{bottom:8px;right:8px;transform:rotate(180deg)}
figcaption{position:absolute;left:0;right:0;bottom:0;padding:24px 12px 10px;background:linear-gradient(transparent,rgba(10,30,25,.85));display:flex;flex-direction:column}
figcaption b{font-weight:500;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
figcaption em{font-family:'Cormorant',serif;font-size:16px;color:var(--ivory)}
.steps{padding-left:20px;max-width:76ch}.steps li{margin-bottom:8px}
pre{background:var(--emerald);color:var(--ivory);padding:20px 24px;border-radius:2px;overflow-x:auto;font-size:13px;line-height:1.6;margin:12px 0}
code{font-family:ui-monospace,Menlo,monospace}
.colophon{padding:48px 0;font-size:13px;color:var(--muted);display:flex;align-items:center;gap:14px}
.colophon img{width:28px}
@media screen and (max-width:900px){
  .wrap{grid-template-columns:minmax(0,1fr)}nav.toc{display:none}
  main{padding:0 20px 60px}.cover{margin:0 -20px;padding:40px 24px;min-height:88vh}
  .soul{grid-template-columns:1fr}.soul img{width:140px}
  .yn,.copies{grid-template-columns:1fr}
  .logos{grid-template-columns:1fr 1fr}.lg.wide{grid-column:span 2}.lg img{height:80px}.lg.wide img{height:56px}
  .pal{grid-template-columns:1fr 1fr}
  .grid4{grid-template-columns:1fr 1fr}
  .lead{font-size:16px}.big{font-size:23px}
  table{font-size:13.5px}td,th{padding:8px}
}
@page{size:A4;margin:16mm 15mm 16mm}
@media print{
  html,body{background:#fff}body{font-size:10pt}
  .wrap{display:block}nav.toc{display:none}main{padding:0}
  .cover{min-height:265mm;margin:0;break-after:page;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .ch{break-before:page;padding-top:0;border:0}
  .lead{font-size:11.5pt}h2{font-size:26pt}h3{font-size:15pt;margin-top:18px}
  table{font-size:9pt}td,th{padding:6px 8px}
  tr,.copy,.lg,.sw,.soul,.fr,pre,.steps li{break-inside:avoid}
  .lg img{height:80px}.lg.wide img{height:64px}
  .colophon{break-before:avoid}
  .grid4{grid-template-columns:repeat(4,1fr)}.logos,.pal{grid-template-columns:repeat(4,1fr)}.lg.wide{grid-column:span 4}
  .yn,.copies{grid-template-columns:1fr 1fr}.soul{grid-template-columns:150px 1fr}
  .lg img{height:70px}.lg.wide img{height:96px}
  pre{white-space:pre-wrap;word-break:break-all;font-size:8pt}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
"""


def build():
    toc = ''.join(f'<a href="#c{n}"><span>{n}</span>{k.split(" / ")[0]}</a>' for n, k, t in CH)
    cover = (f'<header class="cover"><div class="over"><span>AM Flowers / Kwiaciarnia / Oława</span><span>Brand book {VERSION} · LITE</span></div>'
             f'<div class="mid"><img src="{LOGO["gold"]}" alt="AM flowers"><h1 aria-label="Ta sama AMiłość do kwiatów. Teraz w dwóch pokoleniach."><span aria-hidden="true">Ta sam<span style="color:var(--gold)">AM</span>iłość do kwiatów.</span><em aria-hidden="true">Teraz w dwóch pokoleniach.</em></h1></div>'
             f'<div class="sub">System marki · projekt do oceny właścicielskiej · 2026</div></header>')
    html = (f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>AM Flowers · Brand book {VERSION}</title><style>{FONTS}{CSS}</style></head><body>'
            f'<div class="wrap"><nav class="toc" aria-label="Spis treści"><img src="{LOGO["gold"]}" alt="">{toc}</nav>'
            f'<main>{cover}{"".join(S)}<div class="colophon"><img src="{LOGO["star"]}" alt="">AM Flowers · brand book {VERSION} · S = źródło właścicielskie, E = dane rynkowe, D = decyzja projektowa, H = hipoteza</div></main></div></body></html>')
    out = ROOT / f'AM_Flowers_Brand_Book_{VERSION}.html'
    out.write_text(html)
    print(out, len(html) // 1024, 'KB')


if __name__ == '__main__':
    build()
