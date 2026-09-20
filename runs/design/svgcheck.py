#!/usr/bin/env python3
"""svgcheck.py - a shim. The geometry check moved to scripts/plate_check.py on
2026-09-20, which also checks anchors, charset, title, grounding, captions and
alignment. This name stays because the plate notes and inbox checks cite it;
it prints the old geometry-only report."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from plate_check import legacy  # noqa: E402

if __name__ == "__main__":
    legacy(sys.argv[1:])
