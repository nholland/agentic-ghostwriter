#!/usr/bin/env python3
"""Compatibility entry point for the single approved Chromium PDF format.

Usage: chapter_pdf.py BOOK_ROOT CHAPTER | --markdown SOURCE OUTPUT
Rendering and typography live in chapter_pdf_local.py and pdf_chapter_style.py.
"""
import os
import re
import sys
from pathlib import Path

def resolve_chapter_dir(book_root: str, chapter: str) -> str:
    """Accept 1, 01, ch01, or prologue; return the chapters/ subdirectory."""
    key = chapter.lower().removeprefix("ch")
    if key.isdigit():
        key = key.zfill(2)
        name = f"ch{key}"
    else:
        name = key
    return os.path.join(book_root, "chapters", name)


NOTES_HEADINGS = ("Editor's Notes", "Editor’s Notes", "Draft Notes")


def strip_apparatus(md: str) -> str:
    """Drop the editorial notes sections, keep the chapter and its Distillation.

    The Distillation is reader-facing: its Lesson, Challenge, and Practice items
    are what book-compile renders as the chapter's closing section, so a shared
    PDF that omitted them would not be the chapter as a reader meets it. The
    notes are internal and never ship.

    Notes sections can sit before or after the Distillation, so this excises
    each notes block by range (heading to the next top-level heading) rather
    than truncating at the first marker.
    """
    for heading in NOTES_HEADINGS:
        while True:
            m = re.search(rf"^##\s+{re.escape(heading)}\s*$", md, flags=re.MULTILINE)
            if not m:
                break
            nxt = re.search(r"^##\s+", md[m.end():], flags=re.MULTILINE)
            end = m.end() + nxt.start() if nxt else len(md)
            # Take the --- divider that introduced the block with it.
            start = m.start()
            lead = re.search(r"\n+---\s*\n+$", md[:start])
            if lead:
                start = lead.start()
            md = md[:start] + "\n\n" + md[end:]

    md = re.sub(r"\n{3,}", "\n\n", md)
    return re.sub(r"\n+---\s*$", "\n", md.rstrip()) + "\n"


def markup(md: str) -> str:
    """Prepare markdown for rendering: label beats, break metadata, quote passages.

    Three transforms, each fixing a defect the author found in a shipped PDF:

    1. A bold-only line is a beat label. Markdown would render it as an inline
       <strong> inside an ordinary paragraph, which is why beat labels read as
       body text on the page rather than as section headers.
    2. Consecutive `**Label:** value` lines (the Distillation's Mechanism,
       Conversation, Lesson, Challenge) are separate lines in the source but one
       paragraph to Markdown, so they ran together on the page. Each becomes its
       own block.
    3. A paragraph that is entirely an italicised quotation is a pulled Stoic
       passage; render it as a blockquote so it is set off the way a quotation
       should be, instead of as an italic run inside the prose.

    Transforms 1 and 2 emit raw block HTML, and Markdown does not process
    inline markup inside raw block HTML. Without `markdown="span"` (handled by
    the `md_in_html` extension that `extra` bundles), a Stoic term italicised
    inside a Distillation line shipped with its asterisks visible: the Ch1
    manuscript read "*Prohairesis*, the faculty of choice" on the page. Added
    2026-08-23 after the defect reached a compiled manuscript PDF.
    """
    # 2 first: these lines are bold-prefixed but not bold-only, so they cannot
    # collide with the beat-label rule below.
    md = re.sub(
        r"^\*\*([^*]+?):\*\*[ \t]*(.*)$",
        lambda m: f'<p class="meta" markdown="span"><strong>{m.group(1)}:</strong> {m.group(2)}</p>',
        md,
        flags=re.MULTILINE,
    )
    # 1
    md = re.sub(
        r"^\*\*(.+?)\*\*[ \t]*$",
        lambda m: f'<p class="beat-label" markdown="span">{m.group(1)}</p>',
        md,
        flags=re.MULTILINE,
    )
    # 3
    md = re.sub(
        r'(?m)^\*"(.+?)"\*[ \t]*$',
        lambda m: f'<blockquote><p>“{m.group(1)}”</p></blockquote>',
        re.sub(r'\*"(.+?)"\*', lambda m: '*"' + " ".join(m.group(1).split()) + '"*', md, flags=re.S),
    )
    return md


def pdf_name(md: str, chapter_dir: str) -> str:
    """Derive the PDF filename from the chapter's H1, per the Ch9 convention."""
    m = re.search(r"^#\s+(.+?)\s*$", md, flags=re.MULTILINE)
    if not m:
        return os.path.basename(chapter_dir) + ".pdf"
    heading = m.group(1).replace(":", "")
    slug = re.sub(r"[^A-Za-z0-9 ]", "", heading)
    return "-".join(slug.split()) + ".pdf"



def main():
    import chapter_pdf_local as renderer
    if len(sys.argv) == 4 and sys.argv[1] == '--markdown':
        source, out = map(Path, sys.argv[2:])
        renderer.build(source.read_text(), None, [], str(out), source.stem,
                       base_dir=str(source.resolve().parent))
    elif len(sys.argv) == 3:
        from compile_current import chapter
        chapter(Path(sys.argv[1]).resolve(), int(sys.argv[2].removeprefix('ch')))
    else:
        print(__doc__)
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
