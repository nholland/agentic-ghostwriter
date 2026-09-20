"""Part closing plates 3, 4, 5, in the house style of plates 1 and 2.

Values read off plate-1-steady-river.svg and plate-2-sturdy-oak.svg:
  canvas 600x900, white rect, ink #111111, field weight 1.1 (plate 2: 1.05),
  accent weight 1.35-1.6, drawing box x 90..510, y 190..652,
  ~20 field lines at 23.7 spacing (plate 1) / 30 rings (plate 2),
  caption Georgia italic 17px, anchor middle, x=300, baseline 730.
"""
import math, os

INK = "#111111"
FIELD = 1.1
ACCENT = 1.4
HEAVY = 1.35
WALL = 1.6      # plate 1 draws its canyon walls at this weight
X0, X1 = 90.0, 510.0
CX = 300.0
CAP_Y = 730
OUT = "/home/user/agentic-ghostwriter/runs/parts"

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="600" height="900" '
        'viewBox="0 0 600 900">\n<rect width="600" height="900" fill="#ffffff"/>\n')


def cap(line):
    return (f'<text x="300.0" y="{CAP_Y}" text-anchor="middle" '
            "font-family='Georgia, \"Times New Roman\", serif' "
            f'font-size="17" font-style="italic" fill="{INK}">{line}</text>\n')


def poly(pts, w=FIELD):
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polyline points="{s}" fill="none" stroke="{INK}" '
            f'stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>\n')


def line(x1, y1, x2, y2, w=FIELD):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{INK}" stroke-width="{w}"/>\n')


def wob(u, seed):
    """Smooth hand-wobble, the same organic irregularity plate 2's rings have."""
    return (math.sin(u * 1.9 + seed * 1.7) * 0.6
            + math.sin(u * 4.3 + seed * 2.9) * 0.3
            + math.sin(u * 8.1 + seed * 0.7) * 0.15)


def stack(gaps, bottom, top):
    """Lay out layer baselines from a list of spacings, scaled so the field
    fills the house drawing box exactly (plate 1 runs y 190..640)."""
    k = (bottom - top) / sum(gaps)
    ys, y = [bottom], bottom
    for g in gaps:
        y -= g * k
        ys.append(y)
    return ys


# ---------------------------------------------------------------- plate 3
def plate3():
    """Days of light laid down in layers: each day's arc over the one before,
    the arc reaching a little further every time.

    Irregularity: one day's arc is broken on its morning side, and the days
    laid down after it rise unbroken through the same stretch of sky.
    "It comes back every morning, whether or not anyone thanked it for yesterday."
    """
    out = [HEAD]
    n = 20
    broken = 10
    gx0, gx1 = 210.0, 282.0
    for i in range(n):
        t = i / (n - 1)
        apex = 600.0 - 410.0 * t
        depth = 34.0 + 72.0 * t
        segs, cur = [], []
        steps = 168
        for k in range(steps + 1):
            x = X0 + (X1 - X0) * k / steps
            u = (x - CX) / 210.0
            y = apex + depth * u * u + 1.6 * wob(u * 3.0 + t * 5.0, i)
            if i == broken and gx0 < x < gx1:
                if cur:
                    segs.append(cur)
                    cur = []
                continue
            cur.append((x, y))
        if cur:
            segs.append(cur)
        for s in segs:
            out.append(poly(s, FIELD))
    out.append(cap("What it reaches, opens."))
    out.append("</svg>\n")
    return "".join(out)


# ---------------------------------------------------------------- plate 4
def plate4():
    """Years laid down in layers, thinning for a long time before the cold
    shows, then one band where nothing was laid down at all.

    Irregularity: that empty band has a top edge, and above it the layers are
    back at the spacing they had before. "Every winter ends."
    """
    tighten = [26, 26, 25, 24, 23, 22, 20, 18, 16, 14, 12, 10, 8.5, 7.5, 7]
    after = [26, 26, 26, 25, 26, 26, 26]
    winter = 72.0
    ys = stack(tighten + [winter] + after, 640.0, 190.0)
    heavy = {len(tighten), len(tighten) + 1}
    out = [HEAD]
    for i, yy in enumerate(ys):
        pts = []
        steps = 60
        for k in range(steps + 1):
            x = X0 + (X1 - X0) * k / steps
            u = (x - CX) / 210.0
            pts.append((x, yy + 1.3 * wob(u * 3.0 + i, i)))
        out.append(poly(pts, WALL if i in heavy else FIELD))
    out.append(cap("No winter is the last one."))
    out.append("</svg>\n")
    return "".join(out)


# ---------------------------------------------------------------- plate 5
def plate5():
    """The same layers, opening: the tight bands at the bottom give way to
    wider and wider ones as the days stretch.

    Irregularity: under the hard straight line of the surface the water is
    already moving, while the layers above it are still tight.
    "The thaw starts under the ice, weeks before anything shows on the surface."
    """
    ice_y = 652.0
    gaps = [6.5, 7, 7.5, 8.5, 9.5, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
            31, 33, 35, 37, 39]
    ys = stack(gaps, 636.0, 190.0)
    out = [HEAD]
    for i, yy in enumerate(ys):
        pts = []
        steps = 60
        for k in range(steps + 1):
            x = X0 + (X1 - X0) * k / steps
            u = (x - CX) / 210.0
            pts.append((x, yy + 1.3 * wob(u * 3.0 + i, i)))
        out.append(poly(pts, FIELD))
    # the surface: one straight, hard line
    out.append(line(X0, ice_y, X1, ice_y, ACCENT))
    # under it, the water already moving
    pts = []
    x = 168.0
    while x <= 432.01:
        pts.append((x, 676.0 - 5.0 * math.sin(2 * math.pi * (x - 168.0) / 48.0)))
        x += 1.5
    out.append(poly(pts, ACCENT))
    out.append(cap("Stand in the summer you built."))
    out.append("</svg>\n")
    return "".join(out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("plate-3-warm-sun", plate3),
                     ("plate-4-fall-to-winter", plate4),
                     ("plate-5-spring-to-summer", plate5)):
        p = os.path.join(OUT, name + ".svg")
        open(p, "w").write(fn())
        print("wrote", p)
