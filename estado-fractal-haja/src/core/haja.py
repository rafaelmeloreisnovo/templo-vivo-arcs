from __future__ import annotations

from .estado import Estado


def haja(estado: Estado) -> None:
    print("[HAJA] EXECUÇÃO AUTORIZADA")
    estado.executar()
