---
id: 118
status: resolved
kind: parked
trigger: 
aka: P-003
raised_by: Publisher
chapter: -
opened: 2026-09-19 00:46
resolved: 2026-10-03 22:00
---

# Triage the old pipeline's open parking-lot items against the new house

*Migrated 2026-10-04 from runs/parked.md (P-003); the id is kept as an alias.*

**Parked:** 2026-09-19 00:46
**Raised at:** the author asking "what else did you miss" after the Substack
finding, which led to actually reading `books/the-stoic-husband/parking-lot.md`
in full rather than trusting `CLAUDE.md`'s "read for history" framing to mean
"nothing in it is still live."

**What was found:** `parking-lot.md` has roughly 17 items still marked `OPEN`
(numbers #5, #8, #9, #12, #20–#24, #26, #27, #29–#35), spanning 2026-06-12 through
2026-09-10 — content decisions, not just tooling. Two examples surfaced already:
`#8` (Buffer social auto-posting, now in `GAPS.md`) and the general shape that
`#7` in `.claude/LEARNINGS.md` warned about (a manifest field asserting a state
nobody re-checked). "Migrated as history, read never extended" is correct for
*resolved* items; it silently mis-describes an *open* one, since an open item is
undecided business, not a record of something that already happened.

**Why not done in this pass:** 17 items, each needing a judgment call about
current relevance (has this house since decided it? is it superseded by
something in `FINDINGS.md` or `progress.md`'s later entries? is it still live?)
is a real read-through, not a grep. Guessing at 17 answers to look responsive
would be worse than flagging it plainly.

**Revisit trigger:** the next session with room for a dedicated pass, or before
the whole-book QA trigger fires (P-002) — QA is a bad time to discover a decision
was never actually made. Each item that's still genuinely open moves to this file
with a real trigger; each one superseded gets a one-line note saying by what.

## Outcome, 2026-10-03

The triage read all 21 open items in the old `parking-lot.md` against this house
(`runs/qa/2026-10-03-parking-lot-triage.md`). The old file is history and was not
edited; this is where the outcomes live.

**Closed, with what superseded each:** #34 (this house is the Publishing House);
#31 (Parts IV and V renamed by the 2026-10-02 outline revision); #8 (carried in
`GAPS.md`); #30 (all five Part pages exist; `/book-status` is gone); #21 (Rule 7
and `voice_check.py` `check_devices`); #22 (`gw-revise`, "If the change is a
chapter retitle"); #36 and #37 (governed by P-005 / #39).

**Closed on his word, 2026-10-03:** #20, read-aloud step: *"Already how I work."*
Explore JEV: *"Drop it."* The supporting research stays in `runs/qa/` as apparatus.

**Still live, trigger unchanged:** #5 (Ch24 research; pointer now in the Ch24
spec), #9 (before a second book), #12 (Ch26 research; the audiobook scene to Ch23,
*Repair*, was Ch17), #23 (his call, after `/gw-qa`), #29, #32 (recount: 136 of
140 citations open), #33, #35, #39 (P-005).

**Held:** #24 and #26, now P-006.

**#38 folded into P-005, 2026-10-03.** The author approved the Publisher's
recommendation: *"Yes, do 1 and 3."* Both whole-set plate findings (Ch7 and Ch11
converged on one composition; no plate in the set draws warmth) now share P-005's
trigger, **once the book's arcs are complete**, instead of "the first Part III
chapter plate," which had already fired. Evidence read 2026-10-03: the Ch12 plate
draws neglect (an empty box) and the Ch13 plate is a two-path decision diagram,
so neither broke the damage-avoided register; the Ch14 watering can is the first
plate in the set that draws something given. Ch12 and Ch13 stay as landed. The one
near-term action, a label move on the Ch14 plate and a brief note that it should
show something received, is recorded in `runs/ch14/plate-brief.md`.
