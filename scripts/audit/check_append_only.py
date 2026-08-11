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

    try:
        old = subprocess.check_output(
            ["git", "show", f"{base}:{ledger.as_posix()}"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
    except subprocess.CalledProcessError:
        print(f"ledger={ledger}")
        print("APPEND_ONLY_GATE=PASS (ledger did not exist at base)")
        return 0

    new = ledger.read_text(encoding="utf-8").splitlines()
    if len(new) < len(old):
        print(f"ERROR: ledger shrank: {ledger}", file=sys.stderr)
        return 1
    if new[: len(old)] != old:
        print(f"ERROR: existing ledger content changed or was reordered: {ledger}", file=sys.stderr)
        return 1

    print(f"ledger={ledger}")
    print(f"base={base}")
    print(f"old_records={len(old)}")
    print(f"new_records={len(new)}")
    print(f"appended={len(new) - len(old)}")
    print("APPEND_ONLY_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
