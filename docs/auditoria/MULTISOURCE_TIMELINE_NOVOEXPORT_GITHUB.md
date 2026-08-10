# Timeline multi-fonte — NOVOexport × GitHub

## Objetivo

Construir prova temporal mais robusta cruzando fontes independentes ou semi-independentes:

1. exportações ChatGPT/NOVOexport;
2. timestamps de conversas e mensagens;
3. arquivos e metadados do Google Drive;
4. commits Git;
5. blobs/trees Git;
6. pull requests e branches;
7. receipts e checkpoints posteriores.

A tese permitida é de **corroboração temporal multi-fonte**, não de verdade científica automática nem de novidade mundial.

## Fonte NOVOexport observada

- pasta raiz Drive: `NOVOexport`;
- Drive ID: `1P7hJq5R4fgYGEQIVNgRvllAad2lGxWEv`;
- checkpoints existentes registram ingestão de arquivos do tipo `conversations-000.json`, `conversations-001.json` etc.;
- checkpoint observado registra `conversations_total: 51` e cobertura parcial de mensagens;
- outros documentos de 2026 já operam em modo `APPEND_ONLY` e com `CLAIM_ALLOWED=false`.

Esses checkpoints não substituem o JSON bruto. Eles servem como evidência auxiliar de que existe uma cadeia de ingestão/indexação sobre o NOVOexport.

## Modelo de evento temporal

Cada conceito deve ser convertido em um ou mais eventos:

```text
EVENT_ID
CONCEPT_ID
SOURCE_KIND = chat_message | drive_file | git_blob | git_commit | git_pr | receipt
SOURCE_ID
SOURCE_HASH
TIMESTAMP_ORIGINAL
TIMESTAMP_OBSERVED
ACTOR
AGENT
REPOSITORY
PATH
PARENT_EVENT_IDS[]
CLAIM_STATUS
```

## Regra de força

Uma data isolada é indício. A força aumenta quando fontes diferentes convergem:

```text
chat_timestamp
    ↓
mensagem contendo conceito/código/URL/SHA
    ↓
arquivo exportado / Drive metadata
    ↓
Git blob
    ↓
commit SHA + author/committer timestamp
    ↓
PR / branch / agent event
    ↓
receipt posterior
```

Classificação sugerida:

- T1 — uma fonte temporal;
- T2 — duas fontes concordantes;
- T3 — três fontes com ligação de conteúdo;
- T4 — conteúdo idêntico ou hash/URL cruzado entre fontes;
- T5 — cadeia reproduzível com origem→transformação→commit;
- T6 — verificação independente/externa.

## Correlação por conceito

Para cada mecanismo histórico, procurar no NOVOexport:

- nome exato e variantes ortográficas;
- primeira mensagem;
- mensagem que contém código integral;
- links `github.com/.../commit/<sha>`;
- links `blob/<sha>/<path>`;
- nomes de arquivos;
- hashes SHA-1/SHA-256/BLAKE*;
- comandos `git add`, `git commit`, `git push`;
- menções a Copilot, Codex, GPT, ChatGPT ou outro agente;
- mensagens imediatamente anteriores e posteriores ao commit.

## Primeiros alvos

1. `Manifest.txt` / `ee9c7d4a...` — 23/05/2025;
2. `Entropia.md` / `2e6562b0...` — 26/06/2025;
3. `Fe.py` / `a8a96d0...` — 09/07/2025;
4. `Ciclo fe` / `2f323228...` — 09/07/2025;
5. `Minha entropia no Verbo VERBO VIVO.md` / `1a8467b7...` — 27/07/2025;
6. `RafaelVisaoFiBinnaci(Index of Entropy)` / `48b62c7e...` — 27/07/2025;
7. `RaIa∆...` / `becf137a...` — 27/07/2025;
8. `utopia_marte.yaml` / `2eeab71c...` — 27/08/2025;
9. `cristal.sh` / `4fe1d9dc...` — 27/08/2025;
10. `marte.dart` / `b1a57f56...` — 27/08/2025;
11. `Patentes.md` / `b64e6ec6...` — 30/08/2025;
12. `Hashing times` / `a2b13967...` — 10/10/2025;
13. PR #2 Copilot — 19/10/2025;
14. PR #3 Copilot — 22/23/10/2025;
15. primeiros PRs Codex — 2026.

## Regras de cadeia de custódia

- nunca editar o JSON bruto para “corrigir” datas;
- preservar timezone original e adicionar UTC normalizado em campo separado;
- distinguir `create_time`, `update_time`, timestamp de exportação e timestamp do Drive;
- não usar data do upload ao Drive como data original da conversa;
- preservar message ID/conversation ID quando presentes;
- calcular hash do arquivo bruto e de cada chunk normalizado;
- guardar transformações em ledger append-only;
- `TOKEN_VAZIO` quando uma ligação mensagem↔commit não estiver demonstrada;
- não afirmar autoria de IA com base apenas no estilo textual.

## Claim gate

Permitido quando sustentado:

- `PRE_COMMIT_CHAT_EVIDENCE=true` — conversa precede commit e contém conteúdo correlacionável;
- `CHAT_TO_COMMIT_LINK=true` — mensagem contém SHA/URL/path que liga diretamente ao Git;
- `MULTISOURCE_TEMPORAL_CORROBORATION=true` — pelo menos duas fontes temporalmente e semanticamente coerentes;
- `PRE_AGENT_ARCHITECTURE=true` — mecanismo documentado antes do agente GitHub identificado.

Bloqueado sem evidência específica:

- `CHATGPT_CREATED_COMMIT=true`;
- `WORLD_FIRST=true`;
- `PATENT_PRIORITY=true` como conclusão jurídica automática;
- `SCIENTIFIC_VALIDATION=true`.

## Resultado esperado

O produto final deve ser um grafo temporal, não uma lista linear:

```text
ConversationEvent ─┐
DriveRawEvent ─────┼→ ConceptNode → GitBlob → GitCommit → PR/Agent
LocalFileEvent ────┘                         ↓
                                         Receipt
```

Esse grafo permite demonstrar quando um conceito aparece, quando vira arquivo/código, quando entra no Git e quando um agente posterior passa a manipulá-lo.