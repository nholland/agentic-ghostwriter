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

Both blocking. The citation gate runs **before** anything is assembled: a
manuscript is the one artifact that leaves the building, and the old pipeline's
compile runs the same gate for the same reason.

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

## Assembly rules, carried from the old pipeline

- Prologue, then Introduction, then Part opening pages before each Part's first
  chapter — only the ones the range actually crosses.
- Each chapter's prose, apparatus stripped, followed by its "Putting It Into
  Practice" section from `distillation.md`. That section comes from the
  `**Practice:**` field, **not** a `## Practice` heading — the first version of
  the old compile looked for the heading and silently dropped all ten sections,
  1,700 words, caught only by the word count.
- **Compare the word count against the previous compile and investigate any
  unexplained drop.** A compile that loses a section does not error; it produces
  a shorter book. The count is the only signal.

## Which chapters, from which pipeline

While both pipelines are live a chapter may exist in both places. **Say which
you compiled from, per chapter.** Default to the book repo's `refined.md` (the
shipped one); include `runs/chNN/refined.md` only when asked, and label the
output so a reader-facing PDF never carries an unapproved shadow draft.

## Output

The PDF path, the word count and its delta from the previous compile, which
chapters came from which pipeline, and the gate result. Writes only under
`runs/`; migration switch 2 moves this to the book repo.
