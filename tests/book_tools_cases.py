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


def book_tools_cases():
    return switch_cases() + distill_cases()
