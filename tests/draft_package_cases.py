#!/usr/bin/env python3
"""Draft-package regressions through compile.main, also called by tests/run.py."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
import compile as compiler


def draft_package_cases(module=compiler):
    rows = []
    fixtures = REPO / 'tests' / 'fixtures' / 'draft-package'
    source = (fixtures / 'chapter.md').read_text()
    full = (fixtures / 'distillation.md').read_text()

    def exercise(name, expected, draft=source, dist=full, extra=(), mutate=None,
                 no_pdf=True, render_rc=0, omit_dist_arg=False):
        with tempfile.TemporaryDirectory(prefix='gw-draft-package-') as tmp:
            root = Path(tmp)
            chapter = root / 'draft.md'; chapter.write_text(draft)
            distilled = root / 'distillation.md'
            if dist is not None:
                distilled.write_text(dist)
            argv = ['compile.py', '--draft', str(chapter)]
            if not omit_dist_arg:
                argv += ['--distillation', str(distilled)]
            if no_pdf:
                argv.append('--no-pdf')
            argv += list(extra)
            seen = []

            def renderer(repo, md, pdf, title):
                seen.append((Path(md).read_text(), pdf, title))
                return render_rc

            output = io.StringIO()
            with contextlib.ExitStack() as stack:
                stack.enter_context(patch.object(module, 'REPO', str(root)))
                stack.enter_context(patch.object(sys, 'argv', argv))
                stack.enter_context(patch.object(module, 'render_package', renderer, create=True))
                stack.enter_context(contextlib.redirect_stdout(output))
                stack.enter_context(contextlib.redirect_stderr(output))
                if mutate:
                    stack.enter_context(patch.object(module, 'assemble_draft', mutate, create=True))
                try:
                    rc = module.main()
                except SystemExit as exc:
                    rc = exc.code
            files = list(root.glob('output/compiled/assets/chapters/*.md'))
            text = files[0].read_text() if len(files) == 1 else ''
            if expected == 'complete':
                clean = source.split("## Editor's Notes")[0].strip()
                ok = (rc == 0 and text == clean + '\n\n' + full.strip() + '\n'
                      and len(files) == 1 and 'review-draft' in files[0].name)
                if not no_pdf:
                    ok = ok and len(seen) == 1 and seen[0][0] == text
            elif expected == 'render-failure':
                ok = rc != 0 and len(seen) == 1
            else:
                ok = rc != 0 and not seen and not files
            rows.append((ok, 'draft package: ' + name,
                         'requested content is checked in the real assembly caller before rendering',
                         {'exit': rc, 'outputs': len(files), 'renderer_calls': len(seen),
                          'diagnostic': output.getvalue().strip()}))

    exercise('full distillation follows chapter; notes excluded', 'complete')
    exercise('renderer receives all fields and every practice', 'complete', no_pdf=False)
    exercise('missing explicit distillation argument is refused', 'refuse', omit_dist_arg=True)
    exercise('missing distillation file is refused', 'refuse', dist=None)
    exercise('empty distillation is refused', 'refuse', dist='')
    exercise('wrong chapter distillation is refused', 'refuse',
             dist=full.replace('Chapter 11', 'Chapter 12'))
    exercise('title-only chapter is refused', 'refuse', draft='# Chapter 11: Speak or Endure\n')
    exercise('distillation without practices is refused', 'refuse',
             dist=full.split('**Practice:**')[0])
    exercise('empty practice field is refused', 'refuse',
             dist=full.split('**Practice:**')[0] + '**Practice:**\n')
    exercise('empty lesson is refused', 'refuse', dist=full.replace('Name the problem and listen.', ''))
    exercise('range arguments cannot silently change draft mode', 'refuse', extra=('--from', '1'))
    exercise('omitted distillation never reaches renderer', 'refuse', no_pdf=False,
             mutate=lambda prose, dist: (fixtures / 'missing-distillation.md').read_text())
    exercise('practice-only substitution cannot satisfy full request', 'refuse', no_pdf=False,
             mutate=lambda prose, dist: prose + '\n\n**Practice:**' + dist.split('**Practice:**')[1])
    exercise('lost final practice never reaches renderer', 'refuse', no_pdf=False,
             mutate=lambda prose, dist: prose + '\n\n' + dist.split('3. **Reactive.**')[0])
    exercise('reversed package never reaches renderer', 'refuse', no_pdf=False,
             mutate=lambda prose, dist: dist + '\n\n' + prose + '\n')
    exercise('renderer failure is not reported as success', 'render-failure', no_pdf=False, render_rc=1)
    return rows


if __name__ == '__main__':
    rows = draft_package_cases()
    for ok, name, why, detail in rows:
        print(('[ ok ] ' if ok else '[FAIL] ') + name)
        if not ok:
            print(detail)
    print('%d/%d draft-package fixtures pass' % (sum(row[0] for row in rows), len(rows)))
    sys.exit(0 if all(row[0] for row in rows) else 1)
