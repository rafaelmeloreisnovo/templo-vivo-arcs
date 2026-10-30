# Templo Vivo ARCΣ — Auditoria de titularidade, concessões e rito internacional
**V1 · Data-base 2026-10-30 · SOURCE_BOUND / DOCUMENTARY_ONLY / CLAIM_ALLOWED=false**
**Produtor:** `rafaelmeloreisnovo/templo-vivo-arcs` · **source main:** `e5468415e22d26668c0094522eac5b33f0079669`
**Escopo:** inventário de metadados Git e comparação de documentos existentes; nenhum conteúdo binário inspecionado, nenhum dado pessoal extraído, nenhum contrato externo autenticado; sem laudo ou parecer profissional.
**Artefato associado:** [Censo file-level de 373 arquivos](./2026-10-30_TVARCS_FILE_RIGHTS_CENSUS_373_V1.jsonl). Cada registro preserva `path, blob_sha1, size_bytes, class, duplicate_of` e estados de prova/titularidade separados. Git blob SHA-1 é identificador de conteúdo Git, **não** comprovação autônoma da identidade civil, anterioridade absoluta, copyright ou data de criação.

## A. Medição da árvore exata
- 447 entradas no tree Git; 373 blobs de arquivo e 74 diretórios; `truncated=false`.
- 357 SHAs de blob distintos; **9 famílias de conteúdo idêntico** e 16 caminhos excedentes por duplicação. A duplicidade é estrutural: não permite afirmar direitos iguais, cópia ilegítima ou dispensa de atribuição.
- Classes inferidas **apenas por extensão**: 162 documentos/avisos; 49 mídia; 46 dados/manifestos estruturados; 41 código; 22 configuração; 8 binários/arquivos comprimidos; 45 outros. Isso não é classificação de conteúdo validada.
- Em `LICENSES/`, 25 caminhos nominados `IMG/Screenshot/Screenshots` são mídia/arquivos; sua presença numa pasta de licenças **não** lhes confere licença nem os transforma em prova de autoria. Inspeção autorizada de consentimentos/direitos e de dados pessoais ainda falta.
- `psione-egg (1).apk` e `psione-egg (2).apk` têm blob idêntico; `psione-egg-real (3).apk` é diferente. APK / ZIP não foram desmontados nem submetidos a SBOM, assinaturas ou análise de componentes.
- Gravações com nomes `hino_hurriano6_fractal.wav`, `musica_sumeria_reconstruida.wav` e outros são **candidatos a clearance de composição, arranjo, gravação, intérpretes e fontes**. Nomes não provam uso indevido nem domínio público.

## B. Conflito documental material — P1
**Fontes localizadas no HEAD:** `docs/legal/LICENSING_AND_RIGHTS_MATRIX_V1.md`, `LICENSE_POLICY.md`, `LICENSES/SOFTWARE_LICENSE_DECISION.md`, `LICENSE-RAFCODE-PROPRIETARY-V1.md`, `docs/legal/RAFCODE_PHI_SOURCE_AVAILABLE_LICENSE_V1.md`.

A matriz V1 afirma, na linha de código original e documentação original, tratamento padrão `RAFCODE Proprietary V1`. O gate de decisão do software, entretanto, mantém `TOKEN_VAZIO / DECISION_REQUIRED` e nega promoção geral de SPDX. O documento `RAFCODE_PHI_SOURCE_AVAILABLE_LICENSE_V1.md` declara ser **DRAFT**, não prova adoção. Logo, os materiais não permitem inferir que toda a árvore esteja abrangida por uma licença proprietária uniforme nem que todo o repositório tenha sido aberto sob licença OSI. **Resolução operacional não-regressiva:** registro `CONFLICT_LICENSE_SCOPE_UNRESOLVED`; respeitar direitos de terceiros, concessões válidas anteriores e notices específicos; exigir ato de adoção granular e comprovação da cadeia de titularidade. Este relatório **não modifica** documentos históricos nem estabelece nova licença.

