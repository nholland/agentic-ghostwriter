---
name: gw-note
description: Record something the author said that should outlive the session - a decision, a ruling, or a question he wants to defer rather than answer now. His words, kept verbatim. Use when he says something worth keeping but there is no artifact to put it in.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-note/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-note — keep what he said

Argument: what he said, optionally `park` for a deferred question (which goes to the inbox). `$ARGUMENTS`

The engine's session log is **derived** — clock, branch, files, next action — so it
cannot carry a wrong date or a stale next. What it also cannot carry is the author's
own words. This is that half.

**This command is author-invoked:** it keeps his words verbatim. Rule 9's automatic
OKF reconciliation is separate and does not require invoking this command. Label
summaries as summaries; never present them as his exact words.

## Two kinds, and they are different

**A note** — something now settled. A decision between commands, a ruling on a
question, a reason for a choice that a future reader would otherwise have to infer.
Append to `runs/notes.md` with the real clock from `date '+%Y-%m-%d %H:%M'`.

**A parked question** — something he does *not* want to decide now and does not want
to lose. It goes in the inbox as an item of kind `parked`, so he has one place to
look; nothing is blocked on it and it does not count as "waiting on you":

    python3 scripts/inbox.py --add "title" --kind parked --raised-by author \
        --trigger "the event that should bring it back" --context "what it is, with his words"

The **revisit trigger** is the event that should bring it back ("at the Ch13
interview", "before the first compile of Part II"), not a date. A date on a deferred
question is a guess; a trigger is a condition the board can actually check.

## Write it in his words

Quote him. If you must compress, quote the operative sentence verbatim and summarise
only the context around it. Where a decision reversed an earlier one, say what it
reversed — that is the part a future reader cannot reconstruct.

## Close

Read back what you wrote, in one line, so he can correct it while he is still here. A
note he never saw is a note he cannot trust.

## Knowledge completion

Before handoff or completion, follow the reconciliation procedure in `.claude/OKF.md`.
Reconcile durable knowledge, record the receipt and report its disposition.
Author-approved facts need no repeated approval; unapproved interpretations remain proposals.
