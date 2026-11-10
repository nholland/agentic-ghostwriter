"""Interlude, Part III: the warm sun.

"Everything alive leans toward the light. What it reaches, opens."
The sun stands over a row of flowers. Every stem leans toward it. Where
its light falls, the flowers are open; beyond it, they are still shut.
"""
import math
from platekit import Plate, W, write_interlude

p = Plate(height=330, seed=419, title="The warm sun")
rng = p.rng

SUN = (162, 62)
R = 21
GROUND = 316
LIT = 0.35                                  # half-angle of the light that reaches the ground, in radians

# the sun
p.parts.append(f'<circle class="ink bold" cx="{SUN[0]}" cy="{SUN[1]}" r="{R}"/>')
rays = 36
for k in range(rays):
    a = math.tau * k / rays
    ang_from_down = abs(((a - math.pi / 2 + math.pi) % math.tau) - math.pi)     # 0 when the ray points straight down
    if ang_from_down < LIT + 0.06:
        continue                                                              # those are drawn below, reaching the ground
    r1 = R + (19 if k % 2 else 11)
    p.seg(SUN[0] + (R + 6) * math.cos(a), SUN[1] + (R + 6) * math.sin(a),
          SUN[0] + r1 * math.cos(a), SUN[1] + r1 * math.sin(a), wobble=0.0)

# the light that reaches the ground
beams = 13
for k in range(beams):
    off = -LIT + 2 * LIT * k / (beams - 1)
    dx, dy = math.sin(off), math.cos(off)
    start = R + 6
    end = (GROUND - 58 - SUN[1]) / dy - rng.uniform(0, 10)
    t = start
    while t < end:                                         # long strokes with breaths, like the river
        e = min(t + rng.uniform(40, 95), end)
        p.seg(SUN[0] + dx * t, SUN[1] + dy * t, SUN[0] + dx * e, SUN[1] + dy * e, cls="hair", wobble=0.1)
        t = e + rng.uniform(5, 9)

# the flowers
p.straight(16, GROUND, 308, GROUND)
N = 13
for i in range(N):
    x = 30 + (W - 60) * i / (N - 1) + rng.uniform(-3, 3)
    h = rng.uniform(34, 46)
    toward = math.atan2(SUN[0] - x, GROUND - SUN[1])
    lean = math.tan(toward) * h * 0.55                       # every stem leans toward the sun
    tip = (x + lean, GROUND - h)
    p.curve([(x, GROUND), (x + lean * 0.12, GROUND - h * 0.45), (x + lean * 0.55, GROUND - h * 0.8), tip])
    # a leaf or two
    for side, at in ((1, 0.38), (-1, 0.58)):
        lx, ly = x + lean * (0.1 + at * 0.4), GROUND - h * at
        p.curve([(lx, ly), (lx + side * 5.5, ly - 4.5), (lx + side * 9, ly - 2.2)], cls="line")
        p.curve([(lx, ly), (lx + side * 5.0, ly - 0.6), (lx + side * 9, ly - 2.2)], cls="hair")

    reached = abs(math.atan2(tip[0] - SUN[0], tip[1] - SUN[1])) < LIT + 0.03
    face = math.atan2(SUN[0] - tip[0], tip[1] - SUN[1])      # the flower turns its face to the sun
    if reached:                                              # open
        petals = 9
        for k in range(petals):
            a = -math.pi / 2 + face + (k - (petals - 1) / 2) * 0.36
            p.seg(tip[0] + 2.6 * math.cos(a), tip[1] + 2.6 * math.sin(a),
                  tip[0] + 8.5 * math.cos(a), tip[1] + 8.5 * math.sin(a), wobble=0.0)
        p.dot(tip[0], tip[1], r=1.6)
    else:                                                    # still shut
        a = -math.pi / 2 + face
        ux, uy = math.cos(a), math.sin(a)
        px, py = -uy, ux
        bud = [(tip[0] + px * 0.2, tip[1] + py * 0.2), (tip[0] + ux * 3.5 + px * 2.5, tip[1] + uy * 3.5 + py * 2.5),
               (tip[0] + ux * 8.5, tip[1] + uy * 8.5), (tip[0] + ux * 3.5 - px * 2.5, tip[1] + uy * 3.5 - py * 2.5),
               (tip[0] - px * 0.2, tip[1] - py * 0.2)]
        p.curve(bud)

write_interlude(p, "interlude-3-the-warm-sun", "What it reaches, opens.")
