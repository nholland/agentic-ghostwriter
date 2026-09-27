#!/usr/bin/env python3
"""Behavioral coverage for inbox #064/#071/#074/#079/#104."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
import retro_window as rw
import log_check as lc


def maintenance_batch_cases():
    rows = []
    def check(ok, name, detail=None):
        rows.append((ok, name, 'inbox maintenance regression', detail))
    def heading(branch, day='01'):
        return f'2026-09-{day} 12:00 — `{branch}` — 1 commit(s) this session'
    def block(h, files=('i/a.md', 'i/b.md')):
        return '## ' + h + '\n' + ''.join(f'- `{f}`\n' for f in files) + '\n**Next:** x\n'
    a, b, a2 = heading('A'), heading('B'), heading('A', '02')
    for first, second in ((a, b), (b, a)):
        check(lc.lost_entries({first:block(first)}, {second:block(second)}) == [first],
              'log union: cross-branch coincidence cannot excuse missing session ' + first)
    check(lc.lost_entries({a:block(a)}, {a2:block(a2)}) == [], 'log union: same-branch restatement survives')
    check(lc.lost_entries({a:block(a)}, {a2:block(a2, ('i/a.md',))}) == [a], 'log union: partial file set cannot excuse loss')
    check(lc.lost_entries({a:block(a, ())}, {a2:block(a2, ())}) == [a], 'log union: empty entries do not excuse loss')
    check(lc.lost_entries({a:block(a)}, {a:block(a)}) == [], 'log union: exact heading survives')
    with tempfile.TemporaryDirectory(prefix='gw-maintenance-') as tmp:
        root = Path(tmp)
        def git(*args):
            return rw.git(root, *args)
        git('init', '-q'); git('config', 'user.name', 'Fixture'); git('config', 'user.email', 'fixture@example.com')
        def commit(paths):
            for p, content in paths.items():
                f = root / p; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(content)
            git('add', '--', *paths)
            git('commit', '-qm', 'fixture')
            return git('rev-parse', 'HEAD')
        base = commit({'scripts/a.py':'0'})
        state = root / '.claude/state'
        rw.write(state, 'session-start-sha', base)
        env = dict(os.environ, CLAUDE_PROJECT_DIR=tmp)
        env.pop('CLAUDE_PLUGIN_ROOT', None)
        def hook():
            return subprocess.run(['bash', str(REPO / '.claude/hooks/retro-check.sh')],
                                  cwd=tmp, env=env, capture_output=True, text=True)
        commit({'scripts/a.py':'1'})
        check(hook().returncode == 0, 'review: below threshold does not dispatch')
        commit({'scripts/a.py':'2'}); end1 = commit({'scripts/a.py':'3'})
        check(hook().returncode == 2, 'review: three work commits dispatch')
        check(hook().returncode == 0, 'review: same HEAD does not redispatch')
        for i in range(4, 7):
            end2 = commit({'scripts/a.py':str(i)})
        check(hook().returncode == 2 and rw.read(state, 'retro-window') == [base, end2],
              'review: second dispatch keeps the older window start')
        check(rw.bounds(root) == (base, end2), 'review: manual read retains unreviewed coverage')
        # Merely committing a report cannot consume a range.
        report_commit = commit({'runs/retro/review.md':f'Reviewed: {base}..{end1}\n', 'inbox/one.md':'finding'})
        check(rw.bounds(root)[0] == base, 'review: report commit alone does not consume coverage')
        check(rw.work_commits(root, end2, report_commit) == 0, 'review: report plus inbox does not trigger itself')
        for i in range(2):
            commit({f'runs/retro/r{i}.md':'report', f'inbox/r{i}.md':'finding'})
        check(hook().returncode == 0, 'review: three report-and-inbox commits stay quiet')
        mixed = commit({'runs/retro/mixed.md':'report', 'scripts/a.py':'7'})
        check(rw.work_commits(root, report_commit, mixed) == 1, 'review: substantive code alongside report still counts')
        try:
            rw.complete(root, base, end2, 'runs/retro/review.md')
            rejected = False
        except ValueError:
            rejected = True
        check(rejected and rw.bounds(root)[0] == base, 'review: mismatched report range refuses completion')
        rw.complete(root, base, end1, 'runs/retro/review.md')
        check(rw.bounds(root) == (end1, mixed), 'review: completion consumes only reviewed range and preserves later work')
        (root / 'runs/retro/current.md').write_text(f'Reviewed: {end1}..{mixed}\n')
        rw.complete(root, end1, mixed, 'runs/retro/current.md')
        check(rw.bounds(root) == (mixed, mixed), 'review: completed range is not returned again')
        new_head = commit({'scripts/a.py':'8'})
        check(rw.bounds(root) == (mixed, new_head), 'review: manual review after completion sees only new work')
        rw.write(state, 'retro-reviewed-sha', 'invalid')
        rw.write(state, 'retro-window', f'invalid {new_head}')
        check(rw.bounds(root) == (base, new_head), 'review: invalid stale state falls back without dropping session work')
        (state / 'session-start-sha').unlink()
        try:
            rw.bounds(root)
            rejected = False
        except ValueError:
            rejected = True
        check(rejected, 'review: missing valid bounds reports error instead of claiming clean')
    return rows


if __name__ == '__main__':
    rows = maintenance_batch_cases()
    for ok, name, _, detail in rows:
        print(f"{'[ ok ]' if ok else '[FAIL]'} {name}")
        if not ok:
            print(detail)
    print(f'{sum(r[0] for r in rows)}/{len(rows)} maintenance fixtures pass')
    sys.exit(any(not r[0] for r in rows))
