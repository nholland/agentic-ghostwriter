---
id: 041
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:49
applied_by: python3 tests/run.py 2>&1 | grep -q '^\[ ok \] inbox refuses a gw-retro tests/run.py proof with no \[FAIL\] in evidence'
resolved: 2026-09-19 06:49
---

# Make 'seen red' mechanical: refuse a gw-retro item proved by tests/run.py unless its evidence shows a [FAIL] line from before the fix - and withdraw the still-undecided rule-text alternative (requiring every future --applied-by to name a case), since #039 named its case and still closed green over the defect?

Four instances of one shape now: #030's grep, voice_rules_check passing its own defect, the dedup half-fix, and the fixture written for that half-fix (just fixed as #040). Every one was green when it landed. The prior session's proposal to require case-specific --applied-by wouldn't have caught this - #039 already named its case, and it was still unproven.

**Recommendation:** inbox.py --add refuses a gw-retro item whose --applied-by mentions tests/run.py unless --evidence contains a [FAIL] line; withdraw the pending rule-text change to gw-retro.md rather than adding it on top

**Checked:**

```
reverted scripts/inbox.py to c17f979 (git show c17f979:scripts/inbox.py), ran python3 tests/run.py: [FAIL] inbox refuses a gw-retro tests/run.py proof with no [FAIL] in evidence  got: 0 (should have refused, exit 2). Restored the fix: [ ok ], 53/53 fixtures pass. Corpus (cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w) unchanged by this proposal - it's inbox.py code, not rule text; the rule-text alternative would have cost +58 words and is withdrawn rather than added.
```

**What unblocks this:** whether the next half-fix is caught by a script or only by another Archivist happening to look

**Resolution (2026-09-19 06:49):** Applied directly - structural fix closing a gap demonstrated twice in one hour, costs zero corpus words, and supersedes the undecided rule-text alternative rather than stacking on top of it.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] inbox refuses a gw-retro tests/run.py proof with no \[FAIL\] in evidence'` exits 0.

**Applied, confirmed 2026-09-19 06:49:** `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] inbox refuses a gw-retro tests/run.py proof with no \[FAIL\] in evidence'` now exits 0.
