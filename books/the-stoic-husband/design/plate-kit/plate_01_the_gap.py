"""The Gap (Chapter 1).

What she says arrives as a current. In the gap it keeps running, dotted,
toward the old worn channel (inherited) unless a single line is started
on purpose (chosen). The gap is drawn as open paper, three seconds wide.
"""
from platekit import Plate, W, ease, write

p = Plate(height=176, seed=11, title="The Gap")
rng = p.rng

MID = 88            # y of the incoming current
GAP0, GAP1 = 118, 206
N = 9               # lines in the current
PIVOT = (176, MID)  # where the choice is made, two-thirds through the gap


def rut_center(x):                      # the inherited channel sinks to the right
    return MID + 56 * ease((x - 168) / (W - 168))


def rut_spacing(x):                     # ...and its lines pack tighter: worn in
    return 3.0 - 1.5 * ease((x - GAP0) / (W - GAP0))


swell = p._noise(1.3, 90)               # one shared slow wave so the lines move together

for i in range(N):
    off = i - (N - 1) / 2
    # 1. what she says: open on the left, gathering toward the gap
    incoming = lambda x, off=off: MID + off * (3.0 + 1.6 * (1 - x / GAP0)) + swell(x)
    p.stroke(incoming, rng.uniform(0, 16), GAP0 - 1.5)
    # 2. through the gap: the same lines, not yet said
    through = lambda x, off=off: rut_center(x) + off * rut_spacing(x) + swell(x) * (1 - ease((x - GAP0) / 60))
    p.stroke(through, GAP0 + 1.5, GAP1 - 1.5, cls="line dotted", wobble=0.1)
    # 3. inherited: the old channel
    p.stroke(through, GAP1 + 1.5, W - rng.uniform(0, 14), wobble=0.3)

# chosen: one deliberate line leaving the current
chosen = lambda x: PIVOT[1] - 52 * ease((x - PIVOT[0]) / (W - PIVOT[0] + 30))
p.stroke(chosen, PIVOT[0], W - 3, cls="bold", wobble=0.12)
p.ring(*PIVOT, r=3.1)

# the measure: three seconds
my = 134
p.straight(GAP0, my, GAP1, my)
for k in range(4):
    x = GAP0 + (GAP1 - GAP0) * k / 3
    p.straight(x, my - 2.6, x, my + 2.6)
p.label((GAP0 + GAP1) / 2, my + 13, "three seconds", cls="ital", anchor="middle")

# lettering: caps for what is given, italic for what moves
p.label(1, MID - 27, "What she says")
p.label(W, MID + 4, "What you say next", anchor="end")
p.label(W, 32, "chosen", cls="ital", anchor="end")
p.label(W, 170, "inherited", cls="ital", anchor="end")

write(p, "plate-01-the-gap",
      deck="Between what she says and what you say next are three seconds.",
      caption="Your marriage lives there.")
