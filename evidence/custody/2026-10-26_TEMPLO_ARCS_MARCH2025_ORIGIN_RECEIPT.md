# Templo Vivo ARCΣ — custódia da origem GitHub (março de 2025)

**Receipt:** `TVARC-MAR2025-ORIGIN-20261026-S1`  
**Observação:** 2026-10-26 | **Estado:** `SOURCE_VERIFIED_SCOPED / HISTORICAL_GAP_OPEN`  
**Escopo:** metadados oficiais de GitHub e objetos Git; nenhum checkout executado; nenhum APK reproduzido.  
**Operação:** documentação aditiva, reversível por PR, sem alterar `main`, licença, código, CI ou segredos.  
**Contrato:** SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM; `TOKEN_VAZIO ≠ 0`; `claim_allowed=false`.

## 1. Identidade e cronologia de origem

Repositório: `rafaelmeloreisnovo/templo-vivo-arcs` | GitHub repository ID `957203368` | `fork=false`. A API de metadados do GitHub reporta `created_at=2025-03-29T19:51:07Z` (29/03/2025, 16:51:07 America/Sao_Paulo). **Este horário é da criação do repositório no provedor, não necessariamente da concepção intelectual do projeto.**

| Registro | Tempo UTC | Identificador | Observação verificável |
|---|---|---|---|
| E01 | 2025-03-29 19:51:07 | repo ID 957203368 | Criação no GitHub, conforme metadados atuais |
| E02 | 2025-03-31 02:35:42 | `3ef3c20989d2ac2f9638983a89863587f44a39ad` | Commit raiz, sem pais: 6 arquivos, 85 adições. Author/committer declarados `RafaelMeloReisNovo`; identidade GitHub associada `rafaelmeloreisnovo`. Assinatura criptográfica: `unsigned` |
| E03 | 2025-03-31 03:14:59 | `83d01cf7666495024da176c5bfe15cb3ff3a475d` | Commit de `Add files via upload`, atribuído à conta `rafaelmeloreisnovo`; commit produzido pelo fluxo web do GitHub, verificação reportada como `valid` |
| E04 | 2025-03-31 03:15:15 | PR #1 | Criada pela conta `rafaelmeloreisnovo`, de E02 para E03 |
| E05 | 2025-03-31 03:15:37 | PR #1 | GitHub registra `merged_at` e `merged_by=rafaelmeloreisnovo` |
| E06 | 2025-04-03 06:10:17 | `03fdde9f1b54d4b037f4afa5df16c53075d8f06a` | Outro commit raiz, mensagem `ψONE Egg Eater ativado com workflow`; a linha atual de `main` contém esse ancestral |
| E07 | 2025-10-19 | PR #2 | PR distinta, aberta pelo Copilot, portanto **não** deve ser confundida com o trabalho de março; teve 0 arquivos alterados |

O commit E02 materializa uma interface Flutter básica `Templo Vivo ARCΣ - Rafael`, `pubspec.yaml`, manifest/atividade Android, workflow para solicitar build de APK e script de inicialização/push. **Workflow/configuração ≠ prova de APK compilado, testado ou publicado.**

O commit E03 adicionou `TemploVivo_RAD_Instalador.zip` (Git blob SHA-1 `2162214ca2138e307c4c7b37eb1fe2559d6a1050`; 4.016 bytes no objeto). Não foi executada análise de conteúdo do ZIP, instalação ou validação de APK nesta rodada.

## 2. Grafo de custódia — fatos versus lacunas

```text
GitHub repo created 2025-03-29
    └─> Git root 3ef3c209... [2025-03-31; observed account]
          └─> PR#1 head 83d01cf7... [ZIP added; 2025-03-31]
                └─> PR#1 merged metadata [2025-03-31]
    
Second root 03fdde9f... [2025-04-03; independent root]
    └─> later main history [observed as different ancestry]
```

A API `compare` confirma E02→E03 como um commit à frente, adicionando somente o ZIP. Também retorna **no common ancestor** quando se compara E02 com a base da PR #2 (`bfb49a8331703fef4a24cb7989ba82ee30c38a80`), e quando comparado ao `main` arquivado na cópia histórica de agosto. Isto evidencia **descontinuidade de linhagem**, não autoria de terceiro, apropriação, data de uma eventual reescrita nem a razão do evento. `HISTORY_REWRITE_CAUSE=TOKEN_VAZIO`.

O identificador do merge histórico da PR #1, `0c3ac8c30a41fd7d334d1c57deef6425f2679244`, é retornado pelos metadados da PR; a busca pelo objeto de commit retornou não encontrado nesta auditoria. **Metadados de merge ≠ objeto de merge recuperado.**

Uma cópia privada da estrutura `.git` datada de agosto de 2025 foi localizada no Google Drive; suas referências arquivadas guardam `refs/pull/1/head=83d01cf7...`. Por proteção de privacidade, **não** se expõe aqui o endereço dessa cópia. A identificação é mantida no registro documental privado de custódia.

