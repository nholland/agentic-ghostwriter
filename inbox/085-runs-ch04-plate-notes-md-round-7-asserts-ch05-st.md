---
id: 085
status: open
raised_by: gw-retro
chapter: 4
opened: 2026-09-21 12:52
applied_by: python3 -c "import sys; n=open('runs/ch04/plate-notes.md',encoding='utf-8').read(); sys.exit(0 if 'Publisher correction' in n else 1)"
---

# runs/ch04/plate-notes.md Round 7 asserts 'Ch05 still draws the old filled dot' and escalates it as the round's one decision. Ch05 has zero circle elements, and the same file recorded 'Ch05 no longer draws nails at all' 195 lines earlier. Should a desk be required to open a file before asserting its current contents, or is the appended correction enough?

plate-notes.md, not git log, is what the next plate round reads. The Publisher has appended a dated correction rather than deleting the desk's paragraph, so the false claim and its refutation now sit together; this item is about whether the pattern needs a guard, not about the one instance.

**Recommendation:** The correction is already appended, so the live risk is closed. The open question is whether a desk asserting another file's contents must paste the command that verified it - which adds rule text and names no deletion, so it may not be worth it.

**Checked:**

```
notes claimed Ch05 draws a filled dot: True. Circles actually in ch05: 0 (grep -c '<circle' runs/ch05/plate.svg -> 0). Correction appended to runs/ch04/plate-notes.md 2026-09-21 12:56.
```

**What unblocks this:** Whether cross-plate claims in desk notes are checkable or taken on trust

## Second instance, 2026-09-21 13:20 (gw-retro, same session, same desk)

`runs/parts/plate-notes-2026-09-20.md` escalation 5: *"chapter_pdf.py renders it
correctly here."* It did not and could not. `compile.py:part_plate()` returns the
landed book file whenever one exists and only falls back to `runs/parts/`; Parts
I and II are landed, so `--plates` embeds
`books/the-stoic-husband/parts/plate-1-steady-river.svg` and the draft is
unreachable by that path. The 1250 packet HTML contains 0 occurrences of
`clipPath`.

The same escalation also names a mechanism this repo does not have: no
`ElementTree`, `lxml`, `minidom` or `BeautifulSoup` appears anywhere in
`scripts/*.py`, so nothing here re-serialises SVG. The real exposure is
WeasyPrint's SVG engine at `chapter_pdf.py:346`, which is not installed in this
container and therefore untested.

Third in the same file: *"Ch23's The Marriage You Build Every Day"* is Chapter 24
(`03-outline.md:456`); Ch23 is "The Difference Between Endurance and Cowardice"
(`:434`), and neither is written.
