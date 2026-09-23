---
id: 093
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-22 23:19
applied_by: python3 -c "import os,re,collections,sys;ids=[re.match(r'(\\d+)-',f).group(1) for f in os.listdir('inbox') if re.match(r'\\d+-',f)];sys.exit(1 if [k for k,v in collections.Counter(ids).items() if v>1] else 0)"
---

# inbox IDs 053 collided for real: this merge brought inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md onto a branch already holding inbox/053-inbox-py-s-tests-run-py-proof-guard-was-widened-.md. inbox.py now lists two #053 items, so --close 053 is ambiguous. Which of the two is renumbered, and does the duplicate-ID guard land with it?

Two open items share one ID after the merge from main. Any --close 053 acts on an ambiguous target, and the ledger's own addressing scheme can no longer name one of its two entries.

**Recommendation:** Renumber inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md to the next free ID and add a duplicate-ID guard in the same commit, so the repair and its regression check land together

**Checked:**

```
python3 -c "import os,re,collections;ids=[re.match(r'(\\d+)-',f).group(1) for f in os.listdir('inbox') if re.match(r'\\d+-',f)];print(dict((k,v) for k,v in collections.Counter(ids).items() if v>1))" -> {'053': 2}; ls inbox/053-*.md -> two files.
```

**What unblocks this:** Which file is renumbered (the log_check one arrived second, on main, independently of this branch's own #053), and whether a duplicate-ID check lands in the same commit as the repair

**Correction, 2026-09-23 (gw-retro, verified by the Publisher).** Arrival order is the weak reason and happens to agree with the right answer here, but not for a reason that generalizes. The deciding evidence is reference count: `inbox/053-inbox-py-s-tests-run-py-proof-guard-was-widened-.md` is cited live in `scripts/inbox.py`, `tests/run.py`, `FINDINGS.md`, plus five other inbox/retro files - real, shipped code depends on that number meaning that item. `inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md` has zero live references anywhere, only its own frozen commit message (`b22137f`). Renumber the log_check one: nothing breaks. Renumber the other: eight references break. `git log --contains` puts both commits on both refs post-merge, so "arrived on main" doesn't actually distinguish them - reference count is the only criterion that does.

**Also found:** this item's guard half ("add a duplicate-ID guard") duplicates inbox **#046**, already open and unruled since before this collision happened - #046 is the proposal for exactly this structural guard, and `FINDINGS.md` already records that #046 being open-and-unruled is what let the first three ID collisions happen too. This is the fourth. Filing #093 as a fresh item rather than citing #046 repeated the omission it's about. Ruling on #046 covers this item's guard half; #093 itself should be understood as narrowing to the renumber alone.
