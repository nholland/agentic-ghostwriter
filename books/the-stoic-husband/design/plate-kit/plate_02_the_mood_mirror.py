"""The Mood Mirror (Chapter 2).

Her weather is the same in both rows. Above, his line is its reflection,
so the storm is on the page twice. Below, his line keeps its own gentle
motion: steady, but not flat, because the point is not to go cold.
"""
import math
from platekit import Plate, W, ease, write

p = Plate(height=176, seed=23, title="The Mood Mirror")
X0, X1 = 0, 246          # the lines stop short so the right margin can carry the italic labels


def storm(x):
    """Her weather: calm at the door, building across the evening."""
    build = 0.6 + 10.5 * ease((x - 8) / 105)
    return build * (0.6 * math.sin(x / 8.6 + 0.4) + 0.3 * math.sin(x / 4.3 + 2.0) + 0.12 * math.sin(x / 2.6 + 5.0))


def her(y):
    for off in (-2.3, 0, 2.3):                       # three close lines: a weather front
        p.stroke(lambda x, off=off: y + off + storm(x), X0, X1 - abs(off) * 1.5, wobble=0.15, step=1.5)


# Row 1: he mirrors her
AXIS = 52
her(AXIS - 14)
p.stroke(lambda x: AXIS + 14 - storm(x), X0, X1, cls="bold", wobble=0.1, step=1.5)
p.label(1, 12, "Her weather")
p.label(W, AXIS + 2.8, "the storm doubles", cls="ital", anchor="end")

# Row 2: he brings his own
Y2 = 132
her(Y2)
own = p._noise(1.1, 150)
p.stroke(lambda x: Y2 + 27 + own(x), X0, X1, cls="bold", wobble=0.0, step=8.0)
p.label(1, Y2 - 22, "Her weather")
p.label(W, Y2 + 29.8, "your own weather", cls="ital", anchor="end")

write(p, "plate-02-the-mood-mirror",
      deck="When her mood sets your mood, you&#8217;ve outsourced your peace.",
      caption="Not to go cold. To bring something real through the door.")
