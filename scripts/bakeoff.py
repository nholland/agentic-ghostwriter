#!/usr/bin/env python3
"""
bakeoff.py - compare two versions of the same chapter, blind.

WHY BLIND
    The author is the judge, and he is also the person who wants the new system
    to win. If he knows which draft came from which pipeline, that is the
    finding, not the prose. So this writes two neutrally-named variants plus a
    sealed mapping, and the counted comparison is labelled by variant, never by
    system. Unseal after the verdict is written down.

USAGE
    python3 scripts/bakeoff.py --chapter 12 \\
        --control  /path/to/old/refined.md \\
        --variant  /path/to/new/refined.md \\
        [--metaphor-family door,doors] [--out bakeoff]

    python3 scripts/bakeoff.py --unseal bakeoff/ch12

OUTPUT  (bakeoff/chNN/)
    variant-1.md  variant-2.md   prose only, apparatus stripped, shuffled
    comparison.md                counted diff, labelled by variant
    verdict.md                   template for the author, written before unsealing
    .sealed.json                 the mapping. Do not open until verdict.md is filled in.
"""

import argparse
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import voice_check as vc  # noqa: E402

DEFAULT_CONFIG = os.path.join(os.path.dirname(HERE), "config", "house.json")


def read_prose(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    raw = vc.strip_code_fences(raw)
    body, info = vc.split_front_matter(raw)
    return body, info


def fingerprint(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def placeholders(text):
    return re.findall(r"\[PLACEHOLDER:[^\]]*\]", text)


def stats(path, cfg, family):
    rep = vc.run(path, cfg, family)
    body, info = read_prose(path)
    return {
        "source": path,
        "report": rep,
        "placeholders": placeholders(body),
        "apparatus": info,
        "fingerprint": fingerprint(body),
    }


def row(label, a, b):
    return f"| {label} | {a} | {b} |"


def build_comparison(s1, s2, chapter):
    r1, r2 = s1["report"], s2["report"]

    def hard(rep, name):
        for r in rep["results"]:
            if r["check"] == name:
                return r
        return None

    L = []
    L.append(f"# Bake-off comparison - Chapter {chapter}")
    L.append("")
    L.append("Counted facts only. Variants are deliberately unlabelled: nothing below")
    L.append("says which pipeline produced which. Write `verdict.md` before unsealing.")
    L.append("")
    L.append("## Shape")
    L.append("")
    L.append("| Measure | variant-1 | variant-2 |")
    L.append("|---|---|---|")
    L.append(row("Prose words", r1["word_count"], r2["word_count"]))
    L.append(row("Sentences", r1["sentence_count"], r2["sentence_count"]))
    L.append(row("Placeholders left", len(s1["placeholders"]), len(s2["placeholders"])))
    L.append(row("Apparatus words", s1["apparatus"].get("apparatus_words", 0),
                 s2["apparatus"].get("apparatus_words", 0)))
    L.append("")
    L.append("## Counted voice rules (HARD - a FAIL is a fact)")
    L.append("")
    L.append("| Rule | variant-1 | variant-2 |")
    L.append("|---|---|---|")
    for name in ["em-dash", "bold-as-crutch", "long-sentence share",
                 "you-density", "metaphor family"]:
        a, b = hard(r1, name), hard(r2, name)
        fa = f"{a['status']} ({a['value']})" if a else "n/a"
        fb = f"{b['status']} ({b['value']})" if b else "n/a"
        L.append(row(name, fa, fb))
    L.append("")
    L.append("## Candidates (need a read - clear is not a pass)")
    L.append("")
    L.append("| Check | variant-1 | variant-2 |")
    L.append("|---|---|---|")
    for name in ["single ending", "rhetorical-device repetition",
                 "Stoic term gloss on first use"]:
        a, b = hard(r1, name), hard(r2, name)
        fa = f"{a['status']}: {a['value']}" if a else "n/a"
        fb = f"{b['status']}: {b['value']}" if b else "n/a"
        L.append(row(name, fa, fb))
    L.append("")
    L.append("## What this does NOT measure")
    L.append("")
    L.append("Whether the chapter is good. Every number above can match while one")
    L.append("variant says the true thing and the other says a plausible one. The")
    L.append("counted rules are a floor, not the verdict - that is what the blind")
    L.append("read in `verdict.md` is for. Run the `spec-checker` agent against both")
    L.append("variants separately for conformance; it is clean-room and must not be")
    L.append("told which is which either.")
    return "\n".join(L)


VERDICT_TEMPLATE = """# Verdict - Chapter {chapter}

Fill this in BEFORE unsealing. That is the whole point.

## Blind read

Read `variant-1.md` and `variant-2.md` cold, in that order, then answer.

**Which one would you publish?**  variant-_

**Where did the other one lose you?** (a line, a paragraph, a moment that rang false)

**Did either say something you did not tell it?** (the thing only the interview
could have produced - if one variant has it and the other does not, that is the
finding this whole exercise exists to surface)

**Did either need you to fix something the counts called clean?**

## Counted result

See `comparison.md`. Note any place where the counts and your read disagree -
that disagreement is more informative than either one alone.

## Decision

- [ ] The new pipeline is at least as good on the cold stages. Proceed to the
      Ch13 lead run (the interview).
- [ ] The new pipeline is worse. What specifically: ______
- [ ] Too close to call on this chapter. Ch12 was short and low-research; run
      the shadow again on a meatier chapter before deciding.

## Then

Unseal with: `python3 scripts/bakeoff.py --unseal bakeoff/ch{chapter}`
"""


def do_build(args, cfg):
    chapter = str(args.chapter).zfill(2)
    outdir = os.path.join(args.out, f"ch{chapter}")
    os.makedirs(outdir, exist_ok=True)

    for p in (args.control, args.variant):
        if not os.path.isfile(p):
            print(f"bakeoff: no such file: {p}", file=sys.stderr)
            return 2

    family = [x for x in (args.metaphor_family or "").split(",") if x.strip()]
    s_ctrl = stats(args.control, cfg, family)
    s_var = stats(args.variant, cfg, family)

    if s_ctrl["fingerprint"] == s_var["fingerprint"]:
        print("bakeoff: both inputs have identical prose. Nothing to compare.",
              file=sys.stderr)
        return 2

    pair = [("control", s_ctrl), ("variant", s_var)]
    rnd = random.Random(f"ch{chapter}:{s_ctrl['fingerprint']}{s_var['fingerprint']}")
    rnd.shuffle(pair)

    mapping = {}
    for i, (origin, s) in enumerate(pair, start=1):
        body, _ = read_prose(s["source"])
        dest = os.path.join(outdir, f"variant-{i}.md")
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(body.rstrip() + "\n")
        mapping[f"variant-{i}"] = {
            "origin": origin,
            "source": os.path.abspath(s["source"]),
            "fingerprint": s["fingerprint"],
        }

    s1 = pair[0][1]
    s2 = pair[1][1]
    with open(os.path.join(outdir, "comparison.md"), "w", encoding="utf-8") as fh:
        fh.write(build_comparison(s1, s2, chapter) + "\n")

    vpath = os.path.join(outdir, "verdict.md")
    if os.path.exists(vpath):
        print(f"bakeoff: keeping existing {vpath} (not overwriting your notes)")
    else:
        with open(vpath, "w", encoding="utf-8") as fh:
            fh.write(VERDICT_TEMPLATE.format(chapter=chapter))

    with open(os.path.join(outdir, ".sealed.json"), "w", encoding="utf-8") as fh:
        json.dump(mapping, fh, indent=2)

    print(f"bakeoff: wrote {outdir}/")
    print("  variant-1.md, variant-2.md   <- read these cold, in order")
    print("  comparison.md                <- counted diff, unlabelled")
    print("  verdict.md                   <- fill in BEFORE unsealing")
    print(f"  .sealed.json                 <- sealed mapping")
    print("")
    print("  HARD failures, by variant (not by system):")
    for lbl, s in (("variant-1", s1), ("variant-2", s2)):
        f = s["report"]["hard_failed"] or ["none"]
        k = s["report"]["hard_skipped"]
        line = f"    {lbl}: {', '.join(f)}"
        if k:
            line += f"   [unchecked: {', '.join(k)}]"
        print(line)
    return 0


def do_unseal(path):
    sealed = os.path.join(path, ".sealed.json")
    if not os.path.isfile(sealed):
        print(f"bakeoff: no sealed mapping at {sealed}", file=sys.stderr)
        return 2
    verdict = os.path.join(path, "verdict.md")
    if os.path.isfile(verdict):
        txt = open(verdict, encoding="utf-8").read()
        if "variant-_" in txt:
            print("bakeoff: verdict.md still has an unfilled answer (`variant-_`).")
            print("         Write the verdict first - unsealing now wastes the blind.")
            print("         Re-run with --force-unseal if you really mean to.")
            if "--force-unseal" not in sys.argv:
                return 1
    with open(sealed, encoding="utf-8") as fh:
        m = json.load(fh)
    print("Unsealed:")
    for k, v in sorted(m.items()):
        print(f"  {k} = {v['origin']:<8} {v['source']}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Blind A/B of two chapter versions.")
    ap.add_argument("--chapter")
    ap.add_argument("--control", help="the old pipeline's refined.md")
    ap.add_argument("--variant", help="the new pipeline's refined.md")
    ap.add_argument("--metaphor-family", default="")
    ap.add_argument("--out", default="bakeoff")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--unseal", metavar="DIR")
    ap.add_argument("--force-unseal", action="store_true")
    a = ap.parse_args()

    if a.unseal:
        return do_unseal(a.unseal)
    if not (a.chapter and a.control and a.variant):
        ap.error("--chapter, --control and --variant are required to build a bake-off")
    try:
        cfg = vc.load_config(a.config)
    except Exception as exc:
        print(f"bakeoff: cannot read config: {exc}", file=sys.stderr)
        return 2
    return do_build(a, cfg)


if __name__ == "__main__":
    sys.exit(main())
