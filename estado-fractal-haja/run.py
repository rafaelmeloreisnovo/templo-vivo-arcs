from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from src.core.estado import Estado
from src.core.fractal import Fractal
from src.core.haja import haja
from src.espiritual.rituais import RITUAIS_BASE
from src.espiritual.templo import Templo
from src.governance.regras import REGRAS_BASE
from src.governance.validacao import validar_regras
from src.proof.prova import registrar_hash, registrar_timestamp


@dataclass
class ModuloLog:
    nome: str

    def executar(self) -> None:
        print(f"[MÓDULO] {self.nome} em execução")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nome", default="Estado Fractal HAJA")
    parser.add_argument("--profundidade", type=int, default=3)
    parser.add_argument("--registro", default="manifesto/livro-vivo.md")
    args = parser.parse_args()

    estado = Estado(nome=args.nome)
    estado.adicionar_modulo(ModuloLog("governança"))
    estado.adicionar_modulo(ModuloLog("prova"))
    estado.adicionar_modulo(ModuloLog("templo_vivo"))

    validacao = validar_regras(REGRAS_BASE)
    if not validacao.valido:
        print(f"[ERRO] Pendências de compliance: {validacao.pendencias}")
        raise SystemExit(2)

    fractal = Fractal(estado=estado, profundidade=args.profundidade)
    fractal.expandir()
    haja(estado)

    templo = Templo()
    for ritual in RITUAIS_BASE:
        templo.adicionar_pratica(ritual)
    templo.executar_culto()

    alvo = Path(args.registro)
    hash_out = Path("proof/hashes/hash.txt")
    time_out = Path("proof/timestamps/time.txt")

    digest = registrar_hash(alvo, hash_out)
    ts = registrar_timestamp(time_out)

    print(f"[PROVA] SHA256: {digest}")
    print(f"[PROVA] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
