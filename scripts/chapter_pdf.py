#!/usr/bin/env python3
"""Render a chapter, or any book markdown, to PDF.

This is the single renderer for the project. Styling, beat-label handling, and
quotation formatting live here and nowhere else, so a fix improves the chapter
PDFs and the compiled manuscript at the same time. `book-compile.md` used to
carry its own inline weasyprint script with a second copy of the stylesheet;
that copy was removed on 2026-08-17 after both copies shipped the same two
formatting defects and only one was fixed.

Usage:
    python3 scripts/chapter_pdf.py <bookRoot> <chapter>
    python3 scripts/chapter_pdf.py --markdown <source.md> <out.pdf>

    <chapter> may be a zero-padded number (01, 10), a bare number (1, 10),
    or a non-numeric chapter key (prologue, introduction).

    --markdown renders an arbitrary file to an explicit destination and does
    not strip apparatus, since a compiled manuscript has none to strip.

Reads {bookRoot}/chapters/ch<NN>/refined.md, falling back to draft.md when no
refined version exists yet. Writes the PDF beside it, named from the chapter's
own H1 heading: "# Chapter 9: Silence Is Not Peace" becomes
Chapter-9-Silence-Is-Not-Peace.pdf. That convention comes from the author's own
hand-made Ch9 PDF, which is the only one in the repo and is git-tracked; the
script matches it rather than introducing a second scheme. A retitled chapter
therefore produces a differently-named PDF, and the stale one should be deleted.

The PDF is deliberately reader-facing: Editor's Notes and Draft Notes are
stripped, while the chapter and its Distillation are kept. The Distillation's
Lesson, Challenge, and Practice items are what book-compile renders as the
chapter's closing section, so a PDF without them would not be the chapter as a
reader actually meets it. This format is meant to be shareable with outside
readers for feedback, which is why nothing internal survives into it.

`parking-lot.md` records that Chapter 9's largest structural failure survived
two text-based check-ins and was caught only when the author read it as a PDF,
and that Chapter 10's original failure was caught the same way. Text review and
reading review catch different classes of problem.

Styling matches book-compile.md's manuscript PDF so a chapter read in isolation
looks like the same book.
"""
import json
import os
import re
import sys


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


def ensure_toolchain():
    """Import markdown and weasyprint, installing them once if absent.

    Cloud containers are rebuilt per session, so a previous session's install is
    never there. Rather than failing with instructions a human has to act on,
    bootstrap it: the install is quick and this is the only dependency the
    renderer has.
    """
    try:
        import markdown
        import weasyprint
        return markdown, weasyprint
    except ImportError:
        pass

    import subprocess
    print("PDF toolchain missing, installing weasyprint and markdown...", file=sys.stderr)
    r = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--quiet", "weasyprint", "markdown"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(
            "could not install the PDF toolchain. Install it manually with:\n"
            "    pip install weasyprint markdown\n"
            f"pip said: {r.stderr.strip()[:400]}"
        )
    try:
        import markdown
        import weasyprint
        return markdown, weasyprint
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(f"toolchain installed but import still failed: {exc}")


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


