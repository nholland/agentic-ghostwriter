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
import glob
import json
import os
import re
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


def resolve_cases():
    """Self must outrank every other source for the book repo.

    Fixtured because the danger is live rather than theoretical: this cloud
    container still exports GW_BOOK_REPO=/opt/playground-260420 from the
    two-repo era, and under the pre-2026-09-19 ordering that variable outranked
    everything. It resolves to nothing today only because the path happens not
    to exist - the day anything creates it, every desk reads the frozen
    archive's constitution, and a desk handed a dead voice spec does not raise,
    it writes to it. Exactly the silent wrong answer resolve_book.py exists to
    prevent, arriving by a new route.

    Four cases: the override loses; the override is still NAMED (an ignored
    override must not be a mystery); discovery is skipped while the book is
    here (with a book in this repo, the only thing a sibling scan can find is
    the wrong book); and the un-migrated path still works, so the fallback was
    reordered rather than destroyed.
    """
    import resolve_book
    out = []
    decoy = _fake_book("# decoy voice spec\n")
    try:
        r = subprocess.run(
            [sys.executable, os.path.join(REPO, "scripts", "resolve_book.py"), "--json"],
            capture_output=True, text=True, env=dict(os.environ, GW_BOOK_REPO=decoy))
        got = json.loads(r.stdout)
        out.append((os.path.realpath(got.get("bookRepo", "")) == os.path.realpath(REPO),
                    "resolve: a stale $GW_BOOK_REPO must not outrank this repo",
                    "the book is here since the migration; an override pointing "
                    "elsewhere must lose, or a desk drafts against a frozen spec",
                    got.get("bookRepo")))
        named = [o["path"] for o in got.get("outranked", [])]
        out.append((any(os.path.realpath(x) == os.path.realpath(decoy) for x in named),
                    "resolve: the outranked book repo is named, not dropped",
                    "an override that loses must be printed, so 'which book did "
                    "that desk read' is never a mystery",
                    named or "not reported"))

        cand = resolve_book.candidates(resolve_book.load_config())
        out.append((not any(w.startswith("discovered") for w, _ in cand),
                    "resolve: no sibling discovery while the book is in this repo",
                    "with book-manifest.json at the root, a sibling scan can only "
                    "find the wrong book",
                    [w for w, _ in cand]))

        # The un-migrated shape: an engine copy with no book-manifest.json at its
        # root. The override must still win there - this reorders the chain, it
        # does not delete it.
        eng = _isolated_engine()
        try:
            r2 = subprocess.run(
                [sys.executable, os.path.join(eng, "scripts", "resolve_book.py"), "--json"],
                capture_output=True, text=True, env=dict(os.environ, GW_BOOK_REPO=decoy))
            got2 = json.loads(r2.stdout)
            out.append((os.path.realpath(got2.get("bookRepo", "")) == os.path.realpath(decoy),
                        "resolve: $GW_BOOK_REPO still wins when the book is NOT here",
                        "an engine checkout with no book of its own must still "
                        "resolve by override, not fail",
                        got2.get("bookRepo")))
        finally:
            shutil.rmtree(eng, ignore_errors=True)
    finally:
        shutil.rmtree(decoy, ignore_errors=True)
    return out


def _fake_bundle():
    """A minimal book with an okf/ bundle: two citations on disk, one of them
    listed in index.md with the WRONG status, the other not listed at all, plus
    a framework row carrying a hand-written gloss that must survive --fix."""
    book = tempfile.mkdtemp(prefix="gw-tests-bundle-")
    root = os.path.join(book, "the-book")
    for d in ("frameworks", "stories", "citations", "signals"):
        os.makedirs(os.path.join(root, "okf", d))
    json.dump({"bookRoot": "the-book", "books": {"the-book": {"title": "test"}}},
              open(os.path.join(book, "book-manifest.json"), "w"))

    def concept(kind, name, title, extra=""):
        open(os.path.join(root, "okf", kind, name), "w", encoding="utf-8").write(
            f"---\ntype: X\ntitle: {title}\n{extra}---\nbody\n")
    concept("citations", "listed-wrong.md", "Listed Wrong", "status: unverified\n")
    concept("citations", "not-listed.md", "Not Listed", "status: verifiable\n")
    concept("frameworks", "kept.md", "Kept")

    open(os.path.join(root, "okf", "index.md"), "w", encoding="utf-8").write(
        "# Index\n\n## Frameworks\n\n"
        "- [Kept](/frameworks/kept.md) — a gloss nobody generated\n\n"
        "## Stories\n\nNone yet.\n\n## Citations\n\n"
        "- [Listed Wrong](/citations/listed-wrong.md) — status: verifiable — anchors Ch3\n\n"
        "## Signals\n\nNone yet.\n")
    return book, root


def okf_index_cases():
    """okf_index.py must see what count-parity cannot, and must not eat prose.

    okf_validate compares counts per type, so a row whose status contradicts the
    concept it points at is invisible to it - thirteen were on 2026-09-19, six
    claiming better evidence than the file carried. The reconciler reports per
    concept. The second half of this matters more: 249 rows in the real index
    carry hand-written annotation that exists nowhere else, so --fix preserving
    a gloss and a shortened title is the property that makes it safe to run."""
    out = []
    book, root = _fake_bundle()
    try:
        def run(*args):
            return subprocess.run(
                [sys.executable, os.path.join(REPO, "scripts", "okf_index.py"),
                 root, *args], capture_output=True, text=True)

        r = run("--json")
        d = json.loads(r.stdout)
        out.append((any(m["name"] == "not-listed.md" for m in d["missing"]),
                    "okf_index: a concept absent from the index is named",
                    "membership drift must be reported per concept, not as a count",
                    d["missing"]))
        out.append((any(x["name"] == "listed-wrong.md" and x["index"] == "verifiable"
                        and x["file"] == "unverified" for x in d["status_mismatch"]),
                    "okf_index: a row whose status contradicts the concept is caught",
                    "count-parity is blind to this, and it is how the index came to "
                    "overstate the evidence for six citations",
                    d["status_mismatch"]))
        out.append((r.returncode == 1,
                    "okf_index: drift exits 1",
                    "okf_gate reads the exit code to raise its warning", r.returncode))

        run("--fix")
        idx = open(os.path.join(root, "okf", "index.md"), encoding="utf-8").read()
        out.append(("— a gloss nobody generated" in idx,
                    "okf_index --fix preserves a hand-written gloss",
                    "249 rows in the real index carry annotation found nowhere else; "
                    "a generator would have deleted every one",
                    idx))
        out.append(("status: unverified — anchors Ch3" in idx,
                    "okf_index --fix rewrites the status and keeps the annotation after it",
                    "the status is derived and must be corrected; the note after it is "
                    "editorial and must not be touched",
                    [l for l in idx.splitlines() if "listed-wrong" in l]))
        out.append(("](/citations/not-listed.md)" in idx,
                    "okf_index --fix appends the missing concept",
                    "the 23 Ch12 citations that landed with the migration were absent "
                    "from the index for a day", None))
        out.append((run("--json").returncode == 0,
                    "okf_index: a reconciled bundle exits 0",
                    "the gate must go quiet once the drift is actually gone", None))
    finally:
        shutil.rmtree(book, ignore_errors=True)
    return out


