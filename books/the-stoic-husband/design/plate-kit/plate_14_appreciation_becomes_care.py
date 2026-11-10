"""Appreciation becomes care (Chapter 14).

"The grass is greener where you water it." A watering can, tipped to
pour. The water leaves the rose in fine arcs and the grass stands tall
and thick exactly where it lands, thinning out on either side.
"""
import math
from platekit import Plate, W, write

p = Plate(height=170, seed=113, title="Appreciation becomes care")
rng = p.rng

GROUND = 148
CENTRE = (70, 42)                      # middle of the can's body
TILT = math.radians(30)
COS, SIN = math.cos(TILT), math.sin(TILT)


def at(x, y):
    """Can coordinates (upright, origin at the base, y up is negative) to the page, tipped."""
    y += 17
    return (CENTRE[0] + x * COS - y * SIN, CENTRE[1] + x * SIN + y * COS)


def turn(dx, dy):
    return (dx * COS - dy * SIN, dx * SIN + dy * COS)


def shape(pts, cls="line", smooth=False):
    pts = [at(*q) for q in pts]
    if smooth:
        p.curve(pts, cls=cls)
    else:
        p.parts.append(f'<path class="ink {cls}" d="M' + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + '"/>')


# --- the can ---------------------------------------------------------------
shape([(-19, -34), (-22, 0)])                                   # back wall
shape([(19, -34), (22, 0)])                                     # front wall
shape([(-22, 0), (-11, 2.0), (0, 2.6), (11, 2.0), (22, 0)], smooth=True)          # base
shape([(-19, -34), (-10, -35.6), (0, -36.1), (10, -35.6), (19, -34)], smooth=True)  # rim
shape([(-19, -34), (-10, -32.3), (0, -31.8), (10, -32.3), (19, -34)], cls="hair", smooth=True)
shape([(-19.6, -27), (-29, -29.5), (-36.5, -24), (-37.5, -14), (-32, -7), (-21.4, -7)], smooth=True)   # handle

DIR = (math.cos(math.radians(25)), -math.sin(math.radians(25)))    # the spout rises at 25 degrees
PERP = (-DIR[1], DIR[0])
along = lambda d, off: (21 + DIR[0] * d + PERP[0] * off, -12 + DIR[1] * d + PERP[1] * off)
shape([along(-1, 3.8), along(50, 2.4)])                             # spout, lower edge
shape([along(1, -3.8), along(50, -2.4)])                            # spout, upper edge
shape([along(50, 2.4), along(57, 8.5)])                             # the rose flares out
shape([along(50, -2.4), along(57, -8.5)])
shape([along(57, 8.5), along(57, -8.5)], cls="bold")                # its face

# --- the water -------------------------------------------------------------
out = turn(*DIR)                                                   # which way the rose points once tipped
land = []
for i in range(7):
    u = -1 + 2 * i / 6
    x0, y0 = at(*along(58.2, u * 7.2))
    speed = 22 - 7 * u + rng.uniform(-0.6, 0.6)                   # the top of the rose throws furthest
    arc, t = [], 0.0
    while True:
        x, y = x0 + out[0] * speed * t, y0 + out[1] * speed * t + 27 * t * t
        if y > GROUND - 20:
            break
        arc.append((x, y))
        t += 0.1
    land.append(arc[-1][0])
    p.curve(arc[: len(arc) // 2 - 1])                               # each stream breaks once as it falls
    p.curve(arc[len(arc) // 2 + 1:])
WET = sum(land) / len(land)

# --- the grass: tall and thick where the water lands -------------------------
p.straight(20, GROUND, 304, GROUND)
x = 26.0
while x < 300:
    wet = math.exp(-((x - WET) / 36) ** 2)
    h = 4.5 + 24 * wet + rng.uniform(-1.3, 1.3)
    bend = rng.uniform(-0.3, 0.3) * h
    p.curve([(x, GROUND), (x + bend * 0.22, GROUND - h * 0.55), (x + bend, GROUND - h)])
    x += 2.2 + 5.6 * (1 - wet) + rng.uniform(-0.4, 0.4)

p.label(50, 96, "appreciation", cls="ital", anchor="middle")
p.label(WET + 30, 92, "attention and care", cls="ital")
p.label(WET, GROUND + 15, "the woman already there", cls="ital", anchor="middle")

write(p, "plate-14-appreciation-becomes-care",
      deck="Notice what you value in your wife.",
      caption="The grass is greener where you water it.")
