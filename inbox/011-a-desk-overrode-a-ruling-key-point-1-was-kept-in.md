---
id: 011
status: resolved
raised_by: gw-specchecker
chapter: 12
opened: 2026-09-15 17:36
resolved: 2026-09-16 11:29
applied_by: grep -qi 'nashville' /home/user/agentic-ghostwriter/runs/ch12/refined.md
---

# A desk overrode a ruling: Key point 1 was kept in the interview record, and the brief moved it to Chapter 13.

Two artifacts conflict. The interview record's outline-revision table says Key point 1 ('the man who was relentlessly romantic when trying to win her - the urgency was doing the work') is KEPT. The research brief's section 0 says it 'is Chapter 13's premise, nearly verbatim' and routes it there. The brief's reasoning is good: the outline's Ch12 key point 1 really is close to Ch13's stated premise ('A man who worked relentlessly to win his wife and then stopped has made the most common and costly mistake in a long marriage'), both chapters sit in the same framework cell, and they share two frameworks. But a cold desk resolved a conflict with a ruling artifact silently instead of raising it, which is the thing the two-touch design exists to prevent. The chapter is coherent as drafted without it, so nothing is blocked. What you are deciding is whether the courtship-urgency idea belongs to Ch12, to Ch13, or to both with different framing.

**Recommendation:** Let it go to Ch13 and leave Ch12 as drafted. The brief's reading is right that the two rows are near-duplicates, and Ch12's energy-allocation mechanism already explains why the effort stopped without needing the courtship contrast. But the call is yours because it is your outline.

**Checked:**

```
gw-specchecker conformance row 3: 'Courtship is never mentioned - no winning her, no before/after, no urgency.' interview.md line 309: 'Key point 1 | Keep.' research.md line 35: 'That is Chapter 13's premise, nearly verbatim.'
```

**What unblocks this:** Which chapter owns the courtship-urgency idea, and whether Ch12's draft needs a beat it currently does not have.

**Resolution (2026-09-16 11:29):** Ch12 keeps it, as the author's own story. His words: 'When I was younger I did big things, like I rented planes and cars and wrote her letters, all of which was 20 years ago.' CONSTRAINT HE ADDED: 'Make sure to clarify it was a small tour of Nashville. I don't want to sound rich.' So the plane is a short sightseeing flight over Nashville, named as such, not a charter. Ch13 keeps the pursuit framing. The split: Ch12 is why the effort stopped; Ch13 is the pursuit that should have continued.

**Not applied yet.** This ruling lands outside this repo. It closes when `grep -qi 'nashville' /home/user/agentic-ghostwriter/runs/ch12/refined.md` exits 0.

**Applied, confirmed 2026-09-16 15:26:** `grep -qi 'nashville' /home/user/agentic-ghostwriter/runs/ch12/refined.md` now exits 0.
