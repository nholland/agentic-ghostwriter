---
id: 073
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 23:39
applied_by: grep -qi 'page-break.*parity\|parity_rows' scripts/chapter_pdf.py
---

# chapter_pdf.py cannot be executed here, so its CSS is kept in parity with chapter_pdf_local.py by hand and the parity claim in a commit message is unverified when made. Should a fixture compare the page-break declarations of figure.plate, .pb and h1 across both stylesheets?

88cfa346 hand-mirrored three CSS rules into a renderer no one in this container can run, and claimed parity in the commit message and the runs/manuscript/README.md row. Checked after the fact it is correct - but nothing would have said so, and nothing will say so next time.

**Recommendation:** Add it (119 words) only if you want the claim checkable; otherwise stop writing 'parity' in artifact prose that nothing backs.

**Checked:**

```
parity_rows() -> ('figure.plate','ok',...) ('.pb','ok',[before:always],[before:always]) ('h1','ok',[before:always],[before:always]) when checked by hand. import weasyprint -> ModuleNotFoundError; same for markdown, so nothing here can prove it automatically today.
```

**What unblocks this:** Whether 'both renderers updated for parity' is a checkable claim or prose. Open item: it deletes nothing and passes today, so it is a regression guard, not a defect fix.
