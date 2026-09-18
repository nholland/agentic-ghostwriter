---
id: 029
status: resolved
raised_by: gw-retro
chapter: 12
opened: 2026-09-18 20:18
resolved: 2026-09-18 20:29
applied_by: python3 tests/run.py
---

# Nothing validates runs/chNN/okf/ before it lands in the book. Should okf_gate.py resolve the staged bundle's internal links against the bundle it will join?

Five of Ch12's 23 staged citation files wrote ](/okf/citations/...) against a bundle whose 54 existing links all read ](/citations/...). Nine links would have broken on arrival; the Publisher caught them by eye in commit 56167a7. okf_validate.py checks link integrity, but only on the book's own bundle and only as a non-fatal warning printed under five others - and okf_gate.py never points it at runs/chNN/okf/. This survives the migration: the convention is a property of the bundle, not of the staging directory.

**Recommendation:** Add it inside okf_gate.py rather than as a new script - okf_gate already has every caller a new script would need. Fixture: the pre-repoint chapman-1992 file from commit 61c7f5c.

**Checked:**

```
gw-retro re-ran the check against the pre-repoint tree (61c7f5c): 9 broken links, e.g. citations/chapman-1992-five-love-languages.md -> /okf/citations/impett-park-muise-2024-love-languages-evaluated.md. Against the current tree: 0 broken.
```

**What unblocks this:** Every future chapter's citations are link-checked before they touch the book, by the one function every prose-writing skill already calls.

**Resolution (2026-09-18 20:29):** fix the 9 broken ones

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-18 20:29:** `python3 tests/run.py` now exits 0.
