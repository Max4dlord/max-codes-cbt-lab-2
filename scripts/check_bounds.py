"""Check that no figure draws outside its own viewBox.

Naively regexing a path's `d` attribute treats *relative* commands (h-96, v-70)
as absolute coordinates and reports phantom overflows, so path data is parsed
properly here.   node scripts/draw_diagrams.mjs && python3 scripts/check_bounds.py
"""
import glob, pathlib, re, sys
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/2000/svg}'
OPS = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'T': 2, 'A': 7, 'Z': 0}
TOKEN = re.compile(r'[MmLlHhVvCcSsQqTtAaZz]|-?\d*\.?\d+(?:e-?\d+)?')


def path_points(d):
    pts, i, x, y, cmd = [], 0, 0.0, 0.0, None
    toks = TOKEN.findall(d)
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t; i += 1
            if cmd.upper() == 'Z':
                pts.append((x, y)); continue
        if cmd is None:
            break
        n = OPS[cmd.upper()]
        args = [float(v) for v in toks[i:i + n]]
        if len(args) < n:
            break
        i += n
        rel, C = cmd.islower(), cmd.upper()
        if C == 'H':
            x = x + args[0] if rel else args[0]
        elif C == 'V':
            y = y + args[0] if rel else args[0]
        elif C == 'A':
            x, y = (x + args[5], y + args[6]) if rel else (args[5], args[6])
        elif C == 'C':
            x, y = (x + args[4], y + args[5]) if rel else (args[4], args[5])
        elif C == 'S':
            x, y = (x + args[2], y + args[3]) if rel else (args[2], args[3])
        else:  # M, L, T, Q
            x, y = (x + args[0], y + args[1]) if rel else (args[0], args[1])
        pts.append((x, y))
    return pts


def f(el, k, d=0.0):
    try:
        return float(el.get(k, d))
    except (TypeError, ValueError):
        return d


def main():
    files = sorted(glob.glob(str(pathlib.Path(__file__).resolve().parent.parent
                                 / 'public' / 'images' / 'eee282' / '*.svg')))
    bad = 0
    for path in files:
        root = ET.parse(path).getroot()
        W, H = [float(v) for v in root.get('viewBox').split()][2:]
        xs, ys = [], []
        for el in root.iter():
            tag = el.tag.replace(NS, '')
            if tag == 'rect':
                xs += [f(el, 'x'), f(el, 'x') + f(el, 'width')]
                ys += [f(el, 'y'), f(el, 'y') + f(el, 'height')]
            elif tag == 'circle':
                xs += [f(el, 'cx') - f(el, 'r'), f(el, 'cx') + f(el, 'r')]
                ys += [f(el, 'cy') - f(el, 'r'), f(el, 'cy') + f(el, 'r')]
            elif tag == 'line':
                xs += [f(el, 'x1'), f(el, 'x2')]; ys += [f(el, 'y1'), f(el, 'y2')]
            elif tag == 'text':
                xs.append(f(el, 'x')); ys.append(f(el, 'y'))
            elif tag == 'path':
                for px, py in path_points(el.get('d', '')):
                    xs.append(px); ys.append(py)
            elif tag == 'svg':
                xs += [f(el, 'x'), f(el, 'x') + f(el, 'width')]
                ys += [f(el, 'y'), f(el, 'y') + f(el, 'height')]
        if not xs:
            continue
        over = max(max(xs) - W, max(ys) - H, -min(xs), -min(ys))
        if over > 4:
            bad += 1
            print(f'OVERFLOW {pathlib.Path(path).name}: {over:.0f}px  '
                  f'x[{min(xs):.0f},{max(xs):.0f}] y[{min(ys):.0f},{max(ys):.0f}] '
                  f'vs {int(W)}x{int(H)}')
    print(f'{len(files) - bad}/{len(files)} figures fit inside their canvas')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
