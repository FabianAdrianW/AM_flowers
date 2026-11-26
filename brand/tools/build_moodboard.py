"""Builds AM Flowers moodboard (2 x A4) as one self-contained responsive HTML.
Images: drop Flow renders into images/f{n}.jpg|webp|png and rebuild."""
import base64, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = pathlib.Path('/tmp/fonts')
ICONS = F / 'tabler/package/icons/outline'
VERSION = 'v2'


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def data_uri(p, mime):
    return f'data:{mime};base64,{b64(p)}'


LAT = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
EXT = 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'


def face(fam, pkg, slug, w, style):
    out = ''
    for sub, rng in (('latin', LAT), ('latin-ext', EXT)):
        f = F / f'{pkg}/package/files/{slug}-{sub}-{w}-{style}.woff2'
        out += (f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{style};font-display:block;"
                f"src:url({data_uri(f, 'font/woff2')}) format('woff2');unicode-range:{rng}}}")
    return out


FONTS = ''.join([
    face('Cormorant', 'fontsource-cormorant-garamond-5.3.0', 'cormorant-garamond', 400, 'normal'),
    face('Cormorant', 'fontsource-cormorant-garamond-5.3.0', 'cormorant-garamond', 500, 'normal'),
    face('Cormorant', 'fontsource-cormorant-garamond-5.3.0', 'cormorant-garamond', 400, 'italic'),
    face('Jost', 'fontsource-jost-5.3.0', 'jost', 400, 'normal'),
    face('Jost', 'fontsource-jost-5.3.0', 'jost', 500, 'normal'),
])

LOGO = {k: data_uri(ROOT / f'logo/{v}', 'image/svg+xml') for k, v in {
    'gold': 'am-flowers-gold.svg', 'ivory': 'am-flowers-ivory.svg', 'lockup': 'lockup-am-x-malgorzata.svg', 'lockup_dark': 'lockup-am-x-malgorzata-on-emerald.svg',
    'star': 'ornament-star.svg', 'corner': 'ornament-corner.svg', 'divider': 'ornament-divider.svg',
    'mono': 'am-monogram-gold.svg'}.items()}


def icon(name):
    s = (ICONS / f'{name}.svg').read_text()
    s = re.sub(r'\s+', ' ', s).replace('stroke-width="2"', 'stroke-width="1.5"')
    s = re.sub(r'class="[^"]*"', 'aria-hidden="true"', s)
    return s.replace('width="24" height="24"', 'width="100%" height="100%"')


def find_img(n):
    p = ROOT / f'images/f{n}.jpg'
    if not p.exists():
        return None
    from PIL import Image
    import io
    im = Image.open(p).convert('RGB'); im.thumbnail((900, 900))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=80)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def frame(n, label, detail, cls=''):
    src = find_img(n)
    inner = (f'<img src="{src}" alt="{label}: {detail}">' if src else
             f'<div class="ph"><img class="ph-star" src="{LOGO["star"]}" alt=""><span>Kadr #{n}<br>prompt Google Flow</span></div>')
    return (f'<figure class="fr {cls}">{inner}<i class="cn tl"></i><i class="cn br"></i>'
            f'<figcaption><b>{label}</b><em>{detail}</em></figcaption></figure>')


PALETTE = [
    ('Szmaragd', '#0F2A24', 'głębia, hero, kurtyna', 'dark'),
    ('Złoto', 'linear-gradient(120deg,#A0722F,#C99A4B 30%,#F4D98E 52%,#B07E36 70%,#E0BA6C)', '#C9A45C · ornamenty', 'gold'),
    ('Papier', '#FBF8F2', 'tło, karty', ''),
    ('Atrament', '#1C1A17', 'tekst', 'dark'),
    ('Puder', '#E2C6C0', 'akcent kwiatów', ''),
]


def palette():
    out = ''
    for name, val, role, kind in PALETTE:
        hexv = val if val.startswith('#') else '#C9A45C'
        out += (f'<div class="sw {kind}"><div class="chip" style="background:{val}"></div>'
                f'<b>{name}</b><span>{hexv if kind != "gold" else role}</span>'
                f'{"" if kind == "gold" else f"<small>{role}</small>"}</div>')
    return out


