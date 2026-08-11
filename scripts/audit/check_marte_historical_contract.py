#!/usr/bin/env python3
"""Audit the exact historical Marte component contract without requiring full worktree materialization."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

COMMIT = "b1a57f568b8f4a9c8ed5b23c32b62d816b972a88"
FILES = {
    "dart": "lib/marte/marte.dart",
    "yaml": "assets/utopia_marte.yaml",
    "pubspec": "pubspec.yaml",
}
EXPECTED_BLOBS = {
    "dart": "673bc634edf1d63514b7c53b46e0db64d6174ccb",
    "yaml": "232578e215d15e118d841588ccdd90cdb26b1aa6",
    "pubspec": "30d677883df2496a31bb131a882644df59227ec9",
}


def git_show(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{COMMIT}:{path}"])


def main() -> int:
    subprocess.run(["git", "cat-file", "-e", f"{COMMIT}^{{commit}}"], check=True)
    blobs = {}
    payloads = {}
    for key, path in FILES.items():
        blob = subprocess.check_output(["git", "rev-parse", f"{COMMIT}:{path}"], text=True).strip()
        blobs[key] = blob
        if blob != EXPECTED_BLOBS[key]:
            raise SystemExit(f"blob mismatch for {path}: {blob} != {EXPECTED_BLOBS[key]}")
        payloads[key] = git_show(path)

    dart = payloads["dart"].decode("utf-8")
    pubspec = payloads["pubspec"].decode("utf-8")
    yaml_text = payloads["yaml"].decode("utf-8")

    dart_references_asset = "assets/utopia_marte.yaml" in dart
    parser_placeholder = "placeholder" in dart.casefold()
    pubspec_declares_exact_asset = "assets/utopia_marte.yaml" in pubspec
    yaml_present = bool(yaml_text.strip())

    state = {
        "historical_commit": COMMIT,
        "files": {
            key: {
                "path": FILES[key],
                "blob_sha": blobs[key],
                "sha256": hashlib.sha256(payloads[key]).hexdigest(),
            }
            for key in FILES
        },
        "dart_references_asset": dart_references_asset,
        "yaml_parser_placeholder": parser_placeholder,
        "pubspec_declares_exact_asset": pubspec_declares_exact_asset,
        "yaml_present": yaml_present,
        "runtime_bundle_state": (
            "BLOCKED_ASSET_UNDECLARED" if dart_references_asset and yaml_present and not pubspec_declares_exact_asset
            else "REVIEW_REQUIRED"
        ),
        "parser_state": "PLACEHOLDER" if parser_placeholder else "NOT_PLACEHOLDER_DETECTED",
        "claim_allowed_complete_app": False,
    }
    payload = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    Path("poc08-marte-contract-receipt.json").write_text(payload, encoding="utf-8")

    print(f"historical_commit={COMMIT}")
    print(f"runtime_bundle_state={state['runtime_bundle_state']}")
    print(f"parser_state={state['parser_state']}")
    print("claim_allowed_complete_app=false")
    print(f"receipt_sha256={hashlib.sha256(payload.encode('utf-8')).hexdigest()}")
    print("POC08_HISTORICAL_CONTRACT_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
