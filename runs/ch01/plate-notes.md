# Ch1 Plate Notes — 2026-09-20

**File:** `runs/ch01/plate.svg` — "The Three-Second Window"
**Reused, not new.** Copied from `books/the-stoic-husband/design/plates/three-second-window.svg`.

## What it shows, and why that is the mechanism

The distillation's **Mechanism: The Gap**, and its conversation sentence is
"Between what she says and your response is three seconds. What fills it,
chosen or inherited, is your marriage." The existing plate draws exactly that
and nothing else: one three-second bar, split 0.5s filled / 2.5s open, with
"she says something" at the left end and "the words are already out" at the
right. The filled part is the window; the rest is already firing. Its subtitle
is the second half of the conversation sentence verbatim.

Nothing I could draw would put the mechanism better, and a second Gap diagram
would be a competitor to an approved one.

## Runners-up, for the author's record

Both are Ch1's, both were left where they are:

- `the-operating-system.svg` — draws trigger + loaded meaning + THE GAP +
  automatic response. It is the *route* the impression takes, the chapter's
  umbrella mechanism, not "The Gap" as the distillation names it. It also
  fails the checker as it stands (two labels overflow the right margin, see
  below) and carries an em-dash in a label ("an impression — phantasia").
- `virtue-question.svg` — draws the chapter's practice (the four virtue
  labels), not its mechanism.

One plate per chapter: Ch1 ends with the window.

## Anchor image

The window itself, from the chapter's own line quoted in the plates README:
"that half-second where you're still somewhere between deciding and
reacting... and then the two and a half seconds after." No new image
introduced.

## Two changes I made to the copy

1. **A real defect, caught by the hardened checker and confirmed by
   rendering.** The source file sets `text-anchor="start"` / `"end"` as
   presentation attributes on two captions whose class already says
   `text-anchor:middle`. The stylesheet wins in a browser, so both captions
   rendered centred on the bar ends: "she says something" started 36px outside
   the left margin and "the words are already out" ran 16px past the right
   edge of the artboard. Fixed in the copy by moving the anchors to inline
   `style=`, which does win. The rendered result now matches the intent.
   **The same defect is still live in `design/plates/three-second-window.svg`.**
   I did not touch it (Rule 8). The desk reviewing the existing plates should
   make the same fix there, or the author should rule.
2. **House ink and ground.** Added `style="color:#1a1a1a"` and a white
   background rect, matching `runs/ch12/plate.svg`, the most recent chapter
   plate. Without them the filled block prints pure black against the other
   plates' near-black, and the plate has no opaque ground in the reader PDF.
   Purely a conformance change; no geometry or wording altered.

## Checker output, verbatim

```
runs/ch01/plate.svg
  clean
```

## What the render showed

Correct after the anchor fix: title, subtitle, both stage labels with their
durations, the split bar, both end captions inside the margins, the bracket,
THREE SECONDS, and the closing caption.

**A renderer finding the author should know about, not a plate defect.**
`chapter_pdf_local.svg_to_png` drops everything below roughly 83% of the
canvas height: Chrome is screenshotting a viewport shorter than the requested
window. It cuts the bottom two lines off this plate, the bottom three lines
off `runs/ch12/plate.svg`, and the closing lines off all three of my new
plates. I verified every plate by re-rendering into a viewport padded 140px
taller. Anything compiling plates into the reader PDF today should check that
it is not using the same call, or the bottom of every plate will be missing.

## For the author to rule on

- **Canvas.** This plate is 660x380; the house landscape standard is 640x430
  and Ch12 is 640x460. Three different canvases will show as three different
  page sizes in a reader PDF. I left the reused plate at its own size rather
  than reflowing the author's layout. Say the word and I will reset it to
  640x430.