SYMBOLS = [('flower', 'Bukiet', 'okazja'), ('clock-24', '24/7', 'zawsze pod ręką'),
           ('scissors', 'Pracownia', 'rękodzieło'), ('hearts', 'AMiłość', 'dwa pokolenia'),
           ('truck-delivery', 'Dostawa', 'do drzwi'), ('rings', 'Ślub', 'dzień ważny'),
           ('candle', 'Pamięć', 'z taktem')]

CSS = """
:root{--emerald:#0F2A24;--emerald-deep:#0A1E19;--gold:#C9A45C;--gold-text:#7A5A22;--paper:#FBF8F2;--ink:#1C1A17;--muted:#5E6B63;--blush:#E2C6C0;--ivory:#F4EEE3;--line:rgba(122,90,34,.28)}
*{box-sizing:border-box;margin:0}
html{background:#E9E4DA}
body{font-family:'Jost',system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.amf-moodboard{display:flex;flex-direction:column;align-items:center;gap:28px;padding:28px 12px}
.sheet{width:210mm;max-width:100%;aspect-ratio:210/297;background:var(--paper);position:relative;overflow:hidden;
  display:flex;flex-direction:column;padding:11mm 12mm 9mm;gap:5.2mm;box-shadow:0 1px 2px rgba(0,0,0,.06),0 12px 40px rgba(15,42,36,.12)}
.sheet:before,.sheet:after{content:"";position:absolute;width:15mm;height:15mm;border:solid var(--gold);border-width:1px 0 0 1px;top:5mm;left:5mm;pointer-events:none}
.sheet:after{top:auto;left:auto;bottom:5mm;right:5mm;border-width:0 1px 1px 0;box-shadow:2.2mm 2.2mm 0 -1.2mm transparent}
.sheet .c2{position:absolute;width:15mm;height:15mm;pointer-events:none}
.c2.a{top:7mm;left:7mm;border:solid var(--gold);border-width:1px 0 0 1px}
.c2.b{bottom:7mm;right:7mm;border:solid var(--gold);border-width:0 1px 1px 0}
.over{display:flex;justify-content:space-between;font-size:6.6pt;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-text)}
.over span:last-child{color:var(--muted)}
.serif{font-family:'Cormorant',Georgia,serif}
.head{display:grid;grid-template-columns:30mm 1fr;gap:7mm;align-items:center}
.head img{width:100%}
.claim{font-family:'Cormorant',serif;font-weight:400;font-size:25pt;line-height:1.02;letter-spacing:-.005em}
.claim .am{color:#A0722F;font-weight:500}
.claim em{display:block;font-style:italic;color:var(--emerald)}
.thesis{display:flex;gap:4mm;font-size:8.4pt;line-height:1.55;color:var(--muted);max-width:150mm;align-items:stretch}
.thesis:before{content:"";flex:0 0 1px;background:var(--gold)}
.mosaic{display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:1fr 1fr .9fr;gap:2.4mm;flex:1;min-height:0}
.fr{position:relative;overflow:hidden;border-radius:2px;background:var(--emerald);min-height:0}
.fr>img{width:100%;height:100%;object-fit:cover;display:block}
.m-main{grid-column:1/8;grid-row:1/3}.m-s1{grid-column:8/13;grid-row:1}.m-s2{grid-column:8/13;grid-row:2}
.m-r{grid-row:3;grid-column:span 3}
.ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2mm;
  background:radial-gradient(120% 90% at 30% 20%,#1A3D35 0%,var(--emerald) 55%,var(--emerald-deep) 100%);color:rgba(244,238,227,.55);font-size:6pt;letter-spacing:.14em;text-transform:uppercase;text-align:center;line-height:1.5}
.ph-star{width:7mm;opacity:.9}
.cn{position:absolute;width:5mm;height:5mm;border:solid var(--gold);border-width:1px 0 0 1px;opacity:.9}
.cn:after{content:"";position:absolute;inset:1mm 0 0 1mm;border:solid var(--gold);border-width:1px 0 0 1px}
.cn.tl{top:2mm;left:2mm}.cn.br{bottom:2mm;right:2mm;transform:rotate(180deg)}
figcaption{position:absolute;left:0;right:0;bottom:0;padding:6mm 3mm 2.4mm;background:linear-gradient(transparent,rgba(10,30,25,.82));display:flex;flex-direction:column;gap:.4mm}
figcaption b{font-weight:500;font-size:5.8pt;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
figcaption em{font-family:'Cormorant',serif;font-size:9.5pt;color:var(--ivory);line-height:1.1}
.method{background:var(--emerald);color:var(--ivory);display:flex;align-items:center;gap:3mm;padding:3.4mm 5mm;border-radius:2px;font-size:7.8pt;letter-spacing:.04em}
.method .lab{font-size:5.8pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-right:2mm}
.method .ar{color:var(--gold)}
.method .alt{font-family:'Cormorant',serif;font-style:italic;font-size:10pt;color:var(--blush)}
.pal{display:grid;grid-template-columns:repeat(5,1fr);gap:2.4mm}
.sw{display:flex;flex-direction:column;gap:.6mm;font-size:6.4pt;color:var(--muted)}
.sw .chip{height:11mm;border-radius:2px;border:1px solid rgba(28,26,23,.08);margin-bottom:1mm}
.sw b{font-family:'Cormorant',serif;font-weight:500;font-size:10.5pt;color:var(--ink)}
.sw small{font-size:6pt;letter-spacing:.06em}
.foot{display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:2.4mm;font-size:6pt;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.foot img{height:3.4mm}
h2.t{font-family:'Cormorant',serif;font-weight:400;font-size:21pt;line-height:1.05}
h2.t em{color:var(--gold-text)}
.lab2{font-size:6pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-text);margin-bottom:2mm;display:flex;align-items:center;gap:2mm}
.lab2:after{content:"";flex:1;height:1px;background:var(--line)}
.persp{display:grid;grid-template-columns:repeat(4,1fr);gap:2.4mm}
.persp .fr{aspect-ratio:3/4}
.persp p{font-size:7pt;line-height:1.45;color:var(--muted);margin-top:1.6mm}
.row2{display:grid;grid-template-columns:1.15fr 1fr;gap:6mm}
.logos{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:auto auto;gap:2.4mm}
.lg{border-radius:2px;display:flex;align-items:center;justify-content:center;padding:4mm;border:1px solid var(--line)}
.lg.dark{background:var(--emerald);border-color:var(--emerald)}
.lg img{max-width:100%;max-height:26mm}
.lg.wide{grid-column:1/3;padding:4mm 6mm}
.lg.wide img{max-height:16mm}
.syms{display:grid;grid-template-columns:repeat(7,1fr);gap:1.6mm}
.sym{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.8mm;font-size:5.8pt;color:var(--muted);line-height:1.25}
.sym .ic{width:9mm;height:9mm;color:var(--gold-text)}
.sym b{font-family:'Cormorant',serif;font-weight:500;font-size:9pt;color:var(--ink)}
.type{display:grid;grid-template-columns:auto 1fr;gap:4mm;align-items:end}
.type .aa{font-family:'Cormorant',serif;font-size:44pt;line-height:.8;color:var(--emerald)}
.type .aa i{color:var(--gold-text)}
.type p{font-size:7pt;line-height:1.5;color:var(--muted)}
.type p b{color:var(--ink);font-weight:500}
.rule{display:flex;flex-wrap:wrap;gap:1.6mm;align-items:center;font-size:7.2pt}
.rule span{padding:1mm 2.4mm;border:1px solid var(--line);border-radius:20px;background:#fff}
.rule .ar{border:0;padding:0;background:none;color:var(--gold-text)}
.orn{display:flex;align-items:center;justify-content:space-around;background:var(--emerald);border-radius:2px;padding:3mm 4mm;gap:3mm}
.orn img{height:16mm}.orn .star{height:9mm}.orn .corner{height:10mm}
.orn small{font-size:5.6pt;letter-spacing:.16em;text-transform:uppercase;color:rgba(244,238,227,.6);display:block;text-align:center;margin-top:1mm}
.band{background:var(--emerald);border-radius:2px;display:flex;align-items:center;gap:6mm;padding:6mm 8mm;flex:1;min-height:0}
.band img{height:100%;max-height:30mm}
.band q{font-family:'Cormorant',serif;font-size:19pt;line-height:1.1;color:var(--ivory);quotes:none}
.band q b{color:var(--gold);font-weight:500}
.band small{display:block;margin-top:2.4mm;font-size:6pt;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
.col{display:flex;flex-direction:column;gap:4mm;min-height:0}
@media screen and (max-width:720px){
  .sheet:before,.sheet:after,.c2{display:none}
  .over{flex-direction:column;gap:4px}
  .sheet{aspect-ratio:auto;padding:22px 18px 18px;gap:18px;width:100%}
  .head{grid-template-columns:1fr}.head img{width:110px}
  .claim{font-size:30px}
  .thesis{font-size:13px}
  .mosaic{display:flex;flex-direction:column}
  .mosaic .fr{aspect-ratio:4/3}
  .method{flex-wrap:wrap;font-size:12px}
  .pal{grid-template-columns:repeat(2,1fr)}
  .persp{grid-template-columns:repeat(2,1fr)}
  .persp p{font-size:11px}
  .row2{grid-template-columns:1fr}
  .band{flex-direction:column;align-items:flex-start}.band img{height:90px}.band q{font-size:24px}
  .syms{grid-template-columns:repeat(4,1fr)}
  .sym{font-size:10px}.sym b{font-size:14px}
  .type p,.rule{font-size:11px}
  .over,.foot{font-size:9px}
  figcaption b{font-size:9px}figcaption em{font-size:15px}
  .sw{font-size:10px}.sw b{font-size:16px}.sw small{font-size:9px}
  h2.t{font-size:28px}.lab2{font-size:9px}
}
@page{size:A4;margin:0}
@media print{html,body{background:var(--paper)}.amf-moodboard{padding:0;gap:0}
  .sheet{width:210mm;height:297mm;aspect-ratio:auto;box-shadow:none;break-after:page}
  .sheet:last-child{break-after:auto}}
"""


