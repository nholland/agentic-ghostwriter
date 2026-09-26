"""Exercise landing against real disposable Git histories and a local remote."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync


def land_ancestry_cases():
    rows = []
    for mode in ("unrelated", "ahead", "diverged", "missing", "equal", "behind"):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            remote = Path(tmp) / "remote.git"
            root.mkdir()

            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args],
                                               stderr=subprocess.DEVNULL, text=True).strip()

            git("init", "-q", "-b", "main")
            git("config", "user.email", "fixture@example.com")
            git("config", "user.name", "Fixture")
            git("commit", "--allow-empty", "-qm", "base")
            base = git("rev-parse", "HEAD")
            git("commit", "--allow-empty", "-qm", "remote main")
            upstream = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", upstream)
            git("checkout", "-qb", "session")
            git("commit", "--allow-empty", "-qm", "session work")
            head = git("rev-parse", "HEAD")
            if mode == "unrelated":
                git("checkout", "--orphan", "other")
                git("commit", "--allow-empty", "-qm", "unrelated root")
                local = git("rev-parse", "HEAD")
                git("checkout", "-q", "session")
                git("branch", "-f", "main", local)
            elif mode == "ahead":
                git("branch", "-f", "main", head)
            elif mode == "diverged":
                git("checkout", "-qb", "other", base)
                git("commit", "--allow-empty", "-qm", "local divergence")
                local = git("rev-parse", "HEAD")
                git("checkout", "-q", "session")
                git("branch", "-f", "main", local)
            elif mode == "missing":
                git("branch", "-D", "main")
            elif mode == "behind":
                git("branch", "-f", "main", base)
            subprocess.run(["git", "init", "--bare", "-q", str(remote)], check=True)
            git("remote", "add", "origin", str(remote))
            state = dict(branch="session", uncommitted=0, behind_main=0,
                         ahead_of_main=1, unpushed=1)
            before = git("show-ref")
            calls = []
            original = sync.run

            def recorded(*args, **kwargs):
                calls.append(args)
                return original(*args, **kwargs)

            with patch.object(sync, "REPO", str(root)), patch.object(sync, "run", recorded):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    rc = sync.land(state)
            if mode in ("equal", "behind"):
                ok = (rc == 0 and git("rev-parse", "main") == head
                      and git("branch", "--show-current") == "session"
                      and git("ls-remote", "origin", "refs/heads/main").split()[0] == head)
            else:
                ok = (rc != 0 and git("show-ref") == before
                      and git("branch", "--show-current") == "session"
                      and not any(c[0] in ("checkout", "push", "merge") for c in calls)
                      and "local main" in output.getvalue())
            rows.append((ok, "land local-main ancestry: " + mode,
                         "unsafe histories refuse before side effects; safe histories fast-forward",
                         (rc, calls, output.getvalue())))
    return rows


if __name__ == "__main__":
    rows = land_ancestry_cases()
    for ok, name, _, detail in rows:
        print(("[ ok ] " if ok else "[FAIL] ") + name)
        if not ok:
            print(detail)
    raise SystemExit(0 if all(row[0] for row in rows) else 1)
