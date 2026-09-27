#!/usr/bin/env python3
"""Record knowledge dispositions; check file coverage, never semantic truth.

Use --write PATH --subject inbox:094 --disposition updated --concept PATH
--file PATH --authority TEXT --reason TEXT. Repeat subjects, files and concepts.
--check checks book Markdown and interview records changed since the upstream
(or main for a new branch), including committed, staged and untracked work.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DISPOSITIONS = ('updated', 'already-represented', 'no-knowledge-change')


def local(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('path must stay inside the repository: ' + value)
    return path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else 'deleted'


def validate(root, record, subject=None, files=()):
    if record.get('disposition') not in DISPOSITIONS:
        raise ValueError('choose updated, already-represented, or no-knowledge-change')
    for field in ('authority', 'reason'):
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError(field + ' is required')
    subjects = record.get('subjects')
    if not isinstance(subjects, list) or not subjects or not all(isinstance(s, str) and s.strip() for s in subjects):
        raise ValueError('at least one subject is required')
    if subject and subject not in subjects:
        raise ValueError('receipt does not cover ' + subject)
    concepts = record.get('concepts', [])
    if not isinstance(concepts, list):
        raise ValueError('concepts must be a list')
    if record['disposition'] != 'no-knowledge-change' and not concepts:
        raise ValueError('knowledge dispositions require concept paths')
    for name in concepts:
        if not isinstance(name, str):
            raise ValueError('concept paths must be strings')
        path = local(root, name)
        if 'okf' not in path.relative_to(root.resolve()).parts or not path.is_file():
            raise ValueError('missing OKF concept: ' + name)
        text = path.read_text()
        if not text.startswith('---\n') or '\ntype:' not in text.split('\n---', 1)[0]:
            raise ValueError('not a typed OKF concept: ' + name)
    hashes = record.get('files')
    if not isinstance(hashes, dict):
        raise ValueError('files must map paths to content hashes')
    for name in files:
        if hashes.get(name) != digest(local(root, name)):
            raise ValueError('missing or stale file coverage: ' + name)
    return record


def read(root, name, current=False, **kwargs):
    if not name:
        raise ValueError('OKF reconciliation receipt required (--okf-receipt PATH)')
    try:
        record = json.loads(local(root, name).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError('cannot read OKF receipt: ' + str(exc)) from exc
    if not isinstance(record, dict):
        raise ValueError('receipt must be a JSON object')
    if current:
        kwargs["files"] = record.get("files", {})
    return validate(root, record, **kwargs)


def git(root, *args):
    p = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True)
    if p.returncode:
        raise ValueError(p.stderr.strip() or 'git check failed')
    return p.stdout


def verify(root, ref):
    try:
        return git(root, 'rev-parse', '--verify', '--quiet', ref).strip()
    except ValueError:
        return None


def changed(root, since=None):
    main = None
    if not since:
        since = verify(root, '@{upstream}')
        main = verify(root, 'origin/main') or verify(root, 'main')
        since = since or main
        if not since:
            raise ValueError('no comparison branch; use --since SHA')
    names = set(git(root, 'diff', '--name-only', since, '--').splitlines())
    if main and main != since:
        # A file whose bytes match main's arrived by merging main, where it
        # was already reconciled; only this branch's own changes need a receipt.
        names &= set(git(root, 'diff', '--name-only', main, '--').splitlines())
    names.update(git(root, 'ls-files', '--others', '--exclude-standard').splitlines())
    return sorted(n for n in names if n.endswith('.md') and
                  (n.startswith('books/') or (n.startswith('runs/') and n.endswith('/interview.md'))))


def check(root=ROOT, since=None):
    try:
        names = changed(root, since)
        records = []
        for path in sorted((root / 'runs/reconciliation').glob('*.json')):
            try:
                records.append(read(root, str(path.relative_to(root))))
            except ValueError:
                # Historical receipts can reference subsequently removed concepts.
                # They cannot cover current work but do not invalidate other receipts.
                continue
        missing = [n for n in names if not any(r['files'].get(n) == digest(local(root, n)) for r in records)]
        if missing:
            raise ValueError('unreconciled knowledge-bearing files:\n  ' + '\n  '.join(missing))
        print(f'okf_reconcile: PASS — {len(names)} changed file(s) covered; semantic completeness requires Publisher review.')
        return 0
    except (ValueError, OSError) as exc:
        print('okf_reconcile: ' + str(exc), file=sys.stderr)
        return 2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write')
    g.add_argument('--check', action='store_true')
    ap.add_argument('--since')
    ap.add_argument('--subject', action='append', default=[])
    ap.add_argument('--file', action='append', default=[])
    ap.add_argument('--concept', action='append', default=[])
    ap.add_argument('--disposition', choices=DISPOSITIONS)
    ap.add_argument('--authority')
    ap.add_argument('--reason')
    a = ap.parse_args()
    if a.check:
        return check(since=a.since)
    try:
        path = local(ROOT, a.write)
        if path.parent != ROOT / 'runs/reconciliation' or path.suffix != '.json':
            raise ValueError('write receipts under runs/reconciliation/*.json')
        record = dict(timestamp=datetime.now().astimezone().isoformat(), subjects=a.subject,
                      disposition=a.disposition, concepts=a.concept, authority=a.authority,
                      reason=a.reason, files={n: digest(local(ROOT, n)) for n in a.file})
        validate(ROOT, record)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record, indent=2) + '\n')
        print('okf_reconcile: recorded ' + a.write)
        return 0
    except (ValueError, OSError) as exc:
        print('okf_reconcile: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
