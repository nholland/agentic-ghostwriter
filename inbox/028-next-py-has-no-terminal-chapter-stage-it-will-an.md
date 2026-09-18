---
id: 028
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 20:18
---

# next.py has no terminal chapter stage: it will answer '/gw 12 - waiting on your verdict' forever, and Chapter 13 can never surface as next. Add a 'shipped' state that a runs/chNN/verdict.md closes?

chapter_state() ends at 'verdict' and nothing exits it; awaiting_verdict is tested before next_new in compute(). Ch12 is landed in the book repo and next.py still reports it awaiting your verdict. Nothing in this house writes runs/chNN/verdict.md - only bakeoff.py writes one, into bakeoff/chNN/. This also blocks inbox #007, whose trigger is your Ch12 verdict, and #007 is what deletes Rule 8's exception. Note: /gw 13 (an explicit chapter number) still reaches Chapter 13 directly - this bug affects the oracle's 'next'/menu answer, not direct chapter access.

**Recommendation:** Add the terminal state to chapter_state(), have the verdict step of /gw write runs/chNN/verdict.md with the real clock, and add a fixture asserting next.py advances to ch13 once ch12 has one.

**Checked:**

```
Reproduced by gw-retro: a scratch tree with ch12 (refined+plate) and a fully refined ch13 still answers NEXT_ACTION: /gw 12 - Chapter 12 is refined and waiting on your verdict.
```

**What unblocks this:** next.py's 'next' answer correctly advances past a shipped chapter. #007 becomes answerable. The dead variable engine_refined on next.py:148 goes with it.
