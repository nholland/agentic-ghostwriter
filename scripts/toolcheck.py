#!/usr/bin/env python3
"""Report dependencies of the one approved Chromium renderer; never install."""
import argparse
import importlib.util
import json
import shutil
import sys


def check_python(name):
    return importlib.util.find_spec(name) is not None


def check_binary(name):
    return shutil.which(name) is not None


def main():
    from pathlib import Path
    from chapter_pdf_local import CHROME, node_modules
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    rows = [
        {'tool': 'node', 'present': check_binary('node')},
        {'tool': 'Chromium', 'present': bool(CHROME) and Path(CHROME).is_file()},
        {'tool': 'playwright', 'present': (Path(node_modules()) / 'playwright').is_dir()},
    ]
    missing = [r['tool'] for r in rows if not r['present']]
    if args.json:
        print(json.dumps({'tools': rows, 'missing': missing}, indent=2))
    else:
        print('toolcheck: ' + ('missing ' + ', '.join(missing) if missing else 'approved PDF renderer dependencies present'))
    return 0

if __name__ == '__main__':
    sys.exit(main())
