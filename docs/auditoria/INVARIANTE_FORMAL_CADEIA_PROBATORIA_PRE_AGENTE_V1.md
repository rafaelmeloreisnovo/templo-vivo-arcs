# Invariante Formal da Cadeia Probatória Pré-Agente — V1

Estado: `EVIDENCE_FIRST / CLAIM_GATE_ON / APPEND_ONLY`

## 1. Escopo

Este documento formaliza a condução probatória observada no recorte histórico do repositório entre o PR #1 (31/03/2025) e o primeiro PR explicitamente atribuído ao Copilot (#2, 19/10/2025). Não declara novidade mundial, patente concedida, autoria textual linha a linha ou evento de push quando não houver log específico.

## 2. Sequência material observada

- PR #1 — 31/03/2025 — artefato material `TemploVivo_RAD_Instalador.zip`.
- `Manifest.txt` — 23/05/2025 — commit `ee9c7d4a...`.
- `Entropia.md` — 26/06/2025 — commit `2e6562b0...`.
- `Fe.py` — 09/07/2025 — commit `a8a96d0a...`.
- `Ciclo fe` — 09/07/2025 — commit `2f323228...`.
- derivação por SHA — 27/07/2025 — commit `48b62c7e...`.
- `Raia∆` — 27/07/2025 — commit `becf137a...`.
- `assets/utopia_marte.yaml` — 27/08/2025 — commit `2eeab71c...`.
- `scripts/cristal.sh` — 27/08/2025 — commit `4fe1d9dc...`.
- `lib/marte/marte.dart` — 27/08/2025 — commit `b1a57f56...`.
- `00000/Patentes.md` — 30/08/2025 — commit `b64e6ec6...`.
- `LICENSE` — 10/10/2025 — commit `9323beba...`.
- `Hashing times` — 10/10/2025 — commit `a2b13967...`.
- PR #2 — 19/10/2025 — agente explicitamente identificado como Copilot; o PR recebe a expressão `Estrutura RAFAELIA` como objeto de trabalho e registra zero delta material no tree.
- PR #3 — 23/10/2025 — agente Copilot; zero delta material no tree.
- PR #4 e PR #5 — não encontrados como pull requests no repositório durante a auditoria; qualquer evento equivalente deve ser procurado em commits, branches, issues, actions ou outros repositórios.

## 3. Invariante de condução

`criar -> registrar -> versionar -> derivar -> executar -> governar -> organizar`

A propriedade preservada entre os estados é a continuidade identificável do corpus por caminhos, conteúdo, referências, SHAs, commits e relações documentadas.

## 4. Invariante probatória

Para um claim histórico C, a promoção só é permitida quando existe pelo menos um vínculo verificável entre estados:

`E = {path, blob_sha, commit_sha, exact_text, URL, message_id, tag, receipt}`

Se `E = vazio`, a relação permanece hipótese. Similaridade semântica isolada não estabelece identidade histórica.

## 5. Separação dos atos

- `CREATE`: conteúdo ou mecanismo aparece em um estado identificável.
- `COMMIT`: estado é incorporado ao grafo Git sob um commit SHA.
- `PUSH`: evento de transporte para remoto; não inferido apenas pela existência do commit.
- `PR`: proposta/revisão entre refs.
- `MERGE`: integração da proposta no alvo.
- `AGENT`: participação de agente somente quando identificada por evidência documental.

Logo: `commit != push != PR != merge != autoria intelectual`.

## 6. Classificação dos claims

- `PRE_AGENT_MATERIALIZATION = SUPPORTED_LIMITED`
- `PRE_AGENT_ARCHITECTURAL_COMPONENTS = SUPPORTED_LIMITED`
- `COPILOT_PR2_IDENTITY = SUPPORTED`
- `COPILOT_PR2_MATERIAL_DELTA = ZERO`
- `COPILOT_PR3_IDENTITY = SUPPORTED`
- `COPILOT_PR3_MATERIAL_DELTA = ZERO`
- `EXACT_PUSH_EVENTS_2025 = TOKEN_VAZIO_ACTIONABLE`
- `LINE_BY_LINE_HUMAN_AUTHORSHIP = TOKEN_VAZIO_ACTIONABLE`
- `WORLD_FIRST = BLOCKED_PENDING_PRIOR_ART`
- `PATENT_GRANTED = NOT_DEMONSTRATED`

## 7. TOKEN_VAZIO como obrigação operacional

Nenhum vazio pode ser usado para completar narrativa. Cada vazio deve possuir:

`gap_id -> claim -> fonte esperada -> ação -> evidência mínima -> critério de falha -> próximo estado`.

### TV-PUSH-2025
Fonte esperada: audit/event logs, webhook, local reflog/log, export, email/notificação ou registro independente.
Ação: buscar eventos temporalmente ligados aos commits-chave.
Fechamento: evento que associe ref/commit a ação de push com timestamp verificável.

### TV-AUTHORSHIP-LINE
Fonte esperada: NOVOexport bruto, versões locais anteriores, editor history, patches ou mensagem contendo conteúdo anterior ao commit.
Ação: fingerprint textual/código entre conversa e blob Git.
Fechamento: correspondência reproduzível e documentada; caso contrário, manter atribuição limitada à conta/commit.

### TV-TAGS-2025
Fonte esperada: refs/tags, releases, objetos annotated-tag e assinaturas.
Ação: catalogar `tag -> target SHA -> tagger -> timestamp -> signature -> release`.
Fechamento: inventário verificável das tags históricas.

## 8. Invariante de sustentação

`S = min(temporalidade, proveniencia, integridade, capacidade, juridico, falsificabilidade) * convergencia_verificada`

A convergência não compensa elo essencial ausente. Repetição, antiguidade, parábola ou volume textual não promovem evidência.

## 9. Próxima rota sem regressão

1. cruzar NOVOexport com os commits listados por nome, SHA, URL e fingerprint;
2. enumerar tags/releases históricas;
3. reproduzir `cristal.sh` no checkout histórico para tentar `C4.5 -> C5`;
4. validar YAML e aplicação Flutter em toolchain compatível;
5. gerar receipt por mecanismo;
6. realizar prior-art individual antes de claims de novidade;
7. preservar todos os conflitos e resultados negativos como evidência.

## 10. Conclusão limitada

O recorte auditado sustenta uma cadeia de materialização anterior aos PRs explicitamente atribuídos ao Copilot. A prova é mais forte quando apresentada como sequência de estados identificáveis e capacidades específicas, e não como conclusão universal sobre autoria, novidade ou validade científica.