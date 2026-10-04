#!/usr/bin/env python3
"""Explicit Archivist tools. Checks never commit, push, amend, or dispatch desks.

Run without arguments before committing. After the work commit, --record updates
session memory; review and commit that change separately, then check again.
"""
import argparse
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]
# Generated-file registry, also checked against README by manual.py.
DERIVED = """
scripts/sync_plugin_layout.py|plugin adapters|python3 scripts/sync_plugin_layout.py
scripts/manual.py|house manual|python3 scripts/manual.py
scripts/build_diagrams_page.py|diagram page|python3 scripts/build_diagrams_page.py
scripts/gaps_md.py|gaps list|python3 scripts/gaps_md.py
"""
CHECKS = [
    ("Knowledge receipts", ["scripts/okf_reconcile.py", "--check"]),
    ("Session log integrity", ["scripts/log_check.py"]),
    ("Stored regression tests", ["tests/run.py"]),
] + [(line.split("|")[1], [line.split("|")[0], "--check"])
     for line in DERIVED.strip().splitlines()]


def check():
    failed = []
    for name, args in CHECKS:
        print(f"Archivist: {name}", flush=True)
        result = subprocess.run([sys.executable, *args], cwd=REPO)
        print(f"{'PASS' if result.returncode == 0 else 'FAIL'}: {name}", flush=True)
        if result.returncode:
            failed.append(name)
    print("Archivist: " + ("needs attention: " + ", ".join(failed)
                          if failed else "checks passed; ready for review and commit"))
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="update session log after the work commit")
    args = parser.parse_args()
    if args.record:
        result = subprocess.run([sys.executable, "scripts/session_log.py"], cwd=REPO)
        if result.returncode:
            return result.returncode
        return subprocess.run([sys.executable, "scripts/log_check.py"], cwd=REPO).returncode
    return check()


if __name__ == "__main__":
    sys.exit(main())
