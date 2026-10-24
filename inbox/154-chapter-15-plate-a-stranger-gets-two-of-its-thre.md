---
id: 154
status: open
raised_by: gw-panel
chapter: 15
opened: 2026-10-24 06:06
---

# Chapter 15 plate: a stranger gets two of its three parts after two rounds. Allow one more Designer round on six fixes, or take the plate as it is?

Concept A was picked cold over B and C. Round 2 stranger read: 'When she takes a little shot at you, don't fire back bigger; treat it as a sign of how she's feeling and take something off her plate instead.' That lands 'hear it as a sign of how she feels' and 'help before you answer', but not 'ask yourself whether you were the best part of her day' (your question is on the plate but he reads past it). Six things confuse him: the empty unlabelled dashed box on her side; the label 'how she's feeling on the inside' floats loose; her lower zing looks the same as the top slights; 'an equal or escalated response' is too small in the margin; a defensive man reads the growing zigzags as blame of him; the whole reads 'she insults me and my answer is to do her dishes'. Files: runs/ch15/plate.svg and pdf/plate.png (final), plate-read.md (round 2), plate-read-round-1.md, plate-concepts.md and concepts/ (three concepts), plate-pick.md. The plate never blocks the chapter.

**Recommendation:** One more Designer round on the four drawing problems only (delete or label the dashed box, anchor the inside-feeling label to her zing, make her lower zing visibly different from the top slights, enlarge the 'equal or escalated' label). Leave the skeptic's reading to you at the verdict; it comes from the concept, not the drawing.

**Checked:**

```
python3 scripts/plate_check.py runs/ch15/plate.svg --chapter 15 -> every row [ ok ] (canvas 640x566, 6 captions against a cap of 7, grounded, alignment, ink); Reader Panel round 2 read: 6 confusions listed in runs/ch15/plate-read.md
```

**What unblocks this:** Whether the Designer gets a third pass (gw-plate allows two), or the plate goes to the verdict as drawn
