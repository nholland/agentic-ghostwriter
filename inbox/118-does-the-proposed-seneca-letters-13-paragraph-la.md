---
id: 118
status: resolved
raised_by: Publisher
chapter: 2
opened: 2026-10-04 22:12
resolved: 2026-10-04 22:45
applied_by: grep -q "beaten black and blue" books/the-stoic-husband/chapters/ch02/refined.md
okf_receipt: runs/reconciliation/2026-10-04-ch02-seneca-letters-13.json
---

# Does the proposed Seneca Letters 13 paragraph land in Chapter 2, and may the calm-house post (06) keep its image-word count?

Chapter 2 has had no Seneca since the quotation that is not in De Ira came out (inbox #116, your ruling C). Proposed: add Seneca's prizefighter from Letters 13 (Gummere, the house edition for the Letters) to 'The ruling faculty', after 'It might just be timing.' The paragraph, the sentences either side, and the counted check are in the PDF output/marketing/ch02-review-seneca-and-posts.pdf (source runs/ch02/review-seneca-letter-13.md). The quoted clause is one unbroken clause of Letters 13.2, verifiable but not verified (the Fact-Checker read a proofread copy of the Loeb text, not the scan). Not landed: chapters/ch02/refined.md is unchanged. Substack post 06 (runs/marketing/ch02/06-a-calm-house-isnt-proof.md, built on the same passage plus your line 'you can't be a boxer without being punched in the face') waits on this, because it cites a chapter passage that is not yet there. Second decision: 06's fight-image words (boxer, prizefighter, punched) count 6.2 per 1,000 against a cap of 5, since your line plus Seneca's quote already use three in a 485-word post. Waive that cap for this post as a recorded one-time exception, or stretch the post to about 600 words. If you say yes to the paragraph, the Publisher then adds the Letters 13 citation to the OKF, checks the Ch2 distillation and practice guide, updates the outline's two Seneca lines (03-outline.md lines 85 and 87, a constitution file: needs your word), and lands it as its own commit.

**Recommendation:** Yes to the paragraph as written, and waive the image-word cap for post 06 as a one-time exception in your words, since the image is your chosen spine.

**Checked:**

```
voice_check on the Ch2 prose before and after the paragraph (weather family): em-dash 1 and 1 (epigraph attribution line, unchanged), long sentences 2.9% and 3.4%, you-density 51.6 and 49.6 per 1,000, weather 3 and 3. voice_check on post 06 body (boxer, prizefighter, punched): 3 mentions in 485 words = 6.2 per 1,000, cap 5; every other check passes.
```

**What unblocks this:** Landing the Ch2 Seneca paragraph; finishing post 06 for inbox #117; the outline's Seneca lines.

**Resolution (2026-10-04 22:45):** Author: "The paragraph lands." Landed in chapters/ch02/refined.md with the Letters 13 citation. The second question (whether to waive the image-word cap on post 06) was not ruled; the author is publishing Substack one chapter at a time and asked for no further action, so post 06 stays as drafted, unwaived, noted in inbox #117. The outline lines 85 and 87 still name the removed De Ira quotation; not changed, they need his explicit word.

**Not applied yet.** This ruling lands outside this repo. It closes when `grep -q "beaten black and blue" books/the-stoic-husband/chapters/ch02/refined.md` exits 0.

**Applied, confirmed 2026-10-04 22:45:** `grep -q "beaten black and blue" books/the-stoic-husband/chapters/ch02/refined.md` now exits 0.
