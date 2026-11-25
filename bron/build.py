# Bouwt ../index.html uit src.html door de foto's (img/*.webp) in te voegen.
import base64, pathlib
here = pathlib.Path(__file__).parent
s = (here / 'src.html').read_text()
for p in sorted((here / 'img').glob('*.webp')):
    s = s.replace(f'__IMG_{p.stem}__', 'data:image/webp;base64,' + base64.b64encode(p.read_bytes()).decode())
(here.parent / 'index.html').write_text(s)
print('index.html bijgewerkt')
