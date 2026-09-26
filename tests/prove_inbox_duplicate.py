"""Prove duplicate IDs cannot select a record or execute its completion check."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def inbox_duplicate_cases():
    rows = []
    for ids in (("053", "053"), ("053", "53")):
        for args in ([], ["--json"], ["--close", "53", "--resolution", "test"],
                     ["--add", "Test", "--context", "test", "--recommend", "test",
                      "--evidence", "test", "--unblocks", "test"]):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "scripts").mkdir()
                (root / "inbox").mkdir()
                shutil.copy(ROOT / "scripts/inbox.py", root / "scripts/inbox.py")
                for name, number in zip(("a", "b"), ids):
                    (root / f"inbox/{name}.md").write_text(
                        f"---\nid: {number}\nstatus: ruled\napplied_by: touch PROOF_RAN\n---\n\n# {name}\n")
                before = {p.name: p.read_bytes() for p in (root / "inbox").iterdir()}
                result = subprocess.run([sys.executable, "scripts/inbox.py"] + args,
                                        cwd=root, capture_output=True, text=True)
                after = {p.name: p.read_bytes() for p in (root / "inbox").iterdir()}
                output = result.stdout + result.stderr
                ok = (result.returncode != 0 and "a.md" in output and "b.md" in output
                      and before == after and not (root / "PROOF_RAN").exists())
                rows.append((ok, f"inbox duplicate IDs {ids}: {args or 'list'}",
                             "refuse before mutation or reconciliation and name both files", output))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "scripts").mkdir()
        (root / "inbox").mkdir()
        shutil.copy(ROOT / "scripts/inbox.py", root / "scripts/inbox.py")
        target = root / "inbox/a.md"
        target.write_text("---\nid: 053\nstatus: open\n---\n\n# Unique\n")
        result = subprocess.run([sys.executable, "scripts/inbox.py", "--close", "53",
                                 "--resolution", "approved"], cwd=root, capture_output=True, text=True)
        rows.append((result.returncode == 0 and "status: resolved" in target.read_text(),
                     "inbox unique ID still closes", "do not reject an unambiguous record", result.stdout))
    return rows


if __name__ == "__main__":
    rows = inbox_duplicate_cases()
    for ok, name, _, detail in rows:
        print(("[ ok ] " if ok else "[FAIL] ") + name)
        if not ok:
            print(detail)
    raise SystemExit(0 if all(row[0] for row in rows) else 1)
