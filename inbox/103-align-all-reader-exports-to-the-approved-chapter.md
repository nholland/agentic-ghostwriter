---
id: 103
status: open
raised_by: Publisher
chapter: 0
opened: 2026-09-24 17:34
---

# Align all reader exports to the approved Chapter, Plate, full Distillation sequence?

On 2026-09-24 the author clarified that each chapter should present prose, then its plate, then a reader-facing distillation that helps put the chapter into practice. Chapter 13 review PDF now has that order and a corrected label. Existing Chapter 11 and 12 PDFs retain the old working-notes label; Chapter 9 and 10 PDFs lack plates. The whole-book compiler appends only each Practice list, not the full distillation.

**Recommendation:** Update the whole-book assembler to include each full distillation after its plate, regenerate the older chapter PDFs, and check order, presence, and reader-facing labels in the rendered outputs.

**Checked:**

```
$ rg -n 'pr = practice|Putting It Into Practice' scripts/compile.py
295:            pr = practice(os.path.join(d, "distillation.md"))
297:                # The pb marker, not a "## Putting It Into Practice" heading
302:                body += "\n\n<div class=\"pb\"></div>\n\n## Putting It Into Practice\n\n" + pr + "\n"
360:    got = md.count("## Putting It Into Practice")
```

**What unblocks this:** Consistent reader-facing chapter packets and final manuscript before delivery.
