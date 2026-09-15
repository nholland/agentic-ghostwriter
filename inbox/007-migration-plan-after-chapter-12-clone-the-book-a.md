---
id: 007
status: open
raised_by: gw-note
chapter: 0
opened: 2026-09-15 10:24
---

# Migration plan: after Chapter 12, clone the book assets here and freeze Playground-260420

Recorded so the plan is not re-derived. ARCHITECTURE.md says L4-L7 belong to the book and four of the book repo's scripts are engine code this repo calls by name - okf_validate, citation_queue, verification_probe, chapter_pdf. Those four are the real migration, not the prose. CLAUDE.md also says two repos, not three: book two is a folder there, never a new repository, so a clone changes which repo is the book repo rather than adding one.

**Recommendation:** Park it until Chapter 12 has a verdict. Nothing should move before the bake-off says the house works.

**Checked:**

```
Author, 2026-09-15: 'If chapter 12 goes well, we are going to make the switch from the other repo and bring the assets over here with a clone, freezing the other one in place permanently in case I need to come back.'
```

**What unblocks this:** Nothing yet. Revisit when Chapter 12 has your verdict.
