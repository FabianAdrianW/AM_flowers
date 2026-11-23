import sys, numpy as np, potrace
from PIL import Image
src, out, box = sys.argv[1], sys.argv[2], [int(v) for v in sys.argv[3].split(',')]
im = Image.open(src).convert('RGB').crop(box)
a = np.asarray(im).astype(int)
mask = ~((255 - a[:,:,2]) > 70)         # gold has low blue
bm = potrace.Bitmap(mask)
path = bm.trace(turdsize=40, alphamax=1.0, opticurve=True, opttolerance=0.2)
d = []
for curve in path:
    s = curve.start_point; d.append(f"M{s.x:.1f},{s.y:.1f}")
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        else:
            d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
    d.append("Z")
w, h = im.size
open(out,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill-rule="evenodd" d="{"".join(d)}"/></svg>')
print(w, h, len(path))
