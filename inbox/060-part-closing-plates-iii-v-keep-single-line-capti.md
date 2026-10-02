---
id: 060
status: resolved
raised_by: gw-designer
chapter: -
opened: 2026-09-20 16:33
resolved: 2026-10-01 23:18
applied_by: python3 -c "from pathlib import Path; s=Path('runs/parked.md').read_text(); assert '## P-005' in s and 'arcs are complete' in s and all(x in s for x in ('060','087','089')); assert '### [#39]' in Path('books/the-stoic-husband/parking-lot.md').read_text()"
okf_receipt: runs/reconciliation/2026-10-01-arc-plates-parked.json
---

# Part closing plates III-V: keep single-line captions at plate 1's baseline (y=730) or optically centre them (y=743)? Keep IV and V as a mirrored pair?

runs/parts/plate-3-warm-sun.svg, plate-4-fall-to-winter.svg, plate-5-spring-to-summer.svg, drawn to parts/README.md's form rules. IV and V deliberately share one mirrored geometry the way their pages mirror each other. They do not carry all three elements: the only version that fitted all three read as an infographic and was discarded; V carries the river at plate 1's weight. III is in today's PDF; IV and V wait for landed chapters.

**Recommendation:** Keep 730 and keep the mirror; rule on the elements when you see IV and V against their chapters.

**Checked:**

```
runs/parts/plate-notes-2026-09-20.md; python3 runs/design/svgcheck.py runs/parts/plate-3-warm-sun.svg runs/parts/plate-4-fall-to-winter.svg runs/parts/plate-5-spring-to-summer.svg -> clean, clean, clean.
```

**What unblocks this:** Whether the three land as drawn or with a caption shift, and whether IV/V are redrawn unlike.

**Resolution (2026-10-01 23:18):** Those aren't great. I also don't know where those are supposed to go? If we are creating Plates for the Arcs, let's move that to the parking lot as we'd likely want to revisit once we're done with the arcs vs trying to do them now

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 -c "from pathlib import Path; s=Path('runs/parked.md').read_text(); assert '## P-005' in s and 'arcs are complete' in s and all(x in s for x in ('060','087','089')); assert '### [#39]' in Path('books/the-stoic-husband/parking-lot.md').read_text()"` exits 0.

**Applied, confirmed 2026-10-01 23:18:** `python3 -c "from pathlib import Path; s=Path('runs/parked.md').read_text(); assert '## P-005' in s and 'arcs are complete' in s and all(x in s for x in ('060','087','089')); assert '### [#39]' in Path('books/the-stoic-husband/parking-lot.md').read_text()"` now exits 0.
