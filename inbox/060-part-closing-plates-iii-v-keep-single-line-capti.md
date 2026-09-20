---
id: 060
status: open
raised_by: gw-designer
chapter: -
opened: 2026-09-20 16:33
---

# Part closing plates III-V: keep single-line captions at plate 1's baseline (y=730) or optically centre them (y=743)? Keep IV and V as a mirrored pair?

runs/parts/plate-3-warm-sun.svg, plate-4-fall-to-winter.svg, plate-5-spring-to-summer.svg, drawn to parts/README.md's form rules. IV and V deliberately share one mirrored geometry the way their pages mirror each other. They do not carry all three elements: the only version that fitted all three read as an infographic and was discarded; V carries the river at plate 1's weight. III is in today's PDF; IV and V wait for landed chapters.

**Recommendation:** Keep 730 and keep the mirror; rule on the elements when you see IV and V against their chapters.

**Checked:**

```
runs/parts/plate-notes-2026-09-20.md; python3 runs/design/svgcheck.py runs/parts/plate-3-warm-sun.svg runs/parts/plate-4-fall-to-winter.svg runs/parts/plate-5-spring-to-summer.svg -> clean, clean, clean.
```

**What unblocks this:** Whether the three land as drawn or with a caption shift, and whether IV/V are redrawn unlike.
