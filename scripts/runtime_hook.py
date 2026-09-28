#!/usr/bin/env python3
"""Translate runtime hook events into the same house lifecycle scripts."""
import json
import fcntl
import os
from pathlib import Path
import subprocess
import sys

import runtime_handoff as handoff


def dispatch(root, runtime, event, payload):
    session = payload.get('session_id')
    if not isinstance(session, str) or not session:
        raise ValueError('hook payload needs a session_id; writer ownership cannot be guessed')
    if event == 'SessionStart':
        owner = handoff.read(handoff.owner_path(root), {})
        if owner and not handoff.matches(owner, handoff.identity(runtime, session)):
            return f"Project currently owned by {owner['runtime']} session {owner['session']}. " + handoff.resume(root)
        state = root / '.claude/state'
        state.mkdir(parents=True, exist_ok=True)
        marker = state / 'runtime-session.json'
        previous = handoff.read(marker, {})
        # Resume and compaction must not discard the original review window.
        if previous != handoff.identity(runtime, session):
            (state / 'session-start-sha').write_text(handoff.git(root, 'rev-parse', 'HEAD') + '\n')
            handoff.atomic(marker, handoff.identity(runtime, session))
        p = subprocess.run([sys.executable, str(root / 'scripts/resolve_book.py')],
                           cwd=root, capture_output=True, text=True)
        if p.returncode:
            raise ValueError(p.stdout + p.stderr)
        env = dict(os.environ, GW_PROJECT_ROOT=str(root), GW_RUNTIME=runtime,
                   GW_KEEP_BRANCH='1', GW_PRESERVE_START='1')
        board = subprocess.run(['bash', str(root / '.claude/hooks/session-start.sh')],
                               cwd=root, env=env, capture_output=True, text=True, timeout=180)
        if board.returncode:
            raise ValueError(board.stderr or 'house startup failed')
        return board.stdout + '\n' + handoff.resume(root) + '\nRun scripts/inbox.py before production.'
    if event in ('UserPromptSubmit', 'PreToolUse'):
        handoff.claim(root, runtime, session)
        if event == 'UserPromptSubmit':
            handoff.record_prompt(root, runtime, session, payload)
            return handoff.resume(root)
        return ''
    if event in ('SubagentStart', 'SubagentStop'):
        handoff.desk_event(root, runtime, session, payload.get('agent_id'), event == 'SubagentStart')
        return ''
    if event == 'Stop':
        handoff.claim(root, runtime, session)
        if handoff.read(handoff.owner_path(root), {}).get('desks'):
            raise ValueError('active desks must finish or be stopped before the house can hand off')
        handoff.checkpoint(root, runtime, session)
        env = dict(os.environ, GW_PROJECT_ROOT=str(root), GW_RUNTIME=runtime)
        p = subprocess.run(['bash', str(root / '.claude/hooks/session-stop.sh')], cwd=root,
                           env=env, capture_output=True, text=True, timeout=180)
        if p.returncode:
            raise ValueError(p.stderr or p.stdout or 'house completion checks failed')
        handoff.release(root, runtime, session)
        return (p.stdout + p.stderr).strip()
    if event in ('Interrupt', 'SessionEnd'):
        owner = handoff.read(handoff.owner_path(root), {})
        if owner and handoff.matches(owner, handoff.identity(runtime, session)):
            # Do not release on interruption: pending desks may still be running.
            # Recovery is explicit after the author stops the old session.
            return 'Work interrupted; shared checkpoint retained. Stop all desks before switching runtimes.'
        return ''
    raise ValueError('unsupported event: ' + event)


def main():
    try:
        runtime, event = sys.argv[1:3]
        payload = json.load(sys.stdin)
        if runtime == 'auto':
            runtime = 'codex' if str(payload.get('model', '')).startswith('gpt-') else 'claude'
        # Package scripts are mechanics; the working repository owns book/state.
        root = Path(subprocess.check_output(['git', '-C', payload['cwd'], 'rev-parse', '--show-toplevel'], text=True).strip())
        # Plugin and project hooks can both be enabled. Serialize their
        # completion mechanics so git commits and logs cannot race.
        state = root / '.claude/state'
        state.mkdir(parents=True, exist_ok=True)
        with (state / 'runtime-hook.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            message = dispatch(root, runtime, event, payload)
        if event in ('PreToolUse',):
            print('{}')
        elif event == 'SessionStart':
            print(json.dumps({'hookSpecificOutput': {'hookEventName': event, 'additionalContext': message}}))
        elif event == 'UserPromptSubmit':
            print(json.dumps({'hookSpecificOutput': {'hookEventName': event, 'additionalContext': message}}))
        else:
            print(json.dumps({'systemMessage': message} if message else {}))
        return 0
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as exc:
        print('House runtime: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
