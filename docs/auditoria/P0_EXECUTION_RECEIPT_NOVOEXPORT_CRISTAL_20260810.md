# P0 Execution Receipt — NOVOexport/Drive ↔ Git + Cristal — 2026-08-10

Estado: `PARTIAL_EXECUTION / EVIDENCE_DELTA_POSITIVE / CLAIM_GATE_ON`

## 1. Objetivo

Executar os dois P0 de maior ganho probatório definidos no mapa de rotas:

1. obter âncora temporal/proveniência adicional fora do Git para núcleos históricos;
2. testar a mecânica do `scripts/cristal.sh` e tentar promover `C4 -> C5` sem falsificar reprodução histórica.

## 2. Drive / NOVOexport — evidência observada

Foi localizada a camada estruturada de conversações em `CONVERSATIONS-00001.jsonl.txt`, contendo registros com `conversation_id`, `create_time`, `update_time`, `source_path`, `source_pointer`, `structural_hash`, `privacy_class=PRIVATE_DEFAULT_DENY` e `claim_allowed=false`.

Isso demonstra que existe uma fonte temporal/proveniencial machine-readable capaz de ser cruzada posteriormente com commits e artefatos. O arquivo observado referencia `conversations-003.json` em seus primeiros eventos; portanto o nome `CONVERSATIONS-00001` não deve ser interpretado como equivalência automática ao `conversations-000.json` original.

### Evidência RAIA no Drive

Foi observado `MANIFESTO_RAIA∆.md` com conteúdo material e `modified_time=2025-07-27T04:18:54.488Z`.

O campo `created_time=1970-01-01T00:00:00Z` é inválido como data histórica e foi explicitamente rejeitado para prova de anterioridade.

**Claim permitido:** existe uma observação independente no Drive associando material RAIA ao período de 27/07/2025.

**Claim não permitido:** o `modified_time` isolado não prova a primeira criação mundial nem a gênese original do conteúdo.

## 3. `scripts/cristal.sh` histórico

Fonte histórica recuperada do commit `4fe1d9dc...`.

Blob SHA observado: `6b176a7341f97ea1367d81753a294d4e3af014ee`.

Operações diretamente presentes no script:

- `set -euo pipefail`;
- timestamp UTC via `date -u`;
- enumeração dos arquivos rastreados por `git ls-files -z`;
- SHA-256 de cada arquivo e SHA-256 agregado;
- append em `CHANGELOG.md`;
- emissão de hash no stdout;
- sugestão de tag `Ω-RAFAELIA_MARTE-v0.1`.

## 4. Tentativa de reprodução histórica

Foi tentado clone do repositório para checkout isolado do commit histórico. O ambiente de execução atual falhou antes do checkout por ausência de resolução DNS para `github.com`:

`fatal: unable to access ... Could not resolve host: github.com`

Esse erro é de ambiente/rede e não é classificado como falha do script.

Resultado correto:

`HISTORICAL_CHECKOUT_REPRODUCTION = BLOCKED_BY_ENVIRONMENT`

## 5. Reprodução mecânica controlada

Para testar o mecanismo sem promover falsamente o estado histórico, o script recuperado foi executado sem alteração funcional em um repositório Git sintético local contendo arquivos rastreados.

Resultado:

- exit code: `0`;
- stdout: `[Cristal] 2026-08-10T22:47:59Z hash=8c39e4438f25d047b55c02bda9668d782bd8ddd4cbbc13bc682590ff69da1c4e`;
- `CHANGELOG.md` recebeu bloco `Cristal` com o mesmo timestamp, mesmo hash e tag sugerida.

### Classificação

- `C4_EXECUTABLE = CONFIRMED_BY_SOURCE`;
- `C4_5_MECHANICS_REPRODUCED = TRUE`;
- `C5_HISTORICAL_REPRODUCED = FALSE`;
- bloqueio C5: checkout histórico integral indisponível no ambiente desta execução.

## 6. Delta probatório

Antes:

`cristal.sh = C4, reprodução pendente`

Depois:

`cristal.sh = C4 + mecânica reproduzida em ambiente controlado + bloqueio histórico identificado por causa externa`

Logo:

`evidence_delta > 0`.

## 7. Próximas rotas obrigatórias

1. reproduzir `cristal.sh` em checkout integral do commit `4fe1d9dc...` quando houver ambiente com acesso ao repositório ou snapshot completo local;
2. preservar `stdout`, `stderr`, `git rev-parse HEAD`, lista de arquivos rastreados e hash de ambiente;
3. cruzar RAIA no Drive com primeira ocorrência equivalente em NOVOexport por conteúdo/título/hash e depois com o commit Git de 27/07/2025;
4. não usar `created_time=1970` como evidência;
5. procurar IDs, SHAs, URLs e blocos de código dentro das mensagens exportadas para elevar vínculos de T2/T3 para T4/T5.

## 8. Invariante de sustentação

`fonte -> identidade -> tempo válido -> ação -> evidência -> limitação -> próxima ação`

Nenhum bloqueio é apagado; todo bloqueio recebe causa e rota de fechamento.