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
