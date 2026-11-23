import sys, pathlib
from playwright.sync_api import sync_playwright
html = pathlib.Path(sys.argv[1]).resolve(); pdf = sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, name in ((1440, 'desk'), (375, 'mob')):
        pg = b.new_page(viewport={'width': w, 'height': 900}, device_scale_factor=1)
        pg.goto(html.as_uri()); pg.wait_for_timeout(800)
        pg.screenshot(path=f'/tmp/mb_{name}.png', full_page=True); pg.close()
    pg = b.new_page(); pg.goto(html.as_uri()); pg.wait_for_timeout(800)
    pg.pdf(path=pdf, format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
