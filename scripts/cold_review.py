#!/usr/bin/env python3
"""Fresh conformance review with only two supplied text artifacts.

No author transcript, book path, research brief, or draft apparatus is passed.
Uses a temporary working directory and disables host customization and tools
that can retrieve additional context. This is not an OS read-isolation claim.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def prompt(outline, prose):
    spec = (ROOT / '.claude/agents/gw-specchecker.md').read_text().split('\n---\n', 1)[1]
    # Prose-only input; Draft Notes would contaminate the clean-room check.
    for heading in ('\n## Draft Notes', "\n## Editor's Notes", '\n## Editor’s Notes'):
        prose = prose.split(heading, 1)[0]
    return spec + '\n\nUse only the two supplied inputs. Do not use tools or look for other files.\n' + json.dumps(
        {'outline_section': outline, 'prose': prose}, ensure_ascii=False)


def command(directory, output):
    cmd = ['codex', 'exec', '--ignore-user-config', '--ignore-rules', '--ephemeral',
           '--skip-git-repo-check', '-C', str(directory), '-s', 'read-only',
           '-m', 'gpt-6-astra', '-c', 'model_reasoning_effort="low"',
           '-c', 'approval_policy="never"', '-c', 'web_search="disabled"',
           '-c', 'agents.enabled=false', '-o', str(output)]
    for flag in ('shell_tool', 'unified_exec', 'view_image', 'apps', 'plugins', 'remote_plugin',
                 'browser_use', 'browser_use_external', 'computer_use', 'code_mode_host',
                 'skill_search', 'memories', 'goals', 'hooks', 'image_generation'):
        cmd += ['--disable', flag]
    cmd += ['--enable', 'skip_host_skill_discovery', '-']
    return cmd


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--outline', type=Path, required=True, help='chapter section only, not the entire outline')
    ap.add_argument('--prose', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    try:
        task = prompt(a.outline.read_text(), a.prose.read_text())
        if a.dry_run:
            print(task)
            return 0
        output = a.out.resolve()
        if not output.is_relative_to((ROOT / 'runs').resolve()):
            raise ValueError('the Publisher must store reports under runs/')
        output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='gw-cold-review-') as directory:
            # Output is collected by the Publisher after the child exits.
            result = Path(directory) / 'report.md'
            p = subprocess.run(command(directory, result), input=task, text=True,
                               capture_output=True, timeout=300)
            if p.returncode or not result.is_file():
                raise ValueError('cold review failed: ' + (p.stderr[-2000:] or p.stdout[-2000:]))
            output.write_text(result.read_text())
        print('Cold conformance report: ' + str(output))
        return 0
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print('cold_review: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
