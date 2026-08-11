# Cadeia Estrutural de Custódia — V1

Estado: `AUDITABLE / APPEND_ONLY / CLAIM_GATE_ON`

Esta árvore materializa, em formato operacional, o protocolo já definido em `docs/auditoria/PROTOCOLO_FORENSE_PROVENIENCIA_E_CADEIA_CUSTODIA.md` e o ledger histórico `docs/auditoria/POC_EVIDENCE_LEDGER_2025.md`.

## Invariante

```text
ARTEFATO
  -> IDENTIDADE (blob/commit/hash)
  -> TEMPO
  -> AUTOR / COMMITTER / AGENTE
  -> DERIVAÇÃO
  -> CAPACIDADE C0..C6
  -> REPRODUÇÃO
  -> CLAIM GATE
  -> RECEIPT
  -> RETROALIMENTAÇÃO
```

Nenhum nível é promovido por narrativa, quantidade de texto ou semelhança semântica. Promoção requer `evidence_delta > 0`.

## Estrutura

```text
evidence/custody/
├── README.md
├── schema/
│   └── evidence-record.v1.schema.json
└── ledger/
    └── evidence-ledger.v1.jsonl

scripts/audit/
├── validate_custody.py
└── check_append_only.py

.github/workflows/
└── custody-chain.yml
```

### `schema/`

Contrato de cada `EvidenceRecord`. Campos desconhecidos permanecem `TOKEN_VAZIO` em vez de receber inferência silenciosa.

### `ledger/`

Registro canônico append-only. Uma linha JSON = uma unidade probatória. Correções não apagam a linha antiga: uma nova evidência deve ser acrescentada e ligada ao registro anterior.

### validator

`validate_custody.py` verifica:

- campos obrigatórios;
- unicidade de `proof_id`;
- formato de SHA e compatibilidade prefixo/SHA;
- classes C0–C6;
- estados de reprodução;
- claim gate;
- regra C5/C6;
- presença de fonte probatória;
- hash SHA-256 do próprio ledger.

### append-only gate

`check_append_only.py` rejeita remoção, reordenação ou alteração retroativa de linhas já existentes. Apenas novas linhas podem ser anexadas.

## Regra para correção

Se uma evidência antiga estiver errada ou incompleta, **não editar a linha histórica depois de publicada em `main`**. Adicionar um novo registro, por exemplo:

```text
POC-07
  -> CORR-POC-07-001
```

O registro corretivo deve declarar a evidência nova, o campo corrigido, a razão e o vínculo com o registro anterior.

## Claim gate

`claim_allowed=true` significa apenas que **o claim delimitado naquele registro** é sustentado pelas fontes declaradas. Não significa validade universal do projeto, novidade mundial, patente concedida ou autoria linha a linha.

Estados como `HISTORICAL_CLAIM`, `BLOCKED_PRIOR_ART` e `TOKEN_VAZIO` permanecem com `claim_allowed=false`.

## C5 / C6

- `C5_REPRODUCED` exige reprodução do checkout histórico relevante e receipt contemporâneo separado.
- `C6_INDEPENDENT` exige reprodução independente.
- receipt produzido hoje nunca retrodata execução para 2025.

## Seed V1

O ledger V1 parte das 11 unidades já catalogadas no `POC_EVIDENCE_LEDGER_2025.md`.

Nesta materialização inicial, três commits foram novamente resolvidos para SHA completo por consulta direta ao GitHub:

- `POC-00` — `Manifest.txt` — `ee9c7d4ab25e8e33c36994212d029039892a91ec`;
- `POC-04` — derivação por estado anterior — `48b62c7ea5269fa5a45a4a855469c45de4cc6dda`;
- `POC-07` — `scripts/cristal.sh` — `4fe1d9dce27a3f8023cbcdc116521e1ce90c3fc3`.

Os demais preservam o prefixo observado e usam `TOKEN_VAZIO` nos campos ainda não revalidados nesta passagem.

## Próxima expansão

1. resolver SHA completo + blob SHA dos POCs restantes;
2. registrar `first_known_event` para FCEA, RAIA, RAFAELIA, RAFCODE e ZIPRAF;
3. adicionar receipts C5 sem alterar artefatos históricos;
4. conectar evidência Drive/NOVOexport por fingerprints, nunca somente por nomes;
5. expandir o mesmo contrato para outros repositórios, mantendo `repository` explícito e cadeia cross-repo.
