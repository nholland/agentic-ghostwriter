"""Frontispiece: the opening plate.

One landscape holding all three. The sun is coming up on the horizon.
The river runs from it toward the reader, widening, with a stone in its
path. The oak stands on the near bank.
"""
import math
from platekit import Plate, W, write_interlude
from scenery import oak, sun

p = Plate(height=372, seed=523, title="River, Oak, Sun")
rng = p.rng

HORIZON, BOTTOM = 132, 368
SUN_X = 228
STONES = [(0.22, 296, 15), (-0.5, 336, 10)]            # how far across the river, how far down the page, radius


def depth(y):
    return (y - HORIZON) / (BOTTOM - HORIZON)             # 0 at the horizon, 1 at the reader's feet


def course(y):
    t = depth(y)
    return SUN_X - 6 + 58 * t ** 0.85 * math.sin(2.05 * math.pi * t ** 0.62 + 0.25)


def breadth(y):
    return 2.5 + 86 * depth(y) ** 1.55


def stone_x(fs, sy):
    return course(sy) + fs * breadth(sy)


def flow_x(f, y):
    """x of the line that keeps fraction f of the way across the river, parting round the stones."""
    x = course(y) + f * breadth(y)
    for fs, sy, r in STONES:
        d = (f - fs) * breadth(sy)                                # which side of the stone this line passes, for good
        reach = (r + 4) * math.exp(-abs(d) / (1.45 * r))
        length = 2.8 * r if y < sy else 1.3 * r                   # the water comes toward us: it parts above the stone
        x += math.copysign(reach, d if d else 1) * math.exp(-((y - sy) / length) ** 2)
    return x


# the sun, half risen, and the land it rises over
sun(p, SUN_X, HORIZON, 23, skip=lambda a: math.sin(a) > -0.08, rays=40, long=24, short=13)
p.parts.append(f'<rect class="knock" x="0" y="{HORIZON}" width="{W}" height="40"/>')      # hide the lower half
hill = p._noise(2.2, 120)
p.stroke(lambda x: HORIZON + hill(x) * 0.5, 186, W - 4, wobble=0.15)
p.stroke(lambda x: HORIZON + hill(x) * 0.5, 4, 186, cls="hair", wobble=0.15)
far = p._noise(3.0, 90)
p.stroke(lambda x: HORIZON - 9 - 7 * math.sin((x - 250) / 60) + far(x), 262, W - 6, cls="hair", wobble=0.2)

# the river
N = 13
for i in range(N):
    f = -0.88 + 1.76 * i / (N - 1)
    back = {6: 0.03, 3: 0.11, 9: 0.11, 1: 0.18, 5: 0.18, 7: 0.18, 11: 0.18}.get(i, 0.26)   # few lines reach the horizon
    y = HORIZON + back * (BOTTOM - HORIZON) + rng.uniform(0, 6)
    tremor = p._noise(0.4, 80)
    while y < BOTTOM - 4:
        end = min(y + rng.uniform(40, 120), BOTTOM - rng.uniform(0, 8))
        pts, t = [], y
        while t <= end:
            pts.append((flow_x(f, t) + tremor(t), t))
            t += 4
        if len(pts) > 2:
            p.curve(pts)
        y = end + rng.uniform(4, 7)
for side in (-1, 1):                                              # its banks
    edge = p._noise(1.2, 70)
    pts = [(course(y) + side * (breadth(y) * 1.07 + 1.5 + edge(y) * depth(y)), y) for y in range(HORIZON + 1, BOTTOM + 1, 5)]
    p.curve(pts)
for fs, sy, r in STONES:
    sx = stone_x(fs, sy)
    k = 14
    lump = [rng.uniform(-0.1, 0.1) for _ in range(k)]
    ring = [(sx + r * (1 + lump[j % k]) * 1.15 * math.cos(math.tau * j / k), sy + r * (1 + lump[j % k]) * 0.74 * math.sin(math.tau * j / k)) for j in range(k + 1)]
    p.curve(ring, cls="bold knock")
    p.curve([(sx - r * 0.5, sy - r * 0.3), (sx - r * 0.05, sy - r * 0.42), (sx + r * 0.45, sy - r * 0.28)], cls="hair")

# the oak on the near bank
OAK_X, OAK_Y = 84, 240
p.straight(OAK_X - 34, OAK_Y, OAK_X + 30, OAK_Y)
oak(p, OAK_X, OAK_Y, scale=0.5)

# grass on both banks, taller as it comes near
for _ in range(46):
    gy = rng.uniform(HORIZON + 14, BOTTOM - 2)
    side = rng.choice((-1, 1))
    gx = course(gy) + side * (breadth(gy) * 1.07 + rng.uniform(10, 120))
    if not 6 < gx < W - 6 or (abs(gx - OAK_X) < 24 and gy < OAK_Y + 4 and gy > OAK_Y - 60):
        continue
    h = 2.2 + 4.2 * depth(gy)
    for k in (-1, 0, 1):
        p.straight(gx + k * 1.5, gy, gx + k * 2.8 + rng.uniform(-0.5, 0.5), gy - h * rng.uniform(0.8, 1.1), cls="hair")

write_interlude(p, "frontispiece", "Flow with wisdom.<br>Stand with courage.<br>Love with warmth.")
