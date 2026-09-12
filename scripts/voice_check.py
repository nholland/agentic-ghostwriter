#!/usr/bin/env python3
"""
voice_check.py - the counted half of the voice spec, by literal count.

WHY THIS EXISTS
    Self-reported counts were wrong on Chapter 9, Chapter 10, and the Prologue,
    and one of those wrong reports hid a live violation. 01-voice.md already
    says these rules "cannot be judged by impression." This script is the
    impression-free path.

WHAT IT IS HONEST ABOUT
    Two classes of output, never mixed:

      HARD   - a literal count against a threshold from config/house.json.
               em-dashes, bold, long-sentence share, you-density, declared
               metaphor family, ending shape. A FAIL here is a fact.

      CAND   - candidates needing a human or model read. Rhetorical-device
               repetition and unglossed Stoic terms cannot be fully decided by
               regex: a sentence-shape is a judgement, and a gloss can be
               phrased a hundred ways. The script surfaces suspects and counts
               what it can match. A clean CAND section is NOT a pass.

    A check whose input is missing reports SKIP and says what was missing. It
    never reports a pass for something it did not look at.

USAGE
    python3 scripts/voice_check.py <chapter.md> [--short-form]
                                   [--metaphor-family run,running,installed]
                                   [--config config/house.json] [--json]

EXIT CODES
    0  every HARD check passed
    1  at least one HARD check failed
    2  bad usage / unreadable input
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(os.path.dirname(HERE), "config", "house.json")

ABBREV = [
    "Mr.", "Mrs.", "Ms.", "Dr.", "St.", "Jr.", "Sr.", "Prof.",
    "e.g.", "i.e.", "etc.", "vs.", "cf.", "al.", "Inc.", "No.",
]


def load_config(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


APPARATUS_HEADING = re.compile(
    r"^#{1,6}\s*(Editor'?s Notes|Editorial Notes|Draft Notes|Spec Conformance"
    r"|Distillation|Pass \d+\b|Length Check|Attribution findings"
    r"|Remaining Placeholder|Structural Flag|For the Author'?s Review)\b",
    re.IGNORECASE | re.MULTILINE,
)


def split_front_matter(text):
    """Return (prose, stripped_info).

    Prose ends at the FIRST apparatus heading and everything after it is
    apparatus - Editor's Notes, the conformance table, Pass 4 counts, the
    distillation. An earlier version of this function cut each apparatus
    section individually and resumed counting at the next heading, which let
    ~1,500 words of tables and notes into Chapter 11's counts and inflated it
    from 2,828 prose words to 4,325. One boundary, not many.
    """
    m = APPARATUS_HEADING.search(text)
    if not m:
        return text, {}
    prose = text[: m.start()]
    tail = text[m.start():]
    return prose, {
        "cut_at_heading": m.group(1),
        "apparatus_words": len(re.findall(r"[A-Za-z\u2019']+", tail)),
    }


def strip_tables(text):
    """Markdown table rows are data, not sentences. A table row counted as prose
    produced a '164-word sentence' in the first run of this script."""
    return "\n".join(
        line for line in text.split("\n")
        if not line.lstrip().startswith("|")
    )


def strip_code_fences(text):
    return re.sub(r"^```.*?^```", "", text, flags=re.MULTILINE | re.DOTALL)


def quoted_spans(text):
    """Character ranges inside double quotes or markdown blockquotes. Used only
    to EXCLUDE translator punctuation from the em-dash cap."""
    spans = []
    for m in re.finditer(r'"[^"\n]{0,2000}"', text):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r'[“][^”\n]{0,2000}[”]', text):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r"^>.*$", text, re.MULTILINE):
        spans.append((m.start(), m.end()))
    return spans


def in_spans(idx, spans):
    return any(a <= idx < b for a, b in spans)


def prose_only(text):
    """Drop headings, list markers and blockquote arrows so sentence counting
    sees sentences, not scaffolding."""
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if re.match(r"^[-*+]\s", s) or re.match(r"^\d+[.)]\s", s):
            s = re.sub(r"^([-*+]|\d+[.)])\s+", "", s)
        if s.startswith(">"):
            s = s.lstrip("> ").strip()
        if re.match(r"^[-*_]{3,}$", s):
            continue
        out.append(s)
    return " ".join(out)


def sentences(text):
    """Approximate but deliberate sentence split. Abbreviations and ellipses are
    protected; the remaining error is small and in the same direction for every
    variant, which is what matters for a comparison."""
    t = text
    for i, ab in enumerate(ABBREV):
        t = t.replace(ab, f"\x00{i}\x00")
    t = t.replace("...", "\x01").replace("…", "\x01")
    parts = re.split(r'(?<=[.!?])["”\')\]]*\s+(?=[A-Z“"(])', t)
    out = []
    for p in parts:
        p = p.replace("\x01", "...")
        for i, ab in enumerate(ABBREV):
            p = p.replace(f"\x00{i}\x00", ab)
        p = p.strip()
        if p:
            out.append(p)
    return out


def words(text):
    return re.findall(r"[A-Za-z’']+", text)


# ---------------------------------------------------------------- checks

def check_em_dash(raw, rules):
    spans = quoted_spans(raw)
    bare, quoted = [], []
    for m in re.finditer(r"—", raw):
        line = raw.count("\n", 0, m.start()) + 1
        (quoted if in_spans(m.start(), spans) else bare).append(line)
    cap = rules["em_dash_max"]["value"]
    detail = f"{len(bare)} in prose (cap {cap})"
    if quoted:
        detail += (f"; {len(quoted)} inside quoted/blockquoted text, not counted "
                   f"- each needs a verification_note confirming it is the "
                   f"translator's own (lines {quoted[:8]})")
    return {
        "check": "em-dash", "kind": "HARD",
        "status": "PASS" if len(bare) <= cap else "FAIL",
        "value": len(bare), "threshold": cap,
        "detail": detail, "lines": bare[:20],
    }


def check_bold(raw, rules):
    """Separate the two things a ** span can be.

    01-voice.md caps bold at one genuine pull-quote per piece. But every
    numbered chapter of The Stoic Husband uses bolded run-in section headers
    (`**No door.**` alone on its line after a divider) - ch01 has 9, ch05/10/11
    have 5, ch09 has 4, while the Prologue and Introduction have none. A flat
    count therefore fails every chapter for a convention the spec never
    contemplated, which is a spec-vs-practice gap, not 11 defects.

    So only INLINE bold - a span with prose on the same line, which is bold
    standing in for sentence construction, the thing the rule is actually
    about - counts against the cap. Run-in headers are reported separately and
    left to the author, because loosening a counted rule is his call, not this
    script's.
    """
    cap = rules["bold_max_per_piece"]["value"]
    inline, headers = [], []
    for i, line in enumerate(raw.split("\n"), start=1):
        stripped = line.strip()
        spans = re.findall(r"\*\*[^*\n]+\*\*", stripped)
        if not spans:
            continue
        only_bold = re.fullmatch(r"(\*\*[^*\n]+\*\*)[\s.:\u2014-]*", stripped)
        if only_bold and len(spans) == 1:
            headers.append((i, spans[0]))
        else:
            inline.extend((i, s) for s in spans)
    detail = f"{len(inline)} inline bolded span(s) (cap {cap})"
    if headers:
        detail += (f"; {len(headers)} bolded run-in header(s) on their own line, "
                   f"NOT counted - book-wide convention that 01-voice.md's bold "
                   f"cap does not yet allow for. Needs an author ruling, not a "
                   f"silent exemption.")
    return {
        "check": "bold-as-crutch", "kind": "HARD",
        "status": "PASS" if len(inline) <= cap else "FAIL",
        "value": len(inline), "threshold": cap,
        "detail": detail,
        "inline": inline[:10], "run_in_headers": len(headers),
    }


def check_long_sentences(sents, rules):
    thresh = rules["long_sentence_word_threshold"]["value"]
    cap = rules["long_sentence_max_share"]["value"]
    if not sents:
        return {"check": "long-sentence share", "kind": "HARD", "status": "SKIP",
                "value": None, "threshold": cap, "detail": "no sentences found"}
    longs = [s for s in sents if len(words(s)) >= thresh]
    share = len(longs) / len(sents)
    return {
        "check": "long-sentence share", "kind": "HARD",
        "status": "PASS" if share <= cap else "FAIL",
        "value": round(share, 4), "threshold": cap,
        "detail": (f"{len(longs)}/{len(sents)} sentences at {thresh}+ words "
                   f"= {share*100:.1f}% (cap {cap*100:.0f}%)"),
        "worst": sorted(((len(words(s)), s[:110]) for s in longs), reverse=True)[:3],
    }


def check_you_density(prose, rules):
    w = words(prose)
    total = len(w)
    floor = rules["you_density_min_per_1000"]["value"]
    if total == 0:
        return {"check": "you-density", "kind": "HARD", "status": "SKIP",
                "value": None, "threshold": floor, "detail": "no words found"}
    hits = sum(1 for x in w if x.lower() in ("you", "your", "yours", "you're", "youre", "yourself"))
    per_k = hits / total * 1000
    return {
        "check": "you-density", "kind": "HARD",
        "status": "PASS" if per_k >= floor else "FAIL",
        "value": round(per_k, 1), "threshold": floor,
        "detail": f"{hits} direct-address words in {total} = {per_k:.1f} per 1,000 (floor {floor})",
    }


def check_metaphor_family(prose, rules, family):
    cap = rules["metaphor_family_max_per_1000"]["value"]
    if not family:
        return {
            "check": "metaphor family", "kind": "HARD", "status": "SKIP",
            "value": None, "threshold": cap,
            "detail": ("no family declared - pass --metaphor-family, or have the "
                       "drafter declare the chapter's anchor image in Draft Notes. "
                       "UNCHECKED, not passed."),
        }
    w = [x.lower() for x in words(prose)]
    total = len(w)
    counts, hits = {}, 0
    for term in family:
        t = term.strip().lower()
        if not t:
            continue
        c = sum(1 for x in w if x == t or x.startswith(t))
        if c:
            counts[t] = c
        hits += c
    per_k = hits / total * 1000 if total else 0
    return {
        "check": "metaphor family", "kind": "HARD",
        "status": "PASS" if per_k <= cap else "FAIL",
        "value": round(per_k, 2), "threshold": cap,
        "detail": f"{hits} mentions in {total} words = {per_k:.1f} per 1,000 (cap {cap}); {counts}",
    }


def check_ending(sents, rules):
    want = rules["ending_sentences"]["value"]
    if len(sents) < 2:
        return {"check": "single ending", "kind": "HARD", "status": "SKIP",
                "value": None, "threshold": want, "detail": "too few sentences to judge"}
    last, prev = sents[-1], sents[-2]
    # A double ending is a short restating sentence after the real close. Length
    # alone cannot prove intent, so this is reported HARD only on the structural
    # signal the voice spec names: the final sentence is very short AND echoes
    # vocabulary from the one before it.
    lw = set(x.lower() for x in words(last))
    pw = set(x.lower() for x in words(prev))
    overlap = len(lw & pw)
    suspicious = len(words(last)) <= 12 and overlap >= 3
    return {
        "check": "single ending", "kind": "CAND",
        "status": "REVIEW" if suspicious else "CLEAR",
        "value": overlap, "threshold": want,
        "detail": (f"final sentence {len(words(last))} words, shares {overlap} words "
                   f"with the previous one. Close: {last[:120]!r}"),
    }


DEVICE_PATTERNS = [
    ("reframe  'That's not X. That's Y.'",
     re.compile(r"\b(?:that|this|it)(?:'s| is) not\b[^.!?]{0,90}[.!?]\s+(?:that|this|it)(?:'s| is)\b", re.I)),
    ("negated pair  'not X, Y'",
     re.compile(r"\b\w+ed,\s+not\s+\w+ed\b", re.I)),
    ("you-don't pivot  'you don't X, you Y'",
     re.compile(r"\byou don'?t\b[^.!?]{0,80}\byou\b", re.I)),
    ("colon-then-label",
     re.compile(r"^[A-Z][^:\n]{8,70}:\s+[a-z]", re.M)),
]


def check_devices(prose, rules):
    cap = rules["rhetorical_device_max"]["value"]
    found = {}
    for name, pat in DEVICE_PATTERNS:
        n = len(pat.findall(prose))
        if n:
            found[name] = n
    over = {k: v for k, v in found.items() if v > cap}
    return {
        "check": "rhetorical-device repetition", "kind": "CAND",
        "status": "REVIEW" if over else "CLEAR",
        "value": found, "threshold": cap,
        "detail": (f"detectable shapes over cap {cap}: {over}" if over
                   else f"no detectable shape over cap {cap}. Counts: {found or 'none matched'}. "
                        f"Regex cannot see every sentence-shape - a model read is still required."),
    }


def check_stoic_glosses(prose, cfg):
    terms = cfg.get("stoic_terms", [])
    window = cfg.get("gloss_window_chars", 260)
    flagged = []
    low = prose.lower()
    for term in terms:
        idx = low.find(term.lower())
        if idx == -1:
            continue
        tail = prose[idx: idx + window]
        # A gloss usually arrives as a dash-free apposition, a comma clause, or
        # parentheses close to the term. Absence of any of these is the signal.
        if not re.search(r"[,(:]|\bmeans\b|\bthat is\b|\bwhich is\b|\bthe part\b", tail):
            flagged.append({"term": term, "context": tail[:140]})
    return {
        "check": "Stoic term gloss on first use", "kind": "CAND",
        "status": "REVIEW" if flagged else "CLEAR",
        "value": [f["term"] for f in flagged], "threshold": "gloss within same/next sentence",
        "detail": (f"possibly unglossed: {[f['term'] for f in flagged]}" if flagged
                   else "every listed term that appears has punctuation or a gloss verb nearby"),
        "contexts": flagged[:5],
    }


# ---------------------------------------------------------------- driver

def run(path, cfg, family, short_form=False):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    raw = strip_code_fences(raw)
    body, stripped = split_front_matter(raw)
    body = strip_tables(body)
    prose = prose_only(body)
    sents = sentences(prose)
    rules = cfg["voice_rules"]

    results = [
        check_em_dash(body, rules),
        check_bold(body, rules),
        check_long_sentences(sents, rules),
        check_you_density(prose, rules),
        check_metaphor_family(prose, rules, family),
        check_ending(sents, rules),
        check_devices(prose, rules),
        check_stoic_glosses(prose, cfg),
    ]
    return {
        "file": path,
        "word_count": len(words(prose)),
        "sentence_count": len(sents),
        "stripped_apparatus": stripped,
        "short_form": short_form,
        "results": results,
        "hard_failed": [r["check"] for r in results
                        if r["kind"] == "HARD" and r["status"] == "FAIL"],
        "hard_skipped": [r["check"] for r in results
                         if r["kind"] == "HARD" and r["status"] == "SKIP"],
        "candidates_to_review": [r["check"] for r in results
                                 if r["kind"] == "CAND" and r["status"] == "REVIEW"],
    }


def render(rep):
    L = []
    L.append(f"voice_check: {os.path.basename(rep['file'])}")
    L.append(f"  {rep['word_count']} words of prose, {rep['sentence_count']} sentences")
    if rep["stripped_apparatus"]:
        L.append(f"  excluded from counts: {rep['stripped_apparatus']}")
    L.append("")
    L.append("  HARD (literal counts - a FAIL here is a fact)")
    for r in rep["results"]:
        if r["kind"] != "HARD":
            continue
        mark = {"PASS": "ok  ", "FAIL": "FAIL", "SKIP": "skip"}[r["status"]]
        L.append(f"    [{mark}] {r['check']:<24} {r['detail']}")
        for wc, s in (r.get("worst") or []):
            L.append(f"             {wc}w: {s}...")
    L.append("")
    L.append("  CAND (needs a read - a clear line here is not a pass)")
    for r in rep["results"]:
        if r["kind"] != "CAND":
            continue
        mark = "REVIEW" if r["status"] == "REVIEW" else "clear "
        L.append(f"    [{mark}] {r['check']:<24} {r['detail']}")
    L.append("")
    if rep["hard_failed"]:
        L.append(f"  RESULT: FAIL on {', '.join(rep['hard_failed'])}")
    else:
        L.append("  RESULT: all HARD checks passed")
    if rep["hard_skipped"]:
        L.append(f"  UNCHECKED (not passed): {', '.join(rep['hard_skipped'])}")
    if rep["candidates_to_review"]:
        L.append(f"  REVIEW: {', '.join(rep['candidates_to_review'])}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Counted voice rules, by literal count.")
    ap.add_argument("file")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--metaphor-family", default="",
                    help="comma-separated word family for the chapter's anchor image")
    ap.add_argument("--short-form", action="store_true",
                    help="mark the piece as short-form (Substack/social)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(a.file):
        print(f"voice_check: no such file: {a.file}", file=sys.stderr)
        return 2
    try:
        cfg = load_config(a.config)
    except Exception as exc:
        print(f"voice_check: cannot read config {a.config}: {exc}", file=sys.stderr)
        return 2

    family = [x for x in a.metaphor_family.split(",") if x.strip()]
    rep = run(a.file, cfg, family, a.short_form)
    print(json.dumps(rep, indent=2) if a.json else render(rep))
    return 1 if rep["hard_failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
