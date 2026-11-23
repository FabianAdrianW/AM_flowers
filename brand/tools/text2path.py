from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
def text_path(text, files, size, x0=0, y0=0):
    fonts=[TTFont(f) for f in files]
    upm=fonts[0]['head'].unitsPerEm; s=size/upm
    out=[]; x=x0
    for ch in text:
        for f in fonts:
            cmap=f.getBestCmap()
            if ord(ch) in cmap:
                g=cmap[ord(ch)]; gs=f.getGlyphSet()
                pen=SVGPathPen(gs)
                gs[g].draw(TransformPen(pen,(s,0,0,-s,x,y0)))
                out.append(pen.getCommands()); x+=gs[g].width*s; break
    return ''.join(out), x-x0
