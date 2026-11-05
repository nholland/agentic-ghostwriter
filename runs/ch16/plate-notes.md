# Chapter 16 plate notes (draft 1)

Designer (gw-designer), draft mode. Clock read 2026-11-05 07:21. Concept A, "The capstone", picked by the Reader Panel (`runs/ch16/plate-pick.md`). Files: `runs/ch16/plate.svg`, render `runs/ch16/pdf/plate.png` (looked at).

## What it shows

Two blocks, mirrored about x=320, joined by an arrow.

- **Left:** two posts, CALM and STRENGTH, labelled separately, leaning apart (rotated 5 degrees outward about their bases) under an empty dashed slot. Inside the slot: "calm can go cold".
- **Right:** the same two posts standing true, with the heavy filled stone WARMTH laid flush across them (posts now meet the stone; in the thumbnail there was a gap). Above the stone: "on ordinary days, / without being asked". Below the labels: "one marriage".
- Closing line under a quiet rule: "At peace, at its best, and flourishing".

**The carrier:** completion. The only differences between the blocks are the stone and what it does to the posts: apart and leaning without it, true and joined under it. Warmth is what makes two qualities one structure, which is "what the calm and the strength were for".

The posts are two qualities in him, calm and strength, each named under its own post. Nothing on the plate is "him" or "her".

## Panel edits applied

1. CALM and STRENGTH labelled separately under each post, both blocks; "THE CALM AND THE STRENGTH" cut. Done.
2. Left posts tilted apart; right posts now sit flush under the stone. Done.
3. "calm can go cold" moved inside the empty dashed slot, where the warmth is missing. Done.
4. "on ordinary days," added above "without being asked" over the stone. Grounded check passed (three-word match "on ordinary days" in the Conversation sentence; the prose has "on an ordinary day, without being asked"). Caption count 6 against a cap of 7. Done.

## Every phrase of copy and its source

| Copy | Role | Source |
|---|---|---|
| Calm, strength and warmth together put the marriage in flow | title + aria-label | distillation Mechanism, word for word |
| Warmth is what the calm and the strength were for | subtitle | distillation Lesson; refined.md opening: "The warmth you bring her is what the calm and the strength were for." |
| CALM, STRENGTH (twice each) | labels | Mechanism |
| WARMTH | label (on the stone) | Mechanism |
| calm can go cold | gloss, empty slot | refined.md: "Calm was my first fix for that, and calm can go cold." |
| on ordinary days, / without being asked | gloss, stone | Conversation sentence: "on ordinary days and without being asked"; refined.md: "you did it on an ordinary day, without being asked" |
| one marriage | gloss, right block | Conversation sentence: "the two of you become one marriage" |
| At peace, at its best, and flourishing | closing line | refined.md: "Keep it at peace, at its best, and flourishing"; Conversation sentence |

No Stoic term is printed (equanimity, arete, eudaimonia appear only through their plain glosses). No number, no quotation, no em-dash. The image "capstone" is the chapter's own word ("It's the capstone, the piece that sits on top of everything you've done so far"); see the ruling below.

## Format checklist

- [x] Every centred text on the axis or a shared column: title, subtitle, closing on x=320; "on ordinary days," / "without being asked" / WARMTH / "one marriage" share x=460. **Exception, WARN:** CALM (134, 414), STRENGTH (226, 506) and "calm can go cold" (180) each sit on the axis of their own drawn element (post centre, slot centre) but have no other *text* on that column. The labels are mirrored across the plate (134+506 = 226+414 = 640) but the checker's rule is text-to-text. Adding copy only to give them partners would break the copy cap's spirit; left as a WARN for the Publisher/author.
- [x] Drawing blocks centred or mirrored: left block about x=180, right about x=460, mirrored about 320; arrow on the axis.
- [x] Canvas 640 wide (640x470).
- [x] Caption count within the cap: 6 italic lines against 7.
- [x] No bare `text-anchor` attribute: every anchor is set in a class.

## plate_check.py, verbatim

```
runs/ch16/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x470
  [ ok ] title       title 'Calm, strength and warmth together put the marriage in flow' / aria-label 'Calm, strength and warmth together put the marriage in flow' vs Mechanism 'Calm, strength and warmth together put the marriage in flow'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    6 italic lines against a cap of 7 (5 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'calm can go cold' x=180, 'CALM' x=134, 'STRENGTH' x=226, 'CALM' x=414, 'STRENGTH' x=506
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [ ok ] raster-current preview matches source pixels at its own scale
```

## Style matched

Ch15 and the thumbnail's class set (`ttl`, `sub`, `lbl`, `lblw`, `cap`, `capq`), Georgia with a Times New Roman / serif fallback, one ink `#1a1a1a` via `currentColor` with opacity for lighter tones, white ground, three line weights (1.4 quiet, 2 standard, 3.2 carrier), 640 wide with fitted height, per the approved chapter plate style in `books/the-stoic-husband/design/plates/README.md`.

## For the author to rule on

- **Capstone vs the declared anchor image.** The chapter's `metaphor_family` is the joint account; the plate draws the chapter's other image, "capstone". The Panel recommends the stronger image win on the plate; it needs his word under the one-image rule.
- **Alignment WARN** above: accept as is (labels on their posts' axes), or say if he wants a different label arrangement.
