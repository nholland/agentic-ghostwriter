---
id: 059
status: open
raised_by: gw-designer
chapter: -
opened: 2026-09-20 16:33
---

# Ratify the plate style spec the review desk derived (canvas, palette, type, stroke, label classes, Part-plate captions), plus one rule: set text-anchor in a class, never as an attribute?

Section 4 of runs/design/2026-09-20-plate-review.md is the proposal; inbox #015 left a style file outstanding. Three desks separately hit the attribute-vs-class anchor mismatch today, and it put two landed plates' labels off the artboard. Where it lives is yours: design/plates/README.md is the obvious home.

**Recommendation:** Ratify section 4 as written into design/plates/README.md, with the anchor rule added.

**Checked:**

```
python3 runs/design/svgcheck.py on the 13 existing plates under the corrected checker: 7 clean of 13. Ch12, three-second-window, the-operating-system, small-rocks-big-rocks flagged for the same attribute/class cause.
```

**What unblocks this:** A written style the Designer reads first, instead of inferring it from the SVGs each time.
