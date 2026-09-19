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

        # A gw-retro item proved by tests/run.py must show --prove-* flags -
        # see prove_cases() for the full red/green enforcement, which needs
        # its own git repo and is kept separate from this function's
        # git-less fixture.
        rc4, _ = run_raw("--add", "unproven proof", "--raised-by", "gw-retro", "--chapter", "0",
                         *common, "--applied-by", "python3 tests/run.py")
        out.append((rc4 == 2, "inbox refuses a gw-retro tests/run.py proof with no --prove-* flags",
                    "a claim of having run something red is not proof of it - tests/prove.py must be pointed at what to check",
                    rc4))
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
    rows = (package_cases() + voice_rules_cases() + next_cases()
           + inbox_cases() + staged_link_cases() + toolcheck_cases()
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
