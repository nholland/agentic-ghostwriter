"""Exercise manual descriptions and publication refusal using isolated sources."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import manual


def manual_description_cases():
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        fixtures = {
            "wrapped.py": ('"""wrapped.py - Move the chapter,\n'
                           'after approval. Do not include this sentence."""\n',
                           "Move the chapter, after approval."),
            "inline.py": ('"""Render the chapter."""\n', "Render the chapter."),
            "single.py": ("'''Read config.json safely! More detail.'''\n",
                          "Read config.json safely!"),
        }
        for name, (source, _) in fixtures.items():
            (root / name).write_text(source)
        with patch.object(manual, "SCRIPTS", tmp):
            actual = {s["name"]: s["purpose"] for s in manual.read_scripts()}
        for name, (_, expected) in fixtures.items():
            rows.append((actual.get(name) == expected,
                         "manual description: " + name,
                         "extract a complete first sentence without Python delimiters",
                         actual.get(name)))

        # An incomplete description must block both generation and --check,
        # even if the output digest would otherwise match.
        for source in ('"""unfinished purpose"""\n',
                       'def helper():\n    """Not a module purpose."""\n    pass\n',
                       '"""Valid-looking purpose."""\ninvalid python !\n'):
            (root / "broken.py").write_text(source)
            for flag in ([], ["--check"]):
                output = root / "manual.html"
                sentinel = '<!-- inputs-digest: abc123 -->\nOriginal manual\n'
                output.write_text(sentinel)
                with contextlib.ExitStack() as stack:
                    for name, value in (("SCRIPTS", tmp), ("OUT", str(output))):
                        stack.enter_context(patch.object(manual, name, value))
                    for name, value in (("read_desks", []), ("read_commands", []),
                                        ("read_thresholds", []), ("inputs_digest", "abc123"),
                                        ("governing_doc_drift", []), ("phantom_references", [])):
                        stack.enter_context(patch.object(manual, name, return_value=value))
                    stack.enter_context(patch.object(sys, "argv", ["manual.py"] + flag))
                    capture = stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                    rc = manual.main()
                ok = rc == 1 and output.read_text() == sentinel and "broken.py" in capture.getvalue()
                rows.append((ok, "manual rejects invalid purpose: " + repr(source) + str(flag),
                             "invalid source must not publish or pass freshness checking",
                             (rc, capture.getvalue())))
    return rows


if __name__ == "__main__":
    rows = manual_description_cases()
    for ok, name, _, detail in rows:
        print(("[ ok ] " if ok else "[FAIL] ") + name)
        if not ok:
            print(detail)
    raise SystemExit(0 if all(row[0] for row in rows) else 1)
