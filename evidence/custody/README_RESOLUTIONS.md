# Resolution Layer

A camada de resolução preserva `evidence-ledger.v1.jsonl` como registro histórico e aplica `evidence-resolutions.v1.jsonl` para produzir uma visão efetiva verificável.

Fluxo:

`historical ledger -> append-only resolutions -> resolve_custody.py -> effective JSONL -> CI receipt`

Regras:

- `FILL_TOKEN_VAZIO` só preenche campo vazio, valor idêntico ou timestamp verificado mais específico da mesma data.
- `CORRECT_WITH_EVIDENCE` exige `evidence_delta` e fonte explícita.
- promoção de classe de capacidade não pode ocorrer por resolution patch; exige novo proof/receipt.
- downgrade sustentado por evidência é permitido para impedir overstated claims.
- a visão efetiva é artefato gerado; a fonte canônica continua sendo ledger + resolution ledger.
