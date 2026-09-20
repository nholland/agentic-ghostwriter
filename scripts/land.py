#!/usr/bin/env python3
"""
land.py - move a chapter from runs/chNN/ (apparatus) into books/<slug>/ (the book),
after the author's verdict. The production form of what was done by hand for
Chapter 12 on 2026-09-18, kept as a script because the hand version caught two
defects at exactly this step (nine citation links that would have broken on
arrival; the wrong research round) and a hand step is where the next one hides.

WHAT IT DOES, in order, and refuses at the first thing it cannot do
    1. Requires runs/chNN/verdict.md. No verdict, no landing (CLAUDE.md Rule 8).
    2. Requires refined.md and distillation.md in runs/chNN/.
    3. Refuses if any staged citation under runs/chNN/okf/ still carries a link
       written for the shadow tree (okf_gate.py's #029 check, scoped to NN).
    4. Refuses if {bookRoot}/chapters/chNN/refined.md already exists, unless
       --force. A landed chapter is not overwritten by accident.
    5. Copies: the prose above "## Editor's Notes" -> chapters/chNN/refined.md;
       distillation.md; research-round2.md if present else research.md ->
       research.md (says which); interview.md if present; plate.svg ->
       design/plates/<slug-of-its-aria-label>.svg; runs/chNN/okf/citations/*.md
       -> okf/citations/, refusing a name collision whose content differs.
    6. Appends this chapter's "## Chapter N — ..." section from
       runs/appendix/practice-guide.md to the book's appendix/practice-guide.md,
       once (Rule 15: the guide appends and never rewrites).
    7. Regenerates citation-queue.md with scripts/citation_queue.py.
    8. Runs practice_sync.py --book NN and okf_validate.py, and exits non-zero
       if either does.

It never invents. Anything it cannot find it names and stops. It does not commit:
the landing is its own commit, by the Publisher, naming the verdict.

USAGE
    python3 scripts/land.py 12
    python3 scripts/land.py 12 --dry-run      # say what would happen, write nothing
    python3 scripts/land.py 12 --force        # overwrite an already-landed chapter

EXIT
    0  landed (or dry run complete)
    1  refused, or a post-landing check failed - the message says which
    2  no book repo resolvable
"""
import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402
import okf_gate      # noqa: E402


def refuse(msg):
    print(f"land: REFUSED - {msg}")
    return 1


def prose_above_editors_notes(text):
    m = re.search(r"^## Editor's Notes", text, re.M)
    return (text[:m.start()] if m else text).rstrip() + "\n"


def plate_name(svg_text, n):
    m = re.search(r'aria-label="([^"]+)"', svg_text)
    label = m.group(1) if m else f"chapter-{n:02d}"
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    return f"{slug or f'chapter-{n:02d}'}.svg"


