# Invariante Formal de Proveniência, Cadeia de Custódia e Licenciamento — V1

Estado: `EVIDENCE_FIRST / CLAIM_GATE_ON / LEGAL_REVIEW_RECOMMENDED`

## 1. Objeto

Este documento organiza a cadeia técnica e documental dos artefatos do repositório sem converter automaticamente registros históricos em conclusões jurídicas, científicas ou de patenteabilidade.

## 2. Invariante probatória

`IDEIA/REGISTRO -> ARTEFATO -> COMMIT -> SHA -> ESTADO DO REPOSITÓRIO -> PR/BRANCH/TAG QUANDO EXISTENTE -> TESTE/RECEIPT -> CLAIM DELIMITADO`

Cada seta exige evidência própria. Ausência de um elo não pode ser preenchida por narrativa.

## 3. Classes de evidência

- E0: alegação sem artefato verificável.
- E1: documento/conteúdo preservado.
- E2: artefato estruturado ou código preservado.
- E3: commit Git identificável com SHA/data/tree.
- E4: evento de integração/proveniência adicional (PR, merge, tag, assinatura ou equivalente).
- E5: reprodução controlada com ambiente, stdout/stderr, hashes e receipt.
- E6: validação independente ou terceiro confiável, quando aplicável.

## 4. Condução histórica observada

No intervalo anterior aos PRs explicitamente atribuídos ao Copilot em outubro de 2025, o histórico contém commits materiais criando, entre outros, `Manifest.txt`, `Entropia.md`, `Fe.py`, `Ciclo fe`, artefato de derivação por SHA, `Raia∆`, `utopia_marte.yaml`, `cristal.sh`, `marte.dart`, `Patentes.md`, `LICENSE` e `Hashing times`.

A conclusão permitida é limitada: existem componentes materiais e arquiteturais versionados antes desses eventos de agente. Não se infere daí, sem prova adicional, autoria textual exclusiva de cada linha, novidade mundial, patente concedida ou validade científica.

## 5. Autoria, anterioridade e titularidade

Devem ser tratadas separadamente:

- **Autoria:** relação entre pessoa e expressão concreta da obra.
- **Anterioridade documental:** demonstração de que determinado conteúdo/artefato existia em certo estado/data verificável.
- **Titularidade:** quem detém os direitos patrimoniais ou permissões pertinentes; pode depender de contratos, cessões, emprego, colaboração e legislação aplicável.
- **Inventoria/patenteabilidade:** questão própria, dependente de contribuição inventiva, estado da técnica, jurisdição e procedimento formal.

Commit, hash ou timestamp são evidências técnicas úteis, mas não substituem sozinhos a análise jurídica desses elementos.

## 6. Cadeia de custódia mínima

Para cada ativo relevante preservar:

`asset_id, path, blob_sha, commit_sha, parent_sha, author/committer metadata, timestamps, branch/ref, PR/tag/release quando houver, source_pointer externo quando houver, hash do receipt, ambiente de reprodução, claim_status`.

Mudanças posteriores devem ser aditivas ou versionadas; não apagar o estado histórico usado como evidência.

## 7. Regra de agentes de IA

Registrar separadamente:

`human_input`, `agent_identity`, `agent_prompt/event`, `agent_output`, `tree_delta`, `merge/adoption decision`.

A existência de um agente em um PR não demonstra que o agente originou conteúdo preexistente; inversamente, conteúdo anterior ao evento do agente não prova sozinho ausência de assistência anterior. A conclusão segue somente a evidência disponível.

## 8. Licenciamento

O arquivo `LICENSE` histórico deste repositório contém manifesto e propostas de proteção, mas não constitui uma licença de software operacional suficientemente clara para terceiros. Por isso ele não deve ser silenciosamente substituído.

A política V1 é:

1. preservar `LICENSE` como artefato histórico;
2. adicionar `LICENSE_POLICY.md` como regra prospectiva e legível;
3. nenhum direito adicional é presumido por silêncio;
4. componentes de terceiros mantêm suas próprias licenças;
5. qualquer licença futura de código deve identificar escopo, permissões, condições, limitações e versão;
6. conteúdo, marcas, dados, código e material de pesquisa podem exigir regimes diferentes;
7. contribuições externas exigem declaração clara de proveniência e direitos suficientes para contribuir.

## 9. Claims bloqueados sem prova adicional

`WORLD_FIRST`, `PATENT_GRANTED`, `EXCLUSIVE_AUTHORSHIP_OF_ALL_LINES`, `SCIENTIFICALLY_VALIDATED`, `THIRD_PARTY_INFRINGEMENT`, `AGENT_OR_COMPANY_COPIED_FROM_REPOSITORY`.

## 10. Regra de promoção

`claim_level(t+1) > claim_level(t)` somente se `evidence_delta > 0` e o novo elo for preservado na cadeia de custódia.

## 11. Finalidade

Esta estrutura serve para preservação, auditoria, pesquisa de anterioridade, governança de contribuições e preparação para análise jurídica profissional. Não é parecer jurídico e não cria, por si só, direitos que a lei aplicável não reconheça.