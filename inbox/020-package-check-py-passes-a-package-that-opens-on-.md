---
id: 020
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 04:59
---

# package_check.py passes a package that opens on the distillation, so long as the class says distback. Assert position instead of class name?

The check I wrote yesterday tests the class string and never the index. A section classed 'dist distback' placed FIRST passes clean, and the check prints the fault inside its own pass line: 'opens on: dist distback'. Second escape: any extra attribute on the tag, like an id, makes the section invisible to its regex, and it then reports 'opens on: chapter' for a package that opens on the distillation. So the only check in this house that reads a reader-facing artifact cannot see the defect it was written for. The Archivist drafted and proved a 92-word patch: parse every section tag, fail loudly on any it cannot parse, and assert that a distillation section is last by index.

**Recommendation:** Apply the drafted patch. distback is a label; only the index proves it is at the back.

**Checked:**

```
printf a distback-classed section first | package_check.py -> [ ok ] opens on: dist distback, exit 0. Publisher reproduced both escapes independently.
```

**What unblocks this:** Whether the render gate can see the fault that created it.
