---
id: 074
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 23:44
applied_by: grep -rq 'retro dispatch skips a commit carrying runs/retro/' tests/
---

# retro-check.sh watches inbox/, and the Archivist's only durable output is an inbox filing, so every substantive retrospective triggers one more whose entire subject is the previous retrospective. Two of the last four dispatches fired on nothing else. Should the count skip any commit carrying a runs/retro/ file?

The hook already excludes runs/ for this exact shape and closed only half of it; its own comment and FINDINGS line 336 both claim the loop is cut at the root, which is now false. The loop cannot grow the ledger - the Archivist never applies - but it spends sessions: 15 dispatch markers in .claude/state today against 5 retro docs written. Note for the record: --applied-by greps tests/ rather than naming tests/run.py because inbox.py runs prove.py at filing time and #048 makes that refuse for a case that does not exist yet. This is the seventh consecutive grep-shaped gw-retro proof for that reason.

**Recommendation:** Yes: skip commits touching runs/retro/ when counting, prove it with a two-commit fixture in tests/run.py, and rewrite the loop comment to say three quarters cut rather than root

**Checked:**

```
Ran the proposed count against four real windows: 88cfa346..dec7dd99 old=1 new=0 (only commit is 908a2ef, the prior retro); 21b1f73..dfcb843 old=1 new=0 (only commit is 9332607, the prior retro); dfcb843..88cfa34 old=1 new=1 (the PDF fix, still dispatches); 980e502..dfcb843 old=2 new=1 (real work kept, retro commit dropped). No false negative on either real-work window. Word counts: sed -n '5,12p' .claude/hooks/retro-check.sh | wc -w -> 94; replacement comment -> 90; current count line -> 8 words; replacement block -> 25.
```

**What unblocks this:** Whether a retrospective can trigger the next retrospective, and whether the hook's 94-word loop comment drops to 90 with its false half removed
