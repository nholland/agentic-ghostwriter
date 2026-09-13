#!/usr/bin/env python3
"""STUB for the engine's test harness only. It is not the validator and must
never be copied anywhere a real bundle is checked. The real one lives in the
book repo; okf_gate.py delegates to it. This stub exists so resolve_book's
required-dependency check passes against the fixture and okf_new's post-write
validation has something to call. It always exits 0."""
import sys
print("stub validator: fixture bundle accepted (this is a test stand-in, not a check)")
sys.exit(0)