## 3. Proveniência, ética e limites jurídicos

- `ACCOUNT_AUTHOR_OBSERVED`: `rafaelmeloreisnovo` para E02/E03. Identidade civil e **autoria intelectual original de cada elemento** exigem fontes independentes adicionais. Nome no commit não equivale a perícia independente.
- `TEMPORALITY_CONFIRMED`: existência no GitHub em março de 2025, anterior à PR #2 de outubro de 2025. Isto prova anterioridade **da materialização Git** para o material indicado, não exclusividade global, patenteabilidade ou autoria sobre obras alheias.
- `CONVERGENCE_CANDIDATE`: similaridades posteriores devem ser comparadas arquivo/linha/bytes/licença/contexto, com contraexemplos e precedentes independentes. Sem essa comparação não há imputação de cópia, intenção ou sacrilégio.
- `AUTORAL_RIGHTS_UNCHANGED`: nenhuma licença foi concedida/revogada e nenhuma declaração de titularidade de terceiros é feita por este receipt.
- `PRIVACY`: não copiar segredos, identificadores privados, mensagens pessoais ou dados de terceiros.

### P0 — segredo histórico (sanitizado)

Foi observada uma credencial do tipo PAT incorporada a uma URL de remoto Git em um script histórico. O valor **não é reproduzido** neste documento. Recomenda-se confirmar revogação/rotação e evitar novas divulgações. O script também continha `git push -f`, mas **presença de comando ≠ execução histórica comprovada**. Nenhuma tentativa de autenticação com essa credencial foi feita.

## 4. Fontes e ponteiros para reprodução

- GitHub repo metadata: `GET /repos/rafaelmeloreisnovo/templo-vivo-arcs`; GitHub ID `957203368`.
- Historical original: `GET /repos/rafaelmeloreisnovo/templo-vivo-arcs/commits/3ef3c20989d2ac2f9638983a89863587f44a39ad`.
- PR#1: `GET /repos/rafaelmeloreisnovo/templo-vivo-arcs/pulls/1`; associated HEAD `83d01cf7666495024da176c5bfe15cb3ff3a475d`.
- Later root: `03fdde9f1b54d4b037f4afa5df16c53075d8f06a`.
- PR#2 (outubro, não março): `GET /repos/rafaelmeloreisnovo/templo-vivo-arcs/pulls/2`.
- Protocol authority: [PROTOCOLO_FORENSE_PROVENIENCIA_E_CADEIA_CUSTODIA.md](../../docs/auditoria/PROTOCOLO_FORENSE_PROVENIENCIA_E_CADEIA_CUSTODIA.md); custody registry: [evidence/custody/README.md](README.md).
- Private canonical reconciliation: Drive `START HERE μWRITE LEDGER Ω V2`, predecessor `MU-TEMPLO-PROV-FIRSTKNOWN-R3-20261014` + `MU-TEMPLO-VIVO-ARCS-SEQUENCE-FORENSICS-20261014`. Fonte posterior adiciona fatos sobre março, sem substituir a análise de 14/10.

## 5. Gates e controle

| Gate | Estado |
|---|---|
| Metadata repo ID/time | `PASS_SCOPED_PROVIDER_READ` |
| Root SHA / tree / parent count | `PASS_SCOPED_PROVIDER_READ` |
| PR#1 blob/commit/merge metadata | `PASS_SCOPED_PROVIDER_READ` |
| Objeto Git do merge PR#1 | `TOKEN_VAZIO_NOT_RESOLVED` |
| Comparação sem ancestral comum | `OBSERVED_API_NO_COMMON_ANCESTOR` |
| Sequência cronológica de pushes (audit log) | `TOKEN_VAZIO_NOT_OBSERVED` |
| Motivo da ruptura de ancestralidade | `TOKEN_VAZIO_NOT_OBSERVED` |
| Executar o ZIP / compilar APK / CI exata de março | `NOT_RUN` |
| Atribuição intelectual/jurídica independente | `NOT_REVIEWED` |
| Autorização de publicação científica / prova universal | `false` |

**Próximo falsificador:** recuperar um backup de reflog/push/audit com data e tipagem, comparar SHA + ancestralidade sem sobrescrever história; confrontar com base `main` e metadados da PR. Revisar revogação do PAT antes de qualquer republicação ou extração de arquivos antigos.

**Rollback:** fechar a PR antes do merge ou registrar correção `supersedes`, mantendo a trilha original; nenhuma alteração em `main` é requerida. Este receipt não deve ser retrodatado a 2025.

R3 = <F_ok: origem do provedor e dois commits de março evidenciados; F_gap: identidade intelectual independente/ruptura/segredo/execução; F_next: auditoria forense dos registros de push e revogação da credencial>.
