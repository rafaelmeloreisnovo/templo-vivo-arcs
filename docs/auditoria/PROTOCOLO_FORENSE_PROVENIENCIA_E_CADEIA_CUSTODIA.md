# Protocolo Forense de Proveniência e Cadeia de Custódia

**Estado:** `AUDIT_PROTOCOL_V1`  
**Regra:** append-only para evidência histórica; nunca reescrever o artefato de 2025 para fortalecê-lo retroativamente.  
**Claim gate:** `claim_allowed=false` para novidade mundial, nova física ou atribuição de autoria a agente sem vínculo verificável.

## 1. Objetivo

Converter o histórico do repositório em uma cadeia de evidência reproduzível capaz de responder, para cada mecanismo:

1. o que existia;
2. quando apareceu no Git;
3. em qual arquivo e commit;
4. quem aparece como autor e committer;
5. se havia agente identificável;
6. qual capacidade o artefato realmente demonstra;
7. qual transformação posterior ocorreu;
8. quais claims permanecem não demonstrados.

## 2. Modelo mínimo de evidência

Cada prova deve ser descrita por:

```text
EvidenceRecord = {
  proof_id,
  concept_id,
  repository,
  path,
  blob_sha,
  commit_sha,
  parent_sha,
  authored_at,
  committed_at,
  author_account,
  committer_account,
  agent_identity,
  agent_evidence,
  diff_summary,
  capability_class,
  capability_demonstrated,
  limitation,
  derived_from[],
  derived_into[],
  reproduction_status,
  claim_status
}
```

Campos desconhecidos recebem `TOKEN_VAZIO`, nunca inferência silenciosa.

## 3. Classes de capacidade

- `C0_TEXTUAL`: afirmação ou descrição.
- `C1_FORMAL`: fórmula, esquema, ciclo ou contrato conceitual explícito.
- `C2_STRUCTURED`: YAML/JSON/CSV/esquema legível por máquina.
- `C3_EXECUTABLE_PARTIAL`: código plausível com placeholder, dependência ou lacuna conhecida.
- `C4_EXECUTABLE`: procedimento executável com efeito observável.
- `C5_REPRODUCED`: executado novamente em checkout limpo com receipt.
- `C6_INDEPENDENT`: reprodução externa/independente.

Nenhum nível superior é herdado automaticamente.

## 4. Procedimento por artefato

### P1 — Identificação

- fixar `repository/path/commit_sha`;
- capturar blob SHA quando disponível;
- registrar horário UTC e fuso de apresentação;
- registrar autor e committer separadamente.

### P2 — Preservação

- não alterar o arquivo original;
- calcular hash do conteúdo recuperado;
- guardar resposta/API ou export equivalente;
- registrar ferramenta e data da auditoria.

### P3 — Autoria/agente

Classificar separadamente:

- `AUTHOR_OBSERVED`: conta registrada como author;
- `COMMITTER_OBSERVED`: conta ou infraestrutura que efetivou commit;
- `AGENT_EXPLICIT`: task/PR/bot/branch identifica agente;
- `AGENT_INFERRED`: estilo ou contexto apenas — não serve como prova forte;
- `AGENT_UNKNOWN`: `TOKEN_VAZIO`.

`Signed-off-by` é declaração útil de cadeia, mas não equivale por si só a assinatura criptográfica qualificada.

### P4 — Capacidade

Perguntar sempre: **o que o diff faz, não o que o texto diz que faz?**

Exemplos:

- um `.py` contendo prosa/fórmula = `C1_FORMAL`, não runtime;
- YAML com campos e invariantes = `C2_STRUCTURED`;
- Dart com parser marcado como placeholder = `C3_EXECUTABLE_PARTIAL`;
- shell que calcula SHA-256, timestamp e grava changelog = `C4_EXECUTABLE` até reprodução limpa.

### P5 — Derivação

Registrar arestas:

```text
Entity(source commit/blob)
  -> Activity(read/transform/hash/classify)
  -> Entity(derived artifact)
  <- Agent(human/agent/tool)
```

Esse formato é compatível conceitualmente com W3C PROV: Entity, Activity e Agent.

### P6 — Reprodução

Para código executável:

1. checkout limpo do commit histórico;
2. ambiente identificado;
3. executar apenas procedimentos seguros;
4. guardar stdout/stderr/exit code;
5. hash de entradas e saídas;
6. receipt separado, datado no presente;
7. nunca afirmar que a execução atual ocorreu em 2025.

### P7 — Claim gate

Estados:

- `PROVED_INTERNAL`: demonstrado dentro do histórico do repo;
- `PROVED_PRE_AGENT`: materializado antes do primeiro agente GitHub explicitamente comprovado;
- `PARTIAL`: há material, mas capacidade incompleta;
- `HISTORICAL_CLAIM`: afirmação preservada, não validada;
- `TOKEN_VAZIO`: evidência insuficiente;
- `BLOCKED_PRIOR_ART`: exige estado da técnica externo.

## 5. Melhores práticas de referência

### Evidência digital

A ISO/IEC 27037 orienta identificação, coleta, aquisição e preservação de evidência digital potencialmente probatória. Aplicação aqui: preservar originais, documentar manipulações e manter registros de custódia.

### Proveniência de dados

W3C PROV-O permite representar proveniência entre entidades, atividades e agentes em sistemas heterogêneos. Aplicação aqui: `arquivo/commit -> transformação -> derivado`, com agente explicitamente separado.

### Cadeia de software

SLSA trata proveniência como informação verificável sobre onde, quando e como um artefato foi produzido. Aplicação aqui: distinguir source provenance histórica de build provenance futura.

### Atestações

GitHub Artifact Attestations usa claims criptograficamente assinados ligando artefatos a workflow, repositório, commit e evento. Aplicação futura: binaries/releases, não para fingir retroatividade em arquivos históricos.

### Supply-chain links

in-toto registra etapas, comandos e materiais/produtos em links assináveis e valida a sequência contra um layout. Aplicação possível: formalizar a árvore RAFAELIA como `layout` de atividades autorizadas.

## 6. Assinatura e identidade

Para novos commits/receipts:

- preferir commits/tags assinados por SSH/GPG/S/MIME;
- habilitar verificação consistente quando operacionalmente viável;
- registrar chave/identidade separadamente da autoria intelectual;
- usar timestamp externo quando necessário, sem atribuir a ele data retroativa.

## 7. Invariante de custódia

```text
ORIGINAL
 -> IDENTIDADE(hash/SHA)
 -> CONTEXTO(commit/time/path)
 -> AGENTE/ATIVIDADE
 -> DERIVAÇÃO
 -> RECEIPT
 -> VALIDAÇÃO
```

A convergência relevante da obra não é a presença isolada de palavras semelhantes, mas a repetição dessa estrutura em domínios diferentes.

## 8. Anti-padrões proibidos

- mudar arquivo antigo para “melhorar” anterioridade;
- confundir data no nome com data comprovada;
- confundir `author` com `committer`;
- atribuir GPT/Codex sem task/PR/log ou outro vínculo;
- chamar descrição de POC executável;
- transformar analogia científica em validação científica;
- transformar prioridade interna em novidade mundial;
- usar valor de mercado histórico como avaliação independente.

## 9. Próximo gate

`FORENSIC_GATE_PASS` somente quando cada mecanismo prioritário tiver:

- commit e path;
- diff lido;
- capacidade classificada;
- cadeia de derivação mínima;
- limite de claim;
- reprodução para os itens executáveis relevantes.
