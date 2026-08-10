# Matriz de convergência e anterioridade

**Objetivo:** mapear cada componente histórico por função, evidência, anterioridade e limite de claim.

| ID | Data crítica | Artefato/commit | Função estrutural | Capacidade demonstrada | Agente posterior | Status |
|---|---|---|---|---|---|---|
| M01 | 09/07/2025 | `Fe.py` / `a8a96d0...` | formalização de variáveis | especificação simbólico-matemática | Copilot/Codex posteriores | E2 / conceitual |
| M02 | 09/07/2025 | `Ciclo fe` / `2f323228...` | pipeline por estados | sequência estado→transformação | Copilot/Codex posteriores | E2 / método |
| M03 | 27/07/2025 | `RafaelVisaoFiBinnaci(Index of Entropy)` / `48b62c7e...` | derivação por referência | usa SHA anterior como entrada identificada | Copilot/Codex posteriores | E2 forte |
| M04 | 27/07/2025 | `RaIa∆...` / `becf137a...` | memória/arquivo vivo | hash+tempo+camadas+retroalimentação | Copilot/Codex posteriores | E2 forte |
| M05 | 27/08/2025 | `assets/utopia_marte.yaml` / `2eeab71c...` | contrato declarativo | metas, limites e invariantes éticos | Codex posterior | E3 parcial |
| M06 | 27/08/2025 | `scripts/cristal.sh` / `4fe1d9dc...` | receipt de integridade | UTC + SHA-256 agregado + changelog | Codex posterior | E3 forte |
| M07 | 27/08/2025 | `lib/marte/marte.dart` / `b1a57f56...` | interface/aplicação | lê asset e materializa UI; parser YAML ainda placeholder | Codex posterior | E3 parcial |
| M08 | 30/08/2025 | `00000/Patentes.md` / `b64e6ec6...` | arquitetura legal/técnica/documental | inventário e árvore proposta | Copilot/Codex posteriores | E2 forte |
| M09 | 10/10/2025 | `Hashing times` / `a2b13967...` | amostragem temporal | liga tempo, amostra, métrica e hashing como hipótese | Copilot posterior | E2 / não validado |
| M10 | 19/10/2025 | PR #2 Copilot | reorganização solicitada | prompt reconhece `Estrutura RAFAELIA` preexistente | Copilot | agente comprovado; diff material nulo |

## Combinações estruturais

### C1 — Proveniência evolutiva

`M03 + M04 + M06`

\[
artefato_n + SHA_n + contexto_n \rightarrow transformação \rightarrow artefato_{n+1} + receipt
\]

**Uso probatório:** demonstra que referência a estado anterior, derivação e registro de integridade já estavam presentes antes dos agentes GitHub.

### C2 — Governança executável

`M05 + M06 + M07`

\[
configuração \rightarrow invariantes \rightarrow aplicação \rightarrow hash/timestamp
\]

**Uso probatório:** demonstra passagem de visão para configuração estruturada, código de interface e mecanismo de integridade.

### C3 — Arquitetura de obra

`M02 + M04 + M08`

\[
ciclo \rightarrow memória \rightarrow classificação \rightarrow produção intelectual
\]

**Uso probatório:** demonstra uma metodologia de construção contínua, não apenas arquivos isolados.

### C4 — Relação com convergência reconhecida externamente

A analogia metodológica permitida com o Nobel de Física de 2024 é:

`física de sistemas/padrões -> arquitetura de memória/aprendizado`.

A analogia com a obra é apenas de **princípio de transposição estrutural entre domínios**, nunca de equivalência de descoberta ou validação científica.

## Claim gate

### Permitido

- `PRE_AGENT_ARCHITECTURE=true`: há artefatos estruturais anteriores ao primeiro Copilot comprovado no repositório.
- `HASH_RECEIPT_POC=true`: há script de hashing+timestamp registrado em 27/08/2025.
- `DERIVATION_BY_COMMIT_REFERENCE=true`: há artefato de 27/07/2025 que referencia SHA anterior e o usa como base de derivação.

### Bloqueado

- `WORLD_FIRST=true` → bloqueado até busca de prior art.
- `NEW_PHYSICS=true` → bloqueado até formalização/testes independentes.
- `OPENAI_VALIDATED=true` → falso/não demonstrado.
- `NOBEL_LINK=true` → somente contexto metodológico; não vínculo institucional nem premiação da obra.

## Próximas provas necessárias

1. reproduzir `scripts/cristal.sh` em checkout limpo e guardar stdout, hash e environment receipt;
2. localizar primeiro commit de cada conceito FCEA/RAFCODE/RafBit/ZIPRAF/RAIA/RAFAELIA;
3. comparar blobs para provar continuidade e não reescrita retroativa;
4. construir `PRIOR_ART_MATRIX` por mecanismo e data crítica;
5. preservar originais e gerar apenas receipts append-only em 2026.
