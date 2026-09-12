#!/usr/bin/env python3
"""
okf_gate.py - the citation gate, delegated to the book repo's own validator.

WHY THIS WRAPS RATHER THAN REIMPLEMENTS
    The book repo already has scripts/okf_validate.py, and it is the enforcement
    path for the transcription rule: a verbatim quotation may not hold
    status verifiable/verified while evidence_source is search-synthesis,
    database-abstract, or none. Reimplementing that here would produce two
    validators that drift, which is the citation-manifest.md failure again -
    a second copy of a rule, with nothing keeping the copies equal.

    So this resolves the book repo, runs ITS validator, and refuses to pass on
    a missing one. A gate that cannot find its check must fail closed.

WHY IT EXISTS AT ALL
    The book pipeline's /book-chapter-refine and /book-compile both run
    `okf_validate.py --strict` as a BLOCKING gate before writing prose. The
    first version of this repo's gw-refine ran no citation check whatsoever,
    which made the replacement pipeline less safe on citations than the one it
    replaces - in the exact area where nine defects reached printed prose, six
    of them printed. This closes that.

USAGE
    python3 scripts/okf_gate.py                # gate; exit 1 blocks the caller
    python3 scripts/okf_gate.py --warnings-fatal
    python3 scripts/okf_gate.py --json

EXIT CODES
    0  bundle conforms; caller may write prose
    1  bundle does not conform, or the validator could not be run. BLOCK.
    2  no book repo resolvable
"""

import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Run the book repo's OKF validator as a gate.")
    ap.add_argument("--warnings-fatal", action="store_true",
                    help="treat the validator's non-fatal warnings as blocking too")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cfg = resolve_book.load_config()
    repo_root, why, _ = resolve_book.resolve(cfg)
    if not repo_root:
        msg = ("okf_gate: BLOCKED - no book repo resolvable. "
               "Run scripts/resolve_book.py for the reason.")
        print(json.dumps({"gate": "BLOCKED", "reason": msg}) if a.json else msg,
              file=sys.stderr)
        return 2

    rep = resolve_book.inspect(repo_root, require_okf=True)
    validator = rep["info"].get("okf_validate")
    book_rel = rep["info"].get("bookRootRelative")

    if not validator or not book_rel:
        msg = ("okf_gate: BLOCKED - the book repo has no scripts/okf_validate.py, "
               "or no bookRoot in its manifest. This gate fails closed: prose "
               "must not be written without the transcription rule enforced.")
        print(json.dumps({"gate": "BLOCKED", "reason": msg}) if a.json else msg,
              file=sys.stderr)
        return 1

    # The voice-rule drift check runs here so that it has a caller. A check with
    # no caller is decoration: okf_validate.py itself sat uninvoked by anything in
    # the book repo while a rule called it "Enforcement".
    vrc = subprocess.run(
        [sys.executable, os.path.join(HERE, "voice_rules_check.py")],
        capture_output=True, text=True,
    )
    voice_drift = vrc.returncode != 0

    proc = subprocess.run(
        [sys.executable, validator, book_rel, "--strict"],
        cwd=repo_root, capture_output=True, text=True,
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    warnings = [ln.strip() for ln in out.splitlines() if ln.strip().startswith("!")]

    blocked = (proc.returncode != 0 or voice_drift
               or (a.warnings_fatal and warnings))
    result = {
        "gate": "BLOCKED" if blocked else "PASS",
        "voice_rules_drift": voice_drift,
        "voice_rules_output": vrc.stdout.strip(),
        "validator": validator,
        "bookRoot": book_rel,
        "returncode": proc.returncode,
        "warnings": warnings,
        "output": out.strip(),
    }

    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(out.strip())
        print()
        if voice_drift:
            print(vrc.stdout.strip())
            print()
        if blocked:
            print("okf_gate: BLOCKED. Do not write prose.")
            if voice_drift:
                print("         The counted thresholds may no longer match 01-voice.md.")
            if a.warnings_fatal and warnings and proc.returncode == 0:
                print(f"         (blocked on {len(warnings)} warning(s) because "
                      f"--warnings-fatal was passed)")
        else:
            print("okf_gate: PASS - the caller may write prose.")
            if warnings:
                print(f"         {len(warnings)} non-fatal warning(s) above. Not "
                      f"blocking, but they are drift and someone should own them.")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
