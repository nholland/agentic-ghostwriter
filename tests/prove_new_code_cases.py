#!/usr/bin/env python3
"""Exercise #048 in disposable repositories, including refusal paths."""
import pathlib
import shutil
import subprocess
import sys
import tempfile


def prove_new_code_cases():
    rows = []
    source = pathlib.Path(__file__).with_name('prove.py')
    with tempfile.TemporaryDirectory(prefix='gw-prove-new-') as tmp:
        root = pathlib.Path(tmp)
        def git(*args):
            return subprocess.run(['git', '-C', tmp, *args], check=True,
                                  capture_output=True, text=True).stdout.strip()
        git('init', '-q')
        git('config', 'user.name', 'Fixture')
        git('config', 'user.email', 'fixture@example.com')
        (root / 'tests').mkdir()
        shutil.copy2(source, root / 'tests/prove.py')
        target = root / 'target.py'
        target.write_text('# No new function yet\n')
        harness = root / 'tests/run.py'
        harness.write_text('''from pathlib import Path
p = Path('target.py')
ns = {}
if p.exists():
    exec(p.read_text(), ns)
ok = 'feature' in ns and ns['feature']() == 42
print(('[ ok ]' if ok else '[FAIL]') + ' new feature works')
''')
        git('add', '.')
        git('commit', '-qm', 'before function')
        old_function = git('rev-parse', 'HEAD')
        git('rm', '-q', 'target.py')
        git('commit', '-qm', 'before file')
        old_file = git('rev-parse', 'HEAD')
        target.write_text('def feature():\n    return 42\n')
        # Leave both the source and fixture dirty to exercise live-tree copying.
        def check(label, at, expected, case='new feature works'):
            result = subprocess.run([sys.executable, str(root / 'tests/prove.py'),
                                     '--file', 'target.py', '--at', at, '--case', case],
                                    cwd=tmp, capture_output=True, text=True)
            rows.append((result.returncode == expected,
                         'prove new code: ' + label,
                         'named failure and current success are required',
                         (result.returncode, result.stdout, result.stderr)))
        check('absent historical source proves red then green', old_file, 0)
        check('absent historical function proves red then green', old_function, 0)
        check('invalid revision is refused', 'nonexistent-revision', 2)
        check('missing case is refused', old_file, 2, 'never printed')
        good_harness = harness.read_text()
        harness.write_text("raise RuntimeError('unrelated crash')\n")
        check('unrelated crash is refused', old_file, 2)
        harness.write_text(good_harness)
        target.write_text('def feature():\n    return 0\n')
        check('current failing implementation is refused', old_file, 2)
        rows.append((len(git('worktree', 'list', '--porcelain').split('worktree ')) == 2,
                     'prove new code: all disposable worktrees removed',
                     'success and refusal both clean up', git('worktree', 'list')))
        rows.append((target.read_text() == 'def feature():\n    return 0\n',
                     'prove new code: live source is untouched',
                     'only disposable worktrees may be reverted', target.read_text()))
    return rows


if __name__ == '__main__':
    rows = prove_new_code_cases()
    for ok, name, _, detail in rows:
        print(f"{'[ ok ]' if ok else '[FAIL]'} {name}")
        if not ok:
            print(detail)
    sys.exit(any(not row[0] for row in rows))
