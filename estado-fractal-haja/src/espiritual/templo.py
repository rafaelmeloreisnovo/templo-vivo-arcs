from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Templo:
    praticas: list[str] = field(default_factory=list)

    def adicionar_pratica(self, pratica: str) -> None:
        self.praticas.append(pratica)

    def executar_culto(self) -> None:
        for pratica in self.praticas:
            print(f"[TEMPLO] Executando: {pratica}")