def guide_section(text, n):
    """The '## Chapter N — ...' section, header through the line before the
    next '## ' header (or EOF). None if absent."""
    m = re.search(rf"^## Chapter {n} — .*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    return (m.group(0) + body).rstrip() + "\n"


def same_file(a, b):
    try:
        return open(a, "rb").read() == open(b, "rb").read()
    except OSError:
        return False


def main():
    ap = argparse.ArgumentParser(description="Land a verdict-passed chapter into the book.")
    ap.add_argument("chapter", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite a chapter already landed in the book")
    a = ap.parse_args()
    n = a.chapter
    tag = f"ch{n:02d}"

    cfg = resolve_book.load_config()
    repo_root, _, _ = resolve_book.resolve(cfg)
    if not repo_root:
        print("land: no book repo resolvable - run scripts/resolve_book.py", file=sys.stderr)
        return 2
    rep = resolve_book.inspect(repo_root, require_okf=True)
    book_root = rep["info"].get("bookRoot")
    book_rel = rep["info"].get("bookRootRelative")
    if not book_root or rep["problems"]:
        return refuse("book repo has problems - run scripts/resolve_book.py")

    run = os.path.join(REPO, "runs", tag)
    if not os.path.isdir(run):
        return refuse(f"{os.path.relpath(run, REPO)} does not exist; nothing to land")
    for need in ("verdict.md", "refined.md", "distillation.md"):
        if not os.path.isfile(os.path.join(run, need)):
            why = ("the author has not given the verdict (Rule 8: nothing lands without it)"
                   if need == "verdict.md" else "the chapter is not finished")
            return refuse(f"runs/{tag}/{need} is missing - {why}")

    # 3. Staged links that would break on arrival (#029), this chapter only.
    broken = [(f, l) for f, l in okf_gate.staged_link_defects(REPO)
              if f.startswith(os.path.join("runs", tag) + os.sep)]
    if broken:
        for f, l in broken:
            print(f"  {f}: {l}")
        return refuse(f"{len(broken)} staged citation link(s) still carry the shadow-tree "
                      "prefix; repoint ](/okf/... to ](/... first")

    dest = os.path.join(book_root, "chapters", tag)
    if os.path.isfile(os.path.join(dest, "refined.md")) and not a.force:
        return refuse(f"{book_rel}/chapters/{tag}/refined.md already exists; "
                      "a landed chapter is not overwritten by accident (--force to re-land)")

    # Plan every write before doing any, so a refusal leaves nothing half-landed.
    writes = []   # (description, fn)
    refined = prose_above_editors_notes(open(os.path.join(run, "refined.md"), encoding="utf-8").read())
    words = len(refined.split())
    writes.append((f"chapters/{tag}/refined.md  ({words} words, prose above Editor's Notes)",
                   lambda: open(os.path.join(dest, "refined.md"), "w", encoding="utf-8").write(refined)))
    writes.append((f"chapters/{tag}/distillation.md",
                   lambda: shutil.copy(os.path.join(run, "distillation.md"), os.path.join(dest, "distillation.md"))))
    r2 = os.path.join(run, "research-round2.md")
    r1 = os.path.join(run, "research.md")
    src_research = r2 if os.path.isfile(r2) else (r1 if os.path.isfile(r1) else None)
    if src_research:
        writes.append((f"chapters/{tag}/research.md  (from {os.path.basename(src_research)})",
                       lambda s=src_research: shutil.copy(s, os.path.join(dest, "research.md"))))
    else:
        print(f"  note: no research brief in runs/{tag}/; none landed")
    iv = os.path.join(run, "interview.md")
    if os.path.isfile(iv):
        writes.append((f"chapters/{tag}/interview.md",
                       lambda: shutil.copy(iv, os.path.join(dest, "interview.md"))))
    else:
        print(f"  note: no interview.md in runs/{tag}/; none landed")

    plate = os.path.join(run, "plate.svg")
    if os.path.isfile(plate):
        # Inbox #062: the Ch12 plate landed with a gloss off the artboard past
        # every gate because nothing checked it at the moment it became
        # permanent. A FAIL row stops the land; --force overrides it.
        import plate_check
        fails = [(name, det) for st, name, det in plate_check.rows(plate, chapter=n) if st == "FAIL"]
        if fails and not a.force:
            return refuse("plate_check.py fails on runs/%s/plate.svg (--force to land anyway): "
                          % tag + "; ".join("%s: %s" % f for f in fails))
        pname = plate_name(open(plate, encoding="utf-8").read(), n)
        pdest = os.path.join(book_root, "design", "plates", pname)
        if os.path.isfile(pdest) and not same_file(plate, pdest) and not a.force:
            return refuse(f"design/plates/{pname} exists with different content (--force to replace)")
        if not (os.path.isfile(pdest) and same_file(plate, pdest)):
            writes.append((f"design/plates/{pname}",
                           lambda p=pdest: (os.makedirs(os.path.dirname(p), exist_ok=True),
                                            shutil.copy(plate, p))))
    else:
        print(f"  note: no plate.svg in runs/{tag}/; none landed")

    cites = sorted(glob.glob(os.path.join(run, "okf", "citations", "*.md")))
    cdest_dir = os.path.join(book_root, "okf", "citations")
    new_cites = 0
    for c in cites:
        cdest = os.path.join(cdest_dir, os.path.basename(c))
        if os.path.isfile(cdest):
            if same_file(c, cdest):
                continue
            if not a.force:
                return refuse(f"okf/citations/{os.path.basename(c)} exists with different "
                              "content (--force to replace)")
        new_cites += 1
        writes.append((f"okf/citations/{os.path.basename(c)}",
                       lambda c=c, d=cdest: shutil.copy(c, d)))

    guide_src = os.path.join(REPO, "runs", "appendix", "practice-guide.md")
    guide_dst = os.path.join(book_root, "appendix", "practice-guide.md")
    section = guide_section(open(guide_src, encoding="utf-8").read(), n) if os.path.isfile(guide_src) else None
    if section is None:
        print(f"  note: no '## Chapter {n} — ...' section in runs/appendix/practice-guide.md; "
              "the practice guide is not appended (the Line Editor writes that section)")
    elif os.path.isfile(guide_dst) and section.splitlines()[0] in open(guide_dst, encoding="utf-8").read():
        print(f"  note: appendix/practice-guide.md already has the Chapter {n} section; not appended twice")
    else:
        writes.append((f"appendix/practice-guide.md  (+ Chapter {n} section, appended)",
                       lambda: open(guide_dst, "a", encoding="utf-8").write("\n" + section)))

    print(f"land: {tag} -> {book_rel}/  ({'DRY RUN' if a.dry_run else 'writing'})")
    for desc, _ in writes:
        print(f"  + {desc}")
    if a.dry_run:
        print(f"land: dry run, nothing written ({len(writes)} write(s) planned, {new_cites} new citation(s))")
        return 0

    os.makedirs(dest, exist_ok=True)
    for _, fn in writes:
        fn()

    # 7. The generated queue, never hand-kept.
    q = subprocess.run([sys.executable, os.path.join(HERE, "citation_queue.py"), book_rel],
                       cwd=repo_root, capture_output=True, text=True)
    print("  " + (q.stdout.strip() or q.stderr.strip()))

    # 8. The checks, independent of what this script believes it did.
    bad = 0
    ps = subprocess.run([sys.executable, os.path.join(HERE, "practice_sync.py"), str(n), "--book"],
                        cwd=REPO, capture_output=True, text=True)
    print("  practice_sync --book: " + (ps.stdout.strip().splitlines()[-1] if ps.stdout.strip() else ps.stderr.strip()[:120]))
    bad += ps.returncode != 0
    ov = subprocess.run([sys.executable, os.path.join(HERE, "okf_validate.py"), book_rel],
                        cwd=repo_root, capture_output=True, text=True)
    print("  okf_validate: " + (ov.stdout.strip().splitlines()[-1] if ov.stdout.strip() else ov.stderr.strip()[:120]))
    bad += ov.returncode != 0

    if bad:
        print("land: landed, but a check FAILED - fix before committing")
        return 1
    print(f"land: {tag} landed. Commit it as its own commit, naming the verdict.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