def tombstone_cases():
    """The retired-source guard must flag a live pointer and clear a record.

    Its line-and-inflection version reported all six of its hits as live when
    every one was historical - prose wraps, so the mention and the word clearing
    it land on different lines, and "supersedes"/"migration" were not in the
    list. A guard that cries wolf on a tombstone teaches its reader to edit good
    prose until it goes quiet, which is the damage it exists to prevent. Both
    directions are fixtured, because loosening it is how the hole it was built
    for (a draft command routing new author IP into the dead file) reopens."""
    import subprocess as sp
    out = []
    book, root = _fake_bundle()
    try:
        def refs():
            r = sp.run([sys.executable, os.path.join(REPO, "scripts", "okf_validate.py"),
                        "the-book"], cwd=book, capture_output=True, text=True)
            return (r.stdout or "") + (r.stderr or "")

        live = os.path.join(root, "governance.md")
        open(live, "w", encoding="utf-8").write(
            "# Draft\n\nStep 7: append new frameworks to sources/evidence-library.md.\n")
        out.append(("governance.md" in refs(),
                    "tombstone guard: a live pointer to the retired file flags",
                    "the hole this guard exists for - a draft step routing the author's "
                    "own IP into a dead file - must still be caught",
                    refs()[:200]))
        os.remove(live)

        # The loosening's own hole, pinned. "has been" was in the clearing list
        # for a day and cleared this decoy silently, while the control - the same
        # sentence without those two words - flagged. A tightened check is proved
        # by its own fixture; a loosened one is only proved by the thing it must
        # still catch, so the live pointer is fixtured once per phrase that could
        # excuse it.
        for tag, body in (
            ("hasbeen", "Step 7: when new author IP has been gathered, append it "
                        "to sources/evidence-library.md."),
            ("nolonger", "Step 7: append new author IP to sources/evidence-library.md. "
                         "Drafts are no longer collected anywhere else."),
            ("insteadof", "Step 7: append new author IP to sources/evidence-library.md "
                          "instead of leaving it in the transcript."),
            ("usedto", "Step 7: append new author IP to sources/evidence-library.md, "
                       "as we used to for interviews."),
            ("drawnfrom", "Step 7: append new author IP drawn from the interview to "
                          "sources/evidence-library.md."),
            ("faithfully", "Step 7: faithfully append new author IP to "
                           "sources/evidence-library.md."),
        ):
            d = os.path.join(root, f"decoy-{tag}.md")
            open(d, "w", encoding="utf-8").write(f"# Draft\n\n{body}\n")
            out.append((f"decoy-{tag}.md" in refs(),
                        f"tombstone guard: a live pointer is not excused by '{tag}'",
                        "ordinary English in the clearing list silently cleared a "
                        "pointer of the exact shape this guard exists for",
                        refs()[:200]))
            os.remove(d)

        # The teeth must not depend on the word list at all. Every clearing stem
        # in turn, inside a real routing instruction: each one cleared this
        # before ROUTE existed - including retir and migrat, which were in the
        # original list from the start - so this is the case that makes the
        # guard's purpose independent of its vocabulary.
        for stem, body in (
            ("retir", "Step 7: append new author IP to sources/evidence-library.md "
                      "before retiring the draft."),
            ("migrat", "Step 7: when migrating an interview, append the new IP to "
                       "sources/evidence-library.md."),
            ("theold", "Step 7: append new author IP to sources/evidence-library.md, "
                       "the same way the old pipeline did."),
            ("correct", "Step 7: append the correct framework text to "
                        "sources/evidence-library.md."),
            ("deriv", "Step 7: append derived claims to sources/evidence-library.md."),
            ("replac", "Step 7: append new author IP to sources/evidence-library.md, "
                       "replacing any older draft."),
            ("supersed", "Step 7: append new author IP to sources/evidence-library.md, "
                         "superseding the transcript."),
        ):
            d = os.path.join(root, f"route-{stem}.md")
            open(d, "w", encoding="utf-8").write(f"# Draft\n\n{body}\n")
            out.append((f"route-{stem}.md" in refs(),
                        f"tombstone guard: a routing instruction flags regardless of '{stem}'",
                        "the guard's teeth must not depend on which words happen to "
                        "surround the pointer; every stem here cleared it before",
                        refs()[:200]))
            os.remove(d)

        hist = os.path.join(root, "history.md")
        open(hist, "w", encoding="utf-8").write(
            "# Notes\n\nThe bundle supersedes `sources/evidence-library.md`, which\n"
            "has been replaced with a tombstone pointing here.\n")
        out.append(("history.md" not in refs(),
                    "tombstone guard: a paragraph that records the retirement does not flag",
                    "the mention and the word clearing it land on different lines once "
                    "prose wraps; matching a single line reported six tombstones as live",
                    refs()[:200]))
        os.remove(hist)
    finally:
        shutil.rmtree(book, ignore_errors=True)
    return out


