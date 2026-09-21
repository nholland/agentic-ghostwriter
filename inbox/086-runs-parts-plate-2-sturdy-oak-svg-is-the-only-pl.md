---
id: 086
status: open
raised_by: gw-designer
chapter: 0
opened: 2026-09-21 13:00
applied_by: ! grep -q 'clipPath' runs/parts/plate-2-sturdy-oak.svg
---

# runs/parts/plate-2-sturdy-oak.svg is the only plate in the book that depends on a clipPath, and it is load-bearing: the clip is what makes the rings run off all four sides with no bark line and no cut end. Any downstream tool that drops or flattens it restores the closed rings, which is the felled-log reading this round existed to remove. Should the clip be baked into the path data before the plate is landed?

Verified: 2 clipPath references in that file, clip-path=url(#box), and it is the only one of the 14 plate SVGs using the feature. Chromium honours it, so both renderers are fine today; the exposure is a future conversion, an SVG optimiser, or a print house re-serialising the file. The failure is silent and it fails back to exactly the picture the author asked to be rid of.

**Recommendation:** Bake it: clip the ring paths at generation time in runs/parts/gen-plate-2-r2.py so the SVG carries no clipPath at all. The generator already exists, so this is a re-run rather than hand-editing path data.

**Checked:**

```
grep -c 'clipPath|clip-path' runs/parts/plate-2-sturdy-oak.svg -> 2. Files among runs/ch*/plate.svg, runs/parts/*.svg and books/the-stoic-husband/parts/*.svg containing clipPath -> 1 (this one). No other plate in the set uses the feature.
```

**What unblocks this:** Whether the Oak plate can be landed as-is or needs its clip resolved into geometry first
