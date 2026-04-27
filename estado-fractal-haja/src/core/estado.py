from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Protocol


class Executavel(Protocol):
    def executar(self) -> None:
        ...


@dataclass
class Estado:
    nome: str
    modulos: List[Executavel] = field(default_factory=list)

    def adicionar_modulo(self, modulo: Executavel) -> None:
        self.modulos.append(modulo)

    def executar(self) -> None:
        for modulo in self.modulos:
            modulo.executar()
