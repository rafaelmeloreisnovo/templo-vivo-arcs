from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class ResultadoValidacao:
    valido: bool
    pendencias: list[str]


def validar_regras(regras: Dict[str, bool]) -> ResultadoValidacao:
    pendencias = [k for k, v in regras.items() if not v]
    return ResultadoValidacao(valido=not pendencias, pendencias=pendencias)
