# Matriz de convergência e anterioridade

**Objetivo:** mapear cada componente histórico por função, evidência, anterioridade e limite de claim, incorporando sete direções de sustentação jurídica e probatória.

| ID | Data crítica | Artefato/commit | Função estrutural | Capacidade demonstrada | Agente posterior | Status |
|---|---|---|---|---|---|---|
| M00 | 23/05/2025 | `Manifest.txt` / `ee9c7d4a...` | governança/auditoria | exige log auditável, transparência e não apagamento/ocultação | Copilot/Codex posteriores | E2 forte / norma |
| M01 | 09/07/2025 | `Fe.py` / `a8a96d0...` | formalização de variáveis | especificação simbólico-matemática | Copilot/Codex posteriores | E2 / conceitual |
| M02 | 09/07/2025 | `Ciclo fe` / `2f323228...` | pipeline por estados | sequência estado→transformação | Copilot/Codex posteriores | E2 / método |
| M03 | 27/07/2025 | `RafaelVisaoFiBinnaci(Index of Entropy)` / `48b62c7e...` | derivação por referência | usa SHA anterior como entrada identificada | Copilot/Codex posteriores | E2 forte |
| M04 | 27/07/2025 | `RaIa∆...` / `becf137a...` | memória/arquivo vivo | hash+tempo+camadas+retroalimentação | Copilot/Codex posteriores | E2 forte |
| M05 | 27/08/2025 | `assets/utopia_marte.yaml` / `2eeab71c...` | contrato declarativo | metas, limites e invariantes éticos | Codex posterior | E3 parcial |
| M06 | 27/08/2025 | `scripts/cristal.sh` / `4fe1d9dc...` | receipt de integridade | UTC + SHA-256 agregado + changelog | Codex posterior | E3/C4 forte |
| M07 | 27/08/2025 | `lib/marte/marte.dart` / `b1a57f56...` | interface/aplicação | lê asset e materializa UI; parser YAML ainda placeholder | Codex posterior | E3 parcial |
| M08 | 30/08/2025 | `00000/Patentes.md` / `b64e6ec6...` | arquitetura legal/técnica/documental | inventário e árvore proposta | Copilot/Codex posteriores | E2 forte |
| M09 | 10/10/2025 | `Hashing times` / `a2b13967...` | amostragem temporal | liga tempo, amostra, métrica e hashing como hipótese | Copilot posterior | E2 / não validado |
| M10 | 19/10/2025 | PR #2 Copilot | reorganização solicitada | prompt reconhece `Estrutura RAFAELIA` preexistente | Copilot | agente comprovado; diff material nulo |

## Sete direções aplicadas

Cada item deve ser avaliado por: D1 anterioridade; D2 proveniência/autoria/agente; D3 integridade/custódia; D4 capacidade/POC; D5 convergência; D6 formalidade jurídica/PI; D7 falsificabilidade/ação.

A força global é limitada pelo elo essencial mais fraco.

## Combinações estruturais

### C1 — Proveniência evolutiva
`M03 + M04 + M06`

`artefato_n + SHA_n + contexto_n -> transformação -> artefato_{n+1} + receipt`

**Uso probatório:** demonstra que referência a estado anterior, derivação e registro de integridade já estavam presentes antes dos agentes GitHub.

### C2 — Governança executável
`M00 + M05 + M06 + M07`

`norma de auditabilidade -> configuração/invariantes -> aplicação -> hash/timestamp`

**Uso probatório:** sequência documental de norma, estrutura e implementação, sem confundir norma com execução reproduzida.

### C3 — Arquitetura de obra
`M02 + M04 + M08`

`ciclo -> memória -> classificação -> produção intelectual`

**Uso probatório:** metodologia de construção contínua, não apenas arquivos isolados.

### C4 — Linha temporal multi-fonte
`NOVOexport + GitHub + Drive + PR`

`chat timestamp -> message/conversation id -> conteúdo/URL/SHA -> raw export -> Git blob -> commit -> PR/agent -> receipt`

**Uso probatório:** aumentar corroborabilidade temporal sem usar horário de upload do Drive como data original da conversa.

## Claim gate

### Permitido/limitado
- `PRE_AGENT_ARCHITECTURE=true`: há artefatos estruturais anteriores ao primeiro Copilot comprovado no repositório.
- `HASH_RECEIPT_POC=true`: há script de hashing+timestamp registrado em 27/08/2025.
- `DERIVATION_BY_COMMIT_REFERENCE=true`: há artefato de 27/07/2025 que referencia SHA anterior e o usa como base de derivação.
- `AUDIT_GOVERNANCE_PRE_AGENT=true`: `Manifest.txt` de 23/05/2025 contém obrigação de log auditável e não ocultação/apagamento de execuções.

### Bloqueado
- `WORLD_FIRST=true` até busca de prior art.
- `NEW_PHYSICS=true` até formalização/testes independentes.
- `OPENAI_VALIDATED=true` não demonstrado.
- `NOBEL_LINK=true` somente contexto metodológico; não vínculo institucional nem premiação da obra.
- `PATENT_GRANTED=true` sem registro oficial.
- `AGENT_IDENTITY=true` sem vínculo documental específico.

## Próximas provas necessárias

1. extrair eventos brutos de NOVOexport para os commits-chave de 2025;
2. reproduzir `scripts/cristal.sh` em checkout controlado e guardar stdout/hash/environment receipt;
3. localizar primeiro commit de cada conceito FCEA/RAFCODE/RafBit/ZIPRAF/RAIA/RAFAELIA;
4. comparar blobs para provar continuidade e não reescrita retroativa;
5. construir `PRIOR_ART_MATRIX` por mecanismo e data crítica;
6. aplicar o contrato `CONTRATO_TOKEN_VAZIO_E_CLAIM_GATE_JURIDICO_V1.json` a todos os claims;
7. preservar originais e gerar apenas receipts append-only em 2026.
