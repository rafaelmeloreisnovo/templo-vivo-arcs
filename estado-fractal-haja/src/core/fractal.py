from __future__ import annotations

from dataclasses import dataclass

from .estado import Estado


@dataclass
class Fractal:
    estado: Estado
    profundidade: int

    def expandir(self, nivel: int = 0) -> None:
        if nivel >= self.profundidade:
            return
        print(f"[FRACTAL] Expansão nível {nivel}")
        self.expandir(nivel + 1)
