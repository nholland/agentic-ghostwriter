---
id: 103
status: resolved
raised_by: Publisher
chapter: 0
opened: 2026-09-24 17:34
resolved: 2026-09-26 17:33
applied_by: $HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tests/verify_reader_exports.py
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

**Resolution (2026-09-26 17:33):** Approved. All thirteen chapter packets and the whole book now use prose, plate, full reader-facing distillation, with fresh chapter starts and intact headings. Regenerated sixteen PDFs; verified complete source text and page order, and inspected rendered pages. Chapter 13 and draft plate approval states are unchanged. Evidence: runs/qa/2026-09-26-export-safety-ch01-ch13.md. No agent instructions changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tests/verify_reader_exports.py` exits 0.

**Applied, confirmed 2026-09-26 17:33:** `$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tests/verify_reader_exports.py` now exits 0.
