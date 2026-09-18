#!/usr/bin/env python3
"""tests/run.py - the fixtures each check was proved against, stored.

WHY. Two checks written on 2026-09-17 both contained the defect they were written
to fix, and both had been "proved" by a one-off run that was never stored. The
Archivist had to reconstruct the failing input to test the claim, and
reconstructing it is what found the escapes. A proof that cannot be re-run is a
comment. So the inputs live here and the Stop hook runs them.

Add a fixture whenever a check gains a case. A check whose escape is not in this
directory has not been proved; it has been asserted.

    python3 tests/run.py          # every fixture; exit 1 on any failure
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FIX = os.path.join(HERE, "fixtures")
sys.path.insert(0, os.path.join(REPO, "scripts"))


def package_cases():
    import package_check
    # (fixture, must_fail, why it is here)
    cases = [
        ("opens-on-distillation.html", True,
         "the founding defect: the package opened on the distillation"),
        ("distback-but-first.html", True,
         "classed distback and placed FIRST - passed clean until 2026-09-18, "
         "because the check tested the class name and never the position"),
        ("extra-attribute.html", True,
         "an id on the section tag made it invisible to the regex, and the "
         "check then reported 'opens on: chapter'"),
        ("apparatus-in-span.html", True,
         "<h2><span>Draft Notes</span></h2> escaped the apparatus scan"),
        ("single-quoted-class.html", True,
         "#025: class='dist distback' (single-quoted) escaped the double-quote regex"),
        ("div-container.html", True,
         "#025: a <div class=\"dist\"> container - only <section> was known"),
        ("nested-distillation.html", True,
         "#025: a distillation nested inside the chapter section was 'last' by "
         "flat index though more chapter prose followed it on the page"),
        ("entity-in-heading.html", True,
         "#025: <h2>Editor&#39;s Notes</h2> - the entity was never unescaped"),
        ("h4-apparatus-heading.html", True,
         "#025: <h4>Draft Notes</h4> - the old scan was h1-h3 only"),
        ("unrecognised-first-section.html", True,
         "#025: a classless, headingless first section defaulted to \"chapter\" "
         "instead of failing closed as unrecognised"),
        ("good.html", False, "chapter first, distillation last and labelled"),
    ]
    out = []
    for name, must_fail, why in cases:
        fails, _ = package_check.check(os.path.join(FIX, name))
        ok = bool(fails) == must_fail
        out.append((ok, f"package_check {name}", why,
                    "; ".join(fails) if fails else "clean"))
    return out


def _isolated_engine():
    """Copy scripts/ + config/ into a tempdir so mutating a threshold never
    touches the tracked config/house.json (#026: a killed run used to leave
    it corrupted - 12/12 on two concurrent runs - and block every prose desk).
    Returns the path to the copied voice_rules_check.py."""
    tmp = tempfile.mkdtemp(prefix="gw-tests-engine-")
    shutil.copytree(os.path.join(REPO, "scripts"), os.path.join(tmp, "scripts"))
    shutil.copytree(os.path.join(REPO, "config"), os.path.join(tmp, "config"))
    return tmp


def _run_isolated(engine_tmp, book_repo, cfg_mutator=None):
    """Run the isolated copy's voice_rules_check.py against book_repo, after
    cfg_mutator (if given) edits the isolated copy's config/house.json."""
    cfg = os.path.join(engine_tmp, "config", "house.json")
    if cfg_mutator:
        d = json.load(open(cfg))
        cfg_mutator(d)
        json.dump(d, open(cfg, "w"), indent=2)
    env = dict(os.environ, GW_BOOK_REPO=book_repo)
    return subprocess.run(
        [sys.executable, os.path.join(engine_tmp, "scripts", "voice_rules_check.py")],
        capture_output=True, text=True, env=env)


def _fake_book(voice_md_text):
    """A minimal book repo - book-manifest.json + bookRoot/01-voice.md - so
    the DRIFT fixture can mutate spec text without touching the real book."""
    book = tempfile.mkdtemp(prefix="gw-tests-book-")
    os.makedirs(os.path.join(book, "the-book"))
    json.dump({"bookRoot": "the-book", "books": {"the-book": {"title": "test"}}},
              open(os.path.join(book, "book-manifest.json"), "w"))
    open(os.path.join(book, "the-book", "01-voice.md"), "w", encoding="utf-8") \
        .write(voice_md_text)
    return book


