---
description: Interactive re-edit of a refined chapter with the author, section by section, then refresh its distillation and practice-guide entry. Runs in session. Use after he has read a chapter and wants to change something.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-edit/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-edit — change a chapter, with him in the room

Argument: a chapter number, optionally a section name. `$ARGUMENTS`

**Runs as you, in session.** This is the one editing path that is not cold, because
its input is the author reacting to finished prose — which is the second of his two
touches, continued. A cold desk cannot hear "that line is not how I'd say it."

## Step 0

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

Find the chapter: `runs/chNN/refined.md`, or the book repo's `chapters/chNN/refined.md`.
**Say which you are editing.** If it is the book repo's, you may not write there —
produce the edit as a diff for him to apply with `/book-edit NN`, and say so up front
rather than after he has worked through it.

## How to run it

Walk the chapter **section by section**, not line by line and not whole-file. For
each section: show it, ask what is wrong, propose the change, get a yes. Then move on.

- Keep his wording. When he says how a line should go, that phrasing is the answer;
  do not improve it into something smoother.
- Change only what he raised. An adjacent sentence you think is weaker is not in scope
  unless he says so.
- One section at a time. A batch of twelve edits shown at once is a file he has to
  proofread, which is the thing he is trying to avoid.

## After any change, re-run the counted gates

An edit can break a count that passed. Do not assume it held:

```
python3 scripts/voice_check.py <file> --metaphor-family "<declared>"
```

Paste the output. If a HARD check now fails, say so and fix it with him — a chapter
that was clean before an edit and is not after is the edit's fault, not a new finding.

Then dispatch `gw-specchecker` if the edit touched anything the outline specifies.
Refinement breaking conformance is a recorded failure mode; so is editing.

## Refresh what the chapter generated

A changed chapter makes its derived artifacts stale. Dispatch `gw-lineeditor` to
regenerate:

- `runs/chNN/distillation.md` — the mechanism label and conversation sentence may
  have moved
- this chapter's section of `runs/appendix/practice-guide.md` — **append-safe: only
  this chapter's section, never another's**
- the plate, via `gw-designer`, if the mechanism changed. A plate drawing a mechanism
  the chapter no longer argues is worse than no plate.

## Close

Report what changed, the counts as the scripts printed them, which derived artifacts
were refreshed, and whether this was an edit in place or a diff for him to apply.
