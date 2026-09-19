#!/usr/bin/env python3
"""
toolcheck.py - report which optional external tools are present, once per
session, so a gap is seen at the door rather than discovered mid-chapter.

WHY THIS EXISTS
    The book's real PDF renderer (scripts/chapter_pdf.py) needs weasyprint and
    markdown; neither has ever been importable in this container, and pip
    cannot reach PyPI here regardless (verified 2026-09-19: pypi.org itself
    returns 403, not merely proxy-blocked - this is the environment's network
    policy, not a missing install step a hook could paper over). A fallback
    renderer (chapter_pdf_local.py, headless Chromium) already covers the gap,
    so this is never fatal - but "the real renderer would work if X were
    present" was three separate discoveries at the point of use before this
    existed, once costing formatting defects already fixed once in the other
    renderer. Report once at the door instead.

    Author, asked directly 2026-09-19 what tools should be set up every
    session: this is the honest answer for what can be CHECKED. What can be
    FIXED from inside a session is a different, shorter list - see the report.

WHAT THIS DOES NOT DO
    Install anything. pip and npm's registries are both unreachable from this
    container by network policy (pypi.org: 403 direct; registry.npmjs.org:
    403 via the proxy's own allowlist) - a session hook cannot fix a network
    policy chosen when the environment was created. If that policy changes,
    re-run this; nothing here needs updating.

    List anything requiring a personal credential (Substack, Buffer). Those
    are MCP connectors tied to the author's own accounts, configured through
    claude.ai's connector settings or the author's own machine - never
    something to script into a shared environment's startup.

USAGE
    python3 scripts/toolcheck.py
    python3 scripts/toolcheck.py --json

EXIT
    Always 0. This reports; it never blocks (Rule 4's own spirit: a gate that
    cannot see is the only kind that blocks).
"""
import argparse
import importlib.util
import json
import shutil
import sys


def check_python(name):
    return importlib.util.find_spec(name) is not None


def check_binary(name):
    return shutil.which(name) is not None


TOOLS = [
    ("weasyprint", "python", "the book's real PDF renderer (chapter_pdf.py)"),
    ("markdown", "python", "markdown->HTML for the same renderer"),
    ("pandoc", "binary", "an alternate renderer, never wired up here"),
    ("wkhtmltopdf", "binary", "an alternate renderer, never wired up here"),
]


def main():
    ap = argparse.ArgumentParser(description="Report optional external tools, once per session.")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    rows = []
    for name, kind, why in TOOLS:
        present = check_python(name) if kind == "python" else check_binary(name)
        rows.append({"tool": name, "kind": kind, "present": present, "why": why})

    missing = [r for r in rows if not r["present"]]

    if a.json:
        print(json.dumps({"tools": rows, "missing": [r["tool"] for r in missing]}, indent=2))
        return 0

    if not missing:
        print("toolcheck: all optional tools present.")
        return 0

    print(f"toolcheck: {len(missing)}/{len(rows)} optional tool(s) absent - not blocking, "
          "chapter_pdf_local.py covers the PDF renderer:")
    for r in missing:
        print(f"  [absent] {r['tool']} ({r['kind']}) - {r['why']}")
    print("  Not fixable from inside a session: pip and npm's registries are both blocked by")
    print("  this environment's network policy (verified 2026-09-19, GAPS.md). Fixing it means")
    print("  creating an environment whose network policy allows pypi.org / registry.npmjs.org,")
    print("  not re-running anything here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
