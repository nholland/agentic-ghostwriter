#!/usr/bin/env python3
"""
term_check.py - no coinage selects evidence unless something defined it.

WHY THIS EXISTS (the "Rock" incident)
    A research brief once organised a chapter's evidence around a capitalised
    term that existed only in the outline line it came from. Nothing had
    defined it, no concept carried it, and the drafter treated it as an
    established idea of the book's. The reader would have met a term the book
    never explained. The Anti-Slop Reader's cross-chapter category "a term used
    as established that nothing defined" catches this at book level, late. This
    catches it at the brief, early, by count.

WHAT IT DOES
    Finds candidate coinages in a brief or draft - bolded phrases, quoted
    Title-Case phrases, and runs of Capitalised Words mid-sentence - and asks
    where each resolves:

      OKF        an okf/ concept whose title or slug matches       -> fine
      DEFINED    the text itself defines it (": " / "call this" /
                 "what I call" within a sentence of first use)     -> fine
      OUTLINE    appears in 03-outline.md but nowhere else         -> WARN
                 (the Rock case: it may organise the brief only if
                 the brief defines it or a concept is created)
      NONE       appears in none of the above                      -> FAIL

    Proper nouns and generic capitalised words are filtered by
    config/house.json "term_check.ignore" (regexes). The filter is a list you
    can see, not a judgement the script makes silently.

USAGE
    python3 scripts/term_check.py runs/ch12/research.md
    python3 scripts/term_check.py runs/ch12/draft.md --json

EXIT CODES
    0 nothing unresolved   1 at least one NONE (or OUTLINE with --strict)   2 usage / no book
"""

import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402
import voice_check  # noqa: E402

DEFAULT_IGNORE = [
    r"^(Chapter|Part|Book|Step|Pass|Gate|Section|Figure|Table|Note|Notes)\b",
    r"^(The )?(Stoic|Stoics|Stoicism|Roman|Greek|Christian|Western)$",
    r"^(Marcus( Aurelius)?|Seneca|Epictetus|Musonius( Rufus)?|Zeno|Chrysippus|Socrates|Plato|Aristotle)$",
    r"^(Gottman|Perel|Brown|Pillemer|Glover|Cloud|Townsend|Tawwab|Hanson|Kahneman|Seligman|Treynor|Basson|Muise|Impett|Herbenick|Weiss|Wiesel)\b",
    r"^(Meditations|Enchiridion|Discourses|Letters?|De Ira|De Beneficiis)\b",
    r"^(Draft Notes|Editor'?s Notes|Research Needed|Story Needed|Placeholder|Research Brief|Key Points?|Reader|Premise|Word count|Transition)\b",
    r"^(Introduction|Prologue|Conclusion|Epilogue|Appendix|Practice|Lesson|Challenge|Mechanism|Conversation)\b",
    r"^[A-Z]\.?$",
    r"^(I|You|He|She|We|They|It|God|Christmas|Tuesday|Monday|Sunday|January|February|March|April|May|June|July|August|September|October|November|December)$",
]

DEFINE_PATTERNS = [
    r"\bcall(?:ed|s)? (?:this|it|that)\b", r"\bwhat I call\b", r"\bI(?:'ll| will) call\b",
    r"\bthe name for (?:this|it)\b", r"\bthink of (?:this|it) as\b", r"\bmeans\b", r"\bis when\b",
]


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return re.sub(r"-+", "-", s)


STOPWORDS = {"of", "the", "a", "an", "and", "or", "in", "to", "for", "with", "without",
             "as", "at", "by", "on", "vs", "versus", "not", "is", "are", "into", "from", "that"}


def norm(s):
    s = re.sub(r"[*_\"“”'‘’]", "", s).strip()
    s = re.sub(r"^(the|a|an)\s+", "", s, flags=re.I)
    return re.sub(r"\s+", " ", s).strip()


