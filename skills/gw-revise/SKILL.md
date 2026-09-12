---
description: Revisit a locked foundation artifact - premise, voice, audience, outline, archetype, framework, sources - with the author. Proposes changes for a book another pipeline ships; writes only for a book this engine owns.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-revise/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-revise — revisit a locked artifact

Argument: the artifact name. `$ARGUMENTS`
(`premise`, `voice`, `audience`, `outline`, `archetype`, `framework`, `sources`)

## Step 0 — who owns this book

```
python3 scripts/resolve_book.py
```

| Case | What you may do |
|---|---|
| **This engine created the book** | Revise in place, after check-in. |
| **Another pipeline ships it** (The Stoic Husband) | **Propose only.** Produce the exact diff and hand it to the author. Writing here creates a second source of truth for an artifact the other pipeline also edits. |

Say which case you are in before showing anything.

## Why revision is not regeneration

These artifacts carry their own history. `01-voice.md` is 200-plus lines where most
rules are paired with the incident that produced them: the long-sentence cap exists
because Ch8 ran at 22% against a Ch1–7 range of 1–15%; the wife's-mood rule exists
because of reader feedback on a Substack post, and then sat on an unpushed branch
for five weeks while Ch9 onward were written without it.

**Regenerating such a file silently deletes that history.** So:

- Read the whole artifact, including its revision log at the bottom where one exists.
- Change only what the author asked to change.
- **Net-zero by construction:** if a rule is being merged or reworded, keep its
  operative test verbatim inside the new text, and say in your diff which old rule
  maps to which new one.
- Append to the revision log: what changed, why, what triggered it, and the date
  from `date '+%Y-%m-%d %H:%M'`.

## If the change touches a counted rule

Any edit to a threshold in `01-voice.md` — the bold cap, the metaphor family cap,
the long-sentence cap, the you-density floor, the device cap — **also requires
updating `config/house.json`**, whose eight thresholds are transcribed from that
file. Run afterwards:

```
python3 scripts/voice_rules_check.py
```

It fails when the spec wording a threshold came from no longer appears. That check
exists because this config was, briefly, a hand-made copy with nothing keeping it
equal to the spec.

## If the change is a chapter retitle

A retitle breaks slug identity. Run the full sweep before calling it done: grep the
old slug across `okf/` and migrate every `chapter_slugs` tag; grep the old title
verbatim across the book folder including the outline and framework; **count
occurrences before editing, edit, then re-grep to confirm zero remain.**

## Check in, then stop

Show the diff. Get a response. For a book another pipeline ships, hand him the diff
and say which of its commands applies it. Do not apply it yourself.
