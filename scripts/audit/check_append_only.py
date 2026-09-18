#!/usr/bin/env python3
"""Fail if existing custody-ledger lines are edited, removed, or reordered."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

DEFAULT_LEDGER = Path("evidence/custody/ledger/evidence-ledger.v1.jsonl")


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD^"
    ledger = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_LEDGER

    if not ledger.is_file():
        print(f"ERROR: missing ledger: {ledger}", file=sys.stderr)
        return 2

    # A missing/invalid commit is not evidence that the ledger is new.
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}"],
            stderr=subprocess.DEVNULL, timeout=30,
        ).decode("ascii").strip()
        entries = subprocess.check_output(
            ["git", "ls-tree", "-z", commit, "--", ledger.as_posix()],
            stderr=subprocess.DEVNULL, timeout=30,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        print("ERROR: base commit cannot be verified", file=sys.stderr)
        return 2

    if not entries:
        print(f"ledger={ledger}")
        print("APPEND_ONLY_GATE=PASS (ledger did not exist at base)")
        return 0

    try:
        old = subprocess.check_output(
            ["git", "show", f"{commit}:{ledger.as_posix()}"],
            stderr=subprocess.DEVNULL, timeout=30,
        )
        new = ledger.read_bytes()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        print("ERROR: historical/current ledger cannot be read", file=sys.stderr)
        return 2
    if not new.startswith(old) or (len(new) > len(old) and old and not old.endswith(b"\n")):
        print(f"ERROR: historical bytes changed or append lacks a record boundary: {ledger}", file=sys.stderr)
        return 1

    print(f"ledger={ledger}")
    print(f"base={base}")
    print(f"old_records={len(old.splitlines())}")
    print(f"new_records={len(new.splitlines())}")
    print(f"appended={len(new.splitlines()) - len(old.splitlines())}")
    print("APPEND_ONLY_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
