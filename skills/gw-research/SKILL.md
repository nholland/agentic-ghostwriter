---
description: The Researcher desk builds a chapter research brief cold from the interview record, gated by the Ghostwriter's plan-only review of whether the brief can be written from at all. Use after /gw-interview.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-research/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
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

It writes **gap markers** and **source findings** directly (Rule 9) — the brief
needs their paths. It **proposes** content concepts, the author's own material,
in `runs/chNN/proposed-concepts.md` (`status: open`) rather than writing them.

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

## Step 3 — citation gate

```
python3 scripts/okf_gate.py
```

A structural failure blocks; unverified citations do not (Rule 4).

## Step 4 — check in

Show the author: the brief, the gap list, the reuse findings, and every **proposed
content concept** in `runs/chNN/proposed-concepts.md`. Get a response before any of
them is written. Write the accepted ones, record his answer under each proposal,
and set the file's `status: answered` — until then `next.py` reports the chapter
as waiting on him. Then hand off:

`/gw-draft NN`
