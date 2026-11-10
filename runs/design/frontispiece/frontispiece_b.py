"""Frontispiece, option B: the close view.

We stand on the near bank. The river passes at our feet, parts around a
stone and closes up again. On the far bank the oak stands square to us, its
roots in the cut bank reaching down toward the water. The sun stands over
its crown, and the light that reaches the oak falls on it.

Bold: the sun's disc, drawn as interlude 3 draws it. The oak and the river
are the larger shapes; the one heavy ring at the top is what the eye starts
from, and the light runs down from it through the tree to the water.
"""
import math
import re
from platekit import Plate, W, write_interlude

p = Plate(height=414, seed=707, title="River, Oak, Sun")
rng = p.rng

CX = 162
GROUND = 292                 # the far bank's top
WATER = 318                  # where the far bank meets the river

# ---- the oak, as interlude 2 draws it, on the far bank ---------------------


def limb(x, y, angle, length, depth, up=True):
    sign = -1 if up else 1
    bend = rng.uniform(-0.22, 0.22)
    pts = []
    for i in range(5):
        t = i / 4
        a = angle + bend * t
        pts.append((x + math.sin(a) * length * t, y + sign * math.cos(a) * length * t))
    cls = "line" if depth >= 3 else "hair"
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
S = 0.8
TRUNK_TOP = GROUND - 54 * S
for i in range(9):
    off = (i - 4) * 3.3 * S
    flare = lambda y, off=off: off * (1 + 1.5 * max(0, (y - (GROUND - 16 * S)) / (16 * S)) ** 2
                                      + 0.6 * max(0, (TRUNK_TOP + 14 * S - y) / (14 * S)) ** 2)
    ys = [TRUNK_TOP + (GROUND - TRUNK_TOP) * j / 9 for j in range(10)]
    p.curve([(CX + flare(y) + rng.uniform(-0.25, 0.25), y) for y in ys])
for a, ln in ((-1.02, 50), (-0.36, 46), (0.30, 47), (0.98, 50)):
    limb(CX + a * 13 * S, TRUNK_TOP + 2 + abs(a) * 3 * S, a, ln * S, 6, up=True)
_xy = [tuple(map(float, m)) for part in p.parts[OAK0:] for m in re.findall(r"(-?[\d.]+) (-?[\d.]+)", part)]
OX0, OX1, OY0 = min(x for x, _ in _xy), max(x for x, _ in _xy), min(y for _, y in _xy)
print("crown", round(OX0), round(OX1), round(OY0), "trunk top", round(TRUNK_TOP))

# the far bank: its top, its cut face, and the roots going down it to the water
p.straight(18, GROUND, 306, GROUND, cls="line")
for a, ln in ((-1.0, 12), (-0.4, 11), (0.35, 11), (0.95, 12)):
    limb(CX + a * 15 * S, GROUND + 0.5, a, ln, 3, up=False)
for row, y in enumerate((GROUND + 9, GROUND + 18)):          # the face of the bank, broken, as interlude 1 draws a bank's rise
    x = 22 + rng.uniform(0, 14)
    while x < 300:
        e = min(x + rng.uniform(16, 38), 302)
        if not (CX - 52 < x < CX + 52 or CX - 52 < e < CX + 52):
            p.stroke(lambda xx, y=y: y, x, e, cls="hair", wobble=0.25)
        x = e + rng.uniform(10, 24)

# ---- the river, as interlude 1 draws it, seen from its near bank -----------
HALF = 50
Q = 0.62                                   # seen from the bank: the breadth foreshortened
RC = WATER + (HALF + 5) * Q
STONES = [(118, 6, 15)]


def across(base, s):
    v = base
    for ss, sv, r in STONES:
        d = base - sv
        reach = (r + 5) * math.exp(-abs(d) / (1.45 * r))
        length = 1.2 * r if s < ss else 3.2 * r
        v += math.copysign(reach, d if d else 1) * math.exp(-((s - ss) / length) ** 2)
    limit = HALF + 22
    return limit * math.tanh(v / limit)


