---
id: 015
status: open
raised_by: gw-designer
chapter: 0
opened: 2026-09-15 18:06
---

# Your book has two visual languages and no style file. Which one is the standard?

Verified: design/plates/ holds 9 SVGs in Georgia serif, stroke-only, currentColor, no background, matching design/marks/ and therefore the cover furniture. visuals/ holds 1 SVG (ch01-distillation.svg) in system sans-serif, amber #b45309 against slate #6b7280, filled boxes, white background. They draw the same Chapter 1 mechanism twice - ch01-distillation.svg and design/plates/three-second-window.svg - which reads as the Georgia language having superseded the sans one, but nothing says so. No style file exists in either directory. The Ch12 plate was drawn in the Georgia language for three reasons: nine files against one, it matches the marks and the cover, and the sans version's amber/slate distinction collapses in greyscale - its two box fills #fffbeb and #f9fafb are effectively the same grey in print, so it fails a print constraint. If visuals/ is meant to be the standard, the Ch12 plate is in the wrong language and should be redrawn. The Designer also proposed a visuals/style.md capturing the Georgia conventions - canvas, ink, type scale, stroke weights, margins, composition - and did not write it, because a style file is a constitution artifact and belongs to you. It is in the desk's return if you want it.

**Recommendation:** Ratify design/plates/ as the standard and retire visuals/ch01-distillation.svg to an archive. Nine files against one, it survives greyscale, and it matches the cover. Then have the style file written so chapter thirteen's plate does not re-open this.

**Checked:**

```
gw-designer, 2026-09-15. Publisher verified: design/plates/ 9 files, visuals/ 1 file; the Ch12 plate uses only #1a1a1a and #ffffff, so no hue carries meaning.
```

**What unblocks this:** Which visual language new plates are drawn in, and whether a style file gets written so this is not re-decided every chapter.
