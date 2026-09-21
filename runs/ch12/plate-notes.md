# Chapter 12 plate notes

**File:** `runs/ch12/plate.svg` · **Title (aria-label):** The Thing With No Deadline

## Round 1 (2026-09-20, no notes filed)

The plate shipped as `design/plates/the-muscle-you-stopped-using.svg`: three full
black bars labelled WALKING / RUNNING / READING over a fourth, broken bar
labelled ROMANCE, with the line *After Epictetus, Discourses 2.18* at the foot.
No notes file was written at the time; this section records what was there so the
replacement has something to be a replacement for.

## Round 2 (2026-09-20 17:45)

**Verdict acted on:** REPLACE CONCEPT, the worst-ranked plate in the set. The
panel's four faults were: the title was not the distillation's Mechanism; the
three identical black bars argued nothing, so the whole case sat in the caption;
the romance bar had three segments and two labels, one of them unexplained; and
it was the only plate in the book carrying a source line. Underneath all four,
the chapter's second half — care arriving in her language — was absent, and that
is where the ah-ha is.

**Panel edits applied, all of them.** Retitled **THE THING WITH NO DEADLINE**.
The three full bars are cut. The source line is cut. The drawing is now the
chapter's own image: a short ruled list of the week's necessary things, each with
a solid mark beside it, and one final ruled line, blank, no mark, glossed *her*.
Under it, as written: *Everything on this list had a day attached. One thing did
not.* The dropped second half is on the plate as one small mark: two glosses
beside the blank line, *said in your language* on a dashed lead that stops short
of the line, and *heard in hers* on a solid one that reaches it.

**Copy, and where it comes from.** Every entry is the chapter's own: "it's never
the mortgage or the kid's game at eight on a Saturday. Those shout. They have a
day attached and other people watching." The heading THE WEEK'S NECESSARY THINGS
is Marcus's correction as the chapter states it ("Do the necessary things
instead. That list is harder to write"). The subtitle *Nobody calls you at work
about this one* compresses "Nobody calls you at work because you haven't
surprised your wife since March". No Stoic term appears, so nothing needs a
gloss; Epictetus's habit line is the chapter's, not the plate's, now that the
bars are gone.

**Where I departed from the panel's spec.** It asked for five or six entries; the
list has four. The chapter names three shouting things and one category, and a
fifth entry would have had to be invented. Four marked lines plus the blank one
still reads as a list.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch12/plate.svg

runs/ch12/plate.svg
  clean
```

**What the render showed.** Ten-second read: a week's list, everything ticked,
one line left blank with her name under it. The missing mark in the left column
is the whole argument and it is visible without reading a word. The two language
glosses read as intended at the blank line's end: one arrives and stops short,
one reaches. Canvas 640x390, no collisions, whole canvas captured.

**For the author to rule on**

1. **"Everything else that shouts" as the fourth entry.** It is the chapter's
   verb ("Those shout") used as a category rather than a thing. If he would
   rather the list held only named items, it comes out and the list is three plus
   the blank line.
2. **The solid connector touches the blank line's right end**, so at small sizes
   it can read as the line bending rather than as something arriving. The
   alternative is an arrowhead, which no other plate uses.

## Round 3, draft from concept C (2026-09-20 19:50)

**What the plate shows.** Two rows of weeks running from the same start rule on
the left to one shared column on the right, labelled THIS WEEK. The top row,
THE THINGS WITH A DAY ATTACHED, carries a mark in every week, unbroken, right
into this one. The bottom row, THE ONE THING FOR HER, carries three marks near
the start and then nothing, and the week line keeps running underneath the
blank. At the far right, in the same THIS WEEK column, the bottom row's square
is open, larger than the marks and the only white shape on the page, with
TONIGHT under it.

**The carrier.** The distance between where the bottom row stopped and where we
are standing now. That length is the Conversation sentence: the elapsed time is
drawn, never printed, so no number appears. A stranger reads a stretch he did
not notice go by, and an open square that is this week rather than a verdict.

**How the two Panel instructions were solved in the drawing.** *Recognition,
not scorecard:* nothing counts his misses. No empty boxes march across the
blank, only the week line continuing, so the page records an absence rather
than a tally. The marks are set at .78 opacity rather than black, so the top
row is not a row of gold stars. The bracket under the blank is hairline weight
and carries two lines, *the stretch you never felt go by* and *you didn't stop
loving her*, the chapter's own exoneration sitting inside the gap itself.
*Visibly this week:* the right column is a shared vertical rule through both
rows with THIS WEEK at its head, so the open square is not the end of a record
but the present moment both rows are standing in; the rows stop there, nothing
runs past it, and TONIGHT sits under the square.

**Every phrase and where it comes from.**

- Title, THE THING WITH NO DEADLINE: the distillation's Mechanism, word for
  word, and the chapter's own section heading.
- Subtitle, *Nothing in a week tells you how long it has been*: "Nothing in a
  week tells you how long it's been." Chosen because it makes sense cold to a
  man who has read nothing, which the retired subtitle did not.
- THE THINGS WITH A DAY ATTACHED and *these shout, and other people are
  watching*: "Those shout. They have a day attached and other people watching."
- THE ONE THING FOR HER and *no day attached, and nobody waiting*: the same
  sentence read in the negative, which is the chapter's argument for why it
  goes.
- THIS WEEK, TONIGHT: "the muscle that puts her there is one you can start
  using tonight."
- *the stretch you never felt go by*: "Close to five months, and I hadn't felt
  one of them go by," with the number removed.
- *you didn't stop loving her*: the chapter's sentence exactly.
- Closing, *It is a thing you stopped doing. Starting again asks nobody's
  forgiveness*: "This is a thing you stopped doing, and starting again asks
  nobody's forgiveness."

No quotation, no statistic, no number, no source line, no Stoic term, so
nothing needs a gloss. The chapter's second half, care in her language, is not
on the plate: it needed a caption to explain rather than one drawn mark, and
the caption cap is spent. It stays in the chapter.

**Checker output, verbatim**

```
$ python3 scripts/plate_check.py runs/ch12/plate.svg --chapter 12

