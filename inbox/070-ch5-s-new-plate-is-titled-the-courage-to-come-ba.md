---
id: 070
status: open
raised_by: gw-designer
chapter: 5
opened: 2026-09-20 22:01
---

# Ch5's new plate is titled 'The courage to come back' (the chapter's own beat heading, verbatim). The distillation's Mechanism line is still 'The Remaining Nails' - Ch04's image, absent from the new concept. Retitle the distillation's Mechanism to match, or keep it and retitle the plate?

Flagged independently by the Designer and the Reader Panel. The plate's carrier (the same man's height, walking in and out twice, the unsaid thing as an empty vs filled box) draws 'becomes small without deciding to' - the chapter's own Conversation sentence - and passed the Panel's cold standalone read. Nothing about the nail survives in this concept; the mismatch is title-only.

**Recommendation:** Retitle the distillation's Mechanism to 'The courage to come back' (or similar chapter language) - the plate is right, the label is stale from an earlier draft of the chapter.

**Checked:**

```
python3 scripts/plate_check.py runs/ch05/plate.svg --chapter 5 -> [WARN] title '...differs...'; all other 10 rows ok. Panel cold sentence: 'If you go quiet in a fight you walk out smaller than you walked in; if you say the real thing, you walk out the same size you came in.' PASS.
```

**What unblocks this:** Whether chapters/ch05/distillation.md's Mechanism line changes, and what design/plates/ the-courage-to-come-back.svg is titled when it lands.
