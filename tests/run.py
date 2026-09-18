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
import os
import subprocess
import sys

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
        ("good.html", False, "chapter first, distillation last and labelled"),
    ]
    out = []
    for name, must_fail, why in cases:
        fails, _ = package_check.check(os.path.join(FIX, name))
        ok = bool(fails) == must_fail
        out.append((ok, f"package_check {name}", why,
                    "; ".join(fails) if fails else "clean"))
    return out


def voice_rules_cases():
    """Mutate each threshold, assert the check catches it, restore the file."""
    import json
    import shutil
    cfg = os.path.join(REPO, "config", "house.json")
    bak = cfg + ".testbak"
    shutil.copy(cfg, bak)
    out = []
    try:
        d = json.load(open(cfg))
        for name in list(d["voice_rules"]):
            if not isinstance(d["voice_rules"][name], dict):
                continue
            if "value" not in d["voice_rules"][name]:
                continue
            orig = d["voice_rules"][name]["value"]
            d["voice_rules"][name]["value"] = float(orig) + 7
            json.dump(d, open(cfg, "w"), indent=2)
            r = subprocess.run([sys.executable, os.path.join(REPO, "scripts",
                                                            "voice_rules_check.py")],
                               capture_output=True, text=True)
            caught = r.returncode != 0 and "Traceback" not in r.stderr
            out.append((caught, f"voice_rules mutation {name}",
                        f"{orig} -> {orig + 7} must be caught",
                        r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[:80]))
            d["voice_rules"][name]["value"] = orig
            json.dump(d, open(cfg, "w"), indent=2)

        # The one honest state must print, not crash. Removing spec_number is
        # exactly what a ninth rule added without one would look like.
        d["voice_rules"]["em_dash_max"].pop("spec_number", None)
        json.dump(d, open(cfg, "w"), indent=2)
        r = subprocess.run([sys.executable, os.path.join(REPO, "scripts",
                                                        "voice_rules_check.py")],
                           capture_output=True, text=True)
        out.append(("Traceback" not in r.stderr, "voice_rules spec_number null",
                    "an undeclared number must report UNCHECKED, never crash",
                    "crashed" if "Traceback" in r.stderr else "reported"))
    finally:
        shutil.copy(bak, cfg)
        os.remove(bak)
    return out


def main():
    rows = package_cases() + voice_rules_cases()
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
