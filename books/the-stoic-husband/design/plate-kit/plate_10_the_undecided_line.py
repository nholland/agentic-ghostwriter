"""The Undecided Line (Chapter 10).

A boundary drawn as what it is: a fence. On the left it stands around
nothing he can name, and it has folded. On the right it stands around a
young tree, and it holds. The tree is the one bold thing: what it protects.
"""
import math
from platekit import Plate, W, write

p = Plate(height=140, seed=101, title="The Undecided Line")
rng = p.rng

BASE, PICKET_H, N, GAP = 118, 41, 7, 12


def fence(cx, lean_deg):
    """A picket fence seen face on, folded over by lean_deg."""
    a = math.radians(lean_deg)
    sx, sy = math.sin(a), math.cos(a)
    at = lambda x, h: (x + h * sx, BASE - h * sy)          # a point h up a picket standing at x
    x0 = cx - (N - 1) * GAP / 2
    for h in (PICKET_H * 0.3, PICKET_H * 0.72):             # two rails, behind the pickets
        p.seg(*at(x0 - 7.5, h), *at(x0 + (N - 1) * GAP + 7.5, h), wobble=0.08)
    for i in range(N):
        x = x0 + i * GAP
        pts = [at(x - 3.0, 0), at(x - 3.0, PICKET_H - 4.4), at(x, PICKET_H), at(x + 3.0, PICKET_H - 4.4), at(x + 3.0, 0)]
        d = "M" + " L".join(f"{px:.2f} {py:.2f}" for px, py in pts)
        p.parts.append(f'<path class="ink line knock" d="{d}"/>')


def tree(cx):
    top = BASE - 66
    p.seg(cx, BASE - 2, cx + 0.6, top + 6, cls="bold", wobble=0.25)
    p.seg(cx + 0.3, top + 19, cx - 9, top + 4, cls="bold", wobble=0.1)
    p.seg(cx + 0.4, top + 13, cx + 8, top + 1, cls="bold", wobble=0.1)
    ring = []
    for k in range(13):                                     # a loose crown
        t = math.tau * k / 12
        r = 23 + rng.uniform(-1.6, 1.6) + 1.4 * math.sin(3 * t)
        ring.append((cx + r * math.cos(t), top - 10 + r * 0.86 * math.sin(t)))
    ring[-1] = ring[0]
    p.curve(ring, cls="bold")


for cx, name, decided in ((81, "Undecided", False), (243, "Decided", True)):
    p.label(cx, 9, name, anchor="middle")
    p.straight(cx - 62, BASE, cx + 62, BASE)
    if decided:
        tree(cx)
        fence(cx, 0)
        p.label(cx, BASE + 15, "what it protects", cls="ital", anchor="middle")
    else:
        fence(cx - 9, 40)
        p.label(cx - 16, BASE + 15, "this protects", cls="ital", anchor="middle")
        p.straight(cx + 11, BASE + 15.6, cx + 44, BASE + 15.6)

write(p, "plate-10-the-undecided-line",
      deck="If you cannot name what it protects, it is probably a preference.",
      caption="")
