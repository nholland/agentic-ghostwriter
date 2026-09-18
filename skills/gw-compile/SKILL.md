---
description: Assemble a clean reader-facing manuscript or a single chapter's PDF - the package the author sends to readers for feedback. Uses the book repo's one renderer. Writes into runs/ while both pipelines are live.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-compile/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-compile — the package readers get

Argument: a chapter number, a range `N-M`, or nothing for everything refined.
`$ARGUMENTS`

This is how feedback happens: the author sends a PDF to readers. Nothing else in
the house matters to a reader.

## Step 0

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

`resolve_book.py` is blocking. The citation gate reports and does not stop the
compile (Rule 4, changed 2026-09-15): an unverified citation is unfinished work,
and the statuses ride along in `scripts/citations.py`. A structural failure there
still blocks.

## One renderer where one can run, and a check on what comes out

The book repo's `scripts/chapter_pdf.py` is the renderer. Use it wherever it runs:
its predecessor was two copies of one stylesheet that shipped the same two defects
and had only one fixed, and its `markup()` already carries three transforms, each
fixing a defect the author found in a shipped PDF.

Where it **cannot** run - this container has no weasyprint, pandoc or
wkhtmltopdf, and pip cannot reach PyPI - `scripts/chapter_pdf_local.py` drives the
headless Chromium already present. That is a registered gap (`GAPS.md`), not a
licence to diverge: **read `markup()` before changing either renderer.** Writing a
second one from scratch is how those three transforms were lost and re-found.

Then check what a reader actually receives:

```
python3 scripts/package_check.py "runs/chNN/pdf/<name>.html"   # quoted: the names have spaces
```

**It must exit 0.** It asserts the package opens on the chapter and not on
apparatus, that any distillation is at the back and labelled (the shipped
manuscript contains none - it is working apparatus feeding the practice guide),
and that no Draft Notes or Editor's Notes heading reached the page. It reads the
emitted HTML, so it cannot see overlapping glyphs or a plate that renders blank.
Those stay with `runs/design/svgcheck.py` and with the author's own eye.

## Assembly is a script, not a checklist

```
python3 scripts/compile.py --to 11       # precursors through chapter 11
python3 scripts/compile.py --from 1 --to 5
```

It reads the Parts and their opening pages out of `03-outline.md` rather than
being told, strips apparatus, appends each chapter's `**Practice:**` field, and
writes a coverage header. Before reporting success it asserts every crossed Part
opening is present, one Practice per in-range distillation, no apparatus, and
chapters in order.

**Do not assemble by hand.** The one time a model followed these rules as prose,
on 2026-09-15, it dropped both Part openings and nothing noticed: the only check
was a word-count delta, the pages are ~120 words, and there was no previous
compile to compare against. A delta cannot see a defect already in the baseline,
which is why the checks above are absolute.

## Which chapters, from which pipeline

While both pipelines are live a chapter may exist in both places. **Say which
you compiled from, per chapter.** Default to the book repo's `refined.md` (the
shipped one); include `runs/chNN/refined.md` only when asked, and label the
output so a reader-facing PDF never carries an unapproved shadow draft.

## Output

The PDF path, the word count and its delta from the previous compile, which
chapters came from which pipeline, and the gate result. Writes only under
`runs/`; migration switch 2 moves this to the book repo.
