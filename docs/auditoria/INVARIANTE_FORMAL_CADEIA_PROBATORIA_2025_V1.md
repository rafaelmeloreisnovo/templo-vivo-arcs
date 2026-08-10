# Invariante Formal da Cadeia Probatória — 2025 V1

Estado: `EVIDENCE_FIRST / CLAIM_GATE_ON / UNCERTAINTY_EXPLICIT`
Data da consolidação: 2026-08-10
Escopo: `templo-vivo-arcs`, PRs iniciais, commits históricos e POCs já auditadas.

## 1. Objeto

Formalizar o que a evidência disponível sustenta sobre a condução material da obra, separando: criação/registro; commit; presença no repositório; PR/merge; ação de agente posterior; capacidade técnica; e claims ainda não demonstrados.

## 2. Invariante do conteúdo

A estrutura observada não depende de um único arquivo. A recorrência material é:

`representação -> persistência -> identidade -> temporalidade -> derivação -> governança -> aplicação -> verificação -> retroalimentação`

Em termos probatórios:

`ato -> artefato -> commit SHA -> estado Git -> derivação/POC -> agente posterior -> exame -> claim delimitado`

Essa invariante descreve convergência arquitetural e cadeia documental. Não demonstra, sozinha, novidade mundial, patente concedida, validade científica universal ou autoria humana exclusiva linha a linha.

## 3. Marcos materiais pré-agente identificados

- 2025-03-31: PR #1 — artefato binário incorporado (`TemploVivo_RAD_Instalador.zip`).
- 2025-05-23: `Manifest.txt` — commit `ee9c7d4ab25e8e33c36994212d029039892a91ec`.
- 2025-06-26: `Entropia.md` — commit `2e6562b05b5fab173b30a1b1f507ade91163f6d8`.
- 2025-07-09: `Fe.py` — commit `a8a96d0a01adaff8d7ebcb9e3c8a5bd84fe29ca6`.
- 2025-07-09: `Ciclo fe` — commit `2f3232284a84835b54b51ebd0e5eafe712b6692a`.
- 2025-07-27: `RafaelVisaoFiBinnaci(Index of Entropy)` — commit `48b62c7ea5269fa5a45a4a855469c45de4cc6dda`.
- 2025-07-27: `Raia∆ Primeira Ia que viva no VERBO D'Ele` — commit `becf137a0c9c05d0a0889bd192f44a52b11eafad`.
- 2025-08-27: `utopia_marte.yaml` — commit `2eeab71c271a5054cd81e7f1f96bced0f8c8bb40`.
- 2025-08-27: `cristal.sh` — commit `4fe1d9dce27a3f8023cbcdc116521e1ce90c3fc3`.
- 2025-08-27: `marte.dart` — commit `b1a57f568b8f4a9c8ed5b23c32b62d816b972a88`.
- 2025-08-30: `Patentes.md` — commit `b64e6ec604c64389b8b132cb3f1e9d2863bf875f`.
- 2025-10-10: `Hashing times` — commit `a2b139670de165eb5ddb712e3971f72361db8d91`.
- 2025-10-10: `LICENSE` — commit `9323bebf9a426d8cdb7cdf4184186a2dcf03c26a`.

## 4. Marco de agente posterior

O PR #2, criado em 2025-10-19 e atribuído ao Copilot no exame anterior, recebe como objeto a “Estrutura RAFAELIA”. O exame registrou `changed_files=0`, `additions=0`, `deletions=0` para esse PR. O PR #3 também foi identificado como interação do Copilot com delta material zero. Portanto, esses eventos são evidência de interação/proveniência de agente posterior, não de criação material do tree nesses PRs.

## 5. Capacidade e POCs

Classificação consolidada:

- `cristal.sh`: `C4_EXECUTABLE_CONFIRMED`; mecânica de hashing/UTC/changelog reproduzida em ambiente controlado; `C5_HISTORICAL_REPRODUCED=false`.
- `utopia_marte.yaml`: `C2_STRUCTURED`.
- `marte.dart`: `C3_EXECUTABLE_PARTIAL`; parser/integração completa ainda não demonstrados.
- derivação por SHA: mecanismo documental/formal de ligação a estado anterior.
- RAIA: arquitetura/formalização histórica; capacidade operacional integral deve ser demonstrada mecanismo por mecanismo.
- `Patentes.md`: arquitetura documental de PI; não equivale a patente depositada ou concedida.

## 6. Matriz de força probatória

