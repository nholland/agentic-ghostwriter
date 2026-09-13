#!/usr/bin/env python3
"""
okf_new.py - create a typed OKF concept the only way a desk is allowed to.

WHY A SCRIPT
    Every wrong date in the book's record was typed by hand; every date taken
    from the clock inside a script was right. Sixteen concepts were once stamped
    one to four days early in a single session, and okf_validate.py could not
    see it because a date in the past looks ordinary. So desks do not type
    frontmatter. They call this, and this reads the clock.

    It also holds the line the whole citation subsystem depends on:
      - it will NEVER write `status: verified` (only the author sets that, against
        his physical copy - see the book's CLAUDE.md Rule 11);
      - it refuses a `quote_form: verbatim` citation at `verifiable` unless the
        evidence_source says a page was actually opened (the transcription rule);
      - it checks every chapter_slugs entry against 03-outline.md, so a slug
        cannot be invented.

    After writing it runs the book repo's own okf_validate.py --strict and
    deletes the new file if the validator rejects it. A concept that would break
    the gate is never left on disk.

WHERE IT WRITES
    Into {bookRoot}/okf/<type-dir>/<slug>.md - the book's shared knowledge
    ledger (layer L5). This is the ONE place the engine writes inside the book
    repo besides Foundation for a book it owns: the ledger is shared by both
    pipelines by design, and both write it through the same validator.
    The constitution (L4) and chapters/ (L6) stay untouchable.

USAGE
    python3 scripts/okf_new.py --type Citation --title "Seneca, Letter 91" \
        --description "..." --provenance "gw-researcher, ch12 brief" \
        --chapter-slugs romance-is-a-discipline --tags romance,askesis \
        --status unverified --quote-form paraphrase --evidence-source none \
        --gap-type research --verification-note "find the primary passage" \
        --by gw-researcher --body "What needs to be found..."

    python3 scripts/okf_new.py --type Story --title "..." ... --dry-run

    --dry-run prints the file and writes nothing (use it to PROPOSE a content
    concept to the author before writing - Rule 9 in CLAUDE.md).

EXIT CODES
    0 written (or dry-run printed)   1 refused (says why)   2 no book / usage
"""

import argparse
import datetime
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

TYPE_DIRS = {
    "Framework": "frameworks",
    "Story": "stories",
    "Citation": "citations",
    "Reader Signal": "signals",
    "QA Finding": "findings",
    "Author Note": "notes",
}
IP_VALUES = {"author", "author-synthesis", "audience-signal", "external"}
STATUS_VALUES = {"unverified", "verifiable", "superseded"}  # never `verified` from here
QUOTE_FORM_VALUES = {"verbatim", "paraphrase", "none"}
EVIDENCE_VALUES = {"author-copy", "page-image", "page-text",
                   "database-abstract", "search-synthesis", "none"}
UNTRANSCRIBED = {"search-synthesis", "database-abstract", "none"}
GAP_TYPES = {"research", "structural"}
DISCLOSURE = {"composite", "identified", "private"}
SIGNAL_CATS = {"resonance", "confusion", "objection", "gift", "extension", "noise"}
GIFT_TYPES = {"supporting", "complicating", "contradicting"}
AUDITS = {"human", "argue", "beta", "tension", "sweep", "panel", "slopreader"}
SEVERITY = {"minor", "significant", "devastating"}


def now():
    """Read the clock. Never a plausible time."""
    try:
        out = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True,
                             text=True, check=True).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return re.sub(r"-+", "-", s)


def valid_chapter_slugs(book_root):
    """Same rule as the book repo's okf_validate.py: chapter headings in
    03-outline.md, plus the fixed tokens."""
    path = os.path.join(book_root, "03-outline.md")
    slugs = {"introduction", "conclusion", "prologue", "all"}
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return None
    for m in re.finditer(r"^## Chapter \d+: (.+)$", text, re.MULTILINE):
        slugs.add(slugify(m.group(1)))
    return slugs


