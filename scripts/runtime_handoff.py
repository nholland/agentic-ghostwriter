#!/usr/bin/env python3
"""One durable checkpoint and one active writer for both house runtimes.

checkpoint --chapter N --note-file PATH records unfinished work verbatim.
attempt --chapter N --desk gw-X increments a durable failed-gate count.
resume reads the checkpoint and asks next.py for current state; it never
advances a chapter or approves a decision. recover requires the old session
to be stopped first. Hook adapters use the same functions as this CLI.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def read(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=path.name + '.')
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(value, f, indent=2, ensure_ascii=False)
            f.write('\n')
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextmanager
def locked(root):
    state = root / '.claude/state'
    state.mkdir(parents=True, exist_ok=True)
    with (state / 'runtime.lock').open('a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield state


def owner_path(root):
    return root / '.claude/state/runtime-owner.json'


def identity(runtime, session):
    if runtime not in ('claude', 'codex') or not session:
        raise ValueError('runtime and session id are required')
    return {'runtime': runtime, 'session': session}


def matches(a, b):
    return a.get('runtime') == b['runtime'] and a.get('session') == b['session']


def claim(root, runtime, session):
    wanted = identity(runtime, session)
    with locked(root):
        owner = read(owner_path(root), {})
        if owner and not matches(owner, wanted):
            raise ValueError(f"{owner['runtime']} session {owner['session']} owns this project. "
                             'Stop its desks and save its handoff before switching. '
                             'For a crashed session, confirm it is stopped, then use '
                             'scripts/runtime_handoff.py recover --stopped-session SESSION.')
        if not owner:
            state = root / '.claude/state'
            if read(state / 'runtime-session.json', {}) != wanted:
                (state / 'session-start-sha').write_text(git(root, 'rev-parse', 'HEAD') + '\n')
                atomic(state / 'runtime-session.json', wanted)
            atomic(owner_path(root), dict(wanted, desks={}, started=datetime.now().astimezone().isoformat()))


def release(root, runtime, session):
    wanted = identity(runtime, session)
    with locked(root):
        owner = read(owner_path(root), {})
        if owner and not matches(owner, wanted):
            raise ValueError('cannot release another session')
        if owner.get('desks'):
            raise ValueError('active desks must finish or be stopped before handoff')
        owner_path(root).unlink(missing_ok=True)


def desk_event(root, runtime, session, agent_id, started):
    if not isinstance(agent_id, str) or not agent_id:
        raise ValueError('subagent event requires an agent_id')
    claim(root, runtime, session)
    with locked(root):
        owner = read(owner_path(root), {})
        if not matches(owner, identity(runtime, session)):
            raise ValueError('subagent does not belong to the active writer')
        desks = owner.setdefault('desks', {})
        if started:
            desks[agent_id] = 'active'
        else:
            desks.pop(agent_id, None)
        atomic(owner_path(root), owner)


def recover(root, stopped_session):
    with locked(root):
        owner = read(owner_path(root), {})
        if not owner or owner['session'] != stopped_session:
            raise ValueError('stopped-session must exactly match the recorded owner')
        owner_path(root).unlink()


def git(root, *args):
    p = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True)
    if p.returncode:
        raise ValueError(p.stderr.strip() or 'git failed')
    return p.stdout.strip()


def oracle(root, chapter=None):
    args = [sys.executable, str(root / 'scripts/next.py'), '--json']
    if chapter is not None:
        if not isinstance(chapter, int) or chapter < 1:
            raise ValueError('chapter must be positive')
        args += ['--chapter', str(chapter)]
    p = subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=120)
    if p.returncode:
        raise ValueError('next.py could not resolve state: ' + p.stderr.strip())
    return json.loads(p.stdout)


def safe_file(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('artifact must stay inside the project')
    return path


def fingerprint(root, name):
    path = safe_file(root, name)
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else 'missing'


def checkpoint(root, runtime, session, chapter=None, note=None, failed_desk=None,
               author_record=None):
    claim(root, runtime, session)
    with locked(root):
        old = read(root / 'runs/handoff.json', {})
        if old and old.get('schema') != 1:
            raise ValueError('unknown handoff schema; preserve and inspect the record')
        chapter = chapter if chapter is not None else old.get('chapter')
        current = oracle(root, chapter)
        notes = dict(old.get('notes', {}))
        attempts = dict(old.get('failed_attempts', {}))
        key = str(chapter) if chapter is not None else 'house'
        if note is not None:
            if not note.strip():
                raise ValueError('handoff note cannot be empty')
            notes[key] = note
        if failed_desk:
            if not (root / '.claude/agents' / (failed_desk + '.md')).is_file():
                raise ValueError('unknown desk')
            attempt_key = key + ':' + failed_desk
            if attempts.get(attempt_key, 0) >= 2:
                raise ValueError('two failed rounds already recorded; route to the inbox instead of retrying')
            attempts[attempt_key] = attempts.get(attempt_key, 0) + 1
        artifacts = sorted(str(p.relative_to(root)) for p in (root / 'inbox').glob('*.md'))
        if chapter is not None:
            artifacts += sorted(str(p.relative_to(root)) for p in
                                (root / f'runs/ch{chapter:02d}').glob('*') if p.is_file())
        author_records = list(old.get('author_records', []))
        if author_record and author_record not in author_records:
            author_records.append(author_record)
        fingerprints = {n: fingerprint(root, n) for n in artifacts}
        record = dict(schema=1, chapter=chapter, runtime=runtime, branch=git(root, 'branch', '--show-current'),
                      oracle=current, notes=notes, failed_attempts=attempts,
                      author_records=author_records, artifacts=fingerprints)
        # Repeated Stop calls without work must not create new commits.
        previous = {k: v for k, v in old.items() if k != 'updated'}
        if record != previous:
            atomic(root / 'runs/handoff.json', dict(record, updated=datetime.now().astimezone().isoformat()))
        return record


def record_prompt(root, runtime, session, payload):
    prompt = payload.get('prompt')
    if not isinstance(prompt, str) or not prompt:
        return
    # Exact words are retained as intake, never interpreted as approval by this script.
    session_key = hashlib.sha256((runtime + ':' + session).encode()).hexdigest()[:16]
    rel = f'runs/handoff/intake-{session_key}.json'
    path = root / rel
    with locked(root):
        rows = read(path, [])
        turn = payload.get('turn_id')
        if turn is None or not any(r.get('turn_id') == turn for r in rows):
            rows.append(dict(runtime=runtime, turn_id=turn, prompt=prompt,
                             recorded=datetime.now().astimezone().isoformat()))
            atomic(path, rows)
    checkpoint(root, runtime, session, author_record=rel)


def resume(root):
    record = read(root / 'runs/handoff.json', {})
    if not record:
        return 'No saved handoff yet. Run scripts/next.py for the current board.'
    if record.get('schema') != 1:
        raise ValueError('unknown handoff schema')
    changed = [n for n, digest in record['artifacts'].items() if fingerprint(root, n) != digest]
    current = oracle(root, record.get('chapter'))
    result = {'checkpoint': record, 'current_oracle': current, 'changed_artifacts': changed,
              'instruction': 'Read referenced intake and chapter records before resuming. '
              'The current oracle wins over the checkpoint. Recheck changed inputs. '
              'Pending concepts and verdicts still require the author. '
              'Failed-attempt counts survive switching; two failures go to the inbox.'}
    return json.dumps(result, indent=2, ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('action', choices=('resume', 'checkpoint', 'attempt', 'recover'))
    ap.add_argument('--runtime', choices=('claude', 'codex'))
    ap.add_argument('--session')
    ap.add_argument('--chapter', type=int)
    ap.add_argument('--note-file', type=Path)
    ap.add_argument('--desk')
    ap.add_argument('--stopped-session')
    a = ap.parse_args()
    try:
        if a.action == 'resume':
            print(resume(ROOT))
        elif a.action == 'recover':
            recover(ROOT, a.stopped_session)
            print('Recovered writer ownership; existing checkpoint and files preserved.')
        else:
            owner = read(owner_path(ROOT), {})
            runtime, session = a.runtime or owner.get('runtime'), a.session or owner.get('session')
            if a.action == 'attempt' and not a.desk:
                raise ValueError('attempt requires --desk')
            record = checkpoint(ROOT, runtime, session, a.chapter,
                                a.note_file.read_text() if a.note_file else None,
                                a.desk if a.action == 'attempt' else None)
            print(json.dumps(record, indent=2, ensure_ascii=False))
        return 0
    except (ValueError, OSError, KeyError, subprocess.TimeoutExpired) as exc:
        print('runtime_handoff: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
