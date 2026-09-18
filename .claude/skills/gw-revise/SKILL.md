---
description: Revisit a locked foundation artifact - premise, voice, audience, outline, archetype, framework, sources - with the author, in session. Shows the diff, applies it on his word as its own commit, and moves the engine's mirrored threshold in the same commit.
---

# /gw-revise — revisit a locked artifact

Argument: the artifact name. `$ARGUMENTS`
(`premise`, `voice`, `audience`, `outline`, `archetype`, `framework`, `sources`)

## Step 0 — who owns this book

```
python3 scripts/resolve_book.py
```

Every book under `books/` is this engine's to revise, in session, after check-in.
L4 is never edited cold: a desk that thinks it should change files an inbox item,
and the Publisher brings it here. Where `config/house.json` mirrors a threshold
(the counted voice rules), the spec changes first and the value in the same
commit; `voice_rules_check.py` blocks the next gate on a mismatch (Rule 8).

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

Show the diff. Get a response. On his yes, apply it as its own commit quoting his
word, then run `python3 scripts/okf_gate.py` - a threshold the spec no longer
states is a structural failure and blocks until `config/house.json` follows.
