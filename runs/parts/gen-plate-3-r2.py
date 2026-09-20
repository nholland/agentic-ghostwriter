"""Part III closing plate, round 2: the opening drawn plainly.

Round 1 drew twenty nested day arcs and, rendered at page size, read as a dome
or a fingerprint (Reader Panel, 2026-09-20). This keeps the set's line
vocabulary from plates 1 and 2 - a field of stacked layers, one weight, black
on white - and draws the opening instead: from one point low on the page the
layers part, and every layer laid down above it parts a little wider, its inner
end lifting toward the opening.

Carries the Part III page's own sentence "Everything alive leans toward the
light." The caption is the page's last sentence, verbatim, at plate 1 and 2's
baseline.
"""
import math
import sys

sys.path.insert(0, "/home/user/agentic-ghostwriter/runs/parts")
from importlib.machinery import SourceFileLoader

g = SourceFileLoader("g", "/home/user/agentic-ghostwriter/runs/parts/gen-plates-345.py").load_module()

X0, X1, CX = g.X0, g.X1, g.CX
FIELD = g.FIELD

PX, PY = 300.0, 600.0        # the point the opening starts from, low on the page
GAPTOP = 152.0               # half width of the parting at the top layer
FLARE = 1.45                 # the parting opens slowly low down and fast high up
LAM = 52.0                   # how far back from the inner end the lean is felt


def plate3():
    out = [g.HEAD]
    n = 22
    bottom, top = 640.0, 190.0
    for i in range(n):
        yy = bottom - (bottom - top) * i / (n - 1)
        h = PY - yy
        if h <= 0:                       # under the point: the layer is whole
            pts = []
            steps = 80
            for k in range(steps + 1):
                x = X0 + (X1 - X0) * k / steps
                u = (x - CX) / 210.0
                pts.append((x, yy + 1.3 * g.wob(u * 3.0 + i, i)))
            out.append(g.poly(pts, FIELD))
            continue
        f = h / (PY - top)
        gap = GAPTOP * (f ** FLARE)      # half width of the parting at this layer
        lean = 5.0 + 18.0 * f
        for side in (-1, 1):
            inner = CX + side * gap
            outer = X0 if side < 0 else X1
            pts = []
            steps = 64
            for k in range(steps + 1):
                x = outer + (inner - outer) * k / steps
                u = (x - CX) / 210.0
                d = abs(x - inner)
                y = (yy
                     - lean * math.exp(-d / LAM)
                     + 1.3 * g.wob(u * 3.0 + i, i))
                pts.append((x, y))
            out.append(g.poly(pts, FIELD))
    out.append(g.cap("What it reaches, opens."))
    out.append("</svg>\n")
    return "".join(out)


if __name__ == "__main__":
    p = "/home/user/agentic-ghostwriter/runs/parts/plate-3-warm-sun.svg"
    open(p, "w").write(plate3())
    print("wrote", p)
