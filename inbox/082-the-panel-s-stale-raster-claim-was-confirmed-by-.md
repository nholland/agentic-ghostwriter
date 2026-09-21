---
id: 082
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 12:43
applied_by: PYTHONPATH=scripts python3 -c 'import plate_check as p; f=getattr(p,"raster_current",None); raise SystemExit(1 if f is None else (0 if f("runs/ch01/plate.svg","runs/ch01/pdf/plate.png") and not f("runs/ch01/plate.svg","runs/ch02/pdf/plate.png") else 1))'
---

# The Panel's stale-raster claim was confirmed by a hash test that compared a scale-3 re-render against a scale-2 cached file, so it could not have returned anything but 'stale'. The rasters were current then and are current now. Should plate_check.py gain raster_current(svg, png), deriving scale from the PNG's own dimensions, so freshness is answered by a check rather than an ad-hoc comparison?

The cached PNG is what the author is shown before a verdict (gw-plate SKILL.md line 110) and is refreshed only by a one-liner a desk must remember (line 83). Nothing reads it at build time, so the exposure is a verdict on stale art, not shipped art.

**Recommendation:** Add raster_current() and call it as a plate_check row; it is the only place the answer is currently guessed.

**Checked:**

```
ch01 cached=(1280,680) fresh-at-default=(1920,1020) -> mismatch. Re-rendered at scale=2: ch01..ch12 all match. Publisher re-verified 2026-09-21: ch01/ch06/ch12 match@3=False, match@2=True. Both plate_packet.py (line 186, no isfile guard) and compile.py (embeds the SVG) bypass the cache entirely.
```

**What unblocks this:** Whether 'is the plate the author is looking at the current plate' is answerable mechanically
