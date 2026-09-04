"""Check that no <text> overflows the viewBox it is actually drawn in.

The CRO figures nest a <svg viewBox="0 0 640 320"> inside the 760x500 panel, so
screen labels live in a *different* coordinate space to the panel labels. Checking
everything against the outer viewBox misses labels that fall outside the inner one
(and get clipped, since a nested <svg> has overflow:hidden by default).
   python3 scripts/check_text_fit.py
"""
import glob, pathlib, re, sys
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/2000/svg}'
CLASS_SIZE = {'t10': 10, 't11': 11, 't12': 12, 't13': 13, 't15': 15,
              'tb': 13, 'tg': 13}
CHAR_W = 0.55      # rough average glyph width as a fraction of font-size


def find_text(el, vb, out):
    """Walk the tree, tracking the coordinate space of each nested <svg>."""
    for child in el:
        tag = child.tag.replace(NS, '')
        if tag == 'svg':
            box = child.get('viewBox')
            if box:
                parts = [float(v) for v in box.split()]
                inner = tuple(parts) if len(parts) == 4 else vb
            else:
                inner = vb
            find_text(child, inner, out)
        elif tag == 'text':
            out.append((child, vb))


def main():
    files = sorted(glob.glob(str(pathlib.Path(__file__).resolve().parent.parent
                                 / 'public' / 'images' / 'eee282' / '*.svg')))
    bad = 0
    for path in files:
        root = ET.parse(path).getroot()
        found = []
        find_text(root, tuple(float(v) for v in root.get('viewBox').split()), found)
        hits = []
        for el, vb in found:
            W, H = vb[2], vb[3]
            attrs = ' '.join(f'{k}="{v}"' for k, v in el.items())
            x = float(el.get('x', 0))
            y = float(el.get('y', 0))
            anchor = el.get('text-anchor', 'start')
            st = re.search(r'font-size:\s*([\d.]+)px', attrs)
            cls = el.get('class', '')
            size = float(st.group(1)) if st else CLASS_SIZE.get(cls, 12)
            body = ''.join(el.itertext())
            plain = re.sub(r'&#?\w+;', 'X', body)
            w = len(plain) * size * CHAR_W
            left = x if anchor == 'start' else (x - w if anchor == 'end' else x - w / 2)
            if left < 1 or left + w > W - 1 or y > H - 2:
                hits.append(f'{body[:46]!r} x {left:.0f}..{left + w:.0f} y {y:.0f}'
                            f' vs {W:.0f}x{H:.0f}')
        if hits:
            bad += 1
            print(f'OVERFLOW {pathlib.Path(path).name}')
            for h in hits:
                print('    !', h)
    print(f'\n{len(files) - bad}/{len(files)} figures have all text inside its viewBox')
    return 0


if __name__ == '__main__':
    sys.exit(main())
