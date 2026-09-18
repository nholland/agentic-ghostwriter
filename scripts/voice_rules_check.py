#!/usr/bin/env python3
"""
voice_rules_check.py - prove config/house.json still agrees with 01-voice.md.

WHY THIS EXISTS
    house.json holds eight counted thresholds that were transcribed BY HAND from
    the book's 01-voice.md. That made it a derived file with nothing deriving it -
    precisely the citation-manifest.md failure, committed inside a repo whose own
    README cites that failure three times as the thing to avoid. If the author
    raises the you-density floor in the voice spec, voice_check.py would go on
    enforcing 40 forever and report PASS while the spec said otherwise.

    Full derivation is not possible: 01-voice.md states its thresholds in prose,
    and parsing prose into numbers would be a new guess layered on the old one.
    So this does the honest achievable thing - it asserts that the phrase each
    threshold came from is STILL THERE. A reworded or renumbered rule breaks the
    probe and the gate fails loudly, which is the outcome that matters.

    A check that calls itself enforcement must have a caller: okf_gate.py runs
    this, and okf_gate.py is blocking in every skill that writes prose.

USAGE
    python3 scripts/voice_rules_check.py [--json]

EXIT CODES
    0  every threshold's source phrase still present in 01-voice.md
    1  at least one probe failed - the spec and the config may have diverged
    2  could not read 01-voice.md or the config
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Check house.json against 01-voice.md.")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cfg = resolve_book.load_config()
    repo_root, _, _ = resolve_book.resolve(cfg)
    if not repo_root:
        print("voice_rules_check: no book repo resolvable", file=sys.stderr)
        return 2
    rep = resolve_book.inspect(repo_root, require_okf=False)
    book_root = rep["info"].get("bookRoot")
    if not book_root:
        print("voice_rules_check: no bookRoot", file=sys.stderr)
        return 2

    spec_path = os.path.join(book_root, "01-voice.md")
    try:
        spec = open(spec_path, encoding="utf-8").read()
    except Exception as exc:
        print(f"voice_rules_check: cannot read {spec_path}: {exc}", file=sys.stderr)
        return 2

    results, failed = [], []
    for name, rule in cfg.get("voice_rules", {}).items():
        if name.startswith("_") or not isinstance(rule, dict):
            continue
        probe = rule.get("spec_probe")
        if not probe:
            results.append({"rule": name, "status": "NO-PROBE", "value": rule.get("value")})
            failed.append(name)
            continue
        m = re.search(probe, spec, re.IGNORECASE)
        ok = m is not None
        status = "ok" if ok else "DRIFT"

        # The phrase being present is not the same as the phrase agreeing with
        # the number this engine enforces. Added 2026-09-16 after an Archivist
        # probe showed `value` could be mutated 3 -> 5 while 01-voice.md still
        # read "~3 mentions" and this check printed [ok] and exited 0. An engine
        # enforcing a number its constitution does not state is the two-sources-
        # of-truth failure the whole check exists to prevent.
        #
        # Rewritten 2026-09-18. The first version accepted any number anywhere in
        # the matched span, and printed ok where the span held no digits at all -
        # so em_dash_max 0 -> 9, the bold cap 1 -> 7 and the you-density floor
        # 40 -> 1 all passed. Each rule now declares `spec_number`: the number the
        # constitution states, in digits or in words ("Never use em-dashes" is a
        # cap of 0, recorded in spec_number_note), and the engine's value is
        # compared against that declaration every time.
        value = rule.get("value")
        want = rule.get("spec_number")
        nums = []
        if ok:
            nums = [float(n) for n in re.findall(r"\d+(?:\.\d+)?",
                                                 m.group(0).replace(",", ""))]
            if want is None:
                status = "NUMBER-UNCHECKED"      # nothing compared; never ok (Rule 12)
            elif nums and float(want) not in nums:
                status = "MISMATCH"              # the spec was reworded under the declaration
            elif float(value) not in (float(want), float(want) / 100.0):
                status = "MISMATCH"              # engine enforces a number the spec does not state

        results.append({"rule": name, "status": status, "value": value,
                        "spec_number": want, "probe": probe,
                        "spec_text": m.group(0) if m else None,
                        "spec_numbers": nums,
                        "note": rule.get("spec_number_note")})
        # UNCHECKED is honest, not broken, and must not fail the build, or
        # okf_gate would read a correctly-declared rule as structural drift.
        if status not in ("ok", "NUMBER-UNCHECKED"):
            failed.append(name)

    out = {"spec": spec_path, "results": results, "failed": failed}
    if a.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"voice_rules_check: against {spec_path}")
        for r in results:
            mark = {"ok": "ok   ", "DRIFT": "DRIFT", "NO-PROBE": "NO-PR",
                    "MISMATCH": "MISMA"}[r["status"]]
            print(f"  [{mark}] {r['rule']:<32} = {r['value']}")
            if r["status"] == "MISMATCH":
                print(f"          spec says {r['spec_numbers']} in: {r['spec_text']!r}")
        print()
        mismatched = [r["rule"] for r in results if r["status"] == "MISMATCH"]
        if mismatched:
            print("  MISMATCH: the spec wording is present but states a different")
            print("            number than this engine enforces. The engine must")
            print("            never enforce a threshold its constitution does not")
            print("            state. Change the spec first, then the value.")
            print(f"            Affected: {', '.join(mismatched)}")
            print()
        mismatched = [r["rule"] for r in results if r["status"] == "MISMATCH"]
        if mismatched:
            print("  MISMATCH: the engine enforces a number the constitution does")
            print("            not state. Change the spec first, then the value.")
            print(f"            Affected: {', '.join(mismatched)}")
            print()
        if failed:
            print("  DRIFT: the voice spec no longer contains the wording these")
            print("         thresholds were transcribed from. Either the author changed")
            print("         a rule (update house.json to match) or reworded it (update")
            print("         the probe). Do not assume the numbers are still right.")
            print(f"         Affected: {', '.join(failed)}")
        else:
            print("  every threshold's source wording is still present in the spec")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
