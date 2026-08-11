# Custody Gaps, Vectors and Use Invariant — V1

Estado: `EVOLUTIVE / APPEND_ONLY / CLAIM_GATE_ON`
Data: 2026-08-10

## Invariante de uso

`evidência observada -> identidade -> temporalidade -> proveniência -> transformação -> capacidade -> reprodução -> claim gate -> receipt -> nova evidência`

A cadeia só evolui quando `evidence_delta > 0`. Informação ausente nunca é completada por narrativa. Uma resolução preenche ou corrige o estado efetivo sem apagar o registro histórico que originou a lacuna.

## Vetor de evolução

Para cada prova `p`:

`V(p) = <path, blob_sha, commit_sha, committed_at, author, committer, agent, derivation, capability, reproduction, claim>`

Estados de um componente:

- `RESOLVED`: fonte verificável localizada;
- `AGENT_UNKNOWN`: não há agente específico demonstrado;
- `TOKEN_VAZIO`: fonte necessária ainda não produziu evidência suficiente;
- `BLOCKED`: depende de fonte externa, ambiente ou validação independente;
- `CONFLICT`: evidência nova contradiz classificação anterior e exige resolução append-only.

## Delta desta passagem

Os 11 POCs históricos receberam resolução append-only para os campos recuperáveis no GitHub:

- SHA-40 completo dos commits antes incompletos;
- blob SHA histórico dos 11 artefatos;
- path histórico de RAIA;
- timestamps de commit em UTC onde a API auditada os expôs;
- author Git observado `rafaelmeloreisnovo` e committer `web-flow` nos commits verificados;
- `AGENT_UNKNOWN` quando nenhum agente específico está documentalmente identificado;
- aresta POC-04 reforçada pela resolução independente do source commit `1a8467...` e seu blob;
- POC-00 corrigido de C4 para C3 executável parcial por dependência de estado local/caminho absoluto não reproduzido.

## Lacunas residuais legítimas

1. `authored_at` separado de `committed_at`: o conector auditado não expõe os dois campos de data de forma separada; permanece `TOKEN_VAZIO`.
2. Identidade específica de IA/agente para eventos pré-Copilot: `AGENT_UNKNOWN`, não inferir por estilo textual.
3. POC-07 C5: exige checkout histórico exato + execução + receipt contemporâneo; workflow dedicado foi adicionado.
4. POC-08 C5: exige ambiente Flutter compatível e reprodução do asset/UI; placeholder YAML continua bloqueando produto completo.
5. POC-09: patente concedida, prior art e valuation independente exigem fontes externas oficiais/independentes.
6. POC-10: métricas de acurácia/erro exigem dataset, metodologia e receipt; continuam `claim_allowed=false`.
7. Evento histórico exato de push: commit incorporado não equivale a push event; permanece sem promoção.
8. Autoria intelectual linha a linha: Git author/committer não resolve origem textual de cada linha.

## Regra de não regressão

- Não alterar registro histórico para fazê-lo parecer mais completo.
- Preencher via resolution ledger.
- Downgrade por evidência contraditória é correção epistemicamente necessária, não regressão de custódia.
- Upgrade de capacidade exige novo proof/receipt; o resolver não permite promoção C0→C6 por simples patch.
- `WORLD_FIRST`, `PATENT_GRANTED` e validação científica não herdam valor de anterioridade interna.

## Uso transversal

O mesmo vetor pode ser aplicado posteriormente a Drive, NOVOexport e outros repositórios, desde que `repository/source_locator/fingerprint` permaneçam explícitos e relações cross-repo sejam arestas verificáveis, nunca fusão de identidades.
