---
id: 168
status: open
raised_by: Publisher
chapter: 0
opened: 2026-11-07 14:54
---

# Rule on the whole-book QA ledger: 138 edit suggestions for the Prologue to Ch16

Reader Panel and Anti-Slop Reader read the Prologue to Ch15 on 2026-11-07, then the Ch16 draft against the book after main was merged in. Ledger: runs/qa/2026-11-07-edits-ch00-ch16.json (138 items: Q001-Q114 for the Prologue to Ch15, Q115-Q138 for the unlanded Ch16 draft; every quote checked against current prose). Review copy: runs/qa/2026-11-07-qa-review-ch00-ch16.pdf; report runs/qa/2026-11-07-qa.md. Section 1 (46 items) needs your facts or a choice between desks, starting with Q001: the Prologue says you both worked full time the whole time, Ch14 says a three-year sabbatical. Inbox #101's backlog is folded into this ledger (17 of 18 still present).

**Recommendation:** Rule on Section 1 first (46 items; Q001, Q115 and Q116 most of all), then accept Section 3's line edits in bulk per chapter, starting with Ch1-5 where the register gap is.

**Checked:**

```
python3 scripts/practice_sync.py --book: RESULT: PASS on 15 chapter(s). voice_check.py: Prologue/Introduction/Ch1 FAIL you-density (30.7/29.9/33.0 per 1,000, floor 40); Ch2 FAIL em-dash 1; others pass HARD. Ledger anchors: 86 found, 0 not found.
```

**What unblocks this:** Accepted items go to /gw-edit chapter by chapter; the ledger records each ruling and the commit that applied it.
