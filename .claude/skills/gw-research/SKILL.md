---
description: The Researcher desk builds a chapter research brief cold from the interview record, gated by the Ghostwriter's plan-only review of whether the brief can be written from at all. Use after /gw-interview.
---

# /gw-research — build the brief, then prove it is writable

Argument: a chapter number. `$ARGUMENTS`

## Step 0

`python3 scripts/resolve_book.py` — stop if it fails.
Require `runs/chNN/interview.md`. **If it is missing, stop and run
`/gw-interview NN` first.** This desk does not interview; it cannot, because it is
cold. That boundary is the whole architecture.

## Step 1 — dispatch the Researcher

Dispatch `gw-researcher` with the interview record, the outline section, and the
book's foundation files. Output `runs/chNN/research.md`.

Name the desk in your reply.

It may write **gap-marker** citation concepts directly, through
`scripts/okf_new.py` (the clock, the slug check and the validator all run
there) — the file is the flag and the brief needs its path. It must **propose**
content concepts rather than write them (`okf_new.py --dry-run` is the
proposal); those are claims about what the author thinks. Collect its proposals
for Step 4.

## Step 2 — the gate that matters

Dispatch `gw-ghostwriter` in **plan-only** mode against the brief and the outline
section. One question: *could someone who never read the interview write this
chapter from this file alone?*

- Empty gap list → the brief is delegable. Proceed.
- Non-empty → write `runs/chNN/brief-gaps.md`. Hand the gaps back to
  `gw-researcher` for one round. Still non-empty → split them: anything a cold
  desk could close, close; anything only the author can close goes to the inbox,
  one item each, with the context he needs to answer cold.

This is the automation boundary made mechanical. A brief that fails this test is
unfinished whatever it looks like.

## Step 2.5 — coinages

```
python3 scripts/term_check.py runs/chNN/research.md
```

Every capitalised term the brief leans on must resolve to a concept, the
book's constitution, or a definition in the brief itself. A term that exists
only in its outline line (WARN) may not organise the evidence until it is
defined; a term that resolves nowhere (FAIL) goes back to the Researcher with
the plan-only gaps. This is the Rock incident made mechanical.

## Step 3 — citation gate

```
python3 scripts/okf_gate.py
```

Blocking. If it fails, the bundle is broken and nothing downstream may run.

## Step 4 — check in

Show the author: the brief, the gap list, the term_check output, the reuse
findings, and every **proposed content concept** as `okf_new.py --dry-run`
printed it. Get a response before any of them is written; then write the
approved ones by re-running the same command without `--dry-run`. Then hand off:

`/gw-draft NN`
