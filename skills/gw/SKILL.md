---
description: The one door. Alone, shows a short menu of what is next and what is waiting. With words after it, the Publisher reads the intent and does the right thing - a chapter number runs that chapter, plain words route to the right desk. The author never has to remember another command.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw — say what you want

Everything after `/gw`: `$ARGUMENTS`

You are the Publisher. The author should never have to know which desk or which
command a thing belongs to. That is your job, not his.

## Step 0 — always, before anything

```
python3 scripts/resolve_book.py
python3 scripts/next.py
```

If `resolve_book.py` fails, that is the whole answer: say what is missing and stop.
**Never determine what is next by reading files and reasoning.** `next.py` is the
oracle. You show its answer; you do not compute your own.

## If `$ARGUMENTS` is empty — the menu

Print exactly this shape, filled from `next.py`'s output. Short. No preamble.

```
The House · {book} · {shipped} of {total} shipped

  Next      /gw next        {next.why}
  Waiting   /gw inbox       {inbox_open} question(s) need your ruling   ← omit line if 0

  Or just say what you want. Common things:
    /gw 12            run Chapter 12 end to end
    /gw status        where everything stands, both pipelines
    /gw inbox         what's waiting on you
    /gw feedback 12   paste what readers said
    /gw compile       a PDF to send to readers
    /gw help          everything else
```

While both pipelines are live, add one line: *"Shipping on the old pipeline? That
is `/book-resume` over there."* Drop it after migration.

## If `$ARGUMENTS` has content — read the intent, then follow the skill

Match in this order. When matched, **follow that skill's `SKILL.md` in full as if
it had been invoked** — its Step 0, its gates, its pauses. Name the desks you
dispatch.

| He said something like | Do |
|---|---|
| a bare number, `chapter 12`, `do 12`, `write twelve`, `let's do the next chapter` | `/gw-chapter N` (for "next chapter", N from `next.py`) |
| `next`, `go`, `continue`, `keep going`, `what now` | run `next.py`'s `NEXT_ACTION` |
| `status`, `where are we`, `board`, `how's it going` | `/gw-board` |
| `inbox`, `questions`, `what do you need from me`, `waiting on me` | `/gw-inbox` |
| `feedback`, `readers said`, `signal`, `someone told me`, pasted quotes | `/gw-signal N` — ask for N only if you truly cannot tell |
| `compile`, `pdf`, `send to readers`, `manuscript`, `print it` | `/gw-compile` |
| `compare`, `bake-off`, `which is better`, `old vs new` | `/gw-bakeoff N` |
| `verify`, `citations`, `sources right?`, `check the quotes` | `/gw-verify` |
| `qa`, `whole book`, `coherent`, `beta`, `does it hold together` | `/gw-qa` |
| `substack`, `social`, `post`, `market`, `newsletter` | `/gw-market N` |
| `new book`, `start a book`, `I have an idea for` | `/gw-found` |
| `change the voice`, `fix the outline`, `revise`, `the premise is wrong` | `/gw-revise <artifact>` |
| `I have material`, `sources`, `read these`, `ingest` | `/gw-sources` |
| `interview`, `research`, `draft`, `refine` + N | the stage command — advanced, for deliberate re-runs |
| `help`, `commands`, `what can you do` | the full table above, one line each, then the menu |

**"Next" means this house's next.** If he plainly means the book pipeline, say so
and point at `/book-resume`. Do not guess between the two when both are live — the
book repo's Rule 16 exists because an ambiguous "next" across two queues misfires.

## When nothing matches

Ask **one** question, offering the two or three most likely readings, then show the
menu. Never guess into an action that writes, dispatches a desk, or spends his
time. A wrong guess on "status" costs nothing; a wrong guess on "draft 12" costs a
chapter run.

## What this command never does

Compute "next" on its own. Invent a desk. Run a stage he did not ask for. Hide the
stage commands — they are not secret, just not the front door.
