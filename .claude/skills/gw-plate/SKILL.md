---
description: The Publisher runs one chapter's plate through the house - a mechanical brief, three concepts from the Designer, the Reader Panel's cold pick, the draft, the counted check, the Panel's standalone read, one revision - and packages it for the author's verdict. Writes only under runs/chNN/. Stage 5 of /gw-chapter, and the way an existing plate is redone.
---

# /gw-plate — one plate, through the house

Argument: a chapter number, optionally `--from <stage>`, `--pick` (the author
chooses the concept himself), or `--part N` for an Arc closing plate.
`$ARGUMENTS`

**The standard, in the author's words (2026-09-20):** *"These plates need to
stand on their own even if somebody hasn't read the chapter."* Every stage
below serves that sentence. A plate that only makes sense after the chapter has
failed, however handsome.

Why these stages exist: on 2026-09-20 eleven plates went from distillation to
finished drawing in one step, the first idea shipped every time, every reviewer
read them *with* the chapter, and the author found in one reading what no desk
had: an off-centre block, a label the chapter never says, a title that was not
the mechanism, a plate that only works if you read the chapter. His own list of
what was missing, *formulate ideas, pick the best, draft, checks, persona
input, revisions, formatting*, is this file.

## Step 0

```
python3 scripts/resolve_book.py
python3 scripts/plate_brief.py N
```

`resolve_book.py` is blocking. The brief needs `distillation.md` and
`refined.md` (in `runs/chNN/` or landed under `{bookRoot}/chapters/chNN/`);
without both there is no mechanism to draw and the run stops. If the author
gave words for this plate in session, record them now, verbatim:
`python3 scripts/plate_brief.py N --add "his words"`. Never write inside
`{bookRoot}` (Rule 8); the plate lands with the chapter's verdict, or on its own
verdict for a chapter already landed.

## Stage 1 — concepts (the Designer, concepts mode)

Dispatch `gw-designer` in **concepts mode** against `runs/chNN/plate-brief.md`,
the distillation and the prose. It returns `runs/chNN/plate-concepts.md` with
**three** concepts, A, B and C, each with three different carriers (the one
drawn relationship that is the argument), and three rough thumbnails in
`runs/chNN/concepts/`. No finished plate. Name the desk when you report.

Gate: three concepts, three carriers. Two variants of one drawing is one
concept; send it back once.

## Stage 2 — the pick (the Reader Panel, cold; or the author with `--pick`)

Dispatch `gw-panel` on the three thumbnails **without the chapter**: for each,
what a stranger takes away in ten seconds on a phone. Then, with the
distillation, which one lands the Conversation sentence, in one line. It writes
`runs/chNN/plate-pick.md`. The runners-up stay on disk for the verdict.

With `--pick`, the Publisher shows the author the three thumbnails and the
Panel's one line each, and he chooses. The author decided on 2026-09-20 that
the Panel picks by default and he overrides at the verdict.

## Stage 3 — draft (the Designer)

Dispatch `gw-designer` to draw the picked concept as `runs/chNN/plate.svg`, in
the house style, with `plate-notes.md` recording what the plate shows, the
carrier, the copy and where each phrase comes from. Title is the Mechanism line,
word for word (inbox #065).

## Stage 4 — the counted check, independently (Rule 7)

Do not take the Designer's word for it. Run it yourself and paste the output:

```
python3 scripts/plate_check.py runs/chNN/plate.svg --chapter N
```

Any `[FAIL]` row goes back to the Designer with the row quoted. `[WARN]` rows
are for judgement: `grounded` names copy the chapter does not say (the author's
words, recorded in the brief, are grounded); `alignment` names what sits on no
axis; `captions` and `title` are WARN until #065/#066 are ratified. Then render
and look:

```
python3 -c "import sys; sys.path.insert(0,'scripts'); from chapter_pdf_local import svg_to_png; svg_to_png('runs/chNN/plate.svg','runs/chNN/pdf/plate.png')"
```

A checker cannot see a beam that misses its fulcrum. Read the PNG.

## Stage 5 — the standalone read (the Reader Panel, cold)

Dispatch `gw-panel` on the finished plate **alone**, no chapter, no brief: one
sentence, *what this says to a man who never read the chapter*. Then against
the distillation: PASS if that sentence is the Conversation sentence in his
words, or an edit list, each edit concrete enough to draw. It writes
`runs/chNN/plate-read.md`.

## Stage 6 — revise and format (the Designer), once

Dispatch `gw-designer` with `plate-read.md` and the check's WARN rows. It
revises, ticks the format checklist in its notes (every centred text on the
axis or a shared column; drawing blocks centred or mirrored; canvas 640 wide;
caption count within the cap; no bare `text-anchor` attribute), and returns.
Then Stage 4 and Stage 5 again, once.

**Two rounds, then the inbox (Rule 6).** A plate that fails the standalone read
twice goes to the inbox with the three concepts and both reads attached, not
around a third time.

## Stage 7 — package

`runs/chNN/pdf/plate.png` rendered from the final SVG, shown to the author with
the Panel's one-sentence read and the check's rows, verbatim. His verdict lands
it: with the chapter through `land.py` (which now runs `plate_check.py` before
copying, inbox #062), or as a plate verdict for a chapter already landed.

## Arc plates (`--part N`)

Same stages, different source: the Part's opening page is the only text, the
caption is its last sentence verbatim, and the form rules are
`{bookRoot}/parts/README.md`. `plate_check.py --part N` checks the canvas and
charset; grounding and title do not apply.

## What this command never does

Draw the first idea. Read a plate with the chapter before reading it without.
Let the Designer report its own check. Land anything. Put a word on a plate that
the chapter or the author did not say.
