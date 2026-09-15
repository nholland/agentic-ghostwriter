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

WHY IT NO LONGER BLOCKS ON UNVERIFIED WORK
    Author's direction, 2026-09-15: "Nothing should stop the progress of the
    book. It should just keep up with its different statuses and let me know in
    the inbox." A citation nobody has confirmed yet is not a defect, it is
    unfinished work, and halting a chapter over it spends the one resource the
    house cannot make more of.

    So the gate now sorts what the validator says into three kinds:

      STRUCTURAL   the check itself cannot be trusted - unreadable frontmatter,
                   a missing validator, a voice threshold that no longer matches
                   the spec. This still blocks, because a gate that cannot see
                   is not a gate.
      OVERCLAIM    a concept claims more than its evidence supports: a verbatim
                   quotation called confirmed when nobody opened the page, or
                   `verified` set by anything but the author's own copy. This
                   does NOT block. The honest repair is to lower the status to
                   what the evidence actually supports, which is a correction,
                   not a halt - so it is reported, and proposed as a downgrade.
      OPEN         simply not verified yet. Counted, never mentioned as a fault.

    The distinction that matters: the house still refuses to let a claim stand
    above its evidence. It just fixes that by telling the truth about the
    status rather than by stopping the book.

    An error line this script does not recognise is treated as OVERCLAIM, not
    STRUCTURAL - non-blocking by default. That is deliberate: the classification
    reads the validator's message text, so an unfamiliar phrasing is much more
    likely to be a new editorial rule than a new structural one, and the author
    asked for nothing to stop the book.

USAGE
    python3 scripts/okf_gate.py                # advisory; exit 0 unless structural
    python3 scripts/okf_gate.py --strict       # the old behaviour: any error blocks
    python3 scripts/okf_gate.py --warnings-fatal
    python3 scripts/okf_gate.py --json

EXIT CODES
    0  the caller may write prose (open and overclaiming items are reported)
    1  STRUCTURAL problem, or --strict and something did not conform. BLOCK.
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


# Substrings that mark an error as STRUCTURAL - the check itself cannot be
# trusted. Everything else the validator reports is editorial: the concept is
# either incomplete or claiming more than its evidence supports, and neither
# stops a chapter. Matching message text couples this to the validator's
# wording, which is why an unrecognised line falls through to OVERCLAIM rather
# than to STRUCTURAL: the author asked that nothing stop the book, so the
# default has to be the non-blocking one.
STRUCTURAL_MARKS = (
    "missing or unparseable YAML frontmatter",
    "frontmatter has no non-empty `type`",
    "is in the future",
)

# A claim standing above its evidence. Not a halt: a status to be lowered.
OVERCLAIM_MARKS = (
    "violates the transcription rule",
    "requires evidence_source: author-copy",
    "but `resource` is empty",
)


def classify(out):
    """Split the validator's error lines into (structural, overclaim)."""
    structural, overclaim = [], []
    for raw in out.splitlines():
        line = raw.strip()
        if not line.startswith("x "):
            continue
        body = line[2:].strip()
        if any(m in body for m in STRUCTURAL_MARKS):
            structural.append(body)
        else:
            overclaim.append(body)
    return structural, overclaim


def main():
    ap = argparse.ArgumentParser(description="Run the book repo's OKF validator as a gate.")
    ap.add_argument("--warnings-fatal", action="store_true",
                    help="treat the validator's non-fatal warnings as blocking too")
    ap.add_argument("--strict", action="store_true",
                    help="block on any error, as this gate did before 2026-09-15")
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

    structural, overclaim = classify(out)
    # Voice-rule drift is structural: a threshold the script enforces has
    # diverged from the spec it claims to come from, so no count can be trusted.
    if voice_drift:
        structural.append("voice thresholds no longer match the book's voice spec "
                          "(scripts/voice_rules_check.py)")

    blocked = bool(structural) or (a.strict and proc.returncode != 0) \
        or (a.warnings_fatal and warnings)
    result = {
        "gate": "BLOCKED" if blocked else "PASS",
        "structural": structural,
        "overclaim": overclaim,
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
            if overclaim:
                print(f"         {len(overclaim)} concept(s) claim more than their "
                      f"evidence supports. Not blocking; the status should come")
                print("         down to match the evidence. Say /gw citations for the list.")
            if warnings:
                print(f"         {len(warnings)} non-fatal warning(s) above. Not "
                      f"blocking, but they are drift and someone should own them.")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
