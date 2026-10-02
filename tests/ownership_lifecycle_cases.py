"""Regression cases for leases stranded by late hooks, session end and reboot."""
import json
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import patch

import runtime_handoff as h
import runtime_hook


def ownership_lifecycle_cases():
    rows = []

    def result(ok, name, detail=''):
        rows.append((ok, 'ownership lifecycle: ' + name,
                     'Dead sessions cannot strand the project; active writers stay protected', detail))

    with tempfile.TemporaryDirectory(prefix='gw-ownership-') as directory:
        root = Path(directory)
        subprocess.run(['git', 'init', '-q', str(root)], check=True)
        subprocess.run(['git', '-C', str(root), '-c', 'user.name=Fixture',
                        '-c', 'user.email=fixture@example.test', 'commit',
                        '--allow-empty', '-qm', 'fixture'], check=True)
        scripts = root / 'scripts'
        scripts.mkdir()
        (scripts / 'next.py').write_text('import json; print(json.dumps({"chapter":14,"stage":"review"}))\n')
        hooks = root / '.claude/hooks'
        hooks.mkdir(parents=True)
        (hooks / 'session-stop.sh').write_text('echo completion >> completion-count\nexit 2\n')
        saved = root / 'runs/handoff.json'
        saved.parent.mkdir()
        saved.write_text(json.dumps(dict(schema=1, chapter=14, artifacts={},
                                        notes={'14': 'Unfinished exact author note.'},
                                        failed_attempts={'14:gw-ghostwriter': 2})))
        partial = root / 'runs/partial.md'
        partial.write_text('Unfinished manuscript stays here.\n')

        h.claim(root, 'codex', 'old')
        with patch.object(h, 'oracle', side_effect=ValueError('checkpoint unavailable')):
            try:
                runtime_hook.dispatch(root, 'codex', 'Stop', {'session_id': 'old'})
            except ValueError:
                pass
        retained = saved.read_bytes()
        result(h.owner_path(root).exists(), 'failed completion still protects active session')
        runtime_hook.dispatch(root, 'codex', 'SessionEnd', {'session_id': 'old'})
        result(not h.owner_path(root).exists() and saved.read_bytes() == retained
               and partial.read_text() == 'Unfinished manuscript stays here.\n',
               'session end releases failed completion without approving or deleting work')
        # Clear only the fixture so the old implementation can continue red.
        if h.owner_path(root).exists():
            h.recover(root, 'old')

        (hooks / 'session-stop.sh').write_text('echo completion >> completion-count\n')
        (root / 'completion-count').unlink(missing_ok=True)
        h.claim(root, 'codex', 'one')
        runtime_hook.dispatch(root, 'codex', 'Stop', {'session_id': 'one'})
        runtime_hook.dispatch(root, 'codex', 'Stop', {'session_id': 'one'})
        result(not (root / 'completion-count').exists() and not h.owner_path(root).exists(),
               'Stop only saves handoff and releases ownership; legacy completion never runs')
        h.desk_event(root, 'codex', 'one', 'late-desk', False)
        result(not h.owner_path(root).exists(), 'late desk stop does not resurrect released writer')
        if h.owner_path(root).exists():
            h.recover(root, 'one')

        h.claim(root, 'claude', 'new')
        try:
            runtime_hook.dispatch(root, 'codex', 'Stop', {'session_id': 'one'})
            h.desk_event(root, 'codex', 'one', 'late-desk', False)
            ok = h.read(h.owner_path(root), {})['session'] == 'new'
        except ValueError:
            ok = False
        result(ok, 'late hooks from previous session leave new writer alone')
        runtime_hook.dispatch(root, 'codex', 'SessionEnd', {'session_id': 'one'})
        result(h.read(h.owner_path(root), {})['session'] == 'new',
               'old SessionEnd cannot release another writer')
        h.release(root, 'claude', 'new')

        h.desk_event(root, 'codex', 'active', 'live-desk', True)
        runtime_hook.dispatch(root, 'codex', 'SessionEnd', {'session_id': 'active'})
        result(h.read(h.owner_path(root), {}).get('desks') == {'live-desk': 'active'},
               'session end retains ownership while desks are recorded active')
        h.desk_event(root, 'codex', 'active', 'live-desk', False)
        result(not h.owner_path(root).exists(), 'last desk releases writer after main session has ended')
        h.claim(root, 'codex', 'active')
        runtime_hook.dispatch(root, 'codex', 'Interrupt', {'session_id': 'active'})
        result(h.owner_path(root).exists(), 'interruption cannot release an unfinished active turn')
        h.release(root, 'codex', 'active')

        h.desk_event(root, 'codex', 'resumed', 'live-desk', True)
        runtime_hook.dispatch(root, 'codex', 'SessionEnd', {'session_id': 'resumed'})
        h.claim(root, 'codex', 'resumed')
        h.desk_event(root, 'codex', 'resumed', 'live-desk', False)
        result(h.owner_path(root).exists() and not h.read(h.owner_path(root), {}).get('ended'),
               'resuming an ended session cancels deferred release while the root is active')
        h.release(root, 'codex', 'resumed')

        if not hasattr(h, 'machine_boot'):
            result(False, 'reboot evidence supports automatic safe recovery', 'boot evidence not implemented')
            return rows
        with patch.object(h.sys, 'platform', 'darwin'), patch.object(h.subprocess, 'run') as run:
            run.return_value = subprocess.CompletedProcess([], 0,
                '{ sec = 1790883184, usec = 244504 } Thu Oct 1 14:33:04 2026\n', '')
            result(h.machine_boot() == {'host': h.socket.gethostname(), 'boot': '1790883184:244504'},
                   'macOS boot identity parses kernel seconds and microseconds')
            run.return_value = subprocess.CompletedProcess([], 1, '', 'Operation not permitted')
            result(h.machine_boot() is None, 'denied macOS boot query fails conservatively')
        before = saved.read_bytes()
        old_boot = {'host': 'fixture-mac', 'boot': 'old'}
        new_boot = {'host': 'fixture-mac', 'boot': 'new'}
        with patch.object(h, 'machine_boot', return_value=old_boot):
            h.desk_event(root, 'codex', 'pre-reboot', 'crashed-desk', True)
        with patch.object(h, 'machine_boot', return_value=new_boot):
            h.claim(root, 'claude', 'post-reboot')
        recovery = h.read(root / '.claude/state/runtime-recovery.json', {})
        result(h.read(h.owner_path(root), {})['session'] == 'post-reboot'
               and recovery['owner']['session'] == 'pre-reboot'
               and recovery['reason'] == 'machine restarted' and saved.read_bytes() == before,
               'reboot clears dead desks and owner while preserving handoff and recovery evidence')
        h.release(root, 'claude', 'post-reboot')

        for name, recorded, observed in [
                ('same boot', old_boot, old_boot),
                ('different host', old_boot, {'host': 'another-mac', 'boot': 'new'}),
                ('unknown boot', old_boot, None),
                ('legacy owner', None, new_boot)]:
            owner = dict(runtime='codex', session='protected', desks={}, machine=recorded)
            h.atomic(h.owner_path(root), owner)
            with patch.object(h, 'machine_boot', return_value=observed):
                refused = False
                try:
                    h.claim(root, 'claude', 'intruder')
                except ValueError:
                    refused = True
            result(refused and h.read(h.owner_path(root), {}) == owner,
                   name + ' cannot expire ownership without positive reboot evidence')
            h.recover(root, 'protected')

        h.atomic(h.owner_path(root), dict(runtime='codex', session='legacy', desks={}))
        with patch.object(h, 'machine_boot', return_value=new_boot):
            h.claim(root, 'codex', 'legacy')
        result(h.read(h.owner_path(root), {})['machine'] == new_boot,
               'matching live session upgrades legacy ownership for future reboot recovery')
        h.release(root, 'codex', 'legacy')

        # Exercise the real stdin/stdout hook protocol with a failed completion.
        hook_script = str(Path(runtime_hook.__file__).resolve())
        (hooks / 'session-stop.sh').write_text('exit 2\n')
        h.claim(root, 'codex', 'native')
        payload = json.dumps(dict(cwd=str(root), session_id='native'))
        (scripts / 'next.py').write_text('raise SystemExit("checkpoint unavailable")\n')
        stopped = subprocess.run(['python3', hook_script, 'codex', 'Stop'],
                                 input=payload, text=True, capture_output=True)
        retained = saved.read_bytes()
        ended = subprocess.run(['python3', hook_script, 'codex', 'SessionEnd'],
                               input=payload, text=True, capture_output=True, timeout=3)
        result(stopped.returncode == 2 and ended.returncode == 0
               and isinstance(json.loads(ended.stdout), dict) and not h.owner_path(root).exists()
               and saved.read_bytes() == retained,
               'native SessionEnd releases after failed Stop within three-second deadline', ended.stderr)
        failure = h.read(root / '.claude/state/runtime-hook-failure-Stop.json', {})
        result(failure.get('session') == 'native' and failure.get('event') == 'Stop'
               and 'checkpoint unavailable' in failure.get('error', ''),
               'completion failure records original cause for later diagnosis')
    return rows


if __name__ == '__main__':
    rows = ownership_lifecycle_cases()
    for ok, name, _, detail in rows:
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail else ''))
    raise SystemExit(any(not row[0] for row in rows))
