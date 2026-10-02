"""The explicit check must report a failed stage and still check the others."""
import contextlib
import io
from types import SimpleNamespace
from unittest.mock import patch
import archivist_check


def archivist_cases():
    rows = []
    for failure in (None, 0, len(archivist_check.CHECKS) - 1):
        calls = []
        def run(args, **kwargs):
            calls.append(args)
            return SimpleNamespace(returncode=1 if len(calls) - 1 == failure else 0)
        with patch.object(archivist_check.subprocess, 'run', run), contextlib.redirect_stdout(io.StringIO()) as output:
            rc = archivist_check.check()
        expected = [[archivist_check.sys.executable, *args] for _, args in archivist_check.CHECKS]
        ok = calls == expected and rc == (0 if failure is None else 1)
        if failure is not None:
            ok = ok and ('FAIL: ' + archivist_check.CHECKS[failure][0]) in output.getvalue()
        rows.append((ok, f'Archivist checks failure={failure}',
                     'All named checks run; failures prevent a ready result without git mutations.',
                     output.getvalue()))
    return rows