def build():
    mosaic = ''.join([
        frame(1, 'Hero', 'Bukiet na szmaragdowym aksamicie', 'm-main'),
        frame(4, 'Pracownia', 'Ręce florystki, ta sama staranność', 'm-s1'),
        frame(6, 'Kwiatomat 24/7', 'Intermarché, Oława', 'm-s2'),
        frame(7, 'Sklep', 'Bukiet w papierze i wstążce', 'm-r'),
        frame(8, 'Flowerbox', 'Szmaragd i złoty brzeg', 'm-r'),
        frame(9, 'Śluby', 'Stół, świece, wiązanka', 'm-r'),
        frame(10, 'Detal', 'Opakowanie i bilecik', 'm-r'),
    ])
    persp = ''.join(f'<div>{frame(n, l, d)}<p>{t}</p></div>' for n, l, d, t in [
        (7, 'Okazja', 'Urodziny, rocznica', 'Wybierasz online, odbierasz gotowy bukiet.'),
        (6, 'Ostatnia chwila', 'Wieczór, niedziela', 'Kwiatomat 24/7: kwiaty, gdy wszystko jest zamknięte.'),
        (9, 'Ślub', 'Dekoracje i wiązanka', 'Rozmowa z florystką, projekt, realizacja.'),
        (11, 'Pamięć', 'Wieńce i wiązanki', 'Spokojnie, z taktem, na czas.'),
    ])
    syms = ''.join(f'<div class="sym"><div class="ic">{icon(i)}</div><b>{n}</b>{m}</div>' for i, n, m in SYMBOLS)
    over = '<div class="over"><span>AM Flowers / Kwiaciarnia / Oława</span><span>Brand book 1.0 / Moodboard</span></div>'

    def foot(page):
        return (f'<div class="foot"><span>AM Flowers · system marki · projekt do oceny właścicielskiej</span>'
                f'<img src="{LOGO["star"]}" alt=""><span>{page} / 2</span></div>')

    s1 = f"""<section class="sheet" aria-label="Arkusz 1: pełne spektrum"><i class="c2 a"></i><i class="c2 b"></i>{over}
<div class="head"><img src="{LOGO['gold']}" alt="AM flowers">
<div><h1 class="claim" aria-label="Dwa pokolenia, AMiłość do kwiatów ta sama."><span aria-hidden="true">Dwa pokolenia,</span><em aria-hidden="true"><span class="am">AM</span>iłość do kwiatów ta sama.</em></h1></div></div>
<p class="thesis"><span>Kwiaciarnia Małgorzata rośnie. Mama i córka układają kwiaty tak jak dotąd, a podają je po nowemu: w sklepie online i w kwiatomacie czynnym całą dobę.</span></p>
<div class="mosaic">{mosaic}</div>
<div class="method"><span class="lab">Metoda</span>Wybierasz <span class="ar">→</span> florystka układa <span class="ar">→</span> odbierasz <span class="alt">w pracowni · w kwiatomacie 24/7 · z dostawą</span></div>
<div class="pal">{palette()}</div>{foot(1)}</section>"""

    s2 = f"""<section class="sheet" aria-label="Arkusz 2: fundament"><i class="c2 a"></i><i class="c2 b"></i>{over}
<div><h2 class="t">Jedna AMiłość. <em>Cztery okazje.</em></h2></div>
<div class="persp">{persp}</div>
<div class="row2"><div class="col">
<div><div class="lab2">Znak</div><div class="logos">
<div class="lg"><img src="{LOGO['gold']}" alt="AM flowers na papierze"></div>
<div class="lg dark"><img src="{LOGO['gold']}" alt="AM flowers na szmaragdzie"></div>
<div class="lg wide"><img src="{LOGO['lockup']}" alt="AM flowers i Kwiaciarnia Małgorzata"></div></div></div>
<div><div class="lab2">Motyw z wizytówki</div><div class="orn">
<div><img class="corner" src="{LOGO['corner']}" alt=""><small>Narożnik</small></div>
<div><img src="{LOGO['divider']}" alt=""><small>Przerywnik</small></div>
<div><img class="star" src="{LOGO['star']}" alt=""><small>Gwiazda 24/7</small></div></div></div>
</div><div class="col">
<div><div class="lab2">Słownik symboli</div><div class="syms">{syms}</div></div>
<div><div class="lab2">Typografia</div><div class="type"><div class="aa">A<i>m</i></div>
<p><b>Cormorant Garamond</b> do nagłówków, kursywa do akcentów.<br><b>Jost</b> do tekstu i etykiet. Obie na licencji OFL.</p></div></div>
<div><div class="lab2">Reguła języka</div><div class="rule"><span>Okazja</span><span class="ar">→</span><span>bukiet</span><span class="ar">→</span><span>jak odebrać</span><span class="ar">→</span><span>jedno działanie</span></div></div>
<div><div class="lab2">Splot</div><p class="thesis" style="font-size:7.4pt"><span>Litery A i M krzyżują się jak dwie łodygi: mama i córka. Ten splot wraca jako szmaragdowa wstążka w każdym kadrze i jako dwie złote linie w przejściu na stronę.</span></p></div>
</div></div>
<div class="band"><img src="{LOGO['divider']}" alt=""><div><q>Kwiaciarnia Małgorzata rośnie.<br><b>AM</b>iłość do kwiatów zostaje.</q><small>Hasło przejścia · suwak na stronie Małgorzaty</small></div></div>
<p style="font-size:6pt;color:var(--muted)">Sceny ilustracyjne, nie przedstawiają wskazanych osób. Zdjęcia wygenerowane w Google Flow.</p>
{foot(2)}</section>"""

    html = (f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>AM Flowers · Moodboard {VERSION}</title><style>{FONTS}{CSS}</style></head>'
            f'<body><main class="amf-moodboard">{s1}{s2}</main></body></html>')
    out = ROOT / f'AM_Flowers_Moodboard_{VERSION}_Responsive.html'
    out.write_text(html)
    print(out, len(html) // 1024, 'KB')


if __name__ == '__main__':
    build()
