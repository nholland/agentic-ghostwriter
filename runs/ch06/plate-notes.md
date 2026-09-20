# Chapter 6 plate notes — 2026-09-20

**File:** `runs/ch06/plate.svg` · **Title (aria-label):** The Tally You Don't Read Aloud · **New drawing.**

## What it shows, and why that is the mechanism

Mechanism: **The Tally You Don't Read Aloud.** Conversation sentence:
"Resentment doesn't come from doing too much. It comes from being the only one
who can see it."

The plate is two bars and one fork.

- **THE WEEK** is a dashed outline: everything you actually carried, real and
  unreadable by anyone else. Caption: "the bucket you emptied, with no slot on
  the calendar."
- **TONIGHT** is the same bar, solid: "her hands moving, yours still." Under
  it: "The comment fires on the one the room can see."
- Below the rule, the fork the chapter turns on. **READ IT ALOUD** gives "now
  there are two tallies / and neither one gets shorter." **SAY WHAT YOU SEE**
  gives the chapter's own sentence back to her.

The closing pair states the mechanism plainly: "Keeping the tally is not the
problem. Reading it out is. / Read yours out and you have handed her a reason
to keep one."

That is the chapter's argument and not Chapter 7's. See the note below.

## How this differs from Chapter 7's plate

Both chapters have a tally. They are different claims and the two plates are
different diagrams.

- **Ch6** is about **visibility in a moment and what you do with it.** The
  tally is accurate; it is just invisible to her, and the damage is done by
  reciting it. The picture is two bars (unseen, seen) and a fork (recite,
  or name what she is doing). There is no rock, no sand, no proportion.
- **Ch7** is about **the tally's data being wrong.** It can only hold the few
  contributions big enough to remember, so it always says you are ahead. The
  picture is proportion: three big rocks against a field of small ones.

One plate says *do not read it out*. The other says *it was never a count*.

## The anchor image, and the prose it comes from

Ch6's own image is the **bucket**: "it just lives in the bucket labeled
'whatever needs doing'... There's no slot on the calendar that says 'ceiling
fan.' There's no moment where either of you notices it got emptied again." The
dashed bar is that bucket-week, drawn as a thing that exists and cannot be
seen. The solid bar is the chapter's visible moment: "What's in this room is
one person sitting and one person folding."

The quoted line on the right of the fork is the chapter's, lightly trimmed:
prose has "I see you're working. I appreciate it. You want to sit down, or
should I help first?"; the plate drops the middle sentence for width and keeps
the rest word for word. It is the author's sentence, not a source quotation, so
the citation rule for quotations does not apply.

Not drawn: Musonius Rufus on the "community of life", Marcus on getting out of
bed, and the Four D's. The Four D's already have their own plate
(`design/plates/four-ds.svg`), and drawing them here would make this the Ch3
plate a second time.

## Stoic terms

None on the plate, so no gloss is owed. The chapter itself uses no Greek or
Latin term (its Editor's Notes say the same), and the Marcus self-check is
carried in the chapter, not here.

## Style decisions, and what they were matched to

- Canvas `0 0 640 430`, white background rect, `style="color:#1a1a1a"` on the
  root: matched to `runs/ch12/plate.svg` and `four-ds.svg`.
- Two stacked bars with a left-hand `lbl` and a 10.5px caption under it is the
  exact form of the ch12 plate's rows (WALKING / RUNNING / READING, then
  ROMANCE with "no deadline, nobody watching" beneath).
- Solid bars are `fill="currentColor" opacity=".82"`, the ch12 value. The
  unseen bar uses `stroke-dasharray="3 5"` at 1.2 stroke and .5 opacity, the
  ch12 / operating-system treatment for what is not in play.
- The vertical hairline between the two halves of the fork is the divider from
  `small-rocks-big-rocks.svg`; the horizontal hairline above it is the
  `four-ds.svg` row rule. No arrowheads, none exist in the house set.
- Curly apostrophes and curly quotation marks, as in `four-ds.svg`.

**One technical correction worth keeping:** left-anchored captions are set with
`style="text-anchor:start"`, not the `text-anchor="start"` attribute. The `.cap`
class sets `text-anchor:middle`, and a CSS class beats a presentation
attribute, so the attribute form silently centres the caption and runs it off
the left edge. That is the defect `runs/design/svgcheck.py` was hardened for
mid-session; the ch12 plate has it.

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/ch06/plate.svg

runs/ch06/plate.svg
  clean
```

## What rendering showed

No geometry defects. The two bars read as the same week twice, once unseen and
once seen, and the fork reads as a choice rather than a sequence. First
rendering carried the caption "The comment fires on the solid one," which is
studio language about the drawing rather than prose about a marriage; changed
to "The comment fires on the one the room can see."

Same renderer caveat as Ch5: `svg_to_png` clips the bottom of the canvas, so
the two closing lines vanish in the shipped helper's PNG. Checked through a
padded window instead.

## For the author to rule on

1. **The subtitle carries half the conversation sentence.** "Resentment does
   not come from doing too much" fits; the whole sentence with "It comes from
   being the only one who can see it" does not fit one line at the house
   subtitle size, and every existing plate has a one-line subtitle. The second
   half is carried by the dashed bar and its caption. If he wants the whole
   sentence, the plate needs a two-line subtitle, which would be a new house
   pattern and is his call, not mine.
2. **The trimmed quoted line.** "I appreciate it." was dropped for width. If it
   matters, the fork's right column becomes three lines instead of two.

## Round 2 (2026-09-20 17:45)

Reader Panel review, section 2, Ch06: EDIT, cut half. The panel's finding was
that this was two plates on one page, and that the divider split attention
exactly where the plate should land.

**Applied.** The entire lower two-column panel is cut: READ IT ALOUD, SAY WHAT
YOU SEE, the vertical divider, and with them **the set's only quotation**, the
scripted line in quotation marks. That removes the one place in the set where a
plate could be photographed carrying speech. One caption is added under the
remaining pair, the panel's wording: *"The week is real. Only tonight is
visible."* The two closing lines are kept as the closing block, as the panel
asked, because they are the mechanism.

With half the plate gone the remaining pair was re-laid out to fill the canvas:
both bars are wider and deeper, and each label and its gloss now sit clear of
the bar rather than tucking under its edge.

**Not applied.** Nothing the panel asked for was declined. The two bars remain
the same length: the argument is visibility, not volume, and making the week
longer would restate Ch07's claim about size.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch06/plate.svg

runs/ch06/plate.svg
  clean
```

**What the render showed.** The first render after the cut had the row-one gloss
running under the dashed bar and touching it; the checker does not see
text-on-shape collisions, the render does. Both glosses were dropped clear and
the bars nudged. The final render reads as one comparison: a dashed empty bar
and a solid black one, the same size, one of them visible. At phone width the
dashed outline still reads as an outline.

**For the author to rule on.**

1. **The filled bar's meaning.** Here it means *visible*; the panel notes the
   same filled bar means accruing cost on Ch03 and rehearsal on Ch11. That is a
   book-wide call, not this plate's, and it is the panel's `design-language.md`
   recommendation in section 4.
