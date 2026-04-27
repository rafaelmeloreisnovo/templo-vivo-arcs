from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


def gerar_hash_arquivo(arquivo: Path) -> str:
    data = arquivo.read_bytes()
    return hashlib.sha256(data).hexdigest()


def registrar_hash(arquivo: Path, destino: Path) -> str:
    digest = gerar_hash_arquivo(arquivo)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(f"{digest}  {arquivo}\n", encoding="utf-8")
    return digest


def registrar_timestamp(destino: Path) -> str:
    agora = datetime.now(timezone.utc).isoformat()
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("a", encoding="utf-8") as f:
        f.write(agora + "\n")
    return agora


def merkle_root_hashes(hashes: Iterable[str]) -> str:
    nivel = [bytes.fromhex(h) for h in hashes]
    if not nivel:
        return hashlib.sha256(b"").hexdigest()
    while len(nivel) > 1:
        if len(nivel) % 2 == 1:
            nivel.append(nivel[-1])
        prox = []
        for i in range(0, len(nivel), 2):
            prox.append(hashlib.sha256(nivel[i] + nivel[i + 1]).digest())
        nivel = prox
    return nivel[0].hex()
