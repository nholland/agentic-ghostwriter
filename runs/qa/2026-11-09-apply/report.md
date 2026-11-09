# Batch 1 and 2 applied: Prologue to Ch16

2026-11-09. Author's word: "I want to accept all of batch 1 and batch 2, We can go with your best choice. If you need to kick off sub agents to rewrite those, I'm good with it."

- **Accepted:** 81 items. **Applied and landed:** 80, one commit per chapter (see `applied_commit` in the ledger).
- **Held:** Q114 (Ch15, delete the last line). It drops you-density to 38.7, below the floor of 40. Needs the author's word.
- **Kept as the author's own words (not changed):** Q059, Q113, Q125.
- **Rejected:** Q134 (Ch16's only caveat; the spec requires it) and Q070 (the Fact-Checker found Haines is the ratified exception).

## How it was done
1. Four gw-lineeditor desks applied the edits to copies in this folder (Prologue to Ch4, Ch5 to Ch9, Ch10 to Ch13, Ch14 to Ch16).
2. Three of them could not write report files (blocked for sub-agents); their reports went back to the Publisher in text.
3. The Ch5–9 desk read the Publisher's "Accept as written" note as "make no change". It skipped Q034, Q036, Q037, Q043, Q079, Q080, Q084 and Q090. The Publisher applied those 8 with exact-match assertions.

## Verified by the Publisher (Rule 7)
- Every changed paragraph traces to an accepted item.
- Every remaining anchor hit is explained: a moved sentence (Q041, Q007), an appended sentence (Q094), a line the ruling did not name (Q098 L113), or text that sits in the Editor's Notes (Q032).
- `practice_sync.py --book`: PASS on 16 chapters.
- `voice_check.py`, landed result vs. the new result:
  - **Prologue:** FAIL you-density, before and after (30.7 → 31.5).
  - **Ch1:** FAIL you-density, before and after (33.0 → 33.8).
  - **Ch2:** FAIL em-dash, before and after (the quotation credit at L8).
  - **Ch3–Ch15:** all HARD checks passed, before and after. Ch15 passes only with Q114 held.
  - **Ch16:** FAIL on the metaphor family, before and after, improved from 6.7 to 6.4 per 1,000 (cap 5).

## Side-effects the Publisher repaired (each named in its chapter's commit)
- **Prologue:** "making it" → "making the mistake I made". Q063 and Q021 left "it" with nothing to refer to.
- **Ch1:** deleted "What matters is what happens next." It echoed Q020's new line.
- **Ch2:** "It might just be timing." → "If it does, it might just be timing."
- **Ch3:** deleted "They wait, dreading it…". Its subject, "most men", went with Q031.
- **Ch8:** deleted "She does.", which repeated Q086's new line.
- **Ch16:** "all need you to show up" → "all count on you". Q137 echoed the sentence before it.

## Desk adjustments kept
- **Q025:** the whole paragraph replaced, as the fix said.
- **Q035:** L65–71 in second person.
- **Q039:** absorbs the next sentence.
- **Q041:** the whole recap paragraph moved.
- **Q042:** the whole sentence replaced.
- **Q092:** "wrote" dropped, because Arrian compiled the *Enchiridion*.
- **Q108:** the opener dropped, to avoid repeating the sentence before it.
- **Q109:** the study's result sentence also cut.
- **Q135:** merged with the sentence after it.
- **Q037:** keeps the original tail ", and that's a fight nobody wins…".

## Derived artifacts
- `distill_status.py` flags all 16 chapters STALE, which means any prose change, not that a distillation is wrong.
- A precise check found one distillation quoting a changed line: Ch14, for Q008. It was synced in its own commit.
- No plate draws a changed mechanism.

## Open, for the author
- **Q114 (Ch15):** keep the last line, or also change L35 so the chapter stays above the floor. The Line Editor tested the L35 change at 40.1.
- **Ch16 image count:** cut three uses of "place" to land exactly at 5.0 per 1,000. Pre-existing; L48 ×2 and L56.
- **Q040 (Pillemer):** the Fact-Checker's proposed wording is in `runs/qa/2026-11-09-factcheck-q040-q070.md`.
