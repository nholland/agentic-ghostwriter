"""Behavioral fixtures for one house resumed through either runtime."""
import importlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from unittest.mock import patch

import codex_layout
import cold_review
import runtime_handoff as h
import runtime_hook


def runtime_cases():
    rows = []

    def result(ok, name, detail=''):
        rows.append((ok, 'shared runtime: ' + name, 'Claude and Codex share durable production state', detail))

    def agent_settings(path):
        # Generated adapters use single-line TOML strings, a JSON-compatible subset.
        return {k.strip(): json.loads(v.strip()) for line in path.read_text().splitlines()
                if not line.startswith('#') and ' = ' in line
                for k, v in [line.split(' = ', 1)]}

    source = Path(__file__).resolve().parents[1]
    state_oracle = importlib.import_module('next')
    with tempfile.TemporaryDirectory(prefix='gw-runtime-fixtures-') as directory:
        root = Path(directory)
        subprocess.run(['git', 'init', '-q', str(root)], check=True)
        subprocess.run(['git', '-C', str(root), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test',
                        'commit', '--allow-empty', '-qm', 'fixture'], check=True)
        shutil.copytree(source / '.claude/agents', root / '.claude/agents')
        shutil.copytree(source / '.claude/skills', root / '.claude/skills')
        chapter = root / 'runs/ch14'
        chapter.mkdir(parents=True)
        (chapter / 'interview.md').write_text('Exact author words.\n')

        def oracle(project, number=None):
            stage, command, detail = state_oracle.chapter_state(14, str(chapter))
            return dict(chapter=14, stage=stage, command=command, detail=detail)

        with patch.object(h, 'oracle', oracle):
            h.claim(root, 'claude', 'c1')
            rejected = False
            try:
                h.claim(root, 'codex', 'x1')
            except ValueError:
                rejected = True
            result(rejected, 'second writer is rejected')
            text = 'He said: "keep the unfinished question exactly as asked."\n'
            first = h.checkpoint(root, 'claude', 'c1', 14, text, 'gw-ghostwriter')
            h.release(root, 'claude', 'c1')
            h.claim(root, 'codex', 'x1')
            resumed = json.loads(h.resume(root))
            result(resumed['current_oracle']['stage'] == 'research' and resumed['checkpoint']['notes']['14'] == text,
                   'Claude interview resumes in Codex with exact unfinished note')
            result(resumed['checkpoint']['failed_attempts']['14:gw-ghostwriter'] == 1,
                   'failed attempt survives Claude-to-Codex switch')
            second = h.checkpoint(root, 'codex', 'x1', 14, failed_desk='gw-ghostwriter')
            h.release(root, 'codex', 'x1')
            h.claim(root, 'claude', 'c2')
            result(json.loads(h.resume(root))['checkpoint']['failed_attempts']['14:gw-ghostwriter'] == 2,
                   'second failed round survives Codex-to-Claude switch')
            rejected = False
            try:
                h.checkpoint(root, 'claude', 'c2', 14, failed_desk='gw-ghostwriter')
            except ValueError:
                rejected = True
            result(rejected, 'switch cannot grant a third failed round')

            (chapter / 'research.md').write_text('brief\n')
            (chapter / 'proposed-concepts.md').write_text('---\nstatus: open\n---\n## Proposed meaning\n')
            h.checkpoint(root, 'claude', 'c2', 14)
            h.release(root, 'claude', 'c2')
            h.claim(root, 'codex', 'x2')
            result(json.loads(h.resume(root))['current_oracle']['stage'] == 'concepts',
                   'pending concept decision stays pending across switch')
            (chapter / 'interview.md').write_text('Author changed the story.\n')
            result('runs/ch14/interview.md' in json.loads(h.resume(root))['changed_artifacts'],
                   'changed input is reported before reuse of old checks')
            h.checkpoint(root, 'codex', 'x2', 14)
            saved = (root / 'runs/handoff.json').read_bytes()
            h.checkpoint(root, 'codex', 'x2', 14)
            result(saved == (root / 'runs/handoff.json').read_bytes(), 'unchanged Stop checkpoint is idempotent')

            h.record_prompt(root, 'codex', 'x2', {'turn_id': 't1', 'prompt': 'My exact author statement.'})
            h.record_prompt(root, 'codex', 'x2', {'turn_id': 't1', 'prompt': 'My exact author statement.'})
            rec = h.read(root / 'runs/handoff.json', {})
            intake = h.read(root / rec['author_records'][0], [])
            result(len(intake) == 1 and intake[0]['prompt'] == 'My exact author statement.',
                   'intake survives interruption without duplicate turn records')
            h.desk_event(root, 'codex', 'x2', 'desk-1', True)
            refused = False
            try:
                runtime_hook.dispatch(root, 'codex', 'Stop', {'session_id': 'x2'})
            except ValueError:
                refused = True
            result(refused and h.read(h.owner_path(root), {}).get('desks'),
                   'completion waits for active desks before releasing writer')
            h.desk_event(root, 'codex', 'x2', 'desk-1', False)
            runtime_hook.dispatch(root, 'codex', 'Interrupt', {'session_id': 'x2'})
            result(h.read(h.owner_path(root), {})['session'] == 'x2', 'interruption keeps lease while desks may run')
            refused = False
            try:
                h.recover(root, 'wrong-session')
            except ValueError:
                refused = True
            result(refused, 'crash recovery requires exact stopped session')
            h.recover(root, 'x2')
            result(not h.owner_path(root).exists() and (root / 'runs/handoff.json').exists(),
                   'explicit recovery preserves checkpoint and partial work')
            rejected = False
            try:
                h.fingerprint(root, '../outside')
            except ValueError:
                rejected = True
            result(rejected, 'checkpoint artifact paths cannot escape project')

        # Run the actual hook protocol in another runtime, with fake production
        # mechanics so fixture checks cannot commit the real book or call models.
        scripts = root / 'scripts'
        scripts.mkdir()
        (scripts / 'resolve_book.py').write_text('print("fixture book resolved")\n')
        (scripts / 'next.py').write_text('import json; print(json.dumps({"chapter":14,"stage":"concepts","command":"/gw-chapter","detail":"pending author"}))\n')
        hooks = root / '.claude/hooks'
        hooks.mkdir()
        (hooks / 'session-start.sh').write_text('echo "fixture board"\n')
        (hooks / 'session-stop.sh').write_text('if [ -f completion-fails ]; then echo "unreconciled" >&2; exit 2; fi\necho "fixture completion"\n')

        def run_hook(runtime, event, session, **fields):
            payload = dict(cwd=str(root), session_id=session, **fields)
            return subprocess.run(['python3', str(source / 'scripts/runtime_hook.py'), runtime, event],
                                  input=json.dumps(payload), capture_output=True, text=True)

        started = run_hook('codex', 'SessionStart', 'native-x')
        result(started.returncode == 0 and 'hookSpecificOutput' in json.loads(started.stdout),
               'native Codex startup emits valid context JSON', started.stderr)
        submitted = run_hook('codex', 'UserPromptSubmit', 'native-x', turn_id='native-turn', prompt='Exact native intake.')
        result(submitted.returncode == 0 and h.read(h.owner_path(root), {})['runtime'] == 'codex',
               'native prompt hook acquires shared ownership', submitted.stderr)
        (root / 'completion-fails').touch()
        stopped = run_hook('codex', 'Stop', 'native-x')
        result(stopped.returncode == 2 and h.owner_path(root).exists(),
               'failed completion retains writer and blocks handoff', stopped.stderr)
        (root / 'completion-fails').unlink()
        stopped = run_hook('codex', 'Stop', 'native-x')
        result(stopped.returncode == 0 and isinstance(json.loads(stopped.stdout), dict)
               and not h.owner_path(root).exists(), 'successful completion releases writer with valid Stop JSON')
        before = (root / 'runs/handoff.json').read_bytes()
        again = run_hook('codex', 'Stop', 'native-x')
        result(again.returncode == 0 and before == (root / 'runs/handoff.json').read_bytes(),
               'repeated native Stop does not rewrite checkpoint')
        run_hook('auto', 'SessionStart', 'native-c')
        submitted = run_hook('auto', 'UserPromptSubmit', 'native-c', prompt='Claude intake.')
        resumed = json.loads(h.resume(root))
        result(submitted.returncode == 0 and resumed['checkpoint']['runtime'] == 'claude'
               and resumed['current_oracle']['stage'] == 'concepts',
               'Claude adapter resumes the same pending decision after Codex')
        run_hook('auto', 'Stop', 'native-c')

        # Two completions from duplicate hook sources must not race git/log mechanics.
        (hooks / 'session-stop.sh').write_text('echo start >> hook-order\nsleep 0.1\necho end >> hook-order\n')
        h.claim(root, 'codex', 'parallel-stop')
        payload = json.dumps(dict(cwd=str(root), session_id='parallel-stop'))
        processes = [subprocess.Popen(['python3', str(source / 'scripts/runtime_hook.py'), 'codex', 'Stop'],
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      text=True) for _ in range(2)]
        for process in processes:
            process.stdin.write(payload)
            process.stdin.close()
        for process in processes:
            process.wait(timeout=10)
        result(all(p.returncode == 0 for p in processes)
               and (root / 'hook-order').read_text().splitlines() == ['start','end','start','end'],
               'duplicate hook sources serialize completion mechanics')

        codex_layout.sync(root)
        result(not codex_layout.check(root), 'fresh generation is in sync')
        p = root / '.codex/agents/gw-ghostwriter.toml'
        parsed = agent_settings(p)
        mandate = (root / '.claude/agents/gw-ghostwriter.md').read_text().split('\n---\n', 1)[1].strip()
        result(parsed['developer_instructions'].startswith(mandate) and parsed['model'] == 'gpt-6-astra',
               'generated desk preserves complete mandate and target model')
        read_only = agent_settings(root / '.codex/agents/gw-specchecker.toml')
        result(read_only['sandbox_mode'] == 'read-only', 'conformance desk is configured read-only')
        result((root / '.agents/skills/gw/SKILL.md').read_bytes() ==
               (root / '.claude/skills/gw/SKILL.md').read_bytes(), 'both runtimes discover identical skill source')
        p.write_text(p.read_text().replace('gpt-6-astra', 'wrong-model'))
        result(bool(codex_layout.check(root)), 'drift check catches altered model adapter')
        codex_layout.sync(root)
        result(not codex_layout.check(root), 'regeneration repairs adapter drift')

    task = cold_review.prompt('Outline-only sentinel', 'Prose-only sentinel\n## Draft Notes\nPRIVATE APPARATUS')
    result('Outline-only sentinel' in task and 'Prose-only sentinel' in task and 'PRIVATE APPARATUS' not in task,
           'isolated conformance input excludes draft apparatus')
    cmd = cold_review.command('/tmp/gw-review', '/tmp/gw-review/report.md')
    result('--ignore-user-config' in cmd and '--ephemeral' in cmd and 'shell_tool' in cmd
           and 'skip_host_skill_discovery' in cmd, 'cold runner uses fresh session without host skill discovery')
    return rows