def yaml_str(v):
    """Quote when YAML would otherwise misread the value."""
    if v is None:
        return '""'
    s = str(v)
    if s == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`,]", s) or s.strip() != s \
            or s.lower() in {"yes", "no", "true", "false", "null", "~"}:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def yaml_list(items):
    return "[" + ", ".join(yaml_str(i) for i in items) + "]"


def split_csv(s):
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def build(a, book_root):
    problems = []
    t = a.type
    if t not in TYPE_DIRS:
        problems.append(f"--type must be one of {sorted(TYPE_DIRS)}")
        return None, problems
    if not a.title.strip():
        problems.append("--title is required")
    if a.ip and a.ip not in IP_VALUES:
        problems.append(f"--ip must be one of {sorted(IP_VALUES)}")

    tags = split_csv(a.tags)
    for tag in tags:
        if re.fullmatch(r"ch\d{1,2}", tag.lower()):
            problems.append(f"tag {tag!r} is a chapter number. Chapters go in "
                            f"--chapter-slugs by slug, never by number (Rule 6).")

    slugs = split_csv(a.chapter_slugs)
    valid = valid_chapter_slugs(book_root)
    if valid is not None:
        for s in slugs:
            if s not in valid:
                problems.append(f"chapter slug {s!r} does not match any heading in "
                                f"03-outline.md. Slugs are identity; do not invent one.")
    elif slugs:
        problems.append("cannot check chapter_slugs: 03-outline.md unreadable")

    fm = [("type", t), ("title", a.title.strip()), ("description", a.description or "")]
    fm.append(("provenance", a.provenance or f"created by {a.by or 'a desk'} via okf_new.py"))
    fm.append(("ip", a.ip or ("external" if t == "Citation" else "author")))
    fm.append(("tags", tags))
    fm.append(("chapter_slugs", slugs))

    if t == "Citation":
        st, qf, ev = a.status or "unverified", a.quote_form or "none", a.evidence_source or "none"
        if a.status == "verified":
            problems.append("REFUSED: `status: verified` is the author's alone, set against "
                            "his physical copy. This script never writes it.")
        elif st not in STATUS_VALUES:
            problems.append(f"--status must be one of {sorted(STATUS_VALUES)}")
        if qf not in QUOTE_FORM_VALUES:
            problems.append(f"--quote-form must be one of {sorted(QUOTE_FORM_VALUES)}")
        if ev not in EVIDENCE_VALUES:
            problems.append(f"--evidence-source must be one of {sorted(EVIDENCE_VALUES)}")
        if qf == "verbatim" and st == "verifiable" and ev in UNTRANSCRIBED:
            problems.append("REFUSED by the transcription rule: a verbatim quotation may not be "
                            "`verifiable` on search-synthesis, database-abstract or no evidence. "
                            "Search may locate a source or flag a defect; it may never transcribe.")
        if st == "verifiable" and not (a.resource or "").strip():
            problems.append("a `verifiable` citation needs --resource (what was looked at)")
        if a.gap_type and a.gap_type not in GAP_TYPES:
            problems.append(f"--gap-type must be one of {sorted(GAP_TYPES)}")
        fm += [("resource", a.resource or ""), ("status", st), ("quote_form", qf),
               ("evidence_source", ev), ("verification_note", a.verification_note or "")]
        if a.gap_type:
            fm.append(("gap_type", a.gap_type))
    elif t == "Story":
        d = a.disclosure or "composite"
        if d not in DISCLOSURE:
            problems.append(f"--disclosure must be one of {sorted(DISCLOSURE)}")
        fm.append(("disclosure", d))
    elif t == "Reader Signal":
        if a.signal_category and a.signal_category not in SIGNAL_CATS:
            problems.append(f"--signal-category must be one of {sorted(SIGNAL_CATS)}")
        if a.gift_type and a.gift_type not in GIFT_TYPES:
            problems.append(f"--gift-type must be one of {sorted(GIFT_TYPES)}")
        fm += [("platform", a.platform or ""), ("signal_category", a.signal_category or "")]
        if a.gift_type:
            fm.append(("gift_type", a.gift_type))
        if a.resolves:
            fm.append(("resolves", a.resolves))
    elif t == "QA Finding":
        if a.audit and a.audit not in AUDITS:
            problems.append(f"--audit must be one of {sorted(AUDITS)}")
        if a.severity and a.severity not in SEVERITY:
            problems.append(f"--severity must be one of {sorted(SEVERITY)}")
        fm += [("audit", a.audit or ""), ("severity", a.severity or ""),
               ("status", "open"), ("chapter", a.chapter or "")]
    elif t == "Author Note":
        fm.append(("topic", a.topic or ""))

    stamp = now()
    fm.append(("timestamp", stamp))

    lines = ["---"]
    for k, v in fm:
        lines.append(f"{k}: {yaml_list(v) if isinstance(v, list) else yaml_str(v)}")
    lines.append("---")
    body = a.body or ""
    if a.body_file:
        body = open(a.body_file, encoding="utf-8").read()
    text = "\n".join(lines) + f"\n\n# {a.title.strip()}\n\n{body.strip()}\n"
    return {"text": text, "stamp": stamp, "type": t}, problems


def append_index(book_root, t, slug, title, description):
    """Add one line to the matching section of okf/index.md so index parity
    holds. The section heading is found by the type's plural; if the heading
    is not found the caller is told, never silently skipped."""
    path = os.path.join(book_root, "okf", "index.md")
    if not os.path.isfile(path):
        return "okf/index.md not found - the bundle has no index to update"
    heading = {"frameworks": "Frameworks", "stories": "Stories", "citations": "Citations",
               "signals": "Signals", "findings": "Findings", "notes": "Notes"}[TYPE_DIRS[t]]
    text = open(path, encoding="utf-8").read()
    m = re.search(rf"^## {heading}\b.*$", text, re.MULTILINE)
    if not m:
        return f"okf/index.md has no `## {heading}` section - add the entry by hand"
    nxt = re.search(r"^## ", text[m.end():], re.MULTILINE)
    end = m.end() + (nxt.start() if nxt else len(text[m.end():]))
    section = text[m.end():end]
    entry = f"- [{title}](/{TYPE_DIRS[t]}/{slug}.md) — {description or title}\n"
    # Replace a "None yet" placeholder paragraph if that is all the section holds.
    stripped = re.sub(r"^None yet\..*?(?=\n\n|\Z)", "", section.strip(), flags=re.DOTALL | re.MULTILINE).strip()
    new_section = "\n\n" + (stripped + "\n" if stripped else "") + entry + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text[:m.end()] + new_section + text[end:])
    return None