def page(s, v):
    return (s, RC + v * Q)


N = 15
for i in range(N):
    base = -HALF + 6 + (2 * HALF - 12) * i / (N - 1)
    tremor = p._noise(0.35, 90)
    s = 8 + rng.uniform(0, 14)
    while s < 310:
        end = min(s + rng.uniform(95, 210), 316 - rng.uniform(0, 10))
        pts, t = [], s
        while t <= end:
            pts.append(page(t, across(base, t) + tremor(t)))
            t += 4
        if len(pts) > 2:
            p.curve(pts)
        s = end + rng.uniform(4, 7)

edge = p._noise(1.2, 80)
p.stroke(lambda s: WATER + edge(s), 8, 316, wobble=0.2)               # the far water's edge
edge2 = p._noise(1.6, 80)
NEAR = RC + (HALF + 5) * Q
p.stroke(lambda s: NEAR + edge2(s), 8, 316, wobble=0.2)               # the near bank, where we stand

for ss, sv, r in STONES:
    cx, cy = page(ss, sv)
    k = 14
    lump = [rng.uniform(-0.1, 0.1) for _ in range(k)]
    ring = []
    for j in range(k + 1):
        t = math.tau * j / k
        rr = r * (1 + lump[j % k])
        ring.append((cx + rr * 1.12 * math.cos(t), cy + rr * 0.84 * Q * math.sin(t)))
    p.curve(ring, cls="line knock")
    p.curve([(cx - r * 0.5, cy - r * 0.42 * Q), (cx - r * 0.05, cy - r * 0.56 * Q), (cx + r * 0.45, cy - r * 0.4 * Q)], cls="hair")

# grass, on the near bank and on the far bank either side of the oak
for _ in range(30):
    if rng.random() < 0.5:
        gx, gy = rng.uniform(14, 310), rng.uniform(NEAR + 9, p.h - 4)
    else:
        gx, gy = rng.uniform(20, 304), GROUND - rng.uniform(1, 6)
        if OX0 - 4 < gx < OX1 + 4 and gy > TRUNK_TOP - 30 and abs(gx - CX) < 40:
            continue
    for k in (-1, 0, 1):
        p.straight(gx + k * 1.6, gy, gx + k * 3.0 + rng.uniform(-0.6, 0.6), gy - rng.uniform(3.2, 5.2), cls="hair")

# ---- the sun over the crown, its light reaching the tree --------------------
SUN = (CX, 40)
R = 19
p.parts.append(f'<circle class="ink bold" cx="{SUN[0]}" cy="{SUN[1]}" r="{R}"/>')
LIT = 0.42
rays = 36
for k in range(rays):
    a = math.tau * k / rays
    if abs(((a - math.pi / 2 + math.pi) % math.tau) - math.pi) < LIT + 0.06:
        continue
    r1 = R + (17 if k % 2 else 10)
    p.seg(SUN[0] + (R + 6) * math.cos(a), SUN[1] + (R + 6) * math.sin(a),
          SUN[0] + r1 * math.cos(a), SUN[1] + r1 * math.sin(a), wobble=0.0)

beams = 13
for k in range(beams):
    off = -LIT + 2 * LIT * k / (beams - 1)
    dx, dy = math.sin(off), math.cos(off)
    # the beam stops where it first meets a twig of the crown
    hits = [(x - SUN[0]) * dx + (y - SUN[1]) * dy for x, y in _xy
             if abs((x - SUN[0]) * dy - (y - SUN[1]) * dx) < 4 and y < TRUNK_TOP]
    end = min(hits) - rng.uniform(1.5, 4)
    t = R + 6
    while t < end:
        e = min(t + rng.uniform(25, 50), end)
        p.seg(SUN[0] + dx * t, SUN[1] + dy * t, SUN[0] + dx * e, SUN[1] + dy * e, cls="hair", wobble=0.1)
        t = e + rng.uniform(4, 7)

write_interlude(p, "frontispiece-b-the-close-view", "")
