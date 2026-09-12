---
description: Whole-book QA - the Reader Panel's four personas plus the Anti-Slop Reader's cross-chapter pass, synthesized into one ranked list. Needs the whole manuscript, not a single chapter.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-qa/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-qa — the Reader Panel and the Anti-Slop Reader

Argument: optional chapter range. `$ARGUMENTS`

These checks only make sense at book level. They find what no per-chapter pass
can: the same opening structure twice across Parts, anchor metaphors that
contradict each other, a term used as established that nothing ever defined.

## Step 0

`python3 scripts/resolve_book.py`. You need the compiled manuscript or the refined
chapter range. The book repo's `/book-compile` produces the manuscript; this repo
does not compile, and must not write one into the book repo.

If fewer than half the planned chapters are refined, say so before running: a
tension audit over a third of an arc will report a flat arc that is simply
incomplete, and that is a false finding the author may act on.

## Step 1 — dispatch both desks, in parallel

- `gw-panel` — skeptic, beta readers, tension, continuity. Returns **one**
  synthesized ranked list, not four reports.
- `gw-slopreader` — qualitative categories per chapter, plus the cross-chapter
  patterns.

Name both. They are read-only; neither fixes anything.

## Step 2 — merge without averaging

Produce one ranked list, most damaging first: what it is, which desk raised it,
which chapters, the evidence, what a fix costs.

Where the two desks disagree, **say so and keep both.** Averaging two readings
into a moderate one destroys the only signal a disagreement carries.

Write to `runs/qa/<date>-qa.md`, dated from the real clock.

## Step 3 — the author's gate

Present the top issues as a table and get his review before anything downstream
acts on them. Findings that need a ruling go to the inbox, one item each.

Do not open a fix loop from here. This command reports.
