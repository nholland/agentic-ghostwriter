---
description: Take reader feedback in - paste what readers said - and route it to the right desk. The Publisher receives it; the Publicist logs it as a signal concept; the Developmental Editor, Line Editor or Fact-Checker act on it depending on what kind of feedback it is.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-signal/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-signal — reader feedback comes in here

Argument: a chapter number, then paste the responses. `$ARGUMENTS`

**The author hands feedback to the Publisher — to you — and never has to decide
which desk it belongs to.** Routing is the Publisher's job.

## Step 0

`python3 scripts/resolve_book.py`. Read the chapter as it was published (the
book repo's `refined.md`, and any Substack or social piece under
`marketing/`) so every response can be matched to the sentence it is about.

## Step 1 — log it before judging it

Dispatch `gw-publicist` to record each response as an OKF signal concept
(`okf/signals/`, per the format contract), attributed to its source and dated
from the clock. **Propose these; write after the author confirms** — a signal
concept is a record of what readers said, but the categorisation below is a
judgement, and the ledger should not carry a judgement he has not seen.

## Step 2 — categorise, then route by category

| What the response is | Goes to | Because |
|---|---|---|
| Reader got lost, misread a sentence, stumbled on a word | **Line Editor** (`gw-lineeditor`) | It is a prose problem. Fix proposed, not applied. |
| Argued objection to the chapter's claim | **Reader Panel** (`gw-panel`, the Skeptic) | Steel-man it, then say where the chapter answers it and where it does not. |
| Reaction without an argument | **Recorded, not routed.** | A pattern of them across readers is data; one is a mood. |
| A gift — a story, a counter-example, a better line | **Developmental Editor** (in session) | It is the author's material now, and it may change the commission. |
| A factual challenge — a study, a quotation, a date | **Fact-Checker** (`gw-factchecker`) | Ledger work. Nothing in prose changes until the ledger does. |
| An extension — "you should also cover…" | **Inbox** | Only the author decides scope. |

## Step 3 — one synthesis

What is landing, where readers get lost, argued objections worth answering,
gifts received, and specific revision recommendations split into
**immediate / pending author verification / consider**. Anything that would
change what the chapter argues goes to the inbox, never straight to a desk.

## What this never does

Change a published chapter on the strength of one reader. Treat a reaction as
an argument. Write a signal concept the author has not seen.
