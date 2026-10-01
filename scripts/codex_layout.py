#!/usr/bin/env python3
"""Generate Codex adapters from canonical .claude instructions."""
import json
from pathlib import Path


def agent_file(path):
    raw = path.read_text()
    head, body = raw[4:].split('\n---\n', 1)
    fields = dict(line.split(':', 1) for line in head.splitlines() if ':' in line)
    fields = {k: v.strip() for k, v in fields.items()}
    # TOML JSON-compatible strings preserve every byte of the desk mandate.
    values = {'name': fields['name'], 'description': fields['description'],
              'model': 'gpt-6-astra', 'model_reasoning_effort': 'low',
              'sandbox_mode': 'read-only' if not any(t in fields.get('tools', '')
                                                   for t in ('Write', 'Edit')) else 'workspace-write',
              'developer_instructions': body.strip() + '\n\n'
              'Run with fresh context and the explicitly commissioned artifacts only. '
              'Do not inherit the author conversation. The Publisher records your report. '
              'Never approve concepts, land chapters, edit books/, or grade your own prose. '
              'When writing is permitted, use only the assigned apparatus output paths. '
              'The conformance checker sees only the outline section and prose. '
              'If runtime permissions cannot preserve these boundaries, report the limitation.'}
    return '# Derived from ' + path.parent.name + '/' + path.name + '; edit .claude/agents only.\n' + '\n'.join(
        k + ' = ' + json.dumps(v, ensure_ascii=False) for k, v in values.items()) + '\n'


def outputs(root):
    files = {'.codex/config.toml': '# House runtime defaults; desktop session overrides may take precedence.\n'
             'model = "gpt-6-astra"\nmodel_reasoning_effort = "low"\n\n'
             '[agents]\nenabled = true\ndefault_subagent_model = "gpt-6-astra"\n'
             'default_subagent_reasoning_effort = "low"\nmax_concurrent_threads_per_session = 3\n'}
    events = {}
    for event in ('SessionStart', 'UserPromptSubmit', 'PreToolUse', 'SubagentStart', 'SubagentStop', 'Stop', 'Interrupt', 'SessionEnd'):
        cmd = 'python3 "$(git rev-parse --show-toplevel)/scripts/runtime_hook.py" codex ' + event
        hook = {'type': 'command', 'command': cmd, 'timeout': 180 if event == 'Stop' else 120}
        if event in ('Interrupt', 'SessionEnd'):
            hook['timeout'] = 3
        events[event] = [{'hooks': [hook]}]
    files['.codex/hooks.json'] = json.dumps({'hooks': events}, indent=2) + '\n'
    for path in sorted((root / '.claude/agents').glob('*.md')):
        files['.codex/agents/' + path.stem + '.toml'] = agent_file(path)
    return files


def sync(root):
    root = Path(root)
    for name, text in outputs(root).items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    for path in (root / '.codex/agents').glob('*.toml'):
        if '.codex/agents/' + path.name not in outputs(root):
            path.unlink()
    # Repo-native discovery avoids installation, caches, and duplicate skill copies.
    dest = root / '.agents/skills'
    dest.mkdir(parents=True, exist_ok=True)
    wanted = {p.name for p in (root / '.claude/skills').iterdir() if p.is_dir()}
    for name in sorted(wanted):
        path = dest / name
        target = '../../.claude/skills/' + name
        if path.is_symlink():
            if str(path.readlink()) == target:
                continue
            path.unlink()
        elif path.exists():
            raise ValueError('refusing to overwrite an authored skill: ' + str(path))
        path.symlink_to(target, target_is_directory=True)
    for path in dest.iterdir():
        if path.is_symlink() and path.name not in wanted:
            path.unlink()
    return len(outputs(root)) + len(wanted)


def check(root):
    root = Path(root)
    drift = []
    expected = outputs(root)
    for name, text in expected.items():
        path = root / name
        if not path.is_file() or path.read_text() != text:
            drift.append(name + ' missing or differs from canonical runtime definitions')
    for path in (root / '.codex/agents').glob('*.toml'):
        if '.codex/agents/' + path.name not in expected:
            drift.append(str(path.relative_to(root)) + ' is stale')
    wanted = {p.name for p in (root / '.claude/skills').iterdir() if p.is_dir()}
    for name in wanted:
        path = root / '.agents/skills' / name
        if not path.is_symlink() or str(path.readlink()) != '../../.claude/skills/' + name:
            drift.append('.agents/skills/' + name + ' is not linked to the canonical skill')
    for path in (root / '.agents/skills').glob('*'):
        if path.name not in wanted:
            drift.append(str(path.relative_to(root)) + ' is stale')
    return drift
