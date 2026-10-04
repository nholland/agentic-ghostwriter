"""Fixtures for scripts/switch_book.py and scripts/distill_status.py.

Each case builds a throwaway repo under a temp dir; nothing here touches the
live manifest or the live book. Rows are (ok, what, why, detail), like the rest
of tests/run.py.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRIPTS = os.path.join(REPO, "scripts")

GOOD_DIST = ("# D\n\n**Mechanism:** m\n\n**Conversation sentence:** c\n\n"
             "**Lesson:** l\n**Challenge:** x\n\n**Practice:**\n1. do it\n")


def _book(root, slug, with_spec=True):
    d = os.path.join(root, "books", slug)
    os.makedirs(d)
    for f in ("00-premise.md", "03-outline.md") + (("01-voice.md",) if with_spec else ()):
        open(os.path.join(d, f), "w").write("x\n")
    return d


def _manifest(root, active, slugs):
    books = {f"books/{s}": {"title": s.title(), "slug": s} for s in slugs}
    # Indented the way the live manifest is, so a text replace is tested for real.
    with open(os.path.join(root, "book-manifest.json"), "w") as fh:
        json.dump({"bookRoot": f"books/{active}", "books": books}, fh, indent=2)
        fh.write("\n")
    return os.path.join(root, "book-manifest.json")


def _run(script, *args):
    r = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def switch_cases():
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        _book(tmp, "one"); _book(tmp, "two"); _book(tmp, "nospec", with_spec=False)
        m = _manifest(tmp, "one", ["one", "two", "nospec", "ghost"])  # ghost: registered, no folder
        before = open(m).read()

        rc, o = _run("switch_book.py", "nope", "--manifest", m)
        out.append((rc == 1 and open(m).read() == before, "switch refuses an unregistered book",
                    "pointing bookRoot at a folder the registry does not know is how a desk runs blind",
                    (rc, o)))
        rc, o = _run("switch_book.py", "ghost", "--manifest", m)
        out.append((rc == 1 and open(m).read() == before, "switch refuses a registered book whose folder is missing",
                    "a registry entry is not a book; the folder must exist", (rc, o)))
        rc, o = _run("switch_book.py", "nospec", "--manifest", m)
        out.append((rc == 1 and open(m).read() == before, "switch refuses a book with no voice spec",
                    "a missing 01-voice.md does not raise later, it produces generic prose", (rc, o)))
        rc, o = _run("switch_book.py", "one", "--manifest", m)
        out.append((rc == 0 and open(m).read() == before, "switching to the active book writes nothing",
                    "idempotent: a no-op must not touch the file", (rc, o)))

        rc, o = _run("switch_book.py", "two", "--manifest", m)
        after = open(m).read()
        diff = [(a, b) for a, b in zip(before.splitlines(), after.splitlines()) if a != b]
        out.append((rc == 0 and json.loads(after)["bookRoot"] == "books/two" and len(diff) == 1
                    and "bookRoot" in diff[0][0] and "FAIL" in o,
                    "switch by slug changes exactly the bookRoot line and warns about the voice mirror",
                    "one value in one file, and the house.json mirror caveat is said at the moment it matters",
                    (rc, diff, o)))
        rc, o = _run("switch_book.py", "books/one", "--manifest", m)
        out.append((rc == 0 and json.loads(open(m).read())["bookRoot"] == "books/one",
                    "switch accepts the books/<slug> path and can switch back",
                    "the registry is keyed by path; both spellings must resolve", (rc, o)))

        rc, o = _run("switch_book.py", "--manifest", m)
        marked = [l for l in o.splitlines() if l.startswith(" *")]
        out.append((rc == 0 and len(marked) == 1 and "books/one" in marked[0], "listing marks exactly the active book",
                    "the author must be able to see which book is live", o))

        dup = open(m).read().replace('"books": {', '"bookRoot": "books/one",\n  "books": {', 1)
        open(m, "w").write(dup)
        snapshot = open(m).read()
        rc, o = _run("switch_book.py", "two", "--manifest", m)
        out.append((rc == 1 and open(m).read() == snapshot, "switch aborts when bookRoot is not unique",
                    "Rule 11: count exact matches, abort if the count is wrong", (rc, o)))
    return out


def distill_cases():
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        git = lambda *a, **k: subprocess.run(["git", "-C", tmp, *a], capture_output=True, text=True,
                                             env=dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                                                      GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t", **k))
        git("init", "-q")
        ch = os.path.join(tmp, "chapters")

        def put(name, refined=True, dist=None):
            d = os.path.join(ch, name)
            os.makedirs(d, exist_ok=True)
            if refined:
                open(os.path.join(d, "refined.md"), "w").write("prose\n")
            if dist is not None:
                open(os.path.join(d, "distillation.md"), "w").write(dist)

        put("ch01", dist=GOOD_DIST)
        put("ch02")  # no distillation
        put("ch03", dist=GOOD_DIST.replace("**Challenge:** x\n", ""))
        put("ch04", dist=GOOD_DIST.replace("1. do it", "no list"))
        put("ch05", dist=GOOD_DIST)
        put("ch07", dist=GOOD_DIST)
        open(os.path.join(ch, "ch07", "refined.md"), "w").write("prose\n\n## Editor's Notes\nold notes\n")
        put("prologue")
        git("add", "-A")
        git("commit", "-q", "-m", "land", "--date=2026-01-01T00:00:00")
        # ch05: refined.md edited in a LATER commit than its distillation.
        open(os.path.join(ch, "ch05", "refined.md"), "w").write("prose, edited\n")
        # ch07: only the Editor's Notes change in the later commit - the ch09 case.
        open(os.path.join(ch, "ch07", "refined.md"), "w").write("prose\n\n## Editor's Notes\nnew notes\n")
        git("add", "-A")
        subprocess.run(["git", "-C", tmp, "commit", "-q", "-m", "edit"], capture_output=True,
                       env=dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                                GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
                                GIT_COMMITTER_DATE="2030-01-01T00:00:00", GIT_AUTHOR_DATE="2030-01-01T00:00:00"))

        rc, o = _run("distill_status.py", "--book-root", tmp, "--repo", tmp)
        lines = {l.split()[0]: l.split()[1] for l in o.splitlines() if l.startswith("  ch")}
        want = {"ch01": "ok", "ch02": "MISSING", "ch03": "MALFORMED", "ch04": "MALFORMED", "ch05": "STALE", "ch07": "ok"}
        out.append((lines == want and rc == 0, "each defect class is named, a notes-only change is not stale, and report mode exits 0",
                    "the report must tell missing, malformed and stale apart; it informs, it does not block",
                    (lines, rc)))
        out.append(("prologue" in o, "a non-chNN folder is named as not read, not silently dropped",
                    "silence about skipped chapters would read as 'all checked'", o))
        rc, o = _run("distill_status.py", "--book-root", tmp, "--repo", tmp, "--strict")
        out.append((rc == 1, "--strict exits 1 when any chapter is flagged", "a caller can gate on it", rc))
        put("ch06", dist=GOOD_DIST)  # never committed
        rc, o = _run("distill_status.py", "--book-root", tmp, "--repo", tmp)
        out.append((rc == 0 and "ch06   UNCHECKED" in o, "an untracked chapter reports UNCHECKED, not a traceback",
                    "no git history is said plainly rather than guessed", o))
    return out


def _inbox_sandbox(tmp, items):
    """A copy of scripts/ beside a throwaway inbox/, never the tracked one."""
    import shutil
    shutil.copytree(os.path.join(REPO, "scripts"), os.path.join(tmp, "scripts"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    idir = os.path.join(tmp, "inbox")
    os.makedirs(idir)
    for iid, kind, status in items:
        extra = "" if kind == "decision" else f"kind: {kind}\ntrigger: when it fires\n"
        open(os.path.join(idir, f"{iid}-fixture.md"), "w").write(
            f"---\nid: {iid}\nstatus: {status}\n{extra}raised_by: fixture\nchapter: 0\n"
            f"opened: 2026-01-01 00:00\n---\n\n# fixture {iid} {kind}\n\nbody\n")
    return idir


def _inbox(tmp, *args):
    r = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "inbox.py"), *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def inbox_kind_cases():
    import importlib.util
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        idir = _inbox_sandbox(tmp, [("001", "decision", "open"), ("002", "parked", "open"),
                                    ("003", "gap", "open"), ("004", "parked", "resolved"),
                                    ("005", "decision", "resolved")])
        rc, o = _inbox(tmp)
        out.append((rc == 0 and "NEEDS YOUR DECISION" in o and "PARKED" in o and "CAPABILITY GAPS" in o
                    and "1 need your decision, 1 parked, 1 gap(s)" in o and "fixture 004" not in o,
                    "the default inbox view shows all three categories with counts, resolved ones hidden",
                    "he asked for one place to look; a category he must ask for by name is a second place",
                    o))
        rc, o = _inbox(tmp, "--kind", "parked")
        out.append((rc == 0 and "fixture 002" in o and "fixture 001" not in o and "fixture 003" not in o,
                    "--kind narrows the view to one category", "the filter must not leak the others", o))
        rc, o = _inbox(tmp, "--kind", "gap", "--json")
        import json
        got = sorted(i["id"] for k in ("open", "ruled", "resolved") for i in json.loads(o).get(k, []))
        out.append((rc == 0 and got == ["003"], "--kind filters the JSON too", "callers read the JSON", got))

        # next.py: only decisions are 'waiting on you'
        spec = importlib.util.spec_from_file_location("gw_next_under_test", os.path.join(REPO, "scripts", "next.py"))
        nx = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(nx)
        nx.REPO = tmp
        op, ru = nx.inbox_counts()
        pk, gp = nx.inbox_other_counts()
        out.append(((op, ru, pk, gp) == (1, 0, 1, 1),
                    "the session banner counts decisions only; parked and gaps are counted apart",
                    "counting a parked item as 'waiting on you' would cry wolf every session",
                    (op, ru, pk, gp)))

        rc, o = _inbox(tmp, "--add", "no trigger", "--kind", "parked", "--context", "c")
        out.append((rc == 2, "a parked item without a trigger is refused",
                    "a deferred thing with no condition for its return is just lost", (rc, o)))
        rc, o = _inbox(tmp, "--add", "with trigger", "--kind", "parked", "--trigger", "at the Ch22 interview",
                       "--context", "c", "--aka", "P-009")
        text = open([os.path.join(idir, f) for f in sorted(os.listdir(idir)) if "with-trigger" in f][0]).read() if rc == 0 else ""
        out.append((rc == 0 and "kind: parked" in text and "trigger: at the Ch22 interview" in text and "aka: P-009" in text,
                    "a parked item needs only a trigger and context, and records its alias",
                    "parking must cost less than deciding", (rc, text)))

        rc, o = _inbox(tmp, "--close", "2", "--resolution", "done")
        t2 = open(os.path.join(idir, "002-fixture.md")).read()
        out.append((rc == 0 and "status: resolved" in t2 and "Resolution" in t2,
                    "a parked item closes on a resolution alone, no OKF receipt",
                    "a receipt on a parked item would make parking cost more than deciding", (rc, o)))
        rc, o = _inbox(tmp, "--close", "1", "--resolution", "done")
        t1 = open(os.path.join(idir, "001-fixture.md")).read()
        out.append((rc == 2 and "status: open" in t1, "a decision still cannot close without its OKF receipt",
                    "the new kinds must not loosen the one that blocks work", (rc, o)))

        # GAPS.md is derived from the gap items and --check says when it is not
        gp_py = os.path.join(tmp, "scripts", "gaps_md.py")
        r1 = subprocess.run([sys.executable, gp_py, "--check"], capture_output=True, text=True)
        subprocess.run([sys.executable, gp_py], capture_output=True, text=True)
        r2 = subprocess.run([sys.executable, gp_py, "--check"], capture_output=True, text=True)
        gaps_text = open(os.path.join(tmp, "GAPS.md")).read()
        out.append((r1.returncode == 1 and r2.returncode == 0 and "fixture 003 gap" in gaps_text,
                    "GAPS.md is generated from gap items; --check fails when stale and passes after regenerating",
                    "a file that calls itself a view needs a script deriving it, or it drifts",
                    (r1.returncode, r2.returncode)))
        _inbox(tmp, "--add", "second gap", "--kind", "gap", "--trigger", "t", "--context", "c")
        r3 = subprocess.run([sys.executable, gp_py, "--check"], capture_output=True, text=True)
        out.append((r3.returncode == 1, "adding a gap item makes GAPS.md stale", "the check must see a new item", r3.returncode))
    return out


def book_tools_cases():
    return switch_cases() + distill_cases() + inbox_kind_cases()
