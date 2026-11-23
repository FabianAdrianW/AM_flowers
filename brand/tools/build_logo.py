"""Builds logo SVGs by tracing Fabian's original files (shapes untouched) + ornaments."""
import sys, math, numpy as np
sys.path.insert(0, 'tools')
from PIL import Image
from trace_logo import trace, ink_mask

GOLD_STOPS = [(0, '#A0722F'), (.30, '#C99A4B'), (.52, '#F4D98E'), (.70, '#B07E36'), (1, '#E0BA6C')]
def grad(id, x1, x2):
    st = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in GOLD_STOPS)
    return f'<linearGradient id="{id}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="0" x2="{x2}" y2="0">{st}</linearGradient>'
def svg(w, h, body, defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs>{defs}</defs>{body}</svg>'
def P(d, fill): return f'<path fill-rule="evenodd" fill="{fill}" d="{d}"/>'

# --- logo 1: AM flowers (original) ---
im = Image.open('logo/am-flowers-monogram.jpg')
x0, y0, x1, y1 = 672, 243, 1905, 1190
m = ink_mask(im.crop((x0, y0, x1, y1)), blur=1.2, thr=55)
W, H = x1 - x0, y1 - y0
d_all = trace(m)
mono_m = m.copy(); mono_m[700:, :] = False          # monogram only (flowers starts ~y 960 abs)
d_mono = trace(mono_m)
for name, fill, defs in [('am-flowers-gold', 'url(#g)', grad('g', 0, W)), ('am-flowers-flat-gold', '#C9A45C', ''),
                         ('am-flowers-ink', '#1C1A17', ''), ('am-flowers-ivory', '#F4EEE3', '')]:
    open(f'logo/{name}.svg', 'w').write(svg(W, H, P(d_all, fill), defs))
open('logo/am-monogram-gold.svg', 'w').write(svg(W, 720, P(d_mono, 'url(#g)'), grad('g', 0, W)))

# --- logo 2: lockup (original) ---
im2 = Image.open('logo/am-flowers-x-malgorzata-lockup.jpg')
X0, Y0, X1, Y1 = 108, 258, 2441, 1184
m2 = ink_mask(im2.crop((X0, Y0, X1, Y1)), blur=1.0, thr=55)
W2, H2 = X1 - X0, Y1 - Y0
caps = np.zeros_like(m2); cy0, cy1, cx0 = 940 - Y0, 1032 - Y0, 1250 - X0
caps[cy0:cy1, cx0:] = m2[cy0:cy1, cx0:]
gold = m2 & ~caps
a = np.asarray(im2.convert('RGB')).astype(int)[940:1032, 1250:2441]
sel = (255 - a[:, :, 2]) > 120
brown = '#%02X%02X%02X' % tuple(int(v) for v in a[sel].mean(0))
body = P(trace(gold, 4), 'url(#g)') + P(trace(caps, 4), brown)
open('logo/lockup-am-x-malgorzata.svg', 'w').write(svg(W2, H2, body, grad('g', 0, W2)))
body_light = P(trace(gold, 4), 'url(#g)') + P(trace(caps, 4), '#F4EEE3')
open('logo/lockup-am-x-malgorzata-on-emerald.svg', 'w').write(svg(W2, H2, body_light, grad('g', 0, W2)))

# --- ornaments: divider traced from the original lockup ---
dv = ink_mask(im2.crop((1060, 280, 1210, 1160)), blur=0.8, thr=55)
open('logo/ornament-divider.svg', 'w').write(svg(150, 880, P(trace(dv, 2), 'url(#g)'), grad('g', 0, 150)))
st = ink_mask(im2.crop((1080, 660, 1190, 770)), blur=0.6, thr=55)
open('logo/ornament-star.svg', 'w').write(svg(110, 110, P(trace(st, 1), 'url(#g)'), grad('g', 0, 110)))
corner = '<path fill="none" stroke="url(#g)" stroke-width="4" d="M4,140 V4 H140 M18,140 V18 H140"/>'
open('logo/ornament-corner.svg', 'w').write(svg(144, 144, corner, grad('g', 0, 144)))
print('ok', W, H, W2, H2, brown)
