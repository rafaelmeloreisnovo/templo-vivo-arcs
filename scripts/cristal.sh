#!/usr/bin/env bash
set -euo pipefail
CHANGELOG=CHANGELOG.md
STAMP="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
HASH="$(git ls-files -z | xargs -0 sha256sum | sha256sum | cut -d' ' -f1)"
echo -e "\n## 💠 Cristal @ $STAMP\n- hash_berna: $HASH\n- tag_sugerida: Ω-RAFAELIA_MARTE-v0.1\n" >> "$CHANGELOG"
echo "[Cristal] $STAMP  hash=$HASH"
