---
description: The Publisher's dashboard - where every chapter stands across both pipelines, what each desk has produced, and what is waiting on the author. Run at the start of a session to re-enter.
---

# /gw-board — where everything stands

## First, load the Publisher's standing rules

Read `CLAUDE.md` at this repo's root before reporting anything. It holds the
Publisher persona, the roster, and the standing rules — and it is **not**
loaded automatically when this repo arrives as a plugin (`claude plugin validate`
warns about exactly this: "CLAUDE.md at the plugin root is not loaded as project
context"). On the attached-repo path it loads on its own and re-reading is cheap;
on the plugin path this is the only thing that loads it.

It is pointed at rather than copied here on purpose. Two copies of the standing
rules with nothing keeping them equal is the `citation-manifest.md` failure.


## Run these first, and report what they say

```
python3 scripts/resolve_book.py
python3 scripts/next.py
python3 scripts/inbox.py
python3 scripts/parked.py
```

**Do not determine state by reading files and reasoning.** These scripts are the
oracle. If `resolve_book.py` fails, that is the whole report: say so and stop.

## Then assemble

**The book, from the old pipeline** (read-only): from `resolve_book.py`, the
active book, chapters planned, chapters refined. The book repo's own
`scripts/pipeline_state.py` owns its NEXT_ACTION — if the author wants that, tell
him to run `/book-resume` there rather than guessing it here. This repo does not
compute the other pipeline's next action.

**This pipeline:** for each `runs/chNN/`, which artifacts exist — `interview.md`,
`research.md`, `brief-gaps.md`, `draft.md`, `refined.md`, `distillation.md`,
`conformance*.md`, `inbox.md`. Name the desk that owns the next step.

**Bake-offs:** for each `bakeoff/chNN/`, whether `verdict.md` has been filled in
and whether the mapping is still sealed. A sealed packet with an unfilled verdict
is the thing to surface — it is work already done that is waiting on a read.

**The inbox:** open count and each item's one-line question.

**Parked questions:** each with its revisit trigger; say which triggers have
arrived (the chapter named is now in interview, the compile named has run).

**The floor:** what `next.py --floor` says could run cold right now, so he can
say "run the floor" and walk away.

## Report

One short paragraph on where things stand, then the three tracks — the book, this
pipeline, the inbox — and one concrete next action per track. Name the desk for
each.

Say plainly which pipeline any given chapter shipped on. The confusion this
command exists to prevent is the author not knowing whether something is real
book progress or a shadow run.