def main() -> int:
    # --markdown renders an arbitrary file to an explicit destination. This is
    # how book-compile.md renders the manuscript, so the stylesheet, beat-label
    # handling, and quotation formatting live in exactly one place. That step
    # used to carry its own inline copy of all three.
    if len(sys.argv) == 4 and sys.argv[1] == "--markdown":
        source, out = sys.argv[2], sys.argv[3]
        if not os.path.exists(source):
            print(f"error: no such file: {source}", file=sys.stderr)
            return 1
        chapter_dir = None
    elif len(sys.argv) == 3:
        book_root, chapter = sys.argv[1], sys.argv[2]
        chapter_dir = resolve_chapter_dir(book_root, chapter)
        source = None
        for candidate in ("refined.md", "draft.md"):
            path = os.path.join(chapter_dir, candidate)
            if os.path.exists(path):
                source = path
                break
        if source is None:
            print(f"error: no refined.md or draft.md in {chapter_dir}", file=sys.stderr)
            return 1
        out = None
    else:
        print(__doc__)
        return 2

    try:
        markdown, weasyprint = ensure_toolchain()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    raw = open(source).read()
    md_text = markup(strip_apparatus(raw) if chapter_dir else raw)

    try:
        with open("book-manifest.json") as f:
            manifest = json.load(f)
        title = manifest["books"][manifest["bookRoot"]].get("title", "Manuscript")
    except Exception:
        title = "Manuscript"

    html_body = markdown.markdown(md_text, extensions=["extra", "smarty"])

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  @page {{ margin: 1in; }}
  body {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 12pt;
    line-height: 1.7;
    color: #000;
    orphans: 2;
    widows: 2;
  }}
  h1 {{
    page-break-before: always;
    font-size: 22pt;
    line-height: 1.25;
    margin: 0 0 1.4em 0;
    padding-bottom: 0.4em;
    border-bottom: 2px solid #000;
  }}
  h1:first-of-type {{ page-break-before: avoid; }}
  h2 {{
    font-size: 15pt;
    margin: 2.2em 0 0.8em 0;
    padding-top: 0.6em;
    border-top: 1px solid #999;
    page-break-after: avoid;
  }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 2em 0; }}
  blockquote {{
    margin: 1.6em 1.5em;
    padding-left: 1.1em;
    border-left: 3px solid #999;
    font-style: italic;
    page-break-inside: avoid;
  }}
  blockquote p {{ margin: 0; }}
  p {{ margin: 0.5em 0 1em 0; }}
  strong {{ font-weight: bold; }}
  em {{ font-style: italic; }}
  /* Beat labels are the chapter's section headers. They were bold body text at
     1.05em, which read as emphasis rather than structure. */
  p.beat-label {{
    font-family: Helvetica, Arial, sans-serif;
    font-weight: bold;
    font-size: 11pt;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    margin: 2.4em 0 0.7em 0;
    page-break-after: avoid;
  }}
  /* Distillation metadata: one labelled line each, not a run-on paragraph. */
  p.meta {{
    margin: 0 0 0.35em 0;
    page-break-inside: avoid;
  }}
  /* Mechanism/Conversation/Lesson/Challenge are one logical block; a page break
     between them split the Distillation across pages 7 and 8 of Ch10. */
  p.meta + p.meta {{ page-break-before: avoid; }}
  ol, ul {{ margin: 0.6em 0 1.2em 0; padding-left: 1.4em; }}
  li {{ margin-bottom: 0.55em; }}
  /* Part closing plates (book-compile Step 2.7): a full-page line drawing on
     a page of its own. The SVG is 6x9 proportioned and carries its own
     caption, so the page has nothing else on it. */
  div.plate {{
    page-break-before: always;
    text-align: center;
    margin: 0;
  }}
  /* Bounded by height, not width: a 6x9 image at full text width would run
     9.75in tall against a 9in content box and spill its bottom onto the next
     page. The following h1 (next Part's opening) already breaks before
     itself, so no page-break-after here; one would strand the separator rule
     on a blank page of its own. */
  div.plate img {{ max-height: 8.6in; max-width: 100%; width: auto; height: auto; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    if out is None:
        out = os.path.join(chapter_dir, pdf_name(md_text, chapter_dir))
    # pdf_tags is requested but does not currently produce a structure tree:
    # weasyprint 69.0 accepts both this and pdf_variant="pdf/ua-1" and emits an
    # untagged file either way (verified 2026-08-17). It costs nothing and will
    # start working if that support lands. The consequence today is that a
    # viewer which reflows text, a phone or an accessibility mode, has to infer
    # paragraph boundaries from line positions and can break mid-sentence. The
    # printed layout is unaffected.
    # base_url lets relative image paths in the markdown (the Part closing
    # plates, `parts/plate-N-<slug>.svg`) resolve from the source file's own
    # directory. Without it weasyprint has no base and drops the image silently.
    base_url = os.path.dirname(os.path.abspath(source))
    weasyprint.HTML(string=html, base_url=base_url).write_pdf(out, options={"pdf_tags": True})

    words = len(re.findall(r"[A-Za-z][A-Za-z'’-]*", md_text))
    print(f"wrote {out} — from {os.path.basename(source)}, ~{words} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
