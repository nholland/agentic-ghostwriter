# Voice spec revision — run-in section headers are structure

**Raised by:** inbox #001 (gw-lineeditor, 2026-09-12)
**Ruled by the author:** 2026-09-14 — "legalize them"
**Target file:** `{bookRoot}/01-voice.md` — the BOOK repo. This engine never
writes there (CLAUDE.md Rule 8). Apply this by hand, or through the book
pipeline's own revise path.

---

## Why

`voice_check.py` failed four artifacts (ch01, ch03, ch07, ch08) on the bold cap.
Every flagged span turned out to be the same device the spec never contemplated:
a short bolded section label. Not one instance of genuine bold-as-crutch — a
bolded sentence doing a sentence's job — exists in any of the thirteen refined
artifacts.

The convention appears in all eleven numbered chapters, in two typeset forms:

```
own-line            **The Gap**
                    (paragraph follows below)

paragraph-leading   **The fix.** The internet goes down on a Tuesday night...
```

The check only ever excused the first form. That was the check's defect, not the
chapters': nine chapters passed on the own-line form while four failed on the
same-line form of the identical device. The engine half is fixed in
`scripts/voice_check.py` as of 2026-09-14; this is the spec half, so the two
cannot drift.

## Change 1 — line 45, the Never Do bullet

Append to the end of the existing bullet, after "...earned, not routine.":

> Bolded **run-in section headers** are structure, not emphasis, and fall
> outside this cap: a short label — eight words at most, closing with a period
> or a colon — that opens a section, whether set on its own line (`**The Gap**`)
> or leading its own paragraph (`**The fix.** The internet goes down on a
> Tuesday night...`). The cap of one still governs every other bolded span,
> including a bolded sentence used as emphasis mid-paragraph.

## Change 2 — line 107, the counted-rules sentence

```
-   the bold cap (at most one per piece)
+   the bold cap (at most one per piece, run-in section headers excluded)
```

## What did NOT change

The cap itself is still one. The rule's target is unchanged: bold standing in
for sentence construction. Verified against a negative fixture — a long bolded
pull-quote, a mid-sentence bolded span, and a bolded opener with no terminal
punctuation all still count, and still fail the cap at three.
