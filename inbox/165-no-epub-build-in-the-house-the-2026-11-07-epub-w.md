---
id: 165
status: open
kind: gap
trigger: the next time the author asks for an ebook, or before any store submission
raised_by: publisher
chapter: -
opened: 2026-11-07 14:31
---

# No EPUB build in the house: the 2026-11-07 EPUB was built ad hoc with pandoc from output/compiled/assets/book.html (headings fixed by a scratch script), and not validated with EPUBCheck

Author asked for an ePub on 2026-11-07. Pandoc 3.1.3 is installed; the build demoted practice-page headings and flattened wrapper divs so the contents list is complete; plates went in as the compiled PNGs with alt text. EPUBCheck could not be downloaded in this session. Nothing in compile_current.py produces an EPUB, so the next one would be ad hoc again.
