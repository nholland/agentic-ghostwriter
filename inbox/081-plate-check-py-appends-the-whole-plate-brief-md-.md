---
id: 081
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 12:43
resolved: 2026-09-26 17:32
applied_by: python3 tests/export_safety_cases.py
---

# plate_check.py appends the whole plate-brief.md to the grounding corpus, so the brief's own generated boilerplate is legal plate copy: 'the drawing carries the argument', 'Nothing here is invented' and the provenance tag 'endorsed by the author' all pass grounded. Should the corpus be narrowed to the distillation fields and the Author-additions bullets, with the bracketed tag stripped?

The row that makes the author-endorsed reviewer copy safe cannot tell the chapter's words from the brief's furniture. A plate could close on 'The drawing carries the argument' and pass.

**Recommendation:** Narrow it: tested against the live set, 0 of 12 plates regress, boilerplate and tag are refused, and every endorsed line stays legal.

**Checked:**

```
PYTHONPATH=scripts, corpus(['books/the-stoic-husband/chapters/ch01'],'runs/ch01'): LEGAL 'the drawing carries the argument' / LEGAL 'a man who never read the chapter' / LEGAL 'Nothing here is invented' / LEGAL 'endorsed by the author'. Under the narrowed corpus: chapters failing grounded: [] ; refused 'the drawing carries the argument' ; refused 'endorsed by the author' ; LEGAL 'Between what she says' ; LEGAL 'Your marriage lives there'.
```

**What unblocks this:** Whether grounded means 'the chapter said it' or 'it appeared anywhere in a generated file'

**Previous proof (retired; replaced by behavioral coverage):**

```sh
PYTHONPATH=scripts python3 -c 'from plate_check import corpus, normalise as n; c = corpus(["books/the-stoic-husband/chapters/ch01"], "runs/ch01"); raise SystemExit(0 if n("the drawing carries the argument") not in c and n("endorsed by the author") not in c and n("Your marriage lives there") in c else 1)'
```

**Resolution (2026-09-26 17:32):** Approved. Grounding now excludes generated boilerplate/provenance and retains chapter prose, distillation fields and attributed Author additions. Unsupported copy remains a warning, not invented evidence. Evidence: runs/qa/2026-09-26-export-safety-ch01-ch13.md. No agent instructions changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/export_safety_cases.py` exits 0.

**Applied, confirmed 2026-09-26 17:32:** `python3 tests/export_safety_cases.py` now exits 0.