### Invariantes jurídicas
1. `COMMITS != IDENTITY_CIVIL != AUTORIA_INTELECTUAL != TITULARIDADE_PATRIMONIAL`.
2. `VISIBLE_ON_GITHUB != DOMÍNIO_PÚBLICO != LICENSE_GRANT_AUTOMÁTICO`; os Termos de Serviço do provedor e exceções legais permanecem separados.
3. `DUPLICATE_CONTENT_HASH != IDENTIDADE_DE_AUTOR`; um mesmo hash representa mesmo byte-stream Git e nada mais.
4. `SOFTWARE != TEXTO != FOTOGRAFIA != GRAVAÇÃO != DADOS != MARCA != PATENTE`.
5. `SÚMULA_VINCULANTE_BR != STARE_DECISIS_US_UK != PRECEDENTE_EU`; cortes e obrigações não são transponíveis automaticamente.
6. `LEGAL_OPINION = TOKEN_VAZIO` enquanto faltar advogado habilitado, fatos concretos, versão da norma e competência territorial.

## C. Dependências declaradas, sem SBOM completo — P1
Fonte direta `pubspec.yaml`: Flutter SDK + `yaml: ^3.1.3`. Fonte direta `android/app/build.gradle`: `androidx.core:core-ktx:1.10.1`, `androidx.appcompat:appcompat:1.6.1`. Fonte direta `estado-fractal-haja/requirements.txt`: `pydantic>=2.7,<3`, `numpy>=1.26,<3`, `scipy>=1.13,<2`, `cryptography>=42,<47`, `networkx>=3.2,<4`. **Não havia** `pubspec.lock`, `package-lock.json`, `poetry.lock`, `Cargo.lock` nem outro lockfile padrão procurado na árvore. Versões transitivas/resolução de build e notices de binários: `TOKEN_VAZIO_UNMEASURED`.

