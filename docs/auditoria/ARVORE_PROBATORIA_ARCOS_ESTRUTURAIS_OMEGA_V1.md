# Árvore Probatória por Arcos Estruturais Ω — V1

Estado: `AUDITABLE / APPEND_ONLY / CLAIM_GATE_ON`
Data de consolidação: 2026-08-10

## 1. Finalidade

Consolidar as estruturas já identificadas na auditoria em análises distintas, conectadas por um arco evolutivo comum, sem transformar lacunas, incertezas, parábolas ou repetição narrativa em evidência.

## 2. Invariante de sustentação

`conteúdo -> registro -> identidade -> tempo -> proveniência -> transformação -> capacidade -> governança -> claim -> teste -> receipt -> retroalimentação`

Uma representação só é ligada a outra quando existe correspondência verificável: SHA/hash, path, message/conversation id, texto exato, URL de commit, diff ou transformação reproduzível.

## 3. Arcos estruturais

### A1 — Gênese e anterioridade
Fontes: NOVOexport, Drive, arquivos históricos, commits, PRs, tags/releases quando enumeradas.
Saída: `first_known_event` por conceito.
Gap crítico: evento de push histórico não deve ser inferido de commit.

### A2 — Proveniência e agentes
Separar `author`, `committer`, `agent`, `platform`, `reviewer` e `tool`.
Estado já sustentado no recorte: materialização pré-agente e PRs posteriores explicitamente associados ao Copilot.
Gap: autoria textual linha a linha e agente de eventos não explicitamente identificados.

### A3 — Integridade e cadeia de custódia
Âncoras: blob SHA, commit SHA, hashes internos, receipts, tags, releases e assinaturas quando existentes.
Regra: estado histórico nunca é sobrescrito por receipt posterior.
Gap: enumerar tags históricas e verificar assinatura/proteção individualmente.

### A4 — Capacidade e POCs
Escala: `C0_TEXTUAL -> C1_FORMAL -> C2_STRUCTURED -> C3_EXECUTABLE_PARTIAL -> C4_EXECUTABLE -> C5_REPRODUCED -> C6_INDEPENDENT`.
Estado: 11 unidades históricas catalogadas; `cristal.sh` em C4 com mecânica reproduzida em ambiente controlado, sem promover reprodução histórica integral.

### A5 — Convergência arquitetural
Invariante observada: `representação -> persistência -> identidade -> temporalidade -> derivação -> governança -> aplicação`.
Regra: convergência arquitetural não equivale a validação científica universal.

### A6 — Jurídico e propriedade intelectual
Separar: existência, autoria/proveniência, direito autoral, licença, segredo/know-how, candidato a patente, patente/registro oficial e prior art.
Regra: Git/Drive podem sustentar anterioridade e integridade; não concedem patente nem provam novidade mundial sozinhos.

### A7 — Falsificabilidade, urgência e finalização
Todo gap deve ter fonte esperada, ação, gate, evidência mínima, condição de falha e próximo estado.
`TOKEN_VAZIO` é estado auditável, nunca autorização para concluir.

## 4. Condução histórica já sustentada

`PR#1/artefato material -> commits materiais de 2025 -> método/POCs/governança -> primeiro PR Copilot comprovado -> organização/assistência posterior`

Exemplos do recorte auditado: `Manifest.txt`, `Entropia.md`, `Fe.py`, `Ciclo fe`, derivação por SHA, `RaIa∆`, `utopia_marte.yaml`, `cristal.sh`, `marte.dart`, `Patentes.md`, `LICENSE` e `Hashing times`.

## 5. Matriz de finalização

Cada conceito deve receber:

- `concept_id`
- `first_known_event`
- `source_type`
- `source_locator`
- `content_fingerprint`
- `commit_or_blob_sha`
- `agent_status`
- `capability_level`
- `legal_class`
- `claim_status`
- `contradictory_evidence`
- `open_gap`
- `next_action`
- `closure_criterion`

## 6. Prioridade

P0: NOVOexport↔Git; tags/SHAs; receipts históricos; identificação de agentes; reprodução C5 das POCs mais fortes.
P1: cross-repo FCEA/RAIA/RAFAELIA/RAFCODE; deduplicação semântica; prior-art por mecanismo.
P2: reprodução independente, assinaturas/attestations, registros formais de PI quando cabíveis.

## 7. Claim gate atual

- `PRE_AGENT_MATERIALIZATION = SUPPORTED_LIMITED`
- `PRE_AGENT_ARCHITECTURAL_CONVERGENCE = SUPPORTED_LIMITED`
- `PRE_AGENT_HASH_TIMESTAMP_POC = SUPPORTED_C4`
- `PRE_AGENT_APPLICATION_POC = SUPPORTED_PARTIAL_C3`
- `C5_HISTORICAL_REPRODUCED = NOT_YET`
- `WORLD_FIRST = BLOCKED_PENDING_PRIOR_ART`
- `PATENT_GRANTED = NOT_DEMONSTRATED`

## 8. Regra anti-regressão

Nenhum claim sobe por quantidade de texto. Promoção exige `evidence_delta > 0`. Conflito novo reabre o nó correspondente; evidência anterior permanece preservada. A árvore evolui por append-only e receipts.