"""Frontispiece, option A: the wide view.

One landscape, the three interludes in it. The river comes toward us out
of the horizon, parts around a stone in the near water and closes up again.
The oak stands back from its far bank. The sun stands over the far
country, and its light reaches the oak.

Bold: the oak (trunk and first limbs), drawn as interlude 2 draws it. It is
the one thing in the scene that stands still while the river moves and the
light arrives, so it holds the page.
"""
import math
from platekit import Plate, W, write_interlude

p = Plate(height=300, seed=601, title="River, Oak, Sun")
rng = p.rng

HZ, YB = 116, 300           # horizon, foot of the drawing
L, HALF = 320, 60           # river space: s runs from the near edge (0) to the horizon (L), v across it

# ---- the river, in river space, then laid into the landscape ------------------
STONES = [(46, 12, 13)]     # along, across, radius (river space)


def course(t):
    """Centre of the river on the page, from near (t=0) to the horizon (t=1)."""
    return 176 + 52 * math.sin(t * math.pi * 1.1) - 88 * t


def page(s, v):
    t = min(s / L, 1.0)
    depth = (1 - t) ** 1.75
    y = HZ + (YB - HZ) * depth
    w = 78 * (1 - t) ** 1.25 + 1.2
    return (course(t) + v / HALF * w, y)


def across(base, s):
    v = base
    for ss, sv, r in STONES:
        d = base - sv
        reach = (r + 5) * math.exp(-abs(d) / (1.45 * r))
        length = 1.2 * r if s > ss else 3.2 * r      # the water comes toward us: parts first, closes nearer
        v += math.copysign(reach, d if d else 1) * math.exp(-((s - ss) / length) ** 2)
    limit = HALF + 28
    return limit * math.tanh(v / limit)


N = 13
for i in range(N):
    base = -HALF + 7 + (2 * HALF - 14) * i / (N - 1)
    tremor = p._noise(0.35, 90)
    s = 2 + rng.uniform(0, 10)
    far = L - 30 - rng.uniform(0, 40) * (1 - abs(base) / HALF)
    while s < far:
        end = min(s + rng.uniform(55, 140), far)
        pts, t = [], s
        while t <= end:
            pts.append(page(t, across(base, t) + tremor(t)))
            t += 3
        if len(pts) > 2:
            p.curve(pts)
        s = end + rng.uniform(5, 9) * (1 + s / 120)

# the banks
for side in (-1, 1):
    edge = p._noise(1.6, 80)
    pts = [page(s, side * (HALF + 5 + edge(s))) for s in range(0, L + 1, 4)]
    p.curve(pts)
    edge2 = p._noise(2.2, 60)
    s = 4
    stop = (0.42 * L) if side > 0 else L - 60
    while s < stop - 10:
        e = min(s + rng.uniform(18, 40), stop)
        p.curve([page(x, side * (HALF + 14 + edge2(x))) for x in range(int(s), int(e) + 1, 3)], cls="hair")
        s = e + rng.uniform(12, 28)

# the stone
for ss, sv, r in STONES:
    k = 14
    lump = [rng.uniform(-0.1, 0.1) for _ in range(k)]
    ring = []
    for j in range(k + 1):
        a = math.tau * j / k
        rr = r * (1 + lump[j % k])
        ring.append(page(ss + rr * 0.84 * math.sin(a), sv + rr * 1.12 * math.cos(a)))
    p.curve(ring, cls="line knock")
    cx, cy = page(ss, sv)
    sc = (page(ss, sv + 10)[0] - cx) / 10
    p.curve([(cx - r * 0.5 * sc, cy - 3), (cx - r * 0.05 * sc, cy - 4.2), (cx + r * 0.45 * sc, cy - 3)], cls="hair")

# ---- the oak, on the far right bank -------------------------------------------
GS = 0.5 * L                                        # how far off it stands, in river space
GX, GROUND = page(GS, HALF + 5)
GX += 34                                            # back from the right bank
CX = GX


def limb(x, y, angle, length, depth, up=True):
    sign = -1 if up else 1
    bend = rng.uniform(-0.22, 0.22)
    pts = []
    for i in range(5):
        t = i / 4
        a = angle + bend * t
        pts.append((x + math.sin(a) * length * t, y + sign * math.cos(a) * length * t))
    cls = "bold" if (up and depth >= 5) else "line" if depth >= 3 else "hair"
    p.curve(pts, cls=cls)
    ex, ey = pts[-1]
    if depth == 0:
        return
    kids = 3 if depth >= 4 and rng.random() < 0.55 else 2
    spread = 0.62 if up else 0.8
    for k in range(kids):
        off = (k - (kids - 1) / 2) * spread + rng.uniform(-0.16, 0.16)
        a = (angle + bend) * 0.82 + off
        if up:
            a += 0.10 * math.copysign(1, a) if abs(a) < 1.25 else 0
            a = max(-1.75, min(1.75, a))
        else:
            a = max(-1.42, min(1.42, a))
        limb(ex, ey, a, length * rng.uniform(0.66, 0.78), depth - 1, up)


