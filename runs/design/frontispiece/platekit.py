"""platekit — the drawing primitives behind every plate.

The style lives in plates.css. This file only supplies geometry:
hand-drawn-feeling lines that are still plain vector paths (no filters,
so Chrome prints them as vectors), seeded so every build is identical.
"""
import math
import random
from pathlib import Path

W = 324  # plate width in pt == text-block width


class Plate:
    def __init__(self, height, seed, title=""):
        self.h = height
        self.rng = random.Random(seed)
        self.title = title
        self.parts = []

    # ---- geometry helpers -------------------------------------------------
    def _noise(self, amp, wavelength):
        """Smooth 1-D noise function: a few summed sines with random phase."""
        ps = [(self.rng.uniform(0, math.tau), wavelength * k, amp / (i + 1))
              for i, k in enumerate((1.0, 0.47))]
        return lambda x: sum(a * math.sin(x / wl * math.tau + p) for p, wl, a in ps)

    @staticmethod
    def _smooth(pts):
        """Catmull-Rom spline through pts, emitted as cubic Béziers."""
        d = f"M{pts[0][0]:.2f} {pts[0][1]:.2f}"
        for i in range(len(pts) - 1):
            p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, len(pts) - 1)]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}"
        return d

    # ---- primitives -------------------------------------------------------
    def stroke(self, f, x0, x1, cls="line", wobble=0.3, step=6.0):
        """Draw y = f(x) from x0 to x1 with a slight hand tremor."""
        n = self._noise(wobble, 64)
        k = max(2, int(abs(x1 - x0) / step))
        pts = [(x0 + (x1 - x0) * i / k, 0) for i in range(k + 1)]
        pts = [(x, f(x) + n(x)) for x, _ in pts]
        self.parts.append(f'<path class="ink {cls}" d="{self._smooth(pts)}"/>')

    def seg(self, x0, y0, x1, y1, cls="line", wobble=0.15):
        """A ruled-by-hand segment in any direction: straight, with a slight sideways tremor."""
        length = math.hypot(x1 - x0, y1 - y0)
        nx, ny = -(y1 - y0) / length, (x1 - x0) / length
        n = self._noise(wobble, 48)
        k = max(2, int(length / 6))
        pts = []
        for i in range(k + 1):
            t = i / k
            d = n(t * length) * math.sin(math.pi * t) ** 0.5   # ends stay put
            pts.append((x0 + (x1 - x0) * t + nx * d, y0 + (y1 - y0) * t + ny * d))
        self.parts.append(f'<path class="ink {cls}" d="{self._smooth(pts)}"/>')

    def curve(self, pts, cls="line"):
        """A smooth outline through the given points."""
        self.parts.append(f'<path class="ink {cls}" d="{self._smooth(pts)}"/>')

    def person(self, x, floor, kind="man", s=1.0, cls="line"):
        """A standing figure, 60 units tall at s=1. The same two people appear on every plate that needs them."""
        body = {"man":   [(-7.2, 0), (-5.9, -12), (-6.5, -24), (-5.6, -31.5), (-2.4, -35), (2.4, -35),
                          (5.6, -31.5), (6.5, -24), (5.9, -12), (7.2, 0)],
                "woman": [(-10.4, 0), (-8.0, -11), (-5.0, -23), (-5.3, -31), (-2.3, -34.5), (2.3, -34.5),
                          (5.3, -31), (5.0, -23), (8.0, -11), (10.4, 0)]}[kind]
        k = s * (1.3 if kind == "man" else 1.22)
        r = 4.5 * k
        self.curve([(x + px * k, floor + py * k) for px, py in body], cls=cls)
        self.parts.append(f'<circle class="ink {cls}" cx="{x:.2f}" cy="{floor - 46 * k + r:.2f}" r="{r:.2f}"/>')

    def dot(self, x, y, r=1.0, clear=0.0):
        if clear:
            self.parts.append(f'<circle class="knock" cx="{x:.2f}" cy="{y:.2f}" r="{clear}"/>')
        self.parts.append(f'<circle class="solid" cx="{x:.2f}" cy="{y:.2f}" r="{r}"/>')

    def straight(self, x0, y0, x1, y1, cls="hair"):
        self.parts.append(f'<path class="ink {cls}" d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}"/>')

    def ring(self, x, y, r, cls="bold"):
        self.parts.append(f'<circle class="ink knock {cls}" cx="{x:.2f}" cy="{y:.2f}" r="{r}"/>')

    def label(self, x, y, text, cls="caps", anchor="start"):
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>')

    # ---- output -----------------------------------------------------------
    def svg(self, standalone=False):
        style = ""
        if standalone:  # inline the shared CSS so the file also opens on its own
            css = (Path(__file__).parent / "plates.css").read_text()
            style = f"<style>{css}</style>"
        body = "\n  ".join(self.parts)
        return (f'<svg class="plate" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {self.h}" '
                f'role="img" aria-label="{self.title}">{style}\n  {body}\n</svg>\n')


