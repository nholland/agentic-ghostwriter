---
id: 072
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 23:39
resolved: 2026-09-26 17:32
applied_by: python3 tests/export_safety_cases.py
---

# package_check.py printed [ ok ] on all four manuscript HTMLs that shipped a literal \pagebreak as body text and the compiler's own comment as escaped text at the top of page one - including the file the author reported. Should it gain a fifth check: no un-interpreted markup token reaches the reader as visible text?

The house's only artifact-reading check is blind to the whole class of defect the author actually found by reading. 88cfa346 fixed the defect with 270 words of comment prose and no fixture; 107/107 passed before and after, so the suite is silent on its return.

**Recommendation:** Add check 5 (119 words, text events only) plus a 2200-shaped and a 2330-shaped fixture; delete the ~150 words of 'this used to be a \pagebreak' narration the fix added.

**Checked:**

```
python3 scripts/package_check.py runs/manuscript/the-stoic-husband-prologue-ch12-plates-draft-2026-09-20-2200.html -> '[ ok ] ... opens on: chapter', exit 0, on a file with 19 'pagebreak' and 1 comment-marker matches. Drafted check fails all four pre-fix HTMLs, passes the 2330 fix.
```

**What unblocks this:** Whether the render gate catches leaked markup or the author keeps catching it, and whether 270 words of historical-defect narration in compile.py and chapter_pdf_local.py can drop to ~120.

**Previous proof (retired; replaced by behavioral coverage):**

```sh
grep -qi 'leaked.markup\|no.un-interpreted' scripts/package_check.py
```

**Resolution (2026-09-26 17:32):** Approved. Package checks now reject leaked visible markup, with behavioral cases covering escaped and fragmented markers; obsolete narration was shortened. Evidence: runs/qa/2026-09-26-export-safety-ch01-ch13.md. No agent instructions changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/export_safety_cases.py` exits 0.

**Applied, confirmed 2026-09-26 17:32:** `python3 tests/export_safety_cases.py` now exits 0.