OAK0 = len(p.parts)
S = 0.36                                            # the interlude's oak, smaller and further off
TRUNK_TOP = GROUND - 54 * S
for i in range(7):
    off = (i - 3) * 3.3 * S
    flare = lambda y, off=off: off * (1 + 1.5 * max(0, (y - (GROUND - 16 * S)) / (16 * S)) ** 2
                                      + 0.6 * max(0, (TRUNK_TOP + 14 * S - y) / (14 * S)) ** 2)
    ys = [TRUNK_TOP + (GROUND - TRUNK_TOP) * j / 8 for j in range(9)]
    p.curve([(CX + flare(y) + rng.uniform(-0.2, 0.2), y) for y in ys], cls="bold" if i in (0, 6) else "line")

for a, ln in ((-1.02, 50), (-0.36, 46), (0.30, 47), (0.98, 50)):
    limb(CX + a * 13 * S, TRUNK_TOP + 2 + abs(a) * 3 * S, a, ln * S, 6, up=True)

# the roots, where the trunk meets the ground
for a, ln in ((-1.38, 8), (1.32, 11)):                   # surface roots, reaching along the ground
    limb(CX + a * 9 * S, GROUND + 0.3, a, ln, 2, up=False)

# what the oak covers, so the horizon and the grass go behind it
import re as _re
_xy = [tuple(map(float, m)) for part in p.parts[OAK0:] for m in _re.findall(r"(-?[\d.]+) (-?[\d.]+)", part)]
OX0, OX1 = min(x for x, _ in _xy), max(x for x, _ in _xy)
OY0 = min(y for _, y in _xy)
print("oak bbox", round(OX0), round(OX1), round(OY0), round(GROUND), "trunk", round(CX))

# the horizon, broken where the river meets it
hx = course(1.0)
for a, b in ((14, hx - 8), (hx + 8, OX0 - 3), (OX1 + 3, 310)):
    if b - a > 6:
        p.stroke(lambda x: HZ, a, b, cls="hair", wobble=0.25)

# grass, thinning toward the horizon
for _ in range(70):
    gx = rng.uniform(16, 308)
    gy = rng.uniform(HZ + 14, YB - 4)
    t = 1 - ((gy - HZ) / (YB - HZ)) ** (1 / 1.75)
    lo, hi = page(t * L, -(HALF + 22))[0], page(t * L, HALF + 22)[0]
    if lo - 4 < gx < hi + 4 or (OX0 - 2 < gx < OX1 + 2 and gy < GROUND + 6):
        continue
    sz = 0.5 + 0.6 * (gy - HZ) / (YB - HZ)
    for k in (-1, 0, 1):
        p.straight(gx + k * 1.6 * sz, gy, gx + k * 3.0 * sz + rng.uniform(-0.5, 0.5), gy - rng.uniform(3.2, 5.2) * sz, cls="hair")

# ---- the sun, over the far country, its light reaching the oak --------------
SUN = (70, 48)
R = 15
p.parts.append(f'<circle class="ink line" cx="{SUN[0]}" cy="{SUN[1]}" r="{R}"/>')
CROWN = ((OX0 + OX1) / 2, (OY0 + TRUNK_TOP) / 2)
CROWN_R = (OX1 - OX0) / 2 * 0.92
toward = math.atan2(CROWN[1] - SUN[1], CROWN[0] - SUN[0])     # the direction of the crown
LIT = 0.10
rays = 36
for k in range(rays):
    a = math.tau * k / rays
    if abs(((a - toward + math.pi) % math.tau) - math.pi) < LIT + 0.06:
        continue
    r1 = R + (15 if k % 2 else 9)
    p.seg(SUN[0] + (R + 5) * math.cos(a), SUN[1] + (R + 5) * math.sin(a),
          SUN[0] + r1 * math.cos(a), SUN[1] + r1 * math.sin(a), wobble=0.0)
beams = 7
for k in range(beams):
    off = -LIT + 2 * LIT * k / (beams - 1)
    a = toward + off
    dx, dy = math.cos(a), math.sin(a)
    ex, ey = SUN[0] - CROWN[0], SUN[1] - CROWN[1]
    rx, ry = CROWN_R, (TRUNK_TOP - OY0) / 2
    qa = (dx / rx) ** 2 + (dy / ry) ** 2
    qb = 2 * (ex * dx / rx ** 2 + ey * dy / ry ** 2)
    qc = (ex / rx) ** 2 + (ey / ry) ** 2 - 1
    disc = max(qb * qb - 4 * qa * qc, 0)
    t, end = R + 5, (-qb - math.sqrt(disc)) / (2 * qa) - rng.uniform(1, 5)
    while t < end:
        e = min(t + rng.uniform(30, 60), end)
        p.seg(SUN[0] + dx * t, SUN[1] + dy * t, SUN[0] + dx * e, SUN[1] + dy * e, cls="hair", wobble=0.1)
        t = e + rng.uniform(5, 8)

write_interlude(p, "frontispiece-a-the-wide-view",
                "Flow with wisdom, stand with courage,<br>and love with warmth.")
