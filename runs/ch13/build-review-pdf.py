"""Compatibility helper: refresh the canonical Chapter 13 packet."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from compile_current import chapter
print(chapter(ROOT / 'books/the-stoic-husband', 13, [13]))