Fonte externa independente: [Flutter FAQ](https://docs.flutter.dev/resources/faq) declara **BSD-3-Clause para o framework**, com licenças adicionais para engine/dependências; isso não resolve os termos de cada pacote Dart nem os componentes efetivamente incorporados no APK. Próxima etapa: inventário SBOM em build reproduzível e inspeção de permissões/avisos do pacote final, sem mudar grant por hipótese.

## D. Plano de comprovação individual (não assinar por terceiros)
Para cada linha do censo, coletar, em repositório privado e mediante autorização:
`asset_id | original_file_hash/URL | created_evidence | lawful_author | coauthor/reviewer | contributor_source | employment_or_assignment | previous_grants | upstream_license | owner_of_economic_rights | moral_rights | permissions_scope | privacy_release | territorial_scope | legal_reviewer | status | evidence_ref`.

**Critérios de evidência:** arquivos originais/datados, histórico do produtor, contratos/cessões quando cabíveis, autorizações de mídia, lista de créditos, permissões upstream completas, notas sobre IA e contribuições humanas e registro de versões. Nenhuma declaração de terceiro é fabricada; ausência recebe `TOKEN_VAZIO_UNVERIFIED`. Credenciais, dados de crianças, imagens identificáveis e contratos privados NÃO entram no repositório público.

## E. Verificação legal/falsificação — 24 países
Referência matriz existente: [V3 24 jurisdições](../2026-10-30_TVARCS_COMPARATIVE_LAW_24_JURISDICTIONS_V3.md). O censo de arquivos NÃO valida por si só os julgamentos dos 24 países.

**Nesta rodada, fontes primárias examinadas de forma direcionada:**
- **Brasil:** [Lei 9.610/1998 arts. 7, 8, 24, 29, 49](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm) distingue expressão/método, direitos morais, autorizações e cessão; [CPC art. 927](https://normas.leg.br/?urn=urn:lex:br:federal:lei:2015-03-16;13105!art927) distingue espécies de precedentes.
- **EUA:** [17 USC §411, vigente em 2026](https://uscode.house.gov/us/usc/119-120/t17/s411/) prevê requisito de registro em ações por infração de obras dos EUA, ressalvadas hipóteses e exceções legais. Não conflitar com proteção automática de Berna.
- **Reino Unido:** [CDPA 1988, seção 16](https://www.legislation.gov.uk/ukpga/1988/48/section/16) descreve atos reservados e sujeição a atos permitidos/licenças; versão consolidada e caso específico devem ser fixados antes de petição.
- **Itália:** [Lei 633/1941, art. 1, consolidada em 2026](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=041U0633&atto.dataPubblicazioneGazzetta=1941-07-16) com alteração pela [Lei 132/2025 art.25](https://www.normattiva.it/eli/id/2025/09/25/25G00143/CONSOLIDATED) sobre criação humana inclusive com auxílio de IA. **Verificar a expressão humana efetivamente demonstrável**.

Demais 20 jurisdições da matriz V3: a existência de referência legislativa **não equivale a jurisprudência específica verificada**. Para as 24, `PIN_CITATION | FOLLOWUP_HISTORY | CASE_FACTS | APPLICABILITY | COUNSEL_SIGNOFF` continuam `TOKEN_VAZIO` neste trabalho, inclusive nas quatro normas verificadas. Nenhuma conclusão de exigibilidade internacional é permitida.

### Checklist do parecer profissional por jurisdição
`jurisdiction | competent_legal_professional | professional_registration_credential_checked | engagement_scope | licensed_asset_list | official_law_version | binding_case_name | court | decision_date | holding_paragraph | adverse_authority | differences_in_facts | choice_of_law | standing | limitation | forum | privacy_child_risk | license_interaction | written_opinion_ref | legal_review_status`.
Toda linha começa `LEGAL_REVIEW_NOT_OBTAINED`; não inventar assinatura, número de registro ou parecer. Para atuação multinacional, pode ser necessário mais de um profissional, e não apenas uma consulta.

## F. Prioridade, risco e menor ação
| Urgência | Lacuna observada | Próxima evidência | Gatilho de bloqueio |
|---|---|---|---|
| P0 | Possível exposição de dados em screenshots, fotos, ZIPs e mídia pública; conteúdo não inspecionado | triagem privada por responsável, sem republicação dos bytes | `PRIVACY_REVIEW_REQUIRED` |
| P0 | Segurança do fornecedor/segredo histórico/branch protection mencionada no CURRENT_STATE, fora desta auditoria | administrador verifica revogação, regras e auditoria do provider | `SECURITY_SIGNOFF_REQUIRED` |
| P1 | Conflito V1 vs decisão de licença de software | análise por arquivo e ato de adoção do titular | `LICENSE_DECISION_REQUIRED` |
| P1 | Sem lockfiles/SBOM de release verificado | build reprodutível, licenças transitivas e componentes de APK | `DEPENDENCY_CHAIN_UNKNOWN` |
| P1 | 373 arquivos sem documento de cadeia de título individual neste censo | fontes originais e cessões/autorizações por ativo | `TITLE_NOT_ATTESTED` |
| P1 | Casos concretos e jurisdição para os 24 países | advogado habilitado, decisão/citação precisa, fatos e contraditório | `COUNSEL_NOT_OBTAINED` |

## G. Política de execução e gate
**Resultado observável:** GitHub tree + textos/fontes designadas; todo o resto fica `TOKEN_VAZIO`. Inventário técnico completo por *pathname* do snapshot não implica auditoria material de conteúdo, pessoal ou jurídico.

**Mudança:** branch separada; nenhum merge, PR, CI manual, relicenciamento, remoção, alteração de `main` ou publicação de documentos privados. **PROMOTION=HOLD; claim_allowed=false** até auditoria e revisão humana competente. **Rollback:** excluir/fechar branch não mesclada após autorização; conservar recibo em ledger privado e histórico, sem destruir evidência.

**R3:** F_ok=censo file-level 373/373, 9 grupos de duplicação, dependencies declaradas e conflito de licença tipado; F_gap=cadeia documental, privacidade dos binários, lock/SBOM, casos/advogados; F_next=triagem de mídia e contratos privada + artefato de SBOM + parecer restrito às jurisdições com atividade/dano real.