def looks_like_a_term(phrase):
    """A coinage is a label, so it reads as a label: Title Case on every word
    that is not a stopword, no terminal punctuation, no brackets, no colon.
    The first version accepted any bold or quoted span and reported 59
    'coinages' in a brief that had perhaps six - every bolded field label
    (`**What to look for:**`), every bracketed filing note, and sentence
    fragments joined across mismatched quote marks. Noise at that level is
    silence with extra steps: nobody reads a 59-row FAIL."""
    if not phrase or re.search(r"[\[\]:;—]|[.!?,]$", phrase):
        return False
    words = phrase.split()
    if len(words) > 6:
        return False
    sig = [w for w in words if w.lower() not in STOPWORDS]
    if not sig:
        return False
    if any(not (w[0].isupper() or w[0].isdigit()) for w in sig):
        return False
    if len(words) == 1 and len(words[0]) < 4:
        return False
    return True


def candidates(text):
    """Return {normalised phrase: [(line, raw)]} of possible coinages."""
    found = {}

    def add(raw, line):
        n = norm(raw)
        if looks_like_a_term(n):
            found.setdefault(n, []).append((line, raw.strip()))

    for i, line in enumerate(text.split("\n"), start=1):
        if line.lstrip().startswith("#") or line.lstrip().startswith("|"):
            continue
        for m in re.finditer(r"\*\*([^*\n]{3,60})\*\*", line):
            add(m.group(1), i)
        # Pair each quote mark with its own kind; "..." and “...” never cross.
        for m in re.finditer(r"\"([A-Z][^\"\n]{2,50})\"", line):
            add(m.group(1), i)
        for m in re.finditer(r"“([A-Z][^”\n]{2,50})”", line):
            add(m.group(1), i)
        # Runs of 2+ Capitalised words. A run at a sentence start is kept:
        # norm() drops a leading article, and looks_like_a_term() still needs
        # every remaining word capitalised, so "The hallway" never qualifies
        # while "The Nail Parable" does.
        for m in re.finditer(r"(?<![\"“(\[])\b((?:[A-Z][a-z’\']+\s+){1,4}[A-Z][a-z’\']+)\b", line):
            add(m.group(1), i)
    return found


def context(text, phrase):
    """The sentence containing the first use, for the DEFINED test. The first
    version took a 500-character window and read 'what I call' from the NEXT
    sentence as a definition of THIS term."""
    low = text.lower()
    idx = low.find(phrase.lower())
    if idx == -1:
        return ""
    start = max(low.rfind(ch, 0, idx) for ch in ".!?\n") + 1
    ends = [low.find(ch, idx + len(phrase)) for ch in ".!?\n"]
    ends = [e for e in ends if e != -1]
    end = min(ends) if ends else len(text)
    return text[start:end]


def slug_in_concepts(slug, slugs):
    """'torpedo' resolves to 'seagull-and-torpedo' because its tokens appear as
    a contiguous run inside the concept slug's tokens. Token-wise, not
    substring-wise, so 'open' does not resolve to 'the-open-door' by accident
    and a single word must carry at least five letters to count."""
    t = slug.split("-")
    if len(t) == 1 and len(t[0]) < 5:
        return False
    for s in slugs:
        st = s.split("-")
        for i in range(len(st) - len(t) + 1):
            if st[i:i + len(t)] == t:
                return True
    return False


def okf_titles(okf_dir):
    titles, slugs = set(), set()
    for p in glob.glob(os.path.join(okf_dir, "*", "*.md")):
        slugs.add(os.path.splitext(os.path.basename(p))[0])
        try:
            head = open(p, encoding="utf-8").read(2000)
        except OSError:
            continue
        m = re.search(r"^title:\s*(.+)$", head, re.MULTILINE)
        if m:
            titles.add(norm(m.group(1)).lower())
    return titles, slugs


