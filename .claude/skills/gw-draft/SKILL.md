---
description: The Ghostwriter desk drafts a chapter cold from its existing research brief, gated by the brief review, the counted voice script, and the clean-room checker. Writes into this repo's runs/ tree and never touches the book repo. Use for the shadow run of a chapter already researched in the playground pipeline.
---

# /gw-draft — draft a chapter cold, gated

Argument: a chapter number. `$ARGUMENTS`

This is the new pipeline's cold half. It reads the *same* research brief the old
pipeline used and writes to a separate tree, so the two can be compared without
either touching the other.

## Step 0 — resolve paths, and refuse rather than guess

Read `config/house.json` for `bookRoot`. Then confirm these exist:

- `{bookRoot}/01-voice.md`, `{bookRoot}/00-premise.md`, `{bookRoot}/03-outline.md`
- `{bookRoot}/chapters/chNN/research.md`  ← the brief. **Required.**

If the brief is missing, stop and say so. This desk does not research; the
research interview needs the author in the room and cannot run cold. That is the
automation boundary and this command does not cross it.

Output directory: `runs/chNN/`. Create it. **Never write inside `{bookRoot}`.**

## Step 1 — brief review (the first gate)

Dispatch `gw-ghostwriter` in **plan-only** mode against the brief and the outline
section. It returns a gap list.

- Empty gap list → proceed.
- Non-empty → write it to `runs/chNN/brief-gaps.md`, show it, and note which gaps
  are things only the author could close. **Proceed anyway** for a shadow run, and
  record the gap list as a finding: if the brief was thin and the old pipeline's
  chapter shipped fine, the author closed those gaps live, and that is exactly the
  measurement this exercise wants.

## Step 2 — draft

Dispatch `gw-ghostwriter` in **draft** mode. Output: `runs/chNN/draft.md`, ending
in a `## Draft Notes` section that declares `metaphor_family:`.

Name the desk you dispatched when you report back, so the author always knows who
is working.

## Step 3 — counted gate (the script, not your judgement)

```
python3 scripts/voice_check.py runs/chNN/draft.md --metaphor-family "<from Draft Notes>"
```

Paste the output verbatim. Do not summarise it and do not restate the numbers
from memory. If `metaphor_family` was not declared, say the check is UNCHECKED —
not passed.

On any HARD failure: hand the script output back to `gw-ghostwriter` to revise,
cold. Two rounds. Still failing after two → stop and write
`runs/chNN/inbox.md` with what is stuck and what ruling would unstick it.

## Step 4 — conformance gate (the clean-room agent)

Dispatch `gw-specchecker` with exactly two inputs: the outline section, and
`runs/chNN/draft.md`. Nothing else. Do not tell it which pipeline wrote the prose.

Write the result to `runs/chNN/conformance.md`. On any FAIL row, same two-round
revise loop, then the inbox.

## Step 5 — report

State: word count against the outline target, HARD check results as the script
printed them, conformance rows passed/total, attribution findings, placeholders
remaining, and every Draft Notes item the author needs to rule on.

Then say what the next command is: `/gw-refine NN`.

## What this command must never do

- Write anywhere inside `{bookRoot}`. The book repo stays untouched.
- Mark a citation verified, or resolve a placeholder with invented content.
- Claim a check passed that it did not run.
