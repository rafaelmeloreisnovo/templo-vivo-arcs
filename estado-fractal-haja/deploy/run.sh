#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 run.py --nome "Estado Fractal HAJA" --profundidade 4 --registro manifesto/livro-vivo.md
