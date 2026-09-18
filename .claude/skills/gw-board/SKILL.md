---
description: The Publisher's dashboard - where every chapter stands, what each desk has produced, and what is waiting on the author. Run at the start of a session to re-enter.
---

# /gw-board — where everything stands

## First, load the Publisher's standing rules

Read `CLAUDE.md` at this repo's root before reporting anything. It holds the
Publisher persona, the roster, and the twelve standing rules — and it is **not**
loaded automatically when this repo arrives as a plugin (`claude plugin validate`
warns about exactly this: "CLAUDE.md at the plugin root is not loaded as project
context"). On the attached-repo path it loads on its own and re-reading is cheap;
on the plugin path this is the only thing that loads it.

It is pointed at rather than copied here on purpose. Two copies of the standing
rules with nothing keeping them equal is the retired citation-manifest failure.


## Run these first, and report what they say

```
python3 scripts/resolve_book.py
python3 scripts/inbox.py
```

**Do not determine state by reading files and reasoning.** These scripts are the
oracle. If `resolve_book.py` fails, that is the whole report: say so and stop.

## Then assemble

**The book** (`books/<slug>/`, read here, written only by a landing): from
`resolve_book.py`, the active book, chapters planned, chapters refined.
`book-manifest.json`'s per-chapter stages are the old pipeline's record and stop
at Chapter 11; `scripts/pipeline_state.py` still reads them if he asks what that
pipeline last thought. Neither is this house's "next" - `next.py` is.

**This pipeline:** for each `runs/chNN/`, which artifacts exist — `interview.md`,
`research.md`, `brief-gaps.md`, `draft.md`, `refined.md`, `distillation.md`,
`conformance*.md`, `inbox.md`. Name the desk that owns the next step.

**Bake-offs:** for each `bakeoff/chNN/`, whether `verdict.md` has been filled in
and whether the mapping is still sealed. A sealed packet with an unfilled verdict
is the thing to surface — it is work already done that is waiting on a read.

**The inbox:** open count and each item's one-line question.

## Report

One short paragraph on where things stand, then the three tracks — the book, this
pipeline, the inbox — and one concrete next action per track. Name the desk for
each.

Say plainly which pipeline any given chapter shipped on. The confusion this
command exists to prevent is the author not knowing whether something is real
book progress or a shadow run.
