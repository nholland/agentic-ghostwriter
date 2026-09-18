---
id: 032
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 20:48
resolved: 2026-09-18 20:48
applied_by: test "$(grep -oP '\d+(?= inbox items raised on this chapter)' FINDINGS.md | tail -1)" = 12
---

# FINDINGS.md's Ch12 entry said 19 inbox items; verdict.md said 11; the script says 12. Correct the ledger?

Both numbers were written into commit 55587a8 without running anything; the entry's own enumeration listed eleven, one of which (#018) is tagged ch0. A wrong number in the ledger passes every format check and looks correct forever.

**Recommendation:** Change 19 to 12, reconcile the enumeration against scripts/inbox.py --all --chapter 12, make verdict.md agree.

**Checked:**

```
python3 scripts/inbox.py --all --chapter 12 -> exactly #005,#008-#014,#016,#017,#019,#029 (12 items).
```

**What unblocks this:** The house's memory of its first shipped chapter matches what happened.

**Resolution (2026-09-18 20:48):** Anything else? (this session's follow-up round)

**Not applied yet.** This ruling lands outside this repo. It closes when `test "$(grep -oP '\d+(?= inbox items raised on this chapter)' FINDINGS.md | tail -1)" = 12` exits 0.

**Applied, confirmed 2026-09-18 20:48:** `test "$(grep -oP '\d+(?= inbox items raised on this chapter)' FINDINGS.md | tail -1)" = 12` now exits 0.