def write_interlude(plate, slug, caption):
    """A full-page drawing with no title: just the image and its closing line."""
    out = Path(__file__).parent / "out"
    out.mkdir(exist_ok=True)
    (out / f"{slug}.book.svg").write_text(book_svg(plate, "", caption, interlude=True))
    (out / f"{slug}.svg").write_text(plate.svg(standalone=True))
    (out / f"{slug}.figure.html").write_text(f"""<figure class="plate-fig interlude">
  {plate.svg()}
  <figcaption>{caption}</figcaption>
</figure>
""")


def write(plate, slug, deck, caption):
    """Write the standalone SVG and the <figure> block that goes into the book."""
    out = Path(__file__).parent / "out"
    out.mkdir(exist_ok=True)
    (out / f"{slug}.book.svg").write_text(book_svg(plate, deck, caption))
    (out / f"{slug}.svg").write_text(plate.svg(standalone=True))
    (out / f"{slug}.figure.html").write_text(f"""<figure class="plate-fig">
  <h2 class="plate-title">{plate.title}</h2>
  <p class="plate-deck">{deck}</p>
  {plate.svg()}
  {f"<figcaption>{caption}</figcaption>" if caption else ""}
</figure>
""")


def ease(t):
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


# ---- the book's single-file plate -------------------------------------------
# Added in the house, 2026-11-10. The book's pipeline (plate_check.py, land.py,
# compile.py, plate_packet.py, the EPUB tool) takes one SVG per plate on the
# house canvas: chapter plates 640 wide, Part plates 600x900. This composes the
# <figure> furniture (title, deck, rule, caption) around the art at the sizes
# plates.css gives the HTML figure, with the art at 86% of the width as
# STYLE.md requires. Lettering is written at its true page position (not
# inside a transformed group) so plate_check.py measures what prints.

import html as _html
import re as _re

TEXT_W = 324.0        # pt, the text block the plate is printed across


def _measure():
    """The house check's metrics (scripts/plate_check.py, DejaVu Serif), so a
    line the composer accepts is a line the check accepts. Falls back to an
    average-width estimate outside the house repo."""
    import sys
    for up in Path(__file__).resolve().parents:
        if (up / "scripts" / "plate_check.py").is_file():
            sys.path.insert(0, str(up / "scripts"))
            try:
                import plate_check as pc
                f = pc.fonts()["reg"]
                return lambda t, size: pc.width(t, size, 0, *f)
            except Exception:
                break
    return None


_MEASURE = _measure()


def _lines(text, size, cap, avg=0.56):
    """Split on <br>, then wrap each piece into balanced lines no wider than cap."""
    out = []
    for piece in text.split("<br>"):
        words = piece.split()
        if not words:
            continue
        width = ((lambda ws: _MEASURE(" ".join(ws), size)) if _MEASURE
                 else (lambda ws: len(" ".join(ws)) * size * avg))
        def split(ws, k):
            if k == 1:
                yield [ws]
                return
            for i in range(1, len(ws) - k + 2):
                for rest in split(ws[i:], k - 1):
                    yield [ws[:i]] + rest
        for n in range(1, len(words) + 1):
            best = min(((max(width(c) for c in cand), cand) for cand in split(words, n)),
                       default=None, key=lambda t: t[0])
            if best and best[0] <= cap:
                out += [" ".join(c) for c in best[1]]
                break
        else:
            out += words
    return out


