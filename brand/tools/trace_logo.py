"""Faithful trace of Fabian's original logo files (letter shapes untouched)."""
import sys, numpy as np, potrace
from PIL import Image, ImageFilter

def trace(mask, turd=8):
    bm = potrace.Bitmap(~mask)  # potracer fills False regions
    path = bm.trace(turdsize=turd, alphamax=1.0, opticurve=True, opttolerance=0.2)
    d = []
    for c in path:
        s = c.start_point; d.append(f"M{s.x:.1f},{s.y:.1f}")
        for seg in c.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
            else:
                d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        d.append("Z")
    return "".join(d)

def ink_mask(img, blur=0.8, thr=60):
    g = img.convert('RGB').filter(ImageFilter.GaussianBlur(blur))
    a = np.asarray(g).astype(int)
    return (255 - a[:, :, 2]) > thr   # gold/brown = low blue

def bbox(mask, pad=20):
    ys, xs = np.where(mask)
    return max(xs.min()-pad, 0), max(ys.min()-pad, 0), xs.max()+pad, ys.max()+pad
