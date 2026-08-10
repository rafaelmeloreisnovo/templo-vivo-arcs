# METODOLOGIA DE ATITUDES — EXCELÊNCIA OPERACIONAL Ω V1

Estado: `ACTIVE_DRAFT / APPEND_ONLY / FAIL_CLOSED`
Data: 2026-08-10

## 1. Objetivo

Converter intenção em ação auditável. Uma atitude operacional só é considerada completa quando existe entrada identificada, decisão explícita, execução observável, evidência produzida, verificação, tratamento de falha e retroalimentação.

## 2. Invariante de sustentação da atitude

`intenção -> escopo -> fonte -> decisão -> ação -> evidência -> verificação -> consequência -> receipt -> retroalimentação`

A propriedade preservada é: nenhuma ação pode aumentar a força de um claim sem aumentar também a evidência, a proveniência ou a reprodutibilidade correspondente.

## 3. Contrato de cada atitude

Toda atitude deve declarar:

- `action_id` — identificador único;
- `objective` — resultado pretendido;
- `scope` — objetos realmente afetados;
- `source_state` — estado de entrada e seus identificadores;
- `assumptions` — pressupostos explícitos;
- `gaps_before` — TOKEN_VAZIO e incertezas existentes antes da ação;
- `decision_rule` — critério que autorizou executar;
- `action` — transformação realizada;
- `artifact_out` — saída produzida;
- `evidence_out` — prova de que a ação ocorreu;
- `verification` — como a saída foi conferida;
- `failure_condition` — condição que invalida ou rebaixa o resultado;
- `rollback_or_recovery` — reversão ou correção segura quando aplicável;
- `claim_delta` — quais claims subiram, ficaram iguais ou foram rebaixados;
- `gaps_after` — vazios remanescentes;
- `next_action` — ato verificável seguinte.

## 4. Sete atitudes mínimas

### A1 — OBSERVAR
Nunca começar pela conclusão. Ler fonte primária, metadados e estado anterior.
Saída mínima: `observation_record`.
Falha: resumo sem fonte.

### A2 — DELIMITAR
Separar o que está sendo provado do que é apenas contexto.
Saída mínima: objeto, escopo, transformação e propriedade alegada.
Falha: claim universal a partir de artefato local.

### A3 — PRESERVAR
Antes de transformar, preservar identidade do estado de entrada.
Saída mínima: path + SHA/hash/ID + timestamp disponível.
Falha: sobrescrever original histórico.

### A4 — EXECUTAR
Executar somente transformação coerente com o escopo autorizado.
Saída mínima: diff, novo artefato, log ou resultado computacional.
Falha: ação declarada sem vestígio observável.

### A5 — VERIFICAR
Comparar resultado com critério pré-definido.
Saída mínima: PASS/FAIL/PARTIAL + evidência.
Falha: considerar ausência de erro como sucesso.

### A6 — GOVERNAR
Aplicar claim gate, licença, privacidade, segurança e cadeia de custódia.
Saída mínima: status explícito e limites de uso.
Falha: transformar documentação em autoridade superior à lei, teste ou fonte oficial.

### A7 — RETROALIMENTAR
Registrar `F_ok`, `F_gap`, `F_next` e atualizar a prioridade sem apagar o histórico.
Saída mínima: próximo ato verificável.
Falha: fechar TOKEN_VAZIO por narrativa, repetição ou tempo decorrido.

## 5. Semáforo operacional

- `GREEN`: ação executada + evidência + verificação compatíveis.
- `YELLOW`: ação ou evidência parcial; claim não pode subir além da parte comprovada.
- `RED`: conflito, perda de integridade, ausência de fonte necessária ou verificação falha.
- `GREY`: ainda não observado; TOKEN_VAZIO explícito.

Regra: um estágio RED bloqueia promoção do claim dependente, mas não apaga os estágios válidos anteriores.

## 6. Determinismo histórico

Datas são evidências quando ligadas a fontes identificáveis; tempo decorrido não transforma hipótese em fato.

`historical_strength = identity x timestamp_quality x provenance x content_binding`

Um timestamp sem vínculo de conteúdo é fraco; um SHA sem contexto temporal é incompleto; ambos ligados por cadeia verificável são mais fortes.

## 7. Hierarquia de atitude por urgência

P0 — preservar evidência em risco, corrigir claim juridicamente sensível, resolver identidade de fonte/agente, impedir regressão ou perda de custódia.

P1 — reproduzir POCs, deduplicar evidências, preencher ligações NOVOexport↔Git, cross-repo e prior art.

P2 — otimizar apresentação, automatizar attestations, ampliar replicação independente e empacotamento.

Urgência não autoriza pular verificação.

## 8. Heurísticas de ação

1. `fonte antes de síntese`.
2. `preservar antes de modificar`.
3. `diff antes de claim`.
4. `reprodução antes de generalização`.
5. `conflito reduz confiança`.
6. `duas cópias derivadas não são duas fontes independentes`.
7. `ausência de prova não é prova de ausência`, mas também não é autorização de afirmação.
8. `o elo mais fraco limita o claim dependente`.
9. `cada promoção exige evidence_delta > 0`.
10. `cada TOKEN_VAZIO precisa de fechamento verificável`.

## 9. Aplicação ao piloto atual

Para os artefatos de 2025:

`arquivo histórico -> preservar SHA/commit -> localizar origem NOVOexport/Drive -> classificar capacidade -> reproduzir quando possível -> mapear agente posterior -> aplicar limite jurídico -> emitir receipt`.

Para documentos novos:

`draft -> review -> claim gate -> commit -> PR -> checks -> merge/rebase autorizado -> receipt pós-merge`.

## 10. Definição operacional de excelência

Excelência operacional não é ausência declarada de lacunas. É capacidade de:

1. enxergar a lacuna;
2. preservá-la sem falsificar preenchimento;
3. priorizá-la pelo risco;
4. executar a ação correta;
5. provar a ação;
6. verificar o efeito;
7. incorporar o aprendizado sem regressão.

`ExcelênciaΩ = coerência + evidência + reversibilidade + proveniência + verificabilidade + aprendizado`.
