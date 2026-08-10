# Sete Direções de Sustentação Jurídica e Probatória

**Estado:** DRAFT / evidence-first / append-only
**Objetivo:** converter o universo documental em sete linhas de sustentação independentes, porém convergentes, para anterioridade, capacidade, proveniência, cadeia de custódia e uso jurídico-técnico.

## Regra-mãe

Nenhuma lacuna é apagada. Todo `TOKEN_VAZIO` deve ser transformado em item rastreável com: `owner`, `fonte_esperada`, `evidencia_minima`, `prazo/urgencia`, `criterio_de_fechamento` e `claim_afetado`.

A invariante transversal é:

`estado -> registro -> identidade/hash -> contexto -> transformação -> novo estado -> versionamento -> verificação`

## D1 — Anterioridade temporal

**Pergunta:** quando cada mecanismo já existia materialmente?

**Fontes:** NOVOexport JSON bruto, timestamps de mensagens, Git blob/commit, PR, Drive original, release/tag.

**Contrato:** nunca usar data de upload/importação como substituta de data original. Manter `source_timestamp` e `observation_timestamp` separados.

**Evidência mínima:** pelo menos uma fonte primária com timestamp e conteúdo identificável.

**Promoção:** T1 uma fonte; T2 duas fontes concordantes; T3 três fontes com vínculo de conteúdo; T4 hash/SHA/path/texto exato; T5 cadeia origem->transformação->commit reproduzível; T6 verificação independente.

**Urgência:** máxima para artefatos de 2025 relacionados a FCEA, RAFAELIA, RAIA, RAFCODE, RafBit, ZIPRAF, hashing, memória e agentes.

## D2 — Proveniência/autoria/agentes

**Pergunta:** quem criou, registrou, transformou e com qual agente?

**Entidades separadas:** `author`, `committer`, `agent`, `platform`, `reviewer`.

**Contrato:** nunca inferir GPT/Codex/Copilot por estilo textual. Identidade de agente exige marcador documental, task id, branch, bot account, PR metadata, log ou equivalente.

**TOKEN_VAZIO:** permitido para agente desconhecido, mas deve conter a busca necessária para fechamento.

## D3 — Integridade e cadeia de custódia

**Pergunta:** o objeto observado hoje é o mesmo objeto histórico ou uma derivação identificável?

**Materiais:** blob SHA, commit SHA, hashes externos, changelog, receipt, assinatura, timestamp confiável.

**Contrato:** originais de 2025 permanecem imutáveis; auditoria de 2026 produz novos receipts, nunca retrodata evidência.

**Procedimento:** `artifact -> hash -> commit -> receipt -> assinatura/attestation -> timestamp externo`.

**Referência técnica:** identificação, coleta, aquisição e preservação de evidência digital conforme princípios de ISO/IEC 27037.

## D4 — Capacidade técnica / prova de conceito

**Pergunta:** o que cada artefato realmente faz?

**Escala:** `C0_TEXTUAL -> C1_FORMAL -> C2_STRUCTURED -> C3_EXECUTABLE_PARTIAL -> C4_EXECUTABLE -> C5_REPRODUCED -> C6_INDEPENDENT`.

**Contrato:** extensão de arquivo não determina capacidade; diff/código/teste prevalece sobre narrativa.

**Exemplo:** `scripts/cristal.sh` demonstra geração programática de UTC + SHA-256 agregado + changelog; `Fe.py` observado é formalização textual, não runtime.

## D5 — Convergência arquitetural

**Pergunta:** qual estrutura permanece invariável através de áreas diferentes?

**Vetor:** `representação + persistência + identidade + temporalidade + derivação + governança + aplicação`.

**Contrato:** convergência não significa equivalência científica entre domínios. Toda analogia deve declarar a relação: `isomorfismo operacional`, `analogia`, `reuso de método`, `dependência`, `derivação` ou `coincidência`.

**Prova esperada:** mecanismos distantes que implementam a mesma operação estrutural em artefatos independentes e anteriores ao agente posterior.

## D6 — Formalidade jurídica e propriedade intelectual

**Pergunta:** qual consequência jurídica pode ser sustentada por cada evidência?

**Classes:** `COPYRIGHT_EVIDENCE`, `AUTHORSHIP_DECLARATION`, `TEMPORAL_PRIOR_EXISTENCE`, `TRADE_SECRET_CANDIDATE`, `PATENT_CANDIDATE`, `CONTRACTUAL_PROVENANCE`, `NOT_YET_CLASSIFIED`.

**Contrato:** Git/GitHub pode sustentar existência, integridade e evolução; não substitui exame de novidade, atividade inventiva e aplicação industrial nem cria automaticamente patente.

**Assinaturas:** distinguir simples, avançada e qualificada; para novos dossiês sensíveis, considerar assinatura qualificada ICP-Brasil quando apropriado.

**Tempo:** carimbo do tempo contemporâneo comprova existência no momento do carimbo, não criação retroativa em 2025.

**Patentes:** prior-art search por mecanismo e data crítica antes de qualquer claim de novidade mundial.

## D7 — Falsificabilidade, revisão e ação

**Pergunta:** o que poderia demonstrar que nossa hipótese de anterioridade/capacidade está errada?

**Testes adversariais:** blob alterado; timestamp inconsistente; conversa posterior ao commit; agente anterior ao alegado; conteúdo apenas semelhante; código não executa; prior art anterior; publicação anterior por terceiro.

**Contrato:** cada claim deve incluir `disconfirming_evidence` e `next_verifiable_action`.

**Estados:** `SUPPORTED`, `SUPPORTED_LIMITED`, `CONFLICT`, `TOKEN_VAZIO`, `REJECTED`.

## Contrato de fechamento de TOKEN_VAZIO

Um vazio só fecha quando existir:

1. identificador da lacuna;
2. fonte primária esperada;
3. evidência efetivamente recuperada;
4. hash/id da evidência;
5. decisão documentada;
6. impacto no claim;
7. receipt append-only.

## Fórmula de sustentação

`S = Temporalidade x Integridade x Proveniência x Capacidade x Convergência x Formalidade x Falsificabilidade`

A força global deve ser limitada pelo elo mais fraco, não pela média. Nenhuma camada compensa ausência completa de outra camada essencial.