def chapter_slug_cases():
    """A titled Introduction/Conclusion heading yields a usable slug.

    'the-man-without-a-blueprint' is a real chapter - "## Introduction: The Man
    Without a Blueprint" - and the checker called it an orphan because it
    slugified only '## Chapter N:' headings. The repair such a warning invites
    is to damage good data until the check goes quiet, so the fixture pins the
    checker instead."""
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import importlib
    v = importlib.import_module("okf_validate")
    tmp = tempfile.mkdtemp(prefix="gw-tests-outline-")
    try:
        open(os.path.join(tmp, "03-outline.md"), "w", encoding="utf-8").write(
            "## Introduction: The Man Without a Blueprint\n\n"
            "## Chapter 1: The Three-Second Window\n\n"
            "## Conclusion: The Blueprint\n")
        slugs = v.valid_chapter_slugs(tmp)
        return [
            ("the-man-without-a-blueprint" in slugs,
             "chapter slugs: a titled Introduction resolves",
             "a real chapter was reported as an orphan slug", sorted(slugs)),
            ("the-blueprint" in slugs,
             "chapter slugs: a titled Conclusion resolves",
             "same hole, same shape, one heading further down", sorted(slugs)),
            ("the-three-second-window" in slugs,
             "chapter slugs: numbered chapters still resolve",
             "the fix must not cost the behaviour that already worked", sorted(slugs)),
        ]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def freshness_cases():
    """resolve_book must say how stale this checkout is, and never stay silent.

    A session opened nine commits behind a main that already held the migration,
    resolved the book to the frozen archive, and reported "11 of 29 shipped" to
    the author as live state. LEARNINGS records the same shape twice before, once
    at 79 commits behind. The hook's guard is silent for up-to-date and for
    could-not-fetch alike, so the two states that must never look the same did.
    Both are pinned here: a behind count reported, and UNVERIFIED said out loud
    when there is nothing to compare against."""
    import resolve_book, subprocess as sp
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-fresh-")
    try:
        def git(repo, *a):
            return sp.run(["git", "-C", repo, *a], capture_output=True, text=True)
        up = os.path.join(tmp, "up")
        os.makedirs(up)
        git(up, "init", "-q", "-b", "main")
        open(os.path.join(up, "f"), "w").write("1")
        git(up, "add", "-A"); git(up, "-c", "user.email=t@t", "-c", "user.name=t",
                                  "commit", "-qm", "one")
        dn = os.path.join(tmp, "down")
        sp.run(["git", "clone", "-q", up, dn], capture_output=True, text=True)
        open(os.path.join(up, "f"), "w").write("2")
        git(up, "add", "-A"); git(up, "-c", "user.email=t@t", "-c", "user.name=t",
                                  "commit", "-qm", "two")
        git(dn, "fetch", "-q", "origin")

        fr = resolve_book.freshness(dn)
        out.append((fr["known"] and fr["behind"] == 1,
                    "freshness: a checkout behind origin/main says how far",
                    "a session nine commits behind reported the frozen archive's "
                    "state to the author as live", fr))

        bare = os.path.join(tmp, "nogit")
        os.makedirs(bare)
        fr2 = resolve_book.freshness(bare)
        out.append((not fr2["known"] and bool(fr2.get("why")),
                    "freshness: nothing to compare against reports UNVERIFIED with a reason",
                    "the hook printed nothing for up-to-date and for could-not-fetch "
                    "alike; the two states must never look the same", fr2))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def migrated_dep_cases():
    """The one check that gates every desk's prose must itself be proved.

    resolve_book reports a REQUIRED migrated dependency missing and exits 1 -
    without scripts/okf_validate.py no desk may write prose. The failure mode of
    breaking it is silent: a missed call site in a key rename makes cfg.get()
    return {}, the check a no-op, and the suite stays green while the line that
    says "migrated deps: 1/1 required" simply stops printing."""
    out = []
    book = _fake_book("# voice\n")
    try:
        os.makedirs(os.path.join(book, "scripts"), exist_ok=True)
        for rel in ("00-premise.md", "03-outline.md"):
            open(os.path.join(book, "the-book", rel), "w").close()
        # An ISOLATED engine copy, not this repo: since the cutover self outranks
        # $GW_BOOK_REPO, so a decoy can only win where the engine holds no book
        # of its own. That is the same shape resolve_cases() pins from the other
        # side, and it is why this fixture cannot simply export the variable.
        eng = _isolated_engine()
        try:
            r = subprocess.run(
                [sys.executable, os.path.join(eng, "scripts", "resolve_book.py")],
                capture_output=True, text=True, env=dict(os.environ, GW_BOOK_REPO=book))
        finally:
            shutil.rmtree(eng, ignore_errors=True)
        said = "REQUIRED migrated dependency missing" in r.stdout and "okf_validate.py" in r.stdout
        out.append((said and r.returncode == 1,
                    "migrated deps: a missing required dependency is named and exits 1",
                    "this is the check that stops a desk writing prose with no citation "
                    "validator; a silent no-op here is invisible to every other fixture",
                    (r.returncode, r.stdout[-200:])))
    finally:
        shutil.rmtree(book, ignore_errors=True)
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


def streak_cases():
    """next.py must count how long NEXT_ACTION has stood still, from the log.

    Derived from runs/log.md's own 'Next:' lines, so there is no counter to go
    stale. Pinned in both directions: a run of identical Next lines counts, and
    a different one breaks the streak rather than being ignored."""
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import importlib, next as next_mod
    importlib.reload(next_mod)

    def _streak(cmd):
        # Tolerant of both return shapes so tests/prove.py can revert
        # next.py to before next_action_streak returned a tuple and still
        # get a clean [FAIL] on the case that actually differs, instead of
        # every case in this function crashing before it's reached - the
        # exact #048-shaped gap this fixture would otherwise fall into.
        r = next_mod.next_action_streak(cmd)
        return r if isinstance(r, tuple) else (r, 0)

    tmp = tempfile.mkdtemp(prefix="gw-tests-streak-")
    out = []
    try:
        os.makedirs(os.path.join(tmp, "runs"))
        entries = ["\n## e1\n\n**Next:** `/gw 5` — x\n",
                   "\n## e2\n\n**Next:** `/gw 13` — x\n",
                   "\n## e3\n\n**Next:** `/gw 13` — x\n",
                   "\n## e4\n\n**Next:** `/gw 13` — x\n"]
        open(os.path.join(tmp, "runs", "log.md"), "w", encoding="utf-8").write(
            "# Session log\n" + "".join(entries))
        real = next_mod.REPO
        next_mod.REPO = tmp
        try:
            three, three_gap = _streak("/gw 13")
            broken, broken_gap = _streak("/gw 5")
        finally:
            next_mod.REPO = real
        out.append((three == 3 and three_gap == 0, "next: NEXT_ACTION streak counts consecutive log entries",
                    "two consecutive reviews counted this by hand before a script owned it",
                    (three, three_gap)))
        out.append((broken == 0, "next: a different Next line breaks the streak",
                    "the count must be consecutive-from-the-end, not a total, or it "
                    "reports staleness that ended sessions ago", broken))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # A malformed entry (no Next: line - a concurrent merge into one shared
    # runs/log.md stripped it from two real entries on 2026-09-19, caught
    # 2026-09-20) must be skipped, not read as a change of direction. The gap
    # sits BETWEEN two matching entries, not next to a real direction change
    # (found 2026-09-20, reviewing this exact fix: the first version of this
    # case placed the gap next to a genuine /gw 5 entry, so break-on-missing
    # and skip-on-missing returned the identical (2, 1) either way - break
    # stops at the gap, and continuing to /gw 5 would have stopped the very
    # next entry regardless. Reverting `continue` to `break` left the suite
    # at 97/97 with this case still [ ok ]. This shape only agrees if the
    # skip logic is actually exercised.)
    tmp2 = tempfile.mkdtemp(prefix="gw-tests-streak-gap-")
    try:
        os.makedirs(os.path.join(tmp2, "runs"))
        entries = ["\n## e0\n\n**Next:** `/gw 13` — x\n",
                   "\n## e1\n\n**Next:** `/gw 13` — x\n",
                   "\n## e2 (malformed, no Next line)\n- `some/file.py`\n",
                   "\n## e3\n\n**Next:** `/gw 13` — x\n",
                   "\n## e4\n\n**Next:** `/gw 13` — x\n"]
        open(os.path.join(tmp2, "runs", "log.md"), "w", encoding="utf-8").write(
            "# Session log\n" + "".join(entries))
        real = next_mod.REPO
        next_mod.REPO = tmp2
        try:
            skip, skip_gap = _streak("/gw 13")
        finally:
            next_mod.REPO = real
        out.append((skip == 4 and skip_gap == 1,
                    "next: a malformed log entry is skipped, not read as a direction change",
                    "e2 has no Next line, sits between two real /gw 13 entries on both sides, and must not break the streak - the true streak is e0+e1+e3+e4=4, with 1 entry unreadable",
                    (skip, skip_gap)))
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)
    return out