def voice_rules_cases():
    """Run voice_rules_check.py, isolated (#026), against three states: the
    real book untouched (must PASS clean - #024's missing baseline), each
    threshold mutated in turn (must MISMATCH, the rule NAMED in the output,
    not just a non-zero exit - #024), and a spec with one probe's wording
    removed (must DRIFT, the rule named - #024's missing fixture)."""
    import resolve_book
    real_cfg = resolve_book.load_config()
    real_book, _, _ = resolve_book.resolve(real_cfg)
    out = []
    if not real_book:
        out.append((False, "voice_rules baseline", "no book repo resolvable",
                    "cannot test against a spec that is not there"))
        return out
    rep = resolve_book.inspect(real_book, require_okf=False)
    spec_path = rep["info"].get("bookRoot")
    real_spec_text = open(os.path.join(spec_path, "01-voice.md"),
                          encoding="utf-8").read() if spec_path else ""

    engine_tmp = _isolated_engine()
    try:
        # Baseline: the pristine config against the real spec must PASS clean.
        # Verified 2026-09-18: without this, a check whose main() only ever
        # returns 1 still scored 14/14, because nothing asserted the healthy
        # case ever printed ok.
        r = _run_isolated(engine_tmp, real_book)
        clean = r.returncode == 0 and "MISMATCH" not in r.stdout and "DRIFT" not in r.stdout
        out.append((clean, "voice_rules baseline",
                    "the unmutated config must PASS with no MISMATCH or DRIFT",
                    r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[:80]))

        # Each threshold mutated +7: must MISMATCH, and that rule must be
        # named in the output - non-zero exit alone is what a dead check and
        # a live one have in common.
        d = json.load(open(os.path.join(REPO, "config", "house.json")))
        for name, rule in d["voice_rules"].items():
            if not isinstance(rule, dict) or "value" not in rule:
                continue
            orig = rule["value"]
            mutated = float(orig) + 7

            def mutate(cfg, name=name, mutated=mutated):
                cfg["voice_rules"][name]["value"] = mutated
            r = _run_isolated(engine_tmp, real_book, mutate)
            named = "MISMATCH" in r.stdout and name in r.stdout
            caught = r.returncode != 0 and "Traceback" not in r.stderr and named
            out.append((caught, f"voice_rules mutation {name}",
                        f"{orig} -> {mutated} must MISMATCH, named in the output",
                        r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[:80]))

        # The one honest state must print, not crash. Removing spec_number is
        # exactly what a ninth rule added without one would look like.
        def strip_spec_number(cfg):
            cfg["voice_rules"]["em_dash_max"].pop("spec_number", None)
        r = _run_isolated(engine_tmp, real_book, strip_spec_number)
        unchecked = "UNCHECKED" in r.stdout and "em_dash_max" in r.stdout
        out.append((unchecked and "Traceback" not in r.stderr,
                    "voice_rules spec_number null",
                    "an undeclared number must report UNCHECKED by name, never crash",
                    "crashed" if "Traceback" in r.stderr else r.stdout.strip().splitlines()[-1]))

        # DRIFT: the founding purpose of this check had no fixture at all.
        # Remove the em-dash rule's own source phrase from the spec; the
        # check must report DRIFT, naming em_dash_max, not silently pass it.
        drifted_spec = real_spec_text.replace("Never use em-dashes", "Avoid long dashes")
        fake_book = _fake_book(drifted_spec)
        try:
            r = _run_isolated(engine_tmp, fake_book)
            drift_named = "DRIFT" in r.stdout and "em_dash_max" in r.stdout
            out.append((drift_named and r.returncode != 0, "voice_rules DRIFT fixture",
                        "a probe phrase removed from 01-voice.md must DRIFT, named",
                        r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[:80]))
        finally:
            shutil.rmtree(fake_book, ignore_errors=True)
    finally:
        shutil.rmtree(engine_tmp, ignore_errors=True)
    return out


def next_cases():
    """chapter_state() must terminate on verdict.md (#028). Before this fixture,
    a refined chapter reported "verdict" forever - nothing in this house ever
    wrote runs/chNN/verdict.md, so the oracle could never advance past it, even
    with a later chapter fully refined beside it."""
    import next as next_mod
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-chapter-")
    try:
        for name in ("interview.md", "research.md", "draft.md", "refined.md"):
            open(os.path.join(tmp, name), "w").close()
        stage, cmd, detail = next_mod.chapter_state(12, tmp)
        out.append((stage == "verdict", "next chapter_state, no verdict.md",
                    "a fully refined chapter with no verdict.md must still report verdict",
                    stage))

        open(os.path.join(tmp, "verdict.md"), "w").close()
        stage, cmd, detail = next_mod.chapter_state(12, tmp)
        out.append((stage == "shipped" and cmd is None, "next chapter_state, verdict.md present",
                    "a chapter with a recorded verdict must report shipped, not verdict, "
                    "so a later chapter can surface as next",
                    stage))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def staged_link_cases():
    """okf_gate.py must catch a runs/chNN/okf/ link written with the shadow-tree
    prefix (#029: 5 of Ch12's 23 staged citations carried 9 such links, caught
    only by the Publisher's eye before landing)."""
    import okf_gate
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-repo-")
    try:
        bad_dir = os.path.join(tmp, "runs", "ch99", "okf", "citations")
        os.makedirs(bad_dir)
        open(os.path.join(bad_dir, "a.md"), "w").write(
            "See [other](/okf/citations/b.md) for more.\n")
        found = okf_gate.staged_link_defects(tmp)
        out.append((len(found) == 1 and found[0][1] == "](/okf/citations/b.md)",
                    "okf_gate staged link, shadow prefix", "a /okf/citations/ link must be caught",
                    found))

        # A separate tree containing only a clean, book-convention link must
        # report nothing.
        clean_tmp = tempfile.mkdtemp(prefix="gw-tests-repo-clean-")
        try:
            cd = os.path.join(clean_tmp, "runs", "ch98", "okf", "citations")
            os.makedirs(cd)
            open(os.path.join(cd, "a.md"), "w").write("See [other](/citations/b.md).\n")
            found_clean = okf_gate.staged_link_defects(clean_tmp)
        finally:
            shutil.rmtree(clean_tmp, ignore_errors=True)
        out.append((found_clean == [], "okf_gate staged link, book convention",
                    "a /citations/ link (the book's own convention) must not be flagged",
                    found_clean))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def main():
    rows = package_cases() + voice_rules_cases() + next_cases() + staged_link_cases()
    bad = 0
    for ok, what, why, detail in rows:
        print(f"{'[ ok ]' if ok else '[FAIL]'} {what}")
        print(f"        {why}")
        if not ok:
            print(f"        got: {detail}")
            bad += 1
    print(f"\n{len(rows) - bad}/{len(rows)} fixtures pass")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
