# Chapter 13 plate notes (attention version, concept C)

Designer desk, draft mode (gw-plate Stage 3). 2026-09-30 14:42 (clock read).
Picked concept: C, "Two routes to Saturday" (`plate-pick.md`; runner-up B).
Earlier notes for the effort/action plate are in `pre-split/plate-notes.md` and git.

## What the plate shows

One target at the top, the chapter's own test: *one thing she'd be excited about
this Saturday*. Two routes rise to it from two mirrored columns.

- Left, grey and dashed: **arrange the whole thing** / what she liked / at
  twenty-six. It runs about three quarters of the way to the target and ends on a
  clean round cap, about 40px short. No stop bar.
- Right, solid with an arrowhead: **ask her** / who she is now / and ask about it
  again. It lands on the centre of the box's bottom edge (320,152).

Under the rule, the takeaway: *What stopped was your curiosity / about who she is
now.*

**Carrier:** reach. Doing things for her from what you knew of her years ago falls
short. Asking her who she is now gets there. Two routes aimed at one point, one
stopping and one arriving, mirrored on x=320.

**Why that is the mechanism:** the Conversation sentence has two halves. "You can
love your wife and keep doing things for her" is the left route: he is still
arranging things for her, and the line is aimed the right way. "And still have
stopped being curious about who she is now" is why it falls short, and the caption
says it in the chapter's own sentence. "Keep learning her" is the right route. Its
third line, *and ask about it again*, is there for the misreading the concepts file
named ("it shows one question answered, not learning kept up").

## Panel edits (plate-pick.md), applied

1. **Action on the dashed route.** "the plan you made" is not in the chapter, so I
   used the chapter's own verb from the same scene: "You want to **arrange the whole
   thing** yourself." Set bold above "what she liked / at twenty-six".
2. **"So you ask her." to "ask her".** Done. I added the Challenge's second ask as a
   third line so the two columns have matching line counts and baselines (1 bold
   + 2 regular each, at y=294/318/342).
3. **Dashed line stops visibly short with a clean end.** The line is 143px, exactly
   nine 8+7 dash periods plus a final full dash, so it ends on a dash with a round
   cap. The gap to the target is about 40px. The tilted bar is gone.
4. **Solid arrow at the centre of the box.** The tip is at (320,152), 4px under the
   box's bottom edge at x=320. Both routes aim at that same point, so the gap on the
   left reads as falling short and not as aiming somewhere else.
5. **Caption.** I did not use "You still do things for her. You stopped asking who
   she is now." Both sentences are paraphrase: the chapter says "you probably still
   do plenty for her" and "What stopped was your curiosity about who she is now."
   I used the second verbatim instead. The left route now carries "you still do
   things for her" through the drawing, so the caption only has to say what stopped.
   It also takes "She's changed" out of the subject position, as the Panel asked.

## Copy and sources (40 words, 11 text elements)

| Text | Words | Source |
|---|---|---|
| Keep learning her after you've won her | 7 | distillation **Mechanism**, verbatim |
| one thing she'd be excited / about this Saturday | 8 | refined, "The date you can't plan": "You can't name one thing she'd be excited about this Saturday."; distillation **Challenge** |
| arrange the whole thing | 4 | refined, same scene: "You want to arrange the whole thing yourself." |
| what she liked / at twenty-six | 5 | refined, same scene: "You know what she liked at twenty-six." |
| ask her | 2 | refined: "So you ask her."; distillation **Challenge**: "If you can't, ask her" |
| who she is now | 4 | refined: "What stopped was your curiosity about who she is now."; distillation **Conversation sentence** and **Lesson** |
| and ask about it again | 5 | distillation **Challenge**: "ask her, and ask about it again later in the week"; refined: "and then asked about it again" |
| What stopped was your curiosity / about who she is now. | 10 | refined, "When the attention changed", verbatim, one sentence over two lines |

Every phrase is the chapter's or the distillation's. No Author additions used. No
numbers, no quotation, no Stoic term (so no gloss needed), no em-dash.

## Style matched

Taken from the current Ch13 house plate
(`books/the-stoic-husband/design/plates/keep-choosing-her-in-ways-she-can-see.svg`)
and the concept thumbnail: 640x480, white ground, #1a1a1a via currentColor, Georgia
with a serif fallback, 24px semibold title on x=320, 17px semibold labels, 19px body,
21px italic takeaway, 2px round strokes, 0.8px rule at 28% opacity from x=64 to 576
at y=361. Columns at x=176 and x=464, mirrored on x=320 (the author's layout,
`author-wrap-direction.md`: centred text, takeaway under a separator). Both lines are
straight. There is no wavy or river-like line.

## Format checklist

- [x] Every centred text sits on x=320 or a shared column (x=176 / x=464): 11 texts.
- [x] The drawing is centred or mirrored: the box is on x=320, and the two routes mirror on it and meet at (320,152).
- [x] Canvas 640 wide (640x480).
- [x] Caption count within the cap: 2 italic lines against a cap of 4.
- [x] No bare `text-anchor` attribute. All anchors are set in classes.
- [x] Every shape has an explicit fill (the paths set `fill:none` in `.ln` and `.rule`).
- [x] Rendered to `runs/ch13/pdf/plate.png` and looked at. Nothing clips or collides, the dashed end reads as short of the box, and the arrowhead sits under the box's centre.

## plate_check.py (Designer's run; the Publisher runs it again)

`python3 scripts/plate_check.py runs/ch13/plate.svg --chapter 13`, run after the render:

```text
runs/ch13/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x480
  [ ok ] title       title "Keep learning her after you've won her" / aria-label "Keep learning her after you've won her" vs Mechanism "Keep learning her after you've won her"
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   11 centred texts on the axis or a shared column; 0 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [ ok ] raster-current preview matches source pixels at its own scale
```

The first draft failed geometry. "what she liked at twenty-six" on one line
measured 16..336 (MARGIN), so I split it over two lines and raised the box 10px to
make room for the third line in each column.

## For the author to rule on

1. **"arrange the whole thing"** stands in for the Panel's "the plan you made",
   which the chapter never says. The fallback is "you chose the place" ("You chose
   the place and made the reservation."), but that comes from the dinner scene, not
   the Saturday scene.
2. **"who she is now" appears twice**, once in the right column and once in the
   takeaway. I kept it on purpose so the takeaway points back at the route that
   arrives. If it reads as repetition, the right column can drop to "ask her / and
   ask about it again".
3. **Anchor image.** The brief still gives `metaphor_family: river`. The attention
   chapter uses no river, and this plate draws none, as the author asked. This is
   still open from the concepts file, and it is a distillation fix.