def log_check_cases():
    """runs/log.md's invariants, both directions.

    Two hand-resolved merges damaged the log before anything noticed - one
    dropped 26 entries whole, one detached a 30-file body - and both commit
    messages asserted the result was complete. The only check that ran was
    `grep -c '<<<<<<<'`, which both bad merges pass. These cases measure against
    a known-right answer instead, which is the only thing that would have caught
    either."""
    import importlib, log_check
    importlib.reload(log_check)
    out = []
    good = ("# Session log\n"
            "\n## 2026-09-20 10:00 — `b` — 1 commit(s) this session\n"
            "- `a.py`\n\n**Next:** `/gw 13` — x\n"
            "\n## 2026-09-20 10:05 — `b` — 2 commit(s) this session\n"
            "- `c.py`\n\n**Next:** `/gw 13` — x\n")
    out.append((log_check.structure_breaches(good) == [],
                "log_check: an intact log reports no structure breach",
                "the check must not cry wolf on a healthy log, or it teaches its "
                "reader to ignore it", log_check.structure_breaches(good)))

    nobody = good.replace("- `a.py`\n", "")
    b = log_check.structure_breaches(nobody)
    out.append((len(b) == 1 and b[0]["files"] == 0,
                "log_check: an entry with no file list is caught",
                "a detached body is what merge bd3a334 produced and grep could not see", b))

    twonext = good.replace("- `c.py`\n\n**Next:** `/gw 13` — x\n",
                           "- `c.py`\n\n**Next:** `/gw 13` — x\n**Next:** `/gw 13` — x\n")
    b2 = log_check.structure_breaches(twonext)
    out.append((len(b2) == 1 and b2[0]["next_lines"] == 2,
                "log_check: an entry with two Next lines is caught",
                "two bodies concatenated under one heading is the other half of "
                "the same merge damage", b2))

    # Two sessions finishing in the same minute on different branches is real
    # (2026-09-14 14:11). Keying on the timestamp would collapse them and let a
    # lost entry hide behind a survivor.
    same_minute = ("# Session log\n"
                   "\n## 2026-09-20 10:00 — `one` — 1 commit(s) this session\n"
                   "- `a.py`\n\n**Next:** `/gw 13` — x\n"
                   "\n## 2026-09-20 10:00 — `two` — 1 commit(s) this session\n"
                   "- `b.py`\n\n**Next:** `/gw 13` — x\n")
    out.append((len(log_check.entries(same_minute)) == 2,
                "log_check: two sessions in the same minute are distinct entries",
                "keying on the timestamp collapses them, and a genuinely lost "
                "entry would hide behind a same-minute survivor",
                len(log_check.entries(same_minute))))

    # The exemption set must not be a timestamp. Its first version was, matched
    # with head[:16], which would have excused any session finishing in that
    # minute on any branch - and the 26-entry restore made exactly that mistake
    # one level down, leaving nine entries behind. Both halves are pinned: a
    # real legacy entry stays exempt, and a same-minute impostor does not.
    legacy = sorted(log_check.LEGACY_MALFORMED)[0]
    ts = legacy[:16]
    exempt_real = ("# Session log\n\n## " + legacy + "\n\n")
    impostor = ("# Session log\n\n## " + ts +
                " — `other-branch` — 1 commit(s) this session\n\n")
    out.append((log_check.structure_breaches(exempt_real) == [],
                "log_check: a proven legacy entry stays exempt",
                "it was malformed where it was written, in every commit that "
                "carries it; failing on it would teach its reader to ignore the check",
                log_check.structure_breaches(exempt_real)))
    out.append((len(log_check.structure_breaches(impostor)) == 1,
                "log_check: a bare timestamp must not exempt another session in the same minute",
                "the exemption is keyed on the whole heading line; keyed on the "
                "timestamp it excuses any branch that finished in that minute",
                log_check.structure_breaches(impostor)))
    return out


