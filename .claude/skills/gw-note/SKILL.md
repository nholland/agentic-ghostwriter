---
description: Record something the author said that should outlive the session - a decision, a ruling, or a question he wants to defer rather than answer now. His words, kept verbatim. Use when he says something worth keeping but there is no artifact to put it in.
---

# /gw-note — keep what he said

Argument: what he said, optionally `park` for a deferred question. `$ARGUMENTS`

The engine's session log is **derived** — clock, branch, files, next action — so it
cannot carry a wrong date or a stale next. What it also cannot carry is the author's
own words. This is that half.

**Never call this on your own initiative.** It records *his* decision, in *his*
words. A note you decided to write is your summary, and a summary of a ruling is not
the ruling.

## Two kinds, and they are different

**A note** — something now settled. A decision between commands, a ruling on a
question, a reason for a choice that a future reader would otherwise have to infer.
Append to `runs/notes.md` with the real clock from `date '+%Y-%m-%d %H:%M'`.

**A parked question** — something he does *not* want to decide now and does not want
to lose. This is **not** an inbox item: the inbox is what a cold desk needs ruled
*to keep working*; a parked question is one he has chosen to defer, and nothing is
blocked on it. Append to `runs/parked.md` with a **revisit trigger** — the event that
should bring it back ("at the Ch13 interview", "before the first compile of Part II"),
not a date. A date on a deferred question is a guess; a trigger is a condition the
board can actually check.

## Write it in his words

Quote him. If you must compress, quote the operative sentence verbatim and summarise
only the context around it. Where a decision reversed an earlier one, say what it
reversed — that is the part a future reader cannot reconstruct.

## Close

Read back what you wrote, in one line, so he can correct it while he is still here. A
note he never saw is a note he cannot trust.
