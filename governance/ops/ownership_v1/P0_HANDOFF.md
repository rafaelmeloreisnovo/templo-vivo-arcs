# Templo Vivo ARCΣ — G01–G04 | passagem responsável ao operador humano

**Data:** 2026-10-30 · **Estado:** PREPARED_NOT_EXECUTED / HOLD · **Parente:** inventário V11 PR #57 · **Escopo:** gabaritos P0 sem atribuição automática de pessoas.

## 1. Observação G02 de provedor — evidencia negativa delimitada

A API do GitHub observada hoje em `main@8b002de05dd01862b1f1ca7a2d3702afe06e4d9b` declarou `protected=false`, `protection.enabled=false`, `required_status_checks.enforcement_level=off`. A consulta dedicada `/branches/main/protection` retornou HTTP 403 por falta de acesso da integração. A listagem `/rulesets` do repositório retornou `[]`, observação **limitada** que não demonstra inexistência de regras herdadas ou de todos os controles possíveis.

**Interpretação:** `G02=FAIL_OBSERVED_SCOPED` para a proteção clássica de `main`; proteção administrativa completa e autorização continuam sem prova; `G02_CLOSED=false`. [Fonte tipada](p0_handoff_g02.json).

A proteção deve ser corrigida no painel do **administrador legitimamente autorizado**, não por modificação de um arquivo, IA ou simples merge de PR. Este documento **não modifica** branch rules, regras do provedor, tokens ou usuários.

## 2. Sequência humana mínima (não executar silenciosamente)

| Prioridade | A quem se solicita aceitação voluntária | Ação e confirmação exigidas |
|---|---|---|
| G01 — credenciais | Administrador autorizado do GitHub e serviços correlatos | Verificar a exposição histórica sem republicar segredo; revogar/rotacionar quando devido, limitar escopo; guardar receipt **privado**, publicar somente hash/ref sanitizado |
| G02 — branch `main` | Administrador autorizado do repo/organização | Inspecionar efetivamente **Settings → Rules → Rulesets** e, se aplicável, proteções da branch; verificar políticas herdadas, exigência de PR, revisão independente, checks apropriados, bloqueio de force-push e exclusão, bypass e acesso administrativo. Ajustar após plano de rollback e testes no fluxo Pages. Produzir **readback** posterior pelo provedor. |
| G03 — crianças | Pessoa com autoridade formal de proteção infantil | Designação privada e aceite explícito; canal seguro de denúncia e escalonamento, política de não contato inadequado, simulação de resposta; **nunca** publicar dados de crianças ou denúncias |
| G04 — dados pessoais e crenças | Operador/controlador e profissional de privacidade habilitado | Identificar os serviços ativos, coleta real, bases legais, finalidade, provedores, idade provável, retenção e exclusão; validar necessidade de medidas adicionais, com avaliação humana |

**As designações NÃO foram realizadas**. Campos de pessoa, aceite, responsável, contato, habilitação e recibo continuam `TOKEN_VAZIO`; nenhum candidato é inferido pela conta que fez commits. A execução de qualquer ação administrativa depende do humano e das respectivas permissões.

## 3. Gabarito de aceite e prova (apenas no ambiente privado autorizado)

```text
handoff_id | gate | service_id | actual_operator_ref | jurisdiction |
candidate_role | authority_document_ref | candidate_consent_ref |
reviewer_independence_ref | exact_provider_ref | prechange_snapshot_ref |
proposed_change | rollback_ref | positive_test_ref | negative_test_ref |
postchange_readback_ref | sanitized_public_hash | human_approval_ref |
status=BLOCKED | parent | timestamp
```

A referência pública pode conter **somente** token identificador e hash sanitizado, nunca dados pessoais ou segredos. Registro de nomeação não é prova de execução; execução não é prova de conformidade. Não usar dados reais de crianças em testes. Leitura do estado atual, dry-run e manutenção de acesso administrativo de recuperação devem preceder mudanças em produção.

## 4. Critério de aceite e falsificação

- **Falhar** se `protected=false` for apresentado como configuração suficiente de proteção obrigatória.
- **Falhar** se HTTP 403 for tratado como evidência de proteção ativa.
- **Falhar** se a listagem vazia de rulesets for tratada como demonstração de ausência global de regras herdadas.
- **Falhar** se G01 for encerrado com menção a token rotacionado sem atestação privada legítima.
- **Falhar** se G03 for encerrado sem responsável de proteção infantil e ensaio de escalonamento.
- **Falhar** se G04 for encerrado sem operador e inventário real de tratamento e bases legais.
- **Falhar** se assinatura jurídica, identidade, emprego, credencial ou autorização de pessoa forem inventados.
- **Falhar** se o campo `release_allowed` virar `true` sem receipt específico e revisão independente.

**O que a suíte local/CI verifica:** estrutura e consistência da observação/publicação, não configuração pós-mudança do provedor. O controle deve continuar `HOLD`.

## 5. Próxima decisão humana e rollback

O operador autorizado deve **primeiro** confirmar quem pode agir em G01/G02 e se o portal processa dados de usuários ou menores, registrando fatos sem segredos. Em seguida, corrigir G02 com controles proporcionais de branch/organização e verificar que a publicação existente não foi comprometida. Um novo receipt `supersedes` registra o estado após o teste e revisão independente; **não** corrigir os documentos históricos para simular conformidade.

**Rollback documental:** fechar PR #57 antes do merge. **Rollback da futura regra de provedor:** plano separado, aprovado pelo administrador e testado em ambiente seguro; não permitir downgrade de proteção como rollback silencioso.

**R3:** F_ok=observação G02 delimitada + handoff pronto; F_gap=autoridade, nomeações, revogação, regras administrativas, infância, tratamento real; F_next=aceite humano privado + controle de main com readback e revisão independente.
