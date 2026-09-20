---
id: 072
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 23:39
applied_by: grep -qi 'leaked.markup\|no.un-interpreted' scripts/package_check.py
---

# package_check.py printed [ ok ] on all four manuscript HTMLs that shipped a literal \pagebreak as body text and the compiler's own comment as escaped text at the top of page one - including the file the author reported. Should it gain a fifth check: no un-interpreted markup token reaches the reader as visible text?

The house's only artifact-reading check is blind to the whole class of defect the author actually found by reading. 88cfa346 fixed the defect with 270 words of comment prose and no fixture; 107/107 passed before and after, so the suite is silent on its return.

**Recommendation:** Add check 5 (119 words, text events only) plus a 2200-shaped and a 2330-shaped fixture; delete the ~150 words of 'this used to be a \pagebreak' narration the fix added.

**Checked:**

```
python3 scripts/package_check.py runs/manuscript/the-stoic-husband-prologue-ch12-plates-draft-2026-09-20-2200.html -> '[ ok ] ... opens on: chapter', exit 0, on a file with 19 'pagebreak' and 1 comment-marker matches. Drafted check fails all four pre-fix HTMLs, passes the 2330 fix.
```

**What unblocks this:** Whether the render gate catches leaked markup or the author keeps catching it, and whether 270 words of historical-defect narration in compile.py and chapter_pdf_local.py can drop to ~120.
