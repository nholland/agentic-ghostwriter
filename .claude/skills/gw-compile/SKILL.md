---
name: gw-compile
description: Assemble a clean reader-facing manuscript or a single chapter's PDF - the package the author sends to readers for feedback. Uses the book's one renderer. Writes into runs/, with the coverage in the filename.
---

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

The book's `scripts/chapter_pdf.py` is the renderer. Use it wherever it runs:
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
Render and inspect every page before delivery. Also extract the PDF text: the
chapter label must read `Chapter N`, never spaced letters, followed by the title
and opening in reading order. Both backends share `pdf_chapter_style.py`: bold,
separate chapter title; ordinary untracked chapter label; flush-left opening
paragraph. This book's reading PDFs feed an audiobook reader, so visual checks
alone are insufficient. No running headers or decorative extractable labels.
For a single chapter, run `tests/check_pdf_opening.py PDF --chapter N --title
"Title"` with Python containing pdfplumber and pypdf; it checks the actual PDF.

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

## Which text

Compile from `{bookRoot}/chapters/chNN/refined.md` - the landed, verdict-passed
text. A chapter still in `runs/chNN/` has no verdict yet; include it only when
asked, and label the output so a reader-facing PDF never carries an unapproved
draft.

## Output

The PDF path, the word count and its delta from the previous compile, and the
gate result. Writes only under `runs/`, coverage in the filename (Rule 15).
`{bookRoot}/manuscript.md` and `manuscript.pdf` are the old pipeline's last
compile and are not refreshed by this command - see `GAPS.md`.
