---
id: 043
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 07:10
applied_by: python3 tests/run.py
resolved: 2026-09-19 07:10
---

# tests/prove.py measured a real red pass but nothing bound the proved case to the item being filed - an unrelated 'should the house adopt a mascot' proposal with fabricated evidence was accepted by reusing prove.py's own real, older, unrelated worked example, exit 0. Sync the live tree's uncommitted paths into the worktree (so a case new this window is provable at all) and refuse a --prove-case that already existed before the review window (so an old case can't be reused)?

git worktree add checks out HEAD, blind to uncommitted work - the only triples that could ever pass were older committed ones, unrelated to whatever was actually being proposed. #042's own first use proved this: it changed tests/prove.py and scripts/inbox.py but proved a session_log case introduced in a prior window's commit, because the fixtures #042 was filed about did not exist in HEAD when --add ran. Verified before building the fix: the exact mascot proposal was accepted, exit 0, reusing prove.py's own USAGE example.

**Recommendation:** prove.py copies every git-status-dirty path into the worktree right after creating it; inbox.py reads .claude/state/retro-window's start SHA and refuses a --prove-case already present in tests/run.py there. Also deleted prove.py's literal copy-pasteable USAGE example, which was the exact triple the mascot attack reused.

**Checked:**

```
Re-ran the mascot attack against the pre-fix code first: accepted, exit 0. Built the fix, verified both halves negatively (reverted sync_dirty's call -> [FAIL] on the new uncommitted-case fixture; reverted the window-start block -> [FAIL] on the new predates-window fixture) and positively (both [ ok ] restored). python3 tests/run.py -> 60/60. Re-ran the mascot attack against the fixed code: 'inbox: refusing - --prove-case already existed at the window start (7ea5e122035e)', exit 2. python3 tests/prove.py --file scripts/inbox.py --at 7ea5e12 --case 'inbox refuses a --prove-case that predates the review window' -> PROVED, exit 0.
```

**What unblocks this:** whether the mechanical proof is bound to the change it is filed for, or only to some case that once discriminated something

**Resolution (2026-09-19 07:10):** Applied directly - the Archivist demonstrated the binding gap concretely, verified independently before trusting it, then built and mutation-tested the fix both directions.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 07:10:** `python3 tests/run.py` now exits 0.
