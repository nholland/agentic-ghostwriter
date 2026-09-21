---
id: 076
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:10
applied_by: test $(git ls-files 'runs/manuscript/*.png' 'runs/manuscript/*.html' | wc -l) -eq 0
---

# runs/manuscript/ commits 29 regenerable PNGs and 6 HTMLs whose stamped names now misrepresent their contents - four Rule-15-stamped HTMLs share one unstamped, repeatedly-overwritten PNG set. Should the rasters and HTML stop being tracked, leaving the self-contained PDF as the committed artifact?

Rule 15 exists because three files 'each looked current'. Round 1's committed HTML, opened today, renders round 3's Ch8 and Ch12 plates while its sibling PDF embeds round 1's. plate_packet.py inherited the collision and worked around it with a packet- prefix, which is why 14 byte-identical duplicate PNGs now exist. The workaround is the tell.

**Recommendation:** gitignore runs/manuscript/*.png and *.html; keep the PDFs (Chrome embeds the images, so they are already self-contained and already correct) and keep README.md's table as the index

**Checked:**

```
md5sum runs/manuscript/*.png grouped by hash: 14 byte-identical pairs, chNN-plate.png == packet-chNN.png for all 12 chapters plus both Part plates; duplicate PNG files (same bytes, different name): 14, 1.9M of 3.8M. All four *plates-draft*.html reference an identical PNG name list (md5 798c330df56f28b71ffd8b607b457b70 x4). git log on the rasters: eb3da38 wrote them, 1be88a2 rewrote them, c5690af rewrote ch07/08/09/12-plate.png again after the Ch8 and Ch12 redraws - while eb3da38's HTML is still tracked and still points at them. Tracked in runs/manuscript: 29 png (3.8M), 6 html (748K), 7 pdf.
```

**What unblocks this:** Whether a stamped filename in runs/manuscript/ can be trusted to show what it showed when it was made

## The shape has reached a second directory, 2026-09-21 13:20

`ecb6285` commits `runs/parts/oak.png` (278 KB) and `runs/parts/river.png`
(79 KB): unstamped renders of two SVGs still in revision, so both names will
silently misrepresent their contents the next time a generator runs. Same shape
as this item, one directory over.

Not this shape, recorded so the distinction survives: the generators in
`runs/parts/` each reproduce their committed SVG byte for byte, and the A/B
variants committed mid-round were deleted in the same commit (-144 lines).