def _esc(t):
    return _html.escape(_html.unescape(t), quote=False)


def book_svg(plate, deck, caption, interlude=False):
    """One self-contained SVG on the house canvas."""
    if interlude:
        VW, page_pt = 600.0, 7.3 * 72 * 600 / 900     # Part plate printed 7.3in tall
    else:
        VW, page_pt = 640.0, TEXT_W
    u = VW / page_pt                  # viewBox units per printed point
    # art scale: 324 canvas units -> 86% of the width (STYLE.md); a Part plate
    # is a whole page, so its art keeps to 78% to clear the 60-unit page bands
    k = VW * (0.78 if interlude else 0.86) / W
    ox = (VW - W * k) / 2
    cx = VW / 2
    css = (Path(__file__).parent / "plates.css").read_text()
    rows, y = [], 0.0

    def text(lines, cls, size_pt, lead):
        nonlocal y
        size = size_pt * u
        for ln in lines:
            y += size * lead
            rows.append(f'<text class="{cls}" x="{cx:.2f}" y="{y - size * (lead - 0.8) / 2 - size * 0.2:.2f}" '
                        f'style="font-size:{size:.2f}px;text-anchor:middle">{_esc(ln)}</text>')

    art_w = W * k
    y = 46.0                           # clear plate_check's 40-unit top band
    if not interlude:
        text(_lines(_html.unescape(plate.title), 19 * u, VW - 2 * 46), "ttl", 19, 1.12)
        y += 6 * u
        text(_lines(_html.unescape(deck), 10 * u, VW - 2 * 46), "ital deck", 10, 1.35)
        y += 26 * u
    art_y, labels, shapes = y, [], []
    for part in plate.parts:
        m = _re.match(r'<text class="(\w+)" x="([\d.\-]+)" y="([\d.\-]+)" text-anchor="(\w+)">(.*)</text>$', part)
        if not m:
            shapes.append(part)
            continue
        c, x, ty, anchor, t = m.groups()
        size = (7.4 if c == "caps" else 10.0) * k
        t = _html.unescape(t)
        ls = ";letter-spacing:0.2em" if c == "caps" else ""
        labels.append(f'<text class="{c}" x="{ox + float(x) * k:.2f}" y="{art_y + float(ty) * k:.2f}" '
                      f'style="font-size:{size:.2f}px;text-anchor:{anchor}{ls}">'
                      f'{_esc(t.upper() if c == "caps" else t)}</text>')
    y += plate.h * k
    if caption:
        c = 12 if interlude else 10.5
        y += (30 if interlude else 24) * u
        if not interlude:
            rows.append(f'<path class="ink" style="stroke-width:{0.5 * u:.2f}" '
                        f'd="M{cx - 9 * u:.2f} {y:.2f}H{cx + 9 * u:.2f}"/>')
            y += 11 * u
        text(_lines(_html.unescape(caption), c * u, VW - 2 * (66 if interlude else 46)), "ital cap", c, 1.5 if interlude else 1.3)
    y += 46.0                          # and its bottom band
    H = y
    shift = 0.0
    if interlude:                      # centre the block on the 600x900 Part canvas
        H = 900.0
        shift = (H - y) / 2
    if shift:                          # write the shift into every position, so checks see it
        mv = lambda t: _re.sub(r' y="([\d.\-]+)"', lambda m: f' y="{float(m.group(1)) + shift:.2f}"', t)
        rows, labels, art_y = [mv(r) for r in rows], [mv(l) for l in labels], art_y + shift
    group = "\n  ".join(shapes)
    body = ("\n".join(rows) + "\n" + "\n".join(labels) + "\n"
            f'<g transform="translate({ox:.2f} {art_y:.2f}) scale({k:.5f})">\n  {group}\n</g>')
    title = _esc(plate.title)
    return (f'<svg class="plate" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW:.0f} {H:.2f}" '
            f'role="img" aria-label="{title}"><style>{css}\n.plate .ttl {{ font-weight: 400; letter-spacing: 0.01em; }}</style>\n'
            + body + "\n</svg>\n")
