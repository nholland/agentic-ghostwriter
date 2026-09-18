---
id: 025
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 18:45
---

# package_check.py still passes six packages that open on apparatus, all printing 'opens on: chapter'. Replace class-name reasoning with document position?

A single-quoted class, a div container, a distillation nested inside the chapter section, an HTML entity in a heading, an h4, and a first section with no class all exit 0. The last is not a straw case: chapter_pdf_local.py emits the chapter as a bare section with no class, so on the only artifact this house has shipped, 'opens on: chapter' is the default value of a variable rather than a verified claim. This is the previous retro's headline, that the check prints its failure inside its own pass line, surviving the fix written for it - the regex was widened and the fabricated default was not removed.

**Recommendation:** Locate the chapter positively by its own h1, compare byte offsets and container depth instead of class names, widen to section|div|article and h1-h6, unescape entities, and fail on anything unrecognised. Drafted at 408 words: 6/6 attacks caught, 4/4 existing fixtures still caught, good.html and the live Ch12 artifact still pass.

**Checked:**

```
grep -o '<section[^>]*>' on the live Ch12 package returns '<section>' then '<section class="dist distback">' - the chapter carries no class, so the opens-on test can never fire.
```

**What unblocks this:** Whether the only gate that reads what a reader receives fails open or fails closed.
