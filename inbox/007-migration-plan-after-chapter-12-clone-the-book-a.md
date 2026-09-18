---
id: 007
status: resolved
raised_by: gw-note
chapter: 0
opened: 2026-09-15 10:24
resolved: 2026-09-18 23:47
applied_by: python3 scripts/resolve_book.py --json | python3 -c "import json,sys,os;d=json.load(sys.stdin);assert d['found'] and os.path.samefile(d['bookRepo'],'.')"
---

# Migration plan: after Chapter 12, clone the book assets here and freeze Playground-260420

Recorded so the plan is not re-derived. ARCHITECTURE.md says L4-L7 belong to the book and four of the book repo's scripts are engine code this repo calls by name - okf_validate, citation_queue, verification_probe, chapter_pdf. Those four are the real migration, not the prose. CLAUDE.md also says two repos, not three: book two is a folder there, never a new repository, so a clone changes which repo is the book repo rather than adding one.

**Recommendation:** Park it until Chapter 12 has a verdict. Nothing should move before the bake-off says the house works.

**Checked:**

```
Author, 2026-09-15: 'If chapter 12 goes well, we are going to make the switch from the other repo and bring the assets over here with a clone, freezing the other one in place permanently in case I need to come back.'
```

**What unblocks this:** Nothing yet. Revisit when Chapter 12 has your verdict.

**Resolution (2026-09-18 23:47):** I'm ready to make the full transition over to this repo.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 scripts/resolve_book.py --json | python3 -c "import json,sys,os;d=json.load(sys.stdin);assert d['found'] and os.path.samefile(d['bookRepo'],'.')"` exits 0.

**Applied, confirmed 2026-09-18 23:47:** `python3 scripts/resolve_book.py --json | python3 -c "import json,sys,os;d=json.load(sys.stdin);assert d['found'] and os.path.samefile(d['bookRepo'],'.')"` now exits 0.
