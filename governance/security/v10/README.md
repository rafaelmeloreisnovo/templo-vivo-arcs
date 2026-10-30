# Templo Vivo ARCΣ — auditoria operacional e riscos P0 V10

**Estado:** EVIDENCE_SCOPED / HUMAN_ADMIN_REVIEW_REQUIRED / HOLD / claim_allowed=false.
**Data:** 2026-10-30. **Repo produtor:** `rafaelmeloreisnovo/templo-vivo-arcs`. **BASE:** `e8cb574b7422305cb2b387f60eb1c6db481393ed`.
Não há autorização inferida para ativar credenciais, alterar configurações administrativas ou declarar certificação. Este pacote não coleta dados pessoais.

## O que foi observado diretamente
| Ref | Fato de SOURCE | O que NÃO se conclui |
|---|---|---|
| [OP01](operational_facts_v10.json) | GitHub repo público ID 957203368 e main; permissão administrativa do conector | Operador legal, regraset, governança aprovada |
| OP02 | `index.html` blob `9d15b2390cf32af4153a1369ff851c1cbda639da` declara portal GitHub Pages | site ativo neste instante, usuários reais, ausência de terceiros |
| OP03 | `.github/workflows/jekyll-gh-pages.yml` blob `e3fa3dbf1f2312e300635da58e6012bda3e0de43` aponta deploy `main` e permissions `pages:write/id-token:write` | proteção main ativa ou autorização jurídica |
| OP04 | Receipt de Pages de 2026-09-24 em `receipts/2026-09-24_CRF_FORMALIZATION_PAGE_V2.md` menciona deploy run 35978442143 SUCCESS | uptime/HTTP real em 2026-10-30 |
| OP05 | README aponta código Flutter/Android e páginas de pesquisa | APK em uso/UGC, idade dos usuários, coleta, operadores reais |
| OP06 | Consulta externa atual à URL pública não obteve resposta pelo pesquisador | prova de que site esteja fora do ar ou acessível |

**Conflito de temporalidade:** SOURCE HTML + CI histórico ≠ monitoramento contínuo de produção. O fluxo de publicação por `main` aumenta a importância de G02.

## P0 fail-closed — definição de pronto
- **G01 credenciais**: somente administrador autorizado verifica no provedor revogação/rotação, escopo mínimo e receipt privado **sem revelar token**. Status: `TOKEN_VAZIO`.
- **G02 proteção main**: ler regras efetivas no provedor; exigir PR review, checks, bloqueio de force push/deletion, governança de bypass; evidenciar readback. Status: `TOKEN_VAZIO` nesta rodada; registro histórico de `protected=false` não equivale a prova atual.
- **G03 crianças**: nomear responsável humano privado, canal seguro de denúncias, teste de escalonamento, zero contato não supervisionado entre adultos e menores; determinar quais serviços são acessíveis/prováveis por menores. Status: `TOKEN_VAZIO`.
- **G04 dados religiosos/menores**: identificar controlador/operador e processadores; mapear formulário, login, cookies, analytics, logs/CDN/GitHub e qualquer terceiro; bases legais, finalidade, retenção, direitos dos titulares e teste de eliminação. Status: `TOKEN_VAZIO`.

## Regra jurídica de urgência
Brasil: a Lei 15.211/2025 (ECA Digital) vigora desde 17-03-2026 e foi regulamentada pelo Decreto 12.880/2026; sua aplicação depende de serviço real dirigido a menores ou de acesso provável. Fonte oficial ANPD: https://www.gov.br/anpd/pt-br/assuntos/eca-digital.
Reino Unido: deveres Online Safety Act dependem do tipo e do escopo do serviço; uma página estática não pode ser classificada como plataforma UGC por inferência. Fonte Ofcom: https://www.ofcom.org.uk/online-safety/protecting-children/protection-of-children-duties-under-the-online-safety-act.
Estados Unidos: COPPA depende das condições de direcionamento a crianças/coleta e alcance territorial. Fonte FTC: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions.
Convicção religiosa pode ser dado sensível (LGPD art. 5º, II): https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes.

## Risco residual e fronteira
`SECURITY.md` e `governance/security/readiness_v1.json` existentes continuam autoridade de governança P0. Este estudo suplementa observações; NÃO altera estados de segurança por documentação. Nenhuma conclusão de conformidade ou sanção. Nenhum operador, processador, assessor jurídico ou canal privado foi inventado.

## Procedimento humano autorizado
1. Administrador autenticado certifica G01/G02 em canais privados com hashes de recibos sanitizados, sem segredos.
2. Responsável por privacidade/proteção infantil faz mapa real de serviços e dados, avaliação da idade/acesso e exercícios de incidente.
3. Consultor jurídico competente analisa apenas jurisdições com nexo factual, em [pacote de revisão jurídica V10](../../legal/v10/REVIEW_REQUESTS.md).
4. Revisor independente repete falsificadores e confere provas. Só depois avaliar alteração de licença, estatuto ou declaração de conformidade.

**ROLLBACK:** fechar PR sem merge. Correção publicada: registro sucessor `supersedes`, sem apagar histórico. `SOURCE≠ARTEFATO≠EXECUTION≠EVIDENCE≠CLAIM`.
