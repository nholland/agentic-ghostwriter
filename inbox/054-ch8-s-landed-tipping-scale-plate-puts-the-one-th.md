---
id: 054
status: resolved
raised_by: gw-designer
chapter: 8
opened: 2026-09-20 16:33
resolved: 2026-10-01 23:03
applied_by: cmp -s runs/ch08/plate.svg books/the-stoic-husband/design/plates/tipping-scale.svg
okf_receipt: runs/reconciliation/2026-10-01-inbox-054.json
---

# Ch8's landed Tipping Scale plate puts 'the one that finally tipped it' on the pan that is UP. Land the corrected plate (weight dropping onto the loaded pan), or relabel it?

Two Designer desks found it independently (runs/design/2026-09-20-plate-review.md; runs/ch08/plate-notes.md). The corrected version is runs/ch08/plate.svg and is what today's feedback PDF carries as a draft. The landed design/plates/tipping-scale.svg is unchanged.

**Recommendation:** Land the corrected plate: it says what the chapter says.

**Checked:**

```
python3 runs/design/svgcheck.py runs/ch08/plate.svg -> clean. Review desk: 'tipping-scale argues the opposite of its caption: the beam tips away from the pan labelled the one that finally tipped it.'
```

**What unblocks this:** Whether design/plates/tipping-scale.svg is replaced by runs/ch08/plate.svg at the next land.

**Resolution (2026-10-01 23:03):** Approved

**Not applied yet.** This ruling lands outside this repo. It closes when `cmp -s runs/ch08/plate.svg books/the-stoic-husband/design/plates/tipping-scale.svg` exits 0.

**Applied, confirmed 2026-10-01 23:03:** `cmp -s runs/ch08/plate.svg books/the-stoic-husband/design/plates/tipping-scale.svg` now exits 0.
