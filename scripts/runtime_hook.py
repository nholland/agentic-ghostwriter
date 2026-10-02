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
        handoff.prune_stale(root)
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
        owner = handoff.read(handoff.owner_path(root), {})
        if not owner or not handoff.matches(owner, handoff.identity(runtime, session)):
            return ''  # Repeated/late Stop and blocked prompts do not acquire a writer.
        if owner.get('desks'):
            raise ValueError('active desks must finish or be stopped before the house can hand off')
        handoff.checkpoint(root, runtime, session)
        handoff.release(root, runtime, session)
        return ''
    if event == 'SessionEnd':
        owner = handoff.read(handoff.owner_path(root), {})
        if owner and handoff.matches(owner, handoff.identity(runtime, session)):
            # Ending a session is not production approval. The checkpoint is
            # already durable; resume reports any changed inputs. No long
            # completion mechanics can fit the native three-second timeout.
            with handoff.locked(root):
                owner = handoff.read(handoff.owner_path(root), {})
                if owner and handoff.matches(owner, handoff.identity(runtime, session)):
                    if owner.get('desks'):
                        owner['ended'] = handoff.datetime.now().astimezone().isoformat()
                        handoff.atomic(handoff.owner_path(root), owner)
                        return 'Session ended with active desks; writer releases when the last desk stops.'
                    handoff.retire(root, owner, 'session ended; unfinished work retained')
            return 'Session ended; writer released. Saved handoff and unfinished files retained; completion checks remain required.'
        return ''
    if event == 'Interrupt':
        owner = handoff.read(handoff.owner_path(root), {})
        if owner and handoff.matches(owner, handoff.identity(runtime, session)):
            # Do not release on interruption: pending desks may still be running.
            # Recovery is explicit after the author stops the old session.
            return 'Work interrupted; shared checkpoint retained. Stop all desks before switching runtimes.'
        return ''
    raise ValueError('unsupported event: ' + event)


def main():
    root, runtime, event, payload = None, None, None, {}
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
        # Keep the actual failing event after the UI has collapsed its output.
        # A later ownership rejection is a symptom, not the original failure.
        if root is not None and event in ('Stop', 'SessionEnd'):
            try:
                handoff.atomic(root / '.claude/state' / ('runtime-hook-failure-' + event + '.json'),
                               dict(runtime=runtime, session=payload.get('session_id'),
                                    event=event, error=str(exc),
                                    recorded=handoff.datetime.now().astimezone().isoformat()))
            except OSError:
                pass
        print('House runtime: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
