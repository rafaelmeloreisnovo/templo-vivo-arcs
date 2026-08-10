# Ω7D — Dimensão 1: Temporalidade e anterioridade

## Objeto
Demonstrar quando cada mecanismo aparece pela primeira vez, sem confundir data de criação, data de upload, data de commit, data de PR, data de auditoria ou data de carimbo posterior.

## Invariante
`evento -> timestamp de origem -> observação independente -> materialização -> derivação`

## Evidências aceitas
1. `create_time`/`update_time` do NOVOexport bruto;
2. conteúdo da mensagem com `conversation_id`/`message_id`;
3. primeiro blob/commit Git que contém o material;
4. PR e agente explicitamente identificados;
5. Drive como observação auxiliar, nunca como substituto da data original;
6. timestamp/attestation posterior claramente rotulado como auditoria atual.

## Força temporal
- T0: sem data confiável;
- T1: uma fonte;
- T2: duas fontes concordantes;
- T3: três fontes com relação semântica verificável;
- T4: texto/hash/SHA/path exato cruzado;
- T5: cadeia origem -> transformação -> commit reproduzível;
- T6: verificação independente.

## Heurísticas
- Preferir a menor data sustentada por artefato primário, não por narrativa posterior.
- Se duas fontes divergem, preservar ambas e abrir `TEMPORAL_CONFLICT`.
- Nome de arquivo contendo data é pista, não prova.
- O carimbo de 2026 não retroage para 2025.

## TOKEN_VAZIO
Todo vazio temporal deve registrar `fonte_esperada`, `intervalo`, `próxima_busca`, `critério_fechamento`.

## Saída
`CONCEPT_ID -> T_origin -> T_chat -> T_git -> T_pr -> T_audit -> temporal_strength`
