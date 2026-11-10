"""Interlude, Part II: the sturdy oak.

"The storm comes through, and in the morning the oak is still there."
A broad oak the morning after: bare, one limb down on the ground, the
trunk and the roots untouched. The roots go as deep as the crown is
tall.
"""
import math
from platekit import Plate, W, write_interlude

p = Plate(height=338, seed=317, title="The sturdy oak")
rng = p.rng

GROUND, CX = 222, 162


def limb(x, y, angle, length, depth, up=True, bundle=0.0):
    """Grow one limb and its children. angle is measured from straight up (or straight down for roots)."""
    sign = -1 if up else 1
    bend = rng.uniform(-0.22, 0.22)
    pts = []
    for i in range(5):
        t = i / 4
        a = angle + bend * t
        pts.append((x + math.sin(a) * length * t, y + sign * math.cos(a) * length * t))
    cls = "bold" if depth >= 5 else "line" if depth >= 3 else "hair"
    p.curve(pts, cls=cls)
    ex, ey = pts[-1]
    if depth == 0:
        return
    kids = 3 if depth >= 4 and rng.random() < 0.55 else 2
    spread = (0.62 if up else 0.8)
    for k in range(kids):
        off = (k - (kids - 1) / 2) * spread + rng.uniform(-0.16, 0.16)
        a = (angle + bend) * 0.82 + off
        if up:                                             # oak limbs reach out more than up
            a += 0.10 * math.copysign(1, a) if abs(a) < 1.25 else 0
            a = max(-1.75, min(1.75, a))
        else:
            a = max(-1.42, min(1.42, a))
        limb(ex, ey, a, length * rng.uniform(0.66, 0.78), depth - 1, up)


# the ground
p.straight(18, GROUND, 306, GROUND)

# the trunk: tone from close lines, flaring into the roots and the first limbs
TRUNK_TOP = GROUND - 54
for i in range(9):
    off = (i - 4) * 3.3
    flare = lambda y, off=off: off * (1 + 1.5 * max(0, (y - (GROUND - 16)) / 16) ** 2 + 0.6 * max(0, (TRUNK_TOP + 14 - y) / 14) ** 2)
    pts = [(CX + flare(y) + rng.uniform(-0.25, 0.25), y) for y in range(TRUNK_TOP, GROUND + 1, 6)]
    p.curve(pts, cls="bold" if i in (0, 8) else "line")

# the crown
for a, ln in ((-1.02, 50), (-0.36, 46), (0.30, 47), (0.98, 50)):
    limb(CX + a * 13, TRUNK_TOP + 2 + abs(a) * 3, a, ln, 6, up=True)

# the roots: as deep as the crown is tall
for a, ln in ((-1.12, 40), (-0.42, 36), (0.38, 36), (1.08, 40)):
    limb(CX + a * 17, GROUND + 1, a, ln, 5, up=False)

# what the storm took: one limb on the ground
bx, by = 250, GROUND - 2.5
p.curve([(bx - 26, by + 1), (bx - 8, by - 2.5), (bx + 10, by - 1.5), (bx + 30, by + 1.5)], cls="line")
p.curve([(bx - 4, by - 2.5), (bx + 4, by - 9), (bx + 15, by - 12)], cls="hair")
p.curve([(bx + 10, by - 1.5), (bx + 18, by - 6), (bx + 27, by - 6)], cls="hair")
p.curve([(bx - 14, by - 1), (bx - 20, by - 7), (bx - 28, by - 8)], cls="hair")

write_interlude(p, "interlude-2-the-sturdy-oak",
                "The storm comes through,<br>and in the morning the oak is still there.")
