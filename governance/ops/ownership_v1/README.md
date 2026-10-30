# Templo Vivo ARCΣ — Matriz de responsáveis, revisores e evidências V11

**2026-10-30 · Inventário dos cinco dias 25–30/10/2026 · STATUS: INVENTORY_ONLY / HUMAN_APPROVAL_REQUIRED / HOLD**

## Por que este artefato existe

O inventário encontrou documentos, gabaritos e PRs de autoria, licenças, constituições, traduções, proteção infantil, privacidade, segurança, navegação e operação. **Não** encontrou a designação e comprovação suficientes dos responsáveis pela eficácia jurídica ou operacional. Esta matriz conecta `ÁREA → ATIVO → PAPEL REQUERIDO → RESPONSÁVEL → REVISOR → GATE → EVIDÊNCIA → ESTADO`, sem transformar a conta GitHub ou o titular autoral em signatário de todas as obrigações.

Leia [responsibility_register.json](responsibility_register.json) como inventário tipado. É uma **fila de governança**, não um diretório de pessoas nem uma atestação de controles. O projeto preserva o princípio `SOURCE != ARTIFACT != EXECUTION != EVIDENCE != CLAIM`.

## Linha de base rastreável

- GitHub produtor: [templo-vivo-arcs](https://github.com/rafaelmeloreisnovo/templo-vivo-arcs) observado em `main@8b002de05dd01862b1f1ca7a2d3702afe06e4d9b`.
- 13 PRs no recorte: 12 incorporados (#43,#44,#45,#46,#47,#48,#49,#50,#51,#52,#53,#55) e #54 encerrado sem merge, substituído por #55. **Merge não equivale a revisão jurídica.**
- A consulta dos PRs mostrou 0 revisões formais GitHub no recorte. Isso não prova inexistência de revisões fora do GitHub.
- O titular/autor declarado nos materiais é Rafael Melo Reis e a conta autora de PRs é `rafaelmeloreisnovo`. **Declaração de autoria ≠ contratação, consentimento para papel operacional ou parecer jurídico.**
- V7 cobre oito idiomas em texto, **zero** revisões jurídicas linguísticas comprovadas; a referência constitucional prevê 186, **zero** certificações locais comprovadas.
- A matriz possui **15 frentes**, com **cinco P0** (G01,G02,G03,G04 e operação real LIVE). O P0 LIVE é um complemento de prudência e não substitui G01–G09.
- P0 principal: credenciais, proteção main, salvaguarda de menores e dados sensíveis. Evidência de administrador e titular do serviço segue `TOKEN_VAZIO`. O GitHub no snapshot observou `main.protected=false`, o que não comprova regras em outros planos nem justifica afirmar controles implantados.

## Roteiro de uso humano (sem automação de pessoas)

1. **Autorizar papéis:** titular/operador decide quem tem mandato para G01–G04 e onde serão armazenadas nomeações **privadamente**. Não publicar nome, e-mail, credencial ou contato de criança.
2. **Designar revisão separada:** o revisor deve ter habilitação e independência compatíveis com o risco; comprovar autoridade, escopo, data e revisão assinada. Não presumir advogados por país nem falantes de idioma como peritos.
3. **Fechar a evidência real:** obter readback de provedor, inventário de serviço ativo, direitos de terceiros, contratos, bases legais, critérios de idade, fluxo de incidente e pareceres quando aplicáveis.
4. **Emitir sucessor:** criar um **novo** registro com `parent/supersedes` + identificador do artefato, *sem* sobrescrever silenciosamente `TOKEN_VAZIO`. No registro público publicar apenas hash/identificador sanitizado; o documento privado mantém prova sensível.
5. **Controlar promoção:** gate só muda após prova de autoridade, execução, teste positivo/negativo, revisão pertinente e receipt. Se faltar qualquer componente, continuar `HOLD`.

## Gabarito mínimo para atribuição e revisão

`μID | record_id | human_role | authority_ref(private) | owner_acceptance_ref(private) | independent_reviewer_ref(private) | qualification_ref(private) | exact_artifact_ref | actual_operational_facts | test_positive | test_negative | evidence_receipt | review_date | state | supersedes`.

**Campos não preenchidos = TOKEN_VAZIO, nunca zero.** Publicação de dados de crianças, crença individual, segredos ou relatórios de vulnerabilidades não integra este artefato.

## Falsificadores e critérios de aceitação

`validate_register.py` valida os quatro hashes Git blob de origem, a existência dos arquivos, a cobertura única dos 15 IDs e gates, prioridades P0, limitação de claims, todos os slots humanos vazios e a restrição do diff. `test_validate_register.py` injeta designações fictícias, declarações de 186 certificações, proteção de main alegada, falsos revisores e mutações fora do escopo.

**PASS do CI = integridade estrutural da fila**, não nomeação de pessoas, revisão jurídica, segurança operacional ou conformidade de 186 países.

**F_ok:** registrar exigência de papel/evidência por área e testar contra aprovações falsas. **F_gap:** pessoas/mandatos, provedores, execução, crianças/dados, advogados locais. **F_next:** nomear um responsável real por G01–G04 de forma privada e aprovada; coletar receipts; abrir sucessor auditável para fechar cada caso.

**Rollback:** fechar PR draft sem merge; correção depois de merge somente por commit sucessor. No files under `LICENSE*`, `README.md` raiz, CI existente, provedor ou dados pessoais são alterados.
