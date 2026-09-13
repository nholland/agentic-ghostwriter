---
description: The production floor - dispatch every cold stage that can run right now, across all chapters, in parallel, without pausing. The Level 3 handle - many chapters, many desks, the author nowhere in the loop until something needs him. Use when he wants the house to work while he is away or while he is in another chapter's interview.
---

# /gw-floor — everything cold, at once

Argument: optional `--only <stage>` (research | draft | refine | plate), `--max N`, `--dry-run`. `$ARGUMENTS`

`/gw-chapter N` runs one chapter through the house. This runs the **floor**:
every chapter whose next stage needs no author, all at once. While he is in the
Chapter 13 interview, the Researcher can be finishing 12's brief follow-ups,
the Ghostwriter drafting 12 cold from the book pipeline's brief, the Line
Editor refining 11, the Designer drawing 10's plate. Nothing waits for him
except what only he can do.

**You are the Publisher for the whole run.** You dispatch; you do not write prose.

## Step 0 — the oracle decides what is cold

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
python3 scripts/next.py --floor
```

All three blocking. The third is the work list: every chapter and the cold
stage it is at. **Do not add a chapter the oracle did not list** and do not
compute your own list from a directory read. If it prints "nothing cold can
run", say so and stop: every open stage is his.

`--dry-run` prints the list and dispatches nothing.

## Step 1 — dispatch in parallel

For each row, dispatch the stage's skill **as a sub-agent run of that skill's
cold section**, all in the same turn, each writing only under its own
`runs/chNN/`:

| Stage | Follow | Cold desk(s) it dispatches |
|---|---|---|
| `research` | `/gw-research` Steps 1–3 | `gw-researcher`, then `gw-ghostwriter` plan-only, `term_check.py`, `okf_gate.py` |
| `draft` | `/gw-draft` Steps 1–4 (`--shadow` when the row says so) | `gw-ghostwriter`, `voice_check.py`, `gw-specchecker` |
| `refine` | `/gw-refine` Steps 1–4 | `gw-lineeditor`, `voice_check.py`, `gw-slopreader`, `gw-specchecker` |
| `plate` | the plate step of `/gw-chapter` | `gw-designer` |

Two chapters never write the same file: each stage writes inside its own
chapter directory, the practice guide is append-only per chapter section, and
concepts are created through `okf_new.py`, which refuses to overwrite. Name
every desk you dispatched, per chapter, in your reply.

## Step 2 — gates and the two-round rule, per chapter

Each chapter's gates run exactly as its stage skill says. A chapter that fails a
gate twice is **parked**, not looped:

```
python3 scripts/inbox.py --add "<what is stuck>" --raised-by <desk> --chapter NN \
    --context "<what he needs to answer cold>" --unblocks "<the ruling>"
```

A parked chapter stops; the others continue. One chapter's failure never holds
the floor.

## Step 3 — the board, and what is waiting on him

When everything dispatched has returned:

```
python3 scripts/next.py
python3 scripts/inbox.py
```

Report per chapter: the stage completed, the counts as the scripts printed them,
conformance rows passed of total, and whether it is parked. Then the inbox. Then
what the floor could run next, and what is his: the interviews not yet held and
the verdicts not yet given.

## What this command never does

Run the interview or the verdict; those are his. Resolve an inbox item to keep
a chapter moving. Dispatch a stage the oracle did not list. Write inside the
book repo. Claim a count it did not see printed.