runs/ch12/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE THING WITH NO DEADLINE' / aria-label 'The Thing With No Deadline' vs Mechanism 'The Thing With No Deadline'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    6 italic lines against a cap of 6 (4 labels + subtitle + closing line)
  [ ok ] alignment   7 centred texts on the axis or a shared column; 8 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

All rows ok, no WARN and no FAIL, so nothing is carried to the Publisher from
the counted check.

**What the render showed.** At full size the ten-second read runs title, top row
full to the right edge, bottom row stopping a long way back, then the eye lands
on the one white square because it is the only unfilled shape on the page. The
open square was 12px and read as one more mark; it went to 13px at 1.8 stroke
and now holds the corner. The bracket and its two lines sit clear of the row
above and the foot rule. TONIGHT and the bottom gloss share a baseline with
about 120px of white between them, no collision. Nothing in the margins.

**For the author to rule on**

1. **TONIGHT set in the same bold small caps as the row labels.** It is the
   only imperative word on the plate, and a word can nag where a drawing does
   not. If it reads as an instruction rather than an opening, it comes out and
   THIS WEEK carries the column alone.
2. **Three marks at the start of her row.** The chapter says the dates stopped,
   not how many there had been, so three is a drawing decision standing for
   "briefly, a while ago". Any small number reads the same; I want it on the
   record that it is not a count of anything.

---

## Round 4, the outside-reader round (2026-09-21 04:53)

**Scope.** The author's ruling: *"No rethinks. Just improve our existing
concepts."* Objects are round 3's: two horizontal timelines running to the same
right-hand endpoint, dark squares along them, one hollow open square at the end.

**The reviewer's verdict.** "The timeline explains it, but again it feels
analytical." He asked for the conspicuous stretch of nothing in the lower line
to be what the eye lands on first, and for the single open square at the end to
read clearly as the chance still available. His overlapping-calendar-pages
redraw is excluded and was not attempted.

**What changed, all of it weighting and copy.**

- **The busy row was turned down.** The things with a day attached now sit at
  .34 with a .22 rule and a .45 label. They are the control, not the argument,
  and at full strength they were the loudest thing on the plate.
- **The row for her was turned up.** Its three early squares are at .9 on a .55
  rule, so the marked weeks are solid and the stretch after them is a hole.
- **The span marker is now visible.** It was a .28 hairline; it is 1.2 at .5,
  and it is the single mark that points at the emptiness.
- **The open square is the heaviest single object on the plate**: eighteen
  square at stroke 2.6, white-filled, up from thirteen at 1.8. The vertical
  guide that used to run straight through it now stops above it, so it reads as
  an opening rather than a crossing. TONIGHT sits directly beneath it.

**Copy, both lines from the endorsed pair on file** (`plate-brief.md`,
2026-09-21). Subtitle: **What has no deadline is easiest to neglect**, replacing
*Nothing in a week tells you how long it has been.* Closing: **Love rarely
becomes urgent. That is why you have to make room for it**, replacing *It is a
thing you stopped doing. Starting again asks nobody's forgiveness.* The author
preferred the second because it is about making room rather than about
scheduling, and that preference is the right one for the plate too: the old
subtitle was a fact about calendars and the new one is a fact about what
happens to unurgent things.

**Two captions cut.** *these shout, and other people are watching* and *no day
attached, and nobody waiting* both restated the labels immediately above them.
Four italic lines remain against a cap of six. **the stretch you never felt go
by** stays, because it names the argument, and **you didn't stop loving her**
stays, because it is the only line that keeps the plate from reading as an
accusation.

**plate_check.py, verbatim**

```
$ python3 scripts/plate_check.py runs/ch12/plate.svg --chapter 12
runs/ch12/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE THING WITH NO DEADLINE' / aria-label 'The Thing With No Deadline' vs Mechanism 'The Thing With No Deadline'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    4 italic lines against a cap of 6 (4 labels + subtitle + closing line)
  [ ok ] alignment   7 centred texts on the axis or a shared column; 9 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Round 3 was already clean; it is still clean, with two fewer captions.

**What the render showed.** Rendered twice at 2x. The first render had the THIS
WEEK guide running straight down through the open square, which muddied the one
object that had to read as open; shortening the guide fixed it. Final render:
the eye goes to the gap in the lower line, then to the heavy open square at the
end of it. Cover every word and the plate still says *this row got marked every
week, this one stopped, and there is one square left open.*

**For the author.** Nothing blocking. Worth knowing: the top row is now quiet
enough that on a small phone it can read as background rather than as a
comparison. That is deliberate and it is the reviewer's instruction, but it is
the one setting in this round I would most expect him to want dialled back.