def main():
    ap = argparse.ArgumentParser(description="Create a typed OKF concept, clock-stamped and validated.")
    ap.add_argument("--type", required=True, help="Framework | Story | Citation | 'Reader Signal' | 'QA Finding' | 'Author Note'")
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug", help="filename slug; derived from the title when omitted")
    ap.add_argument("--description", default="")
    ap.add_argument("--provenance", default="")
    ap.add_argument("--ip", default="")
    ap.add_argument("--tags", default="", help="comma-separated topical tags (no chapter numbers)")
    ap.add_argument("--chapter-slugs", default="", help="comma-separated chapter slugs from 03-outline.md")
    ap.add_argument("--by", default="", help="the desk creating this, for okf/log.md")
    ap.add_argument("--body", default="")
    ap.add_argument("--body-file")
    # Citation
    ap.add_argument("--status"); ap.add_argument("--quote-form"); ap.add_argument("--evidence-source")
    ap.add_argument("--resource"); ap.add_argument("--verification-note"); ap.add_argument("--gap-type")
    # Story
    ap.add_argument("--disclosure")
    # Reader Signal
    ap.add_argument("--platform"); ap.add_argument("--signal-category"); ap.add_argument("--gift-type"); ap.add_argument("--resolves")
    # QA Finding
    ap.add_argument("--audit"); ap.add_argument("--severity"); ap.add_argument("--chapter")
    # Author Note
    ap.add_argument("--topic")
    ap.add_argument("--dry-run", action="store_true", help="print the concept; write nothing")
    ap.add_argument("--no-validate", action="store_true", help="skip the post-write validator run (tests only)")
    a = ap.parse_args()

    cfg = resolve_book.load_config()
    repo_root, _, _ = resolve_book.resolve(cfg)
    if not repo_root:
        print("okf_new: no book repo resolvable - run scripts/resolve_book.py", file=sys.stderr)
        return 2
    rep = resolve_book.inspect(repo_root, require_okf=True)
    if rep["problems"]:
        print("okf_new: book repo has problems - run scripts/resolve_book.py", file=sys.stderr)
        for p in rep["problems"]:
            print("  - " + p, file=sys.stderr)
        return 2
    book_root = rep["info"]["bookRoot"]

    built, problems = build(a, book_root)
    if problems:
        print("okf_new: REFUSED - nothing written")
        for p in problems:
            print("  - " + p)
        return 1

    slug = a.slug or slugify(a.title)
    rel = os.path.join("okf", TYPE_DIRS[a.type], f"{slug}.md")
    path = os.path.join(book_root, rel)

    if a.dry_run:
        print(f"okf_new: DRY RUN - would write {rep['info']['bookRootRelative']}/{rel}\n")
        print(built["text"])
        return 0

    if os.path.exists(path):
        print(f"okf_new: REFUSED - {rel} already exists. Edit it; do not overwrite a concept's history.")
        return 1

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(built["text"])

    if not a.no_validate:
        validator = rep["info"].get("okf_validate")
        if not validator:
            os.remove(path)
            print("okf_new: REFUSED - the book repo has no scripts/okf_validate.py; "
                  "a concept cannot be written where the gate cannot check it.")
            return 1
        proc = subprocess.run([sys.executable, validator, rep["info"]["bookRootRelative"], "--strict"],
                              cwd=repo_root, capture_output=True, text=True)
        out = (proc.stdout or "") + (proc.stderr or "")
        mine = [ln for ln in out.splitlines() if f"{slug}.md" in ln and not ln.strip().startswith("!")]
        if proc.returncode != 0 and mine:
            os.remove(path)
            print("okf_new: REFUSED - the validator rejected the new concept, so it was removed:")
            for ln in mine:
                print("  " + ln.strip())
            return 1

    idx_note = append_index(book_root, a.type, slug, a.title.strip(), a.description)
    log = os.path.join(book_root, "okf", "log.md")
    with open(log, "a", encoding="utf-8") as fh:
        who = a.by or "okf_new"
        extra = f" (status: {a.status or 'unverified'})" if a.type == "Citation" else ""
        fh.write(f"- {built['stamp']} — {who}: created {a.type.lower()} `{slug}.md`{extra} — {a.description or a.title.strip()}\n")

    print(f"okf_new: wrote {rep['info']['bookRootRelative']}/{rel}  (timestamp {built['stamp']}, from the clock)")
    print(f"  okf/log.md appended; okf/index.md {'updated' if not idx_note else 'NOT updated: ' + idx_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
