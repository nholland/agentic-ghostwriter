---
id: 107
status: ruled
raised_by: gw-slopreader
chapter: 13
opened: 2026-09-27 20:21
resolved: 2026-09-27 21:21
applied_by: python3 scripts/next.py | grep -qE 'ch13 (verdict|shipped)'
okf_receipt: runs/reconciliation/2026-09-27-inbox-107.json
---

# Chapter 13 failed its continuity review twice. Allow one more Line Editor round for three one-sentence fixes?

Round 2 fixed all six earlier problems and the Reader Panel passed it. The rewrite introduced three new ones: (1) the 'That's not X. It's Y.' reframe now appears about 8 times (voice cap is 2); (2) a new sentence says the book's river means steadiness rather than change, but the Introduction defines it as steadiness through change; (3) 'ask again on Thursday' reuses Ch12's exact beat. Each is a sentence-level repair, no research or ruling needed. House rule: two failed rounds stop at the inbox rather than loop. Also: the Line Editor's notes claim no sentence runs 25+ words; the reviewer found at least six that do.

**Recommendation:** Yes: one more Line Editor round scoped to these three fixes, then recheck by the continuity reviewer only.

**Checked:**

```
runs/ch13/coherence-refined.md (round 2) N1-N3, M2; runs/ch13/persona-refined.md round 2 PASS
```

**What unblocks this:** a third revision round on Ch13, or your own edit

**Resolution (2026-09-27 21:21):** Yes

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 scripts/next.py | grep -qE 'ch13 (verdict|shipped)'` exits 0.
