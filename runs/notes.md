# Notes

Things the author said that should outlive the session, in his words. The
session log (`runs/log.md`) is derived — clock, branch, files, next action —
so it cannot carry a wrong date or a stale next. What it cannot carry is his
own words. This is that half.

---

## N-001 — A fabricated chapter, and what survived it

**Recorded:** 2026-09-19 07:00
**Raised at:** `/gw` session, routing what arrived as reader feedback on Ch11

**What happened, in his words:**

> "As background, I asked it to read aloud the chapter 11 I uploaded, and I
> would interrupt and give feedback in the voice mode.
>
> IT COMPLETELY MADE UP THE CHAPTER.
>
> Wild."

> "This was hallucinations, I'm shocked ChatGPT did this much."

> "But... I actually love some of the things it wrote."

**What it was:** an 11-point editor's log, presented as consolidated reader
feedback on Chapter 11, plus the ~560 words of chapter prose it was written
against. Neither corresponded to Chapter 11 (*Speak or Endure*). The log
described a chapter titled "How to Endure Without Disappearing," built on an
Endurance/Resilience pair, containing a couch example, a marriage-vow passage
and a parent-child analogy.

**How it was caught — counted, before any desk was dispatched:**

| Landmark the log claimed | In `ch11/refined.md` | In the reader packet |
|---|---|---|
| "load-bearing" | 0 | 1 — but in the *Introduction's* Oak section, not Ch11 |
| "resilien" (any form) | 0 | 0 |
| "couch" | 0 | — |
| "sickness and in health" | 0 | 0 |
| the Oak named in prose | 0 | — |

`resilien` returns 0 across all 14 refined chapters. Ch11's own Structural Flag
already said the thing that broke the story open: *"`parts/part-2-sturdy-oak.md`
supplies the oak this chapter never names."*

**Why this is recorded rather than filed as a mishap.** The material was routed
correctly *because* the mismatch was checked before a desk ran. Had the log gone
to the Line Editor as Ch11 corrections, a desk would have rewritten a passing
chapter against notes for a text that does not exist. The check that caught it
was mechanical — grep for the log's own landmarks in the published chapter —
and cost one tool call.

**The standing rule it argues for:** feedback arriving through an AI
intermediary is not feedback until its landmarks are found in the actual text.
Not offered as a rule edit (Rule 17 — the Archivist proposes, the author
applies); recorded here as the incident a future proposal would cite.

**What survived it.** The ideas were kept and the sentences were not. The pasted
prose failed this book's counted voice spec on its own terms — `voice_check.py`
returned FAIL on you-density (14.2 per 1,000 against a floor of 40), 9
definitional reframes against a cap of 2, "she/her" 0 times against 42 in Ch11,
"your partner" twice, and Oak and River stacked in one chapter against the
author's own ruling in book `parking-lot.md` #259. Nothing from it enters the
book as prose. Two commissions were taken from it: P-004 in
`runs/parked.md`, and the framework question in this session's `/gw-revise`.



## 2026-09-22 21:50 — Author concern: Chapter 11 complexity

> For the record, I don't like chapter 11 much. But I can't put my finger on it. Which desk helps with that.
>
> My sense is the metaphors and structure doesn't land with a basic male reader. Still too complex

Author concern recorded for diagnosis; no revision or specific diagnosis settled.