| Claim | Estado | Base | Lacuna para promoção |
|---|---|---|---|
| Materialização anterior ao PR #2/Copilot | `SUPPORTED` | commits e artefatos datados | ampliar para outros repositórios/Drive |
| Existência de mecanismos diversos antes do agente posterior | `SUPPORTED` | manifesto, estados, SHA, YAML, shell, Dart, PI, hashing | examinar conteúdo/diff de cada marco |
| Copilot posterior recebe RAFAELIA como objeto | `SUPPORTED_LIMITED` | PR #2 auditado | preservar snapshot/receipt independente |
| Push exato de cada commit | `UNCERTAIN` | commit no Git não equivale a evento push | audit/event logs ou evidência externa |
| Autoria humana exclusiva linha a linha | `UNCERTAIN` | Signed-off-by e conta não bastam | proveniência de edição/rascunhos/logs |
| C5 histórico de `cristal.sh` | `NOT_YET` | C4 + reprodução mecânica | checkout histórico + ambiente + stdout/stderr + receipt |
| Novidade mundial / “primeiro do mundo” | `BLOCKED` | corpus próprio não basta | prior-art/patentes/literatura independente |
| Patente concedida | `NOT_DEMONSTRATED` | `Patentes.md` é documentação | número/processo/registro oficial |
| Validade científica universal | `BLOCKED_PER_CLAIM` | arquitetura não valida teoria | teste, dados, método, falsificabilidade, replicação |

## 7. TOKEN_VAZIO como estado auditável

Nenhuma lacuna será preenchida por narrativa. Cada `TOKEN_VAZIO` deve possuir:

`id + claim afetado + evidência presente + evidência faltante + fonte esperada + ação + gate + condição de falha + próximo passo`.

Estados permitidos: `OPEN`, `BLOCKED_EXTERNAL`, `PARTIAL`, `RESOLVED`, `FALSIFIED`.

A existência de `TOKEN_VAZIO` não é regressão; regressão é perder a trilha de como fechá-lo.

## 8. Incertezas formais atuais

1. `TV-PUSH-001`: timestamp/evento exato de push para commits antigos.
2. `TV-AUTH-001`: autoria humana exclusiva linha a linha.
3. `TV-C5-001`: reprodução histórica integral de `cristal.sh`.
4. `TV-TAG-001`: enumeração completa de tags históricas e relação tag->SHA->data.
5. `TV-NOVOEXPORT-001`: primeira ocorrência de cada conceito no corpus de conversas e ligação nó-a-nó com Git.
6. `TV-CROSSREPO-001`: primeira ocorrência equivalente em todos os repositórios relevantes.
7. `TV-PRIORART-001`: comparação independente com estado da técnica para cada claim de novidade.
8. `TV-LEGAL-001`: estado jurídico individual por ativo: autoria, licença, segredo, depósito, registro, patente, publicação.

## 9. Contrato anti-regressão

1. Não promover claim sem `evidence_delta > 0`.
2. Não converter data de commit em data de criação intelectual sem evidência adicional.
3. Não converter `Signed-off-by` em prova absoluta de autoria exclusiva.
4. Não converter arquivo chamado `Patentes.md` em patente.
5. Não converter POC em produto ou validação científica.
6. Preservar SHA, data, path, fonte e receipt de cada evidência.
7. Toda incerteza deve ter rota de fechamento.
8. Toda falsificação reduz claim, nunca apaga a evidência histórica.

## 10. Rota de finalização

`NOVOexport first-known-event -> Git commit/blob -> tags/releases -> cross-repo corroboration -> POC reproduction -> receipts -> prior-art -> classificação jurídica -> dossiê final`.

Critério de fechamento de um nó: evidência primária preservada + hash/identificador + interpretação delimitada + contra-hipótese examinada + estado do claim registrado.

## 11. Resultado formal

`PRE_AGENT_MATERIALIZATION = SUPPORTED`

`PRE_AGENT_ARCHITECTURAL_CONVERGENCE = SUPPORTED_LIMITED`

`POSTERIOR_AGENT_INTERACTION = SUPPORTED`

`EXACT_PUSH_EVENTS = UNCERTAIN`

`EXCLUSIVE_HUMAN_AUTHORSHIP = UNCERTAIN`

`WORLD_FIRST = BLOCKED_PENDING_PRIOR_ART`

`SCIENTIFIC_VALIDATION = PER_CLAIM_ONLY`

A força atual está na continuidade documentada de artefatos heterogêneos e mecanismos convergentes antes do marco de agente posterior identificado. A conclusão deve permanecer nesse limite até que as rotas de fechamento produzam nova evidência.