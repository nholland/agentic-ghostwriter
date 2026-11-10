"""The Courage to Come Back (Chapter 5).

The same man walks in both times. If he goes quiet, he walks out smaller,
with the outline of his full size still standing around him and the real
thing left dotted in the air. If he goes back, he walks out the same
size, and the real thing is one solid line.
"""
from platekit import Plate, W, write

p = Plate(height=226, seed=59, title="The Courage to Come Back")

X_IN, X_OUT = 66, 258
H = 60                     # his full height

BODY = [(-7.2, 0), (-5.9, -12), (-6.5, -24), (-5.6, -31.5), (-2.4, -35), (2.4, -35),
        (5.6, -31.5), (6.5, -24), (5.9, -12), (7.2, 0)]


def man(x, floor, s=1.0, cls="line"):
    s *= 1.3
    r = 4.5 * s
    p.curve([(x + px * s, floor + py * s) for px, py in BODY], cls=cls)
    p.parts.append(f'<circle class="ink {cls}" cx="{x:.2f}" cy="{floor - 46 * s + r:.2f}" r="{r:.2f}"/>')


def row(y0, name, line, said, thing):
    floor = y0 + 80
    p.label(1, y0, name)
    p.label(W, y0 + 0.6, line, cls="ital", anchor="end")
    p.straight(X_IN - 40, floor, X_OUT + 40, floor)

    man(X_IN, floor)
    if said:
        man(X_OUT, floor)
        chest = floor - 36
    else:
        man(X_OUT, floor, cls="line dotted")           # the size he walked in at
        man(X_OUT, floor, s=0.58, cls="line knock")    # the size he walks out
        chest = floor - 36 * 0.58

    # the real thing, spoken back across the room, or not
    drift = p._noise(0.9, 60)
    p.stroke(lambda x: chest + drift(x) - drift(X_OUT - 16), X_IN + 26, X_OUT - 16,
             cls="bold" if said else "bold dotted", wobble=0.0)
    p.label((X_IN + X_OUT) / 2 + 5, chest - 7, thing, cls="ital", anchor="middle")

    p.label(X_IN, floor + 14.5, "walks in", cls="ital", anchor="middle")
    p.label(X_OUT, floor + 14.5, "walks out", cls="ital", anchor="middle")


row(9, "Goes quiet", "he becomes small without deciding to", said=False, thing="the real thing, never said")
row(132, "Goes back", "he leaves the fight the same size", said=True, thing="the real thing, said")

write(p, "plate-05-the-courage-to-come-back",
      deck="A pause is only healthy if you come back.",
      caption="Say the real thing before silence says it for you.")