def inbox_cases():
    """--chapter must filter on read (2026-09-18: it was accepted, exited 0, and
    printed every item under a header claiming the whole inbox's counts - a
    desk asking what one chapter raised got a plausible answer covering all
    30 items, no error. That silent miss produced three disagreeing counts for
    Chapter 12 in one commit before this fixture existed). Isolated: a fake
    scripts/+inbox/ copy, never the tracked inbox/, so this does not depend
    on - or drift with - the real inbox's contents."""
    import subprocess as sp
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-inbox-")
    try:
        shutil.copytree(os.path.join(REPO, "scripts"), os.path.join(tmp, "scripts"))
        idir = os.path.join(tmp, "inbox")
        os.makedirs(idir)
        items = [
            ("001", "12", "open"), ("002", "0", "open"),
            ("003", "12", "resolved"), ("004", "7", "resolved"),
        ]
        for iid, ch, status in items:
            open(os.path.join(idir, f"{iid}-fixture.md"), "w").write(
                f"---\nid: {iid}\nstatus: {status}\nraised_by: fixture\n"
                f"chapter: {ch}\nopened: 2026-01-01 00:00\n---\n# fixture {iid}\n")

        def run(*args):
            r = sp.run([sys.executable, os.path.join(tmp, "scripts", "inbox.py"), *args],
                       capture_output=True, text=True)
            return json.loads(r.stdout) if r.stdout.strip().startswith("{") else None

        d = run("--all", "--json", "--chapter", "12")
        got = sorted(i["id"] for k in ("open", "ruled", "resolved") for i in (d or {}).get(k, []))
        out.append((got == ["001", "003"], "inbox --chapter filters on read",
                    "--chapter 12 must return only the two chapter-12 fixtures",
                    got))

        d_all = run("--all", "--json")
        got_all = sorted(i["id"] for k in ("open", "ruled", "resolved") for i in (d_all or {}).get(k, []))
        out.append((got_all == ["001", "002", "003", "004"], "inbox --all with no --chapter, unfiltered",
                    "omitting --chapter must still return every fixture", got_all))

        def run_raw(*args):
            r = sp.run([sys.executable, os.path.join(tmp, "scripts", "inbox.py"), *args],
                       capture_output=True, text=True)
            return r.returncode, r.stdout

        # gw-retro items without --applied-by: 8 of the first 18 landed with no
        # proof command because --add silently dropped the flag and nothing
        # forced the desk (or the Publisher relaying it) to notice.
        common = ["--context", "c", "--unblocks", "u", "--recommend", "r", "--evidence", "e"]
        rc, _ = run_raw("--add", "no proof cmd", "--raised-by", "gw-retro", "--chapter", "0", *common)
        out.append((rc == 2, "inbox refuses a gw-retro item with no --applied-by",
                    "gw-retro's own brief requires ending every proposal this way",
                    rc))

        rc2, out2 = run_raw("--add", "has proof cmd", "--raised-by", "gw-retro", "--chapter", "0",
                            *common, "--applied-by", "true")
        new_id = out2.strip().split("-> ")[-1].split("/")[-1].split("-")[0] if "-> " in out2 else None
        carried = False
        if new_id:
            path = glob.glob(os.path.join(idir, f"{new_id}-*.md"))
            if path:
                carried = "applied_by: true" in open(path[0]).read()
        out.append((rc2 == 0 and carried, "inbox --add records --applied-by in frontmatter",
                    "a gw-retro proposal's proof command must survive into the item, not require --close to repeat it",
                    (rc2, carried)))

        # --close with no --applied-by must fall back to what --add already
        # wrote, rather than silently dropping it (the exact miss that left
        # #033/#034 with no proof command on their closed items).
        if new_id:
            rc3, out3 = run_raw("--close", str(int(new_id)), "--resolution", "fixture close")
            text = open(glob.glob(os.path.join(idir, f"{new_id}-*.md"))[0]).read()
            out.append((rc3 == 0 and "applied_by: true" in text and "status: resolved" in text,
                        "inbox --close carries forward an item's own --applied-by",
                        "closing without repeating --applied-by must not lose the proof command --add already recorded",
                        text))

        # --close must not crash on an --applied-by containing a backslash-
        # digit sequence (e.g. a sed capture group), which re.sub's
        # replacement argument otherwise parses as its own backreference
        # (found 2026-09-20, closing #049: the exact shape of --applied-by a
        # data-repair fix naturally reaches for).
        rc_bs, out_bs = run_raw("--add", "backref shaped proof", "--raised-by", "gw-retro",
                                "--chapter", "0", *common, "--applied-by",
                                r"test $(ls | sed -n 's/\(a\)/\1/p') -eq x")
        bs_id = out_bs.strip().split("-> ")[-1].split("/")[-1].split("-")[0] if "-> " in out_bs else None
        rc_bs2, out_bs2 = (None, None)
        if bs_id:
            rc_bs2, out_bs2 = run_raw("--close", str(int(bs_id)), "--resolution", "fixture close")
        out.append((bs_id is not None and rc_bs2 == 0,
                    "inbox --close survives a backreference-shaped --applied-by",
                    "re.sub's replacement must be a function, not an f-string, or a sed-capture-group proof command crashes do_close outright",
                    (rc_bs, rc_bs2, out_bs2)))

        # A gw-retro item proved by tests/run.py must show --prove-* flags -
        # see prove_cases() for the full red/green enforcement, which needs
        # its own git repo and is kept separate from this function's
        # git-less fixture.
        rc4, _ = run_raw("--add", "unproven proof", "--raised-by", "gw-retro", "--chapter", "0",
                         *common, "--applied-by", "python3 tests/run.py")
        out.append((rc4 == 2, "inbox refuses a gw-retro tests/run.py proof with no --prove-* flags",
                    "a claim of having run something red is not proof of it - tests/prove.py must be pointed at what to check",
                    rc4))

        # The --prove-* requirement must not be opt-out via --raised-by - #050
        # was filed raised_by: Publisher with a flagless tests/run.py proof
        # and shipped a fixture that turned out to be blind to its own bug.
        rc5, _ = run_raw("--add", "unproven proof, not gw-retro", "--raised-by", "Publisher",
                         "--chapter", "0", *common, "--applied-by", "python3 tests/run.py")
        out.append((rc5 == 2, "inbox refuses a flagless tests/run.py proof regardless of raised_by",
                    "a guard keyed on a string the filer chooses is opt-out by construction",
                    rc5))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def prove_cases():
    """tests/prove.py and inbox.py's integration with it, proved against a
    synthetic git repo whose 'buggy' commit genuinely fails a case and whose
    'fixed' commit genuinely passes it - not the real repo's own history, so
    this does not depend on any specific commit staying reachable.

    #041's first version accepted a typed "[FAIL]" substring in --evidence as
    proof a case was watched fail - an attestation, not a measurement, and
    demonstrably gameable (an item whose evidence read "I did not run
    anything. [FAIL] is a string I typed." was accepted, exit 0). This
    replaces that with tests/prove.py actually running the red pass."""
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-prove-")
    try:
        _git(tmp, "init", "-q")
        _git(tmp, "config", "user.email", "test@example.com")
        _git(tmp, "config", "user.name", "test")
        os.makedirs(os.path.join(tmp, "tests"))
        shutil.copy(os.path.join(REPO, "tests", "prove.py"), os.path.join(tmp, "tests", "prove.py"))
        # A minimal harness in the same [ ok ]/[FAIL] format tests/prove.py
        # parses, checking one thing: whether target.py contains a marker.
        open(os.path.join(tmp, "tests", "run.py"), "w").write(
            "import os\n"
            "HERE = os.path.dirname(os.path.abspath(__file__))\n"
            "REPO = os.path.dirname(HERE)\n"
            "content = open(os.path.join(REPO, 'target.py')).read()\n"
            "ok = 'FIXED' in content\n"
            "print(f\"{'[ ok ]' if ok else '[FAIL]'} target has the fix\")\n")
        open(os.path.join(tmp, "target.py"), "w").write("# buggy\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "buggy")
        buggy_sha = _git_out(tmp, "rev-parse", "HEAD")
        open(os.path.join(tmp, "target.py"), "w").write("# buggy\n# FIXED\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "fixed")
        fixed_sha = _git_out(tmp, "rev-parse", "HEAD")

        prove = os.path.join(tmp, "tests", "prove.py")
        r_ok = subprocess.run([sys.executable, prove, "--file", "target.py", "--at", buggy_sha,
                              "--case", "target has the fix"], cwd=tmp, capture_output=True, text=True)
        out.append((r_ok.returncode == 0 and "PROVED" in r_ok.stdout,
                    "prove.py PROVES a case that genuinely fails at the given commit",
                    "reverting target.py to the buggy commit must show [FAIL], then [ ok ] on the current tree",
                    (r_ok.returncode, r_ok.stdout)))

        r_bad = subprocess.run([sys.executable, prove, "--file", "target.py", "--at", buggy_sha,
                               "--case", "no such case"], cwd=tmp, capture_output=True, text=True)
        out.append((r_bad.returncode == 2 and "REFUSED" in r_bad.stdout,
                    "prove.py refuses a case name that never appears",
                    "a typo'd or nonexistent case name must not silently pass",
                    (r_bad.returncode, r_bad.stdout)))

        wt_list = subprocess.run(["git", "worktree", "list"], cwd=tmp, capture_output=True, text=True).stdout
        out.append((wt_list.strip().count("\n") == 0, "prove.py removes its worktree after running",
                    "a leaked worktree would accumulate across every gw-retro proposal that uses this",
                    wt_list))

        # inbox.py's own integration: copy it in and drive it against this
        # same synthetic repo.
        os.makedirs(os.path.join(tmp, "scripts"))
        shutil.copy(os.path.join(REPO, "scripts", "inbox.py"), os.path.join(tmp, "scripts", "inbox.py"))
        os.makedirs(os.path.join(tmp, "inbox"))
        common = ["--context", "c", "--unblocks", "u", "--recommend", "r", "--evidence", "e"]

        def run_add(*extra):
            r = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "inbox.py"), "--add",
                               "x", "--raised-by", "gw-retro", "--chapter", "0", *common,
                               "--applied-by", "python3 tests/run.py", *extra],
                               cwd=tmp, capture_output=True, text=True)
            return r.returncode, r.stdout

        rc_refused, out_refused = run_add("--prove-file", "target.py", "--prove-at", buggy_sha,
                                          "--prove-case", "no such case")
        out.append((rc_refused == 2, "inbox refuses when tests/prove.py refuses",
                    "a case that does not actually discriminate must not close a gw-retro item",
                    (rc_refused, out_refused)))

        rc_proved, out_proved = run_add("--prove-file", "target.py", "--prove-at", buggy_sha,
                                        "--prove-case", "target has the fix")
        out.append((rc_proved == 0, "inbox accepts when tests/prove.py proves the case",
                    "a genuinely discriminating case must be accepted, not just any [FAIL]-shaped text",
                    (rc_proved, out_proved)))

        # Half (a): git worktree add checks out HEAD, blind to uncommitted
        # work - a case whose check exists only in the live, uncommitted
        # tests/run.py must still be provable, or the only triples that can
        # ever pass are older committed ones unrelated to whatever is
        # actually being proposed (found 2026-09-19: an unrelated "adopt a
        # mascot" item was accepted this way, reusing prove.py's own real,
        # older, unrelated worked example). target2.py's no-marker baseline is
        # committed (--at needs a real commit to revert to); the marker and
        # the case that checks for it are added only as uncommitted edits.
        open(os.path.join(tmp, "target2.py"), "w").write("# no second fix\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "target2 baseline")
        target2_base_sha = _git_out(tmp, "rev-parse", "HEAD")

        # The synthetic tests/run.py is a plain script (not this real file's
        # main()/rows structure), so the appended case must call and print
        # itself directly.
        open(os.path.join(tmp, "tests", "run.py"), "a").write(
            "\n\ncontent2 = open(os.path.join(REPO, 'target2.py')).read()\n"
            "ok2 = 'SECOND' in content2\n"
            "print(f\"{'[ ok ]' if ok2 else '[FAIL]'} target2 has the second fix\")\n")
        # Neither target2.py's marker nor this tests/run.py edit is committed
        # yet - both stay live, uncommitted changes for the next check.
        open(os.path.join(tmp, "target2.py"), "w").write("# no second fix\n# SECOND\n")

        r_uncommitted = subprocess.run([sys.executable, prove, "--file", "target2.py",
                                        "--at", target2_base_sha, "--case", "target2 has the second fix"],
                                       cwd=tmp, capture_output=True, text=True)
        out.append((r_uncommitted.returncode == 0 and "PROVED" in r_uncommitted.stdout,
                    "prove.py proves a case whose check exists only in uncommitted tests/run.py",
                    "without copying the live tree's dirty paths into the worktree, this reports REFUSED - case not found, not PROVED",
                    (r_uncommitted.returncode, r_uncommitted.stdout)))

        # Half (b): a --prove-case must be new within this session's review
        # window, not a case that already existed before it - otherwise any
        # older, unrelated, genuinely-discriminating case can be reused to
        # close an item proving nothing about it.
        os.makedirs(os.path.join(tmp, ".claude", "state"))
        open(os.path.join(tmp, ".claude", "state", "retro-window"), "w").write(f"{buggy_sha} {fixed_sha}")

        rc_stale, out_stale = run_add("--prove-file", "target.py", "--prove-at", buggy_sha,
                                      "--prove-case", "target has the fix")
        out.append((rc_stale == 2 and "already existed at the window start" in out_stale,
                    "inbox refuses a --prove-case that predates the review window",
                    "a case present before this session's window proves nothing about what this item proposes",
                    (rc_stale, out_stale)))

        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "third: add target2 case")
        rc_fresh, out_fresh = run_add("--prove-file", "target2.py", "--prove-at", target2_base_sha,
                                      "--prove-case", "target2 has the second fix")
        out.append((rc_fresh == 0, "inbox accepts a --prove-case genuinely new within the window",
                    "the window-start guard must not block a case that is actually about this window's change",
                    (rc_fresh, out_fresh)))

        # An unreadable window (present but pointing at a commit tests/run.py
        # can't be read from) used to skip the freshness check with no
        # output at all - the exact input that broke it. This does not close
        # the hole (see prove.py's WHAT THIS DOES NOT DO); it only makes the
        # skip visible instead of silent.
        open(os.path.join(tmp, ".claude", "state", "retro-window"), "w").write(
            "0000000000000000000000000000000000000000 " + fixed_sha)
        rc_note, out_note = run_add("--prove-file", "target2.py", "--prove-at", target2_base_sha,
                                    "--prove-case", "target2 has the second fix")
        out.append(("NOTE - could not read tests/run.py at the window start" in out_note,
                    "inbox says the freshness check did not run when the window is unreadable",
                    "a check that cannot see must say so, not pass in silence - the prior behaviour accepted an unrelated item with no warning printed at all",
                    (rc_note, out_note)))
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


