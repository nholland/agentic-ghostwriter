#!/usr/bin/env python3
"""Publish the current chapter and collection PDFs, replacing stable filenames.

python3 scripts/compile_current.py --chapters 11 12 13 --include-run 13
Sources remain authoritative; exports and their assets live in output/compiled/.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime

import compile as assembly
import chapter_pdf_local as renderer
import resolve_book

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/compiled'


def source(book, n, include_runs):
    return ROOT / 'runs' / f'ch{n:02}' if n in include_runs else book / 'chapters' / f'ch{n:02}'


def plate(svg, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    w, h = renderer.svg_to_png(str(svg), str(destination))
    return ('END', str(destination), '', (w, h))


def chapter(book, n, include_runs=()):
    src = source(book, n, include_runs)
    out = OUT / 'chapters' / f'ch{n:02}.pdf'
    out.parent.mkdir(parents=True, exist_ok=True)
    actual_n, prose, dist = assembly.draft_inputs(src / 'refined.md', src / 'distillation.md')
    assert actual_n == n, 'Chapter source number mismatch'
    svg = ROOT / 'runs' / f'ch{n:02}' / 'plate.svg'
    plates = [plate(svg, out.parent / f'ch{n:02}-plate.png')]
    renderer.build(prose, dist, plates, str(out), prose.splitlines()[0].lstrip('# ') +
                   (' (author review)' if n in include_runs else ''), base_dir=str(src))
    subprocess.run([sys.executable, str(ROOT/'scripts/package_check.py'), str(out.with_suffix('.html'))], check=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--chapters', nargs='+', type=int, default=None)
    ap.add_argument('--include-run', action='append', type=int, default=[])
    args = ap.parse_args()
    root, _, _ = resolve_book.resolve(resolve_book.load_config())
    info = resolve_book.inspect(root, require_okf=True)['info']
    book = Path(root) / info['bookRootRelative']
    OUT.mkdir(parents=True, exist_ok=True)
    chapters = sorted({int(p.parent.name[2:]) for p in (book/'chapters').glob('ch[0-9][0-9]/refined.md')} | set(args.include_run))
    assert chapters == list(range(1, max(chapters)+1)), 'Missing chapter in collection'
    outputs = [chapter(book, n, args.include_run) for n in (args.chapters or chapters)]
    command = [sys.executable, str(ROOT/'scripts/compile.py'), '--plates', '--no-pdf', '--outdir', str(OUT/'assets')]
    for n in args.include_run:
        command += ['--include-run', str(n)]
    subprocess.run(command, check=True)
    manuscript = OUT/'assets/manuscript.md'
    renderer.build(manuscript.read_text(), None, [], str(OUT/'book.pdf'),
                   f'The Stoic Husband: through Chapter {max(chapters)} (author review)', base_dir=str(manuscript.parent))
    subprocess.run([sys.executable, str(ROOT/'scripts/package_check.py'), str(OUT/'book.html')], check=True)
    dist_html, sources = [], {}
    for n in chapters:
        src = source(book, n, args.include_run)
        for name in ['refined.md', 'distillation.md']:
            p = src/name
            sources[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
        dist_html.append('<section class="dist">' + renderer.distillation_html((src/'distillation.md').read_text(), 'Chapter distillation') + '</section>')
        svg = ROOT/'runs'/f'ch{n:02}'/'plate.svg'
        sources[str(svg.relative_to(ROOT))] = hashlib.sha256(svg.read_bytes()).hexdigest()
    renderer.render_html(''.join(dist_html), str(OUT/'distillations.pdf'), 'Chapter distillations (author review)')
    from plate_packet import build_packet
    plate_packet = build_packet(book, max(chapters))
    manifest = {'built': datetime.now().astimezone().isoformat(), 'coverage': f'Prologue, Introduction, Chapters 1-{max(chapters)}, relevant Arc openings and plates',
                'unapproved_chapters': args.include_run, 'source_sha256': sources,
                'outputs': sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*.pdf'))}
    manifest['plate_packet'] = plate_packet
    manifest['plates'] = {f'ch{n:02}': {'approved_identical_copy': assembly.chapter_plate(str(book), n)[1]} for n in chapters}
    for folder in [OUT, OUT/'chapters']:
        destination = OUT/'assets'/('chapters' if folder.name == 'chapters' else '')
        destination.mkdir(parents=True, exist_ok=True)
        for generated in list(folder.glob('*.html')) + list(folder.glob('*.png')):
            generated.replace(destination/generated.name)
    (OUT/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    (OUT/'README.md').write_text(
        '# Current compiled copies\n\n'
        + f'Coverage: {manifest["coverage"]}. This is the available book, not all 29 planned chapters.\n\n'
        + f'Unapproved chapter inputs: {args.include_run or "none"}. Plate approval status is recorded in manifest.json.\n\n'
        + '- [Book](book.pdf): prose, chapter/Arc plates, and chapter practices.\n'
        + '- [Distillations](distillations.pdf): full chapter distillations in order.\n'
        + '- [Plates](plates.pdf): chapter and Arc plates, each followed by its maintained plain-language explanation.\n'
        + '\nChapter PDFs include plate and distillation when built by compile_current.py:\n\n'
        + ''.join(f'- [{p.stem}](chapters/{p.name})\n' for p in sorted((OUT/'chapters').glob('*.pdf')))
        + '\nStable filenames are replaced on rebuild. Supporting HTML/images are in assets/. Sources and review reports remain in books/ and runs/.\n')

    print('Current PDFs:', OUT)


if __name__ == '__main__':
    main()
