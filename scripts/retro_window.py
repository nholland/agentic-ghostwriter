#!/usr/bin/env python3
"""Resolve pending review bounds; dispatch is not completion.

Default prints START END for manual and hook-requested reviews. After writing
its report, the reviewer calls --complete START END --report runs/retro/FILE.md.
--dispatch preserves pending coverage and batches three new work commits.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

WATCHED = ('bakeoff/', 'inbox/', 'scripts/', 'config/', 'books/', 'FINDINGS.md')


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def ancestor(root, start, end):
    return subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', start, end],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def read(state, name):
    path = state / name
    return path.read_text().split() if path.exists() else []


def write(state, name, value):
    state.mkdir(parents=True, exist_ok=True)
    path = state / name
    temporary = state / (name + '.tmp')
    temporary.write_text(value + '\n')
    temporary.replace(path)


def bounds(root):
    state = root / '.claude/state'
    head = git(root, 'rev-parse', 'HEAD')
    # Explicit completion supersedes legacy dispatch pointers. Without one,
    # retain the old window's START conservatively, even if HEAD has advanced.
    for name in ('retro-reviewed-sha', 'retro-window', 'session-start-sha'):
        value = read(state, name)
        if value and ancestor(root, value[0], head):
            return value[0], head
    raise ValueError('no valid review start; set .claude/state/session-start-sha to the intended base')


def work_commits(root, start, end):
    count = 0
    for commit in git(root, 'rev-list', f'{start}..{end}').splitlines():
        paths = git(root, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only', '-r', commit).splitlines()
        watched = [p for p in paths if p == 'FINDINGS.md' or p.startswith(WATCHED[:-1])]
        review_output = any(p.startswith('runs/retro/') for p in paths)
        substantive = any(not (p.startswith('inbox/') or p == 'FINDINGS.md') for p in watched)
        if watched and (not review_output or substantive):
            count += 1
    return count


def complete(root, start, end, report):
    current, head = bounds(root)
    if start != current or not ancestor(root, start, end) or not ancestor(root, end, head):
        raise ValueError('completion must cover the pending start through an ancestor of HEAD')
    path = (root / report).resolve()
    try:
        path.relative_to((root / 'runs/retro').resolve())
    except ValueError:
        raise ValueError('report must be under runs/retro/')
    if not path.is_file() or f'Reviewed: {start}..{end}' not in path.read_text():
        raise ValueError('report must exist and contain Reviewed: START..END with the exact hashes')
    state = root / '.claude/state'
    write(state, 'retro-reviewed-sha', end)
    write(state, 'retro-window', f'{end} {head}')


def dispatch(root):
    start, head = bounds(root)
    state = root / '.claude/state'
    previous = read(state, 'retro-last-sha')
    since = previous[0] if previous and ancestor(root, start, previous[0]) and ancestor(root, previous[0], head) else start
    if work_commits(root, since, head) < 3:
        return 0
    write(state, 'retro-window', f'{start} {head}')
    write(state, 'retro-last-sha', head)  # notification cadence only
    print(f'SESSION REVIEW: pending work {start}..{head}. Dispatch the Archivist '
          '(gw-retro); use scripts/retro_window.py for bounds and record completion '
          'only after writing the review report. Show its suggestions; apply none '
          'without author approval.', file=sys.stderr)
    return 2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    group = ap.add_mutually_exclusive_group()
    group.add_argument('--dispatch', action='store_true')
    group.add_argument('--complete', nargs=2, metavar=('START', 'END'))
    ap.add_argument('--report')
    a = ap.parse_args()
    try:
        if a.complete:
            if not a.report:
                raise ValueError('--complete requires --report')
            complete(a.repo, *a.complete, a.report)
        elif a.dispatch:
            return dispatch(a.repo)
        else:
            print(*bounds(a.repo))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'retro_window: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