def session_log_dedup_cases():
    """session_log.py's diff is cumulative from session-start-sha, so a Stop
    with no new work commit since the last entry reproduces the same file set
    verbatim - 39 of 117 real entries were exactly this before the dedup guard
    existed, most from the retro dispatch's own forced second Stop. Proves the
    fix against a real git repo and a real second run, not a grep for the
    guard's text."""
    out = []
    tmp = tempfile.mkdtemp(prefix="gw-tests-log-")
    try:
        shutil.copytree(os.path.join(REPO, "scripts"), os.path.join(tmp, "scripts"))
        _git(tmp, "init", "-q")
        _git(tmp, "config", "user.email", "test@example.com")
        _git(tmp, "config", "user.name", "test")
        open(os.path.join(tmp, "README.md"), "w").write("start\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "session start")
        start_sha = _git_out(tmp, "rev-parse", "HEAD")
        state = os.path.join(tmp, ".claude", "state")
        os.makedirs(state)
        open(os.path.join(state, "session-start-sha"), "w").write(start_sha)

        os.makedirs(os.path.join(tmp, "runs"), exist_ok=True)
        open(os.path.join(tmp, "work.py"), "w").write("# work\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "some work")

        # 34 files, deliberately ABOVE the 30 an entry stores. Below that
        # ceiling every earlier fixture in this lineage passed while dedup was
        # dead in real use: the guard compared the whole diff against a list
        # that only ever holds the first 30, so a session big enough to matter
        # could never match. Third miss here (#035, #039, #040), same cause
        # each time - the synthetic case never reached the real sequence.
        for n in range(34):
            open(os.path.join(tmp, f"big{n:02d}.py"), "w").write("# big\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "a session larger than one entry stores")

        script = os.path.join(tmp, "scripts", "session_log.py")
        r1 = subprocess.run([sys.executable, script], cwd=tmp, capture_output=True, text=True)
        log_path = os.path.join(tmp, "runs", "log.md")
        entries1 = open(log_path).read().count("\n## ") if os.path.exists(log_path) else 0
        out.append((entries1 == 1, "session_log writes an entry for real work",
                    "the first run, with a real commit since session start, must append one entry",
                    (r1.stdout, entries1)))

        # No new commit since the last entry: this Stop's diff is the same
        # session-start..HEAD set as before, and must not restate it. The real
        # Stop hook commits runs/log.md itself between runs. NOTE this case
        # alone does NOT exercise the actual #039 defect: entry 1 was written
        # before runs/log.md was ever committed, so entry 1's own file list
        # never contains "runs/log.md" - last_entry_files() returns the same
        # set whether or not it strips that name, because the name was never
        # there to strip. The defect needs a LOGGED entry whose own file list
        # already contains "runs/log.md"; that only happens after a run that
        # writes a new entry while the log is already tracked. Case 4 below
        # builds that state. (Found 2026-09-19: the #039 fix shipped, this
        # case was added and named for the defect, and the fixed fixture still
        # passed unchanged against the pre-fix script - the precondition it
        # claimed to test was never actually built. This case is kept because
        # it is still real - a same-file-set second run must not duplicate -
        # just renamed to what it actually proves.)
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "auto: session log")
        r2 = subprocess.run([sys.executable, script], cwd=tmp, capture_output=True, text=True)
        entries2 = open(log_path).read().count("\n## ") if os.path.exists(log_path) else 0
        out.append((entries2 == 1 and "same file set" in r2.stdout,
                    "session_log skips a same-file-set second run",
                    "a Stop with no new commit since the last entry (the retro dispatch's forced second pass) must not append a duplicate",
                    (r2.stdout, entries2)))

        # A real second commit must still get logged. This run's own entry
        # (entry 2) DOES now contain "runs/log.md" in its file list, because
        # runs/log.md is genuinely part of the cumulative diff by this point -
        # this is the state case 4 needs to exist before it can test anything.
        open(os.path.join(tmp, "work2.py"), "w").write("# work2\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "more work")
        r3 = subprocess.run([sys.executable, script], cwd=tmp, capture_output=True, text=True)
        entries3 = open(log_path).read().count("\n## ") if os.path.exists(log_path) else 0
        out.append((entries3 == 2, "session_log still logs genuinely new work",
                    "the dedup guard must not suppress an entry when the file set actually grew",
                    (r3.stdout, entries3)))

        # The actual #039 case: commit entry 2 (which lists runs/log.md) into
        # git, then run again with no new work. last_entry_files() must strip
        # "runs/log.md" from what it read back, or this compares unequal to
        # this_set (which always strips it) and duplicates - confirmed to
        # reproduce on the pre-fix script (git show c17f979:scripts/session_log.py).
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "auto: session log 2")
        r4 = subprocess.run([sys.executable, script], cwd=tmp, capture_output=True, text=True)
        entries4 = open(log_path).read().count("\n## ") if os.path.exists(log_path) else 0
        out.append((entries4 == 2 and "same file set" in r4.stdout,
                    "session_log dedups when the last entry itself lists runs/log.md",
                    "the #039 defect: last_entry_files() must strip runs/log.md from a logged entry's own file list, not just from the current diff, or the two sets can never match once a real entry has recorded the log file",
                    (r4.stdout, entries4)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def state_ignore_cases():
    """Every path the hooks write under .claude/state/ must be gitignored.
    retro-window was introduced without its line (2026-09-19) and caught only
    because a review happened to run; the same miss on session-start-sha cost
    five empty auto-commits in one day."""
    out = []
    hooks = os.path.join(REPO, ".claude", "hooks")
    src = "".join(open(os.path.join(hooks, h)).read() for h in sorted(os.listdir(hooks)))
    for name in sorted(set(re.findall(r"\$STATE/([A-Za-z0-9_-]+)", src))):
        probe = ".claude/state/" + (name + "probe" if name.endswith("-") else name)
        rc = subprocess.run(["git", "-C", REPO, "check-ignore", "-q", probe],
                            capture_output=True).returncode
        out.append((rc == 0, f"hook state file {probe} is gitignored",
                    "an unignored state file dirties the tree every session and makes empty auto-commits",
                    probe))
    return out


HARDCODED_SYS_PATH = re.compile(
    r"sys\.path\.insert\(\s*0\s*,\s*(['\"])(/[^'\"]*)\1")


def sys_path_hardcode_cases():
    """A hardcoded absolute literal in sys.path.insert() only works by accident
    - whichever container happens to have a stray copy sitting at that exact
    path. runs/design/svgcheck.py did exactly this until 2026-09-19, importing
    ttfwidth.py from a previous session's scratchpad ('/tmp/claude-0/...').
    GAPS.md used to carry that as a sentence telling the next reader to
    remember to check; a fixture does not need remembering."""
    out = []
    tracked = subprocess.run(["git", "-C", REPO, "ls-files", "*.py"],
                             capture_output=True, text=True, check=True).stdout.split()
    offenders = []
    for f in tracked:
        if f.startswith("tests/"):
            continue
        text = open(os.path.join(REPO, f)).read()
        for m in HARDCODED_SYS_PATH.finditer(text):
            offenders.append(f"{f}: {m.group(0)}")
    out.append((offenders == [], "no tracked script hardcodes an absolute sys.path.insert literal",
                "a literal path only works by accident in whichever container happens to hold a stray copy there",
                offenders))

    # Negative control: the pattern must actually catch the shape that broke
    # svgcheck.py, not just pass because today's tree happens to be clean.
    reintroduced = "import sys\nsys.path.insert(0, '/tmp/claude-0')\nfrom ttfwidth import metrics\n"
    caught = bool(HARDCODED_SYS_PATH.search(reintroduced))
    out.append((caught, "the pattern catches the exact bug it was written for",
                "reintroducing svgcheck.py's old hardcoded line must be flagged, or this check is decorative",
                caught))

    clean = "import sys, os\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n"
    not_flagged = not HARDCODED_SYS_PATH.search(clean)
    out.append((not_flagged, "the pattern does not flag the fix itself",
                "the HERE-based idiom every tracked script now uses must not be a false positive",
                not_flagged))
    return out


def toolcheck_cases():
    """toolcheck.py's own two detectors, proved against something real rather
    than trusted by inspection: a module every fixture run already imports
    (os) must report present, and a binary name no real tool will ever have
    must report absent."""
    import toolcheck
    out = []
    out.append((toolcheck.check_python("os") is True, "toolcheck python detector",
                "a stdlib module that is definitely importable must report present",
                toolcheck.check_python("os")))
    out.append((toolcheck.check_binary("a-binary-that-does-not-exist-gw") is False,
                "toolcheck binary detector",
                "a binary name nothing provides must report absent",
                toolcheck.check_binary("a-binary-that-does-not-exist-gw")))
    return out


def _git(repo, *args):
    subprocess.run(["git", "-C", repo] + list(args), check=True,
                    capture_output=True, text=True)


def _git_out(repo, *args):
    return subprocess.run(["git", "-C", repo] + list(args), check=True,
                           capture_output=True, text=True).stdout.strip()


def retro_window_cases():
    """retro-check.sh's dispatch window, proved against a real git repo rather
    than trusted by inspection. #030: the window collapsed to empty once
    because it was read from a variable the same block was about to overwrite;
    that fix closed on a grep for the new variable's name, not on running the
    hook, and the same collapse recurred (found 2026-09-19 reviewing the
    toolcheck commit). This fixture runs the actual hook against a repo it
    controls and checks the window it writes, not the source text."""
    out = []
    hook = os.path.join(REPO, ".claude", "hooks", "retro-check.sh")
    tmp = tempfile.mkdtemp(prefix="gw-tests-retro-")
    try:
        _git(tmp, "init", "-q")
        _git(tmp, "config", "user.email", "test@example.com")
        _git(tmp, "config", "user.name", "test")
        os.makedirs(os.path.join(tmp, "scripts"))
        open(os.path.join(tmp, "scripts", "a.py"), "w").write("# a\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "session start")
        start_sha = _git_out(tmp, "rev-parse", "HEAD")

        state = os.path.join(tmp, ".claude", "state")
        os.makedirs(state)
        open(os.path.join(state, "session-start-sha"), "w").write(start_sha)

        # The triggering commit: touches a watched path (scripts/).
        open(os.path.join(tmp, "scripts", "a.py"), "w").write("# a changed\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "touch scripts/")
        head_sha = _git_out(tmp, "rev-parse", "HEAD")

        env = dict(os.environ)
        env["CLAUDE_PROJECT_DIR"] = tmp
        env.pop("CLAUDE_PLUGIN_ROOT", None)
        r = subprocess.run(["bash", hook], cwd=tmp, env=env,
                            capture_output=True, text=True)
        out.append((r.returncode == 2, "retro-check dispatches on a watched-path commit",
                    "a commit touching scripts/ must trigger exit 2 (Stop hook signal)",
                    r.returncode))

        window_path = os.path.join(state, "retro-window")
        window = open(window_path).read().split() if os.path.exists(window_path) else []
        out.append((window == [start_sha, head_sha], "retro-window written as START HEAD",
                    "the window must span exactly the session-start commit to the triggering commit",
                    window))

        in_window = int(_git_out(tmp, "rev-list", "--count", f"{start_sha}..{head_sha}"))
        out.append((in_window == 1, "triggering commit falls inside its own window",
                    "the commit that caused the dispatch must be counted in the range gw-retro reads",
                    in_window))

        last_sha = open(os.path.join(state, "retro-last-sha")).read().strip()
        out.append((last_sha == head_sha, "retro-last-sha dedupe pointer still advances",
                    "the unrelated dedupe pointer must still land on HEAD",
                    last_sha))

        # Prove the bug this fixture guards against: reading retro-last-sha as
        # the window START (the pre-fix instruction) gives an empty range,
        # because by dispatch time it has already been overwritten to HEAD.
        naive_start = last_sha
        naive_count = int(_git_out(tmp, "rev-list", "--count", f"{naive_start}..{head_sha}"))
        out.append((naive_count == 0, "reading retro-last-sha as START reproduces #030",
                    "confirms retro-window, not retro-last-sha, is what must be read for the window",
                    naive_count))

        # A second watched-path commit should open a fresh window starting
        # where the first one ended, not from session-start-sha again.
        open(os.path.join(tmp, "scripts", "b.py"), "w").write("# b\n")
        _git(tmp, "add", "-A")
        _git(tmp, "commit", "-q", "-m", "touch scripts/ again")
        head2_sha = _git_out(tmp, "rev-parse", "HEAD")
        r2 = subprocess.run(["bash", hook], cwd=tmp, env=env,
                            capture_output=True, text=True)
        window2 = (open(window_path).read().split()
                   if os.path.exists(window_path) else [])
        out.append((r2.returncode == 2 and window2 == [head_sha, head2_sha],
                    "second dispatch windows from the first dispatch's end",
                    "a later session commit must open a fresh window starting at the prior HEAD, not session-start-sha",
                    (r2.returncode, window2)))

        out.append((f"{start_sha}..{head_sha}" in r.stderr,
                    "dispatch message carries the window range inline",
                    "the range the Publisher actually reads must match the file gw-retro reads, not just agree with it by coincidence",
                    r.stderr))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def main():
    rows = (package_cases() + voice_rules_cases() + resolve_cases()
           + okf_index_cases() + tombstone_cases() + chapter_slug_cases()
           + freshness_cases() + migrated_dep_cases()
           + next_cases() + streak_cases() + log_check_cases() + inbox_cases() + staged_link_cases() + toolcheck_cases()
           + retro_window_cases() + state_ignore_cases()
           + sys_path_hardcode_cases() + session_log_dedup_cases()
           + prove_cases())
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