def main():
    ap = argparse.ArgumentParser(description="Resolve every capitalised coinage in a brief or draft.")
    ap.add_argument("file")
    ap.add_argument("--strict", action="store_true", help="OUTLINE-only terms fail too")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(a.file):
        print(f"term_check: no such file: {a.file}", file=sys.stderr)
        return 2
    cfg = resolve_book.load_config()
    repo_root, _, _ = resolve_book.resolve(cfg)
    if not repo_root:
        print("term_check: no book repo resolvable", file=sys.stderr)
        return 2
    info = resolve_book.inspect(repo_root, require_okf=False)["info"]
    book_root = info.get("bookRoot")
    if not book_root:
        print("term_check: no bookRoot", file=sys.stderr)
        return 2

    tc = cfg.get("term_check") or {}
    ignore = [re.compile(p, re.I) for p in (tc.get("ignore") or DEFAULT_IGNORE)]
    ignore_words = {w.lower() for w in tc.get("ignore_words", [])}
    raw = open(a.file, encoding="utf-8").read()
    # Prose only: apparatus (Editor's Notes, conformance tables) is full of
    # capitalised labels that are not the book's vocabulary.
    text, _ = voice_check.split_front_matter(voice_check.strip_code_fences(raw))
    constitution = ""
    for f in ("00-premise.md", "01-voice.md", "02-audience.md", "04-archetype.md", "05-framework.md"):
        p = os.path.join(book_root, f)
        if os.path.isfile(p):
            constitution += open(p, encoding="utf-8").read().lower() + "\n"
    outline = ""
    op = os.path.join(book_root, "03-outline.md")
    if os.path.isfile(op):
        outline = open(op, encoding="utf-8").read().lower()
    titles, slugs = okf_titles(os.path.join(book_root, "okf"))

    rows = []
    for phrase, hits in sorted(candidates(text).items()):
        if any(rx.search(phrase) for rx in ignore):
            continue
        if any(w.lower().strip("’'s") in ignore_words or w.lower() in ignore_words for w in phrase.split()):
            continue  # a named person or a named work, not a coinage
        low, slug = phrase.lower(), slugify(phrase)
        if low in titles or slug in slugs or slug_in_concepts(slug, slugs):
            where = "OKF"
        elif low in constitution:
            where = "CONSTITUTION"
        elif re.search("|".join(DEFINE_PATTERNS), context(text, phrase), re.I):
            where = "DEFINED"
        elif low in outline:
            where = "OUTLINE"
        else:
            where = "NONE"
        rows.append({"term": phrase, "resolves": where, "uses": len(hits),
                     "first_line": hits[0][0], "sample": hits[0][1]})

    none = [r for r in rows if r["resolves"] == "NONE"]
    outl = [r for r in rows if r["resolves"] == "OUTLINE"]
    failing = none + (outl if a.strict else [])

    if a.json:
        print(json.dumps({"file": a.file, "rows": rows, "unresolved": [r["term"] for r in none],
                          "outline_only": [r["term"] for r in outl]}, indent=2))
    else:
        print(f"term_check: {os.path.basename(a.file)} - {len(rows)} candidate coinage(s) after the ignore list")
        for r in rows:
            mark = {"OKF": "ok  ", "CONSTITUTION": "ok  ", "DEFINED": "ok  ", "OUTLINE": "WARN", "NONE": "FAIL"}[r["resolves"]]
            print(f"  [{mark}] {r['term']:<40} {r['resolves']:<12} x{r['uses']}  first at line {r['first_line']}")
        print()
        if none:
            print(f"  FAIL: {len(none)} term(s) resolve nowhere. Define each in the text, create a concept "
                  f"with scripts/okf_new.py, or stop using it as though the book had established it.")
        if outl:
            print(f"  WARN: {len(outl)} term(s) exist only in 03-outline.md. The outline is a commission, "
                  f"not a definition - a brief may organise evidence around one only after defining it.")
        if not rows or (not none and not outl):
            print("  every coinage resolves to a concept, the constitution, or a definition in the text")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
