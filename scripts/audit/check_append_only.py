#!/usr/bin/env python3
"""Fail if existing custody-ledger lines are edited, removed, or reordered."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LEDGER = Path("evidence/custody/ledger/evidence-ledger.v1.jsonl")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def main() -> int:
    if not LEDGER.is_file():
        print(f"ERROR: missing ledger: {LEDGER}", file=sys.stderr)
        return 2

    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD^"
    try:
        old = subprocess.check_output(
            ["git", "show", f"{base}:{LEDGER.as_posix()}"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
    except subprocess.CalledProcessError:
        print("APPEND_ONLY_GATE=PASS (ledger did not exist at base)")
        return 0

    new = LEDGER.read_text(encoding="utf-8").splitlines()
    if len(new) < len(old):
        print("ERROR: custody ledger shrank", file=sys.stderr)
        return 1
    if new[: len(old)] != old:
        print("ERROR: existing custody ledger content changed or was reordered", file=sys.stderr)
        return 1

    print(f"base={base}")
    print(f"old_records={len(old)}")
    print(f"new_records={len(new)}")
    print(f"appended={len(new) - len(old)}")
    print("APPEND_ONLY_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
