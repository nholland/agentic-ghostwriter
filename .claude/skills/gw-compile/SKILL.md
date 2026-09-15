---
description: Assemble a clean reader-facing manuscript or a single chapter's PDF - the package the author sends to readers for feedback. Uses the book repo's one renderer. Writes into runs/ while both pipelines are live.
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

## One renderer, not two

The book repo has one PDF renderer, `scripts/chapter_pdf.py`, and it is the only
one because its predecessor was two copies of the same stylesheet that shipped
the same two defects and had only one fixed. **Do not write a second renderer
here.** It is declared as an optional dependency; `resolve_book.py` reports if it
is missing.

- Single chapter from this pipeline:
  `python3 {bookRepo}/scripts/chapter_pdf.py --markdown runs/chNN/refined.md runs/chNN/<Title>.pdf`
  (`--markdown` renders an explicit file to an explicit destination — it does
  not strip apparatus, so strip Editor's and Draft Notes first, exactly as
  `voice_check.py` does: prose ends at the first apparatus heading.)
- A range or the whole book: assemble the markdown per the rules below, write
  it to `runs/manuscript/manuscript.md`, then render the same way.

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
