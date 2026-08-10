# RAFCODE-Φ — Data, AI, Security & Provenance Addendum V1 — DRAFT

## 1. Objeto

Regular dados, uso de IA, segurança, logs, proveniência, cadeia de custódia e evidência técnica em atividades autorizadas relacionadas à obra.

## 2. Classificação de informação

Cada ativo deve receber uma classe:

- `PUBLIC` — publicável;
- `INTERNAL` — uso interno;
- `CONFIDENTIAL` — acesso contratualmente restrito;
- `PERSONAL_DATA` — sujeito à LGPD;
- `SENSITIVE_PERSONAL_DATA` — controles reforçados;
- `THIRD_PARTY` — sujeito a direitos/licenças de terceiros;
- `EVIDENCE_ORIGINAL` — vestígio histórico imutável;
- `RECEIPT_DERIVED` — recibo/auditoria produzido posteriormente.

## 3. LGPD

Quando houver dados pessoais, contrato e sistema devem definir finalidade, base legal, controlador/operador quando aplicável, minimização, retenção, segurança, direitos dos titulares, subprocessadores, transferências internacionais e resposta a incidentes.

Licença de software não constitui, por si só, base legal para tratamento de dados pessoais.

## 4. Uso de IA

A identificação de agente deve ser baseada em evidência, não em estilo textual.

Campos mínimos:

`agent_provider`, `agent_product`, `model_if_known`, `task/session id`, `timestamp`, `prompt/source reference`, `tool actions`, `commit/PR`, `confidence`, `evidence_uri`.

Se não houver prova: `TOKEN_VAZIO`.

## 5. Treinamento e mineração

Direitos de treinamento, fine-tuning, embedding, indexação ou mineração devem ser tratados separadamente para:

- conteúdo público hospedado em plataforma com termos próprios;
- conteúdo confidencial;
- dados pessoais;
- datasets de terceiros;
- código sob licença específica;
- material fornecido sob contrato enterprise.

Nenhum bloqueio contratual pretende afastar exceção legal obrigatória nem direitos já concedidos validamente por plataforma ou contrato anterior.

## 6. Cadeia de custódia

Para evidência histórica:

`source_id -> original timestamp -> content fingerprint -> storage observation -> Git blob -> commit -> PR -> derived receipt -> audit event`.

Regras:

1. original histórico nunca é reescrito para “melhorar” prova;
2. correção ocorre por novo evento append-only;
3. timestamp de upload não substitui timestamp original;
4. hash identifica estado, não prova sozinho autoria ou verdade científica;
5. pessoa, committer, agente e plataforma são identidades distintas;
6. toda inferência recebe nível de confiança e base documental.

## 7. Segurança de supply chain

Releases de produção devem buscar, conforme viabilidade:

- commits/tags assinados;
- CI reproduzível;
- SBOM;
- hashes de artefatos;
- artifact attestations/provenance;
- segregação de segredos;
- dependências pinadas e verificadas;
- retention de logs;
- política de vulnerabilidades.

## 8. Incidentes

Incidente relevante deve gerar evento com:

`incident_id`, `discovery_time`, `affected_assets`, `data_class`, `containment`, `root_cause`, `evidence_hashes`, `notifications`, `remediation`, `closure_receipt`.

Notificações regulatórias ou a titulares seguem a lei aplicável e avaliação concreta do incidente.

## 9. Auditoria e privacidade

Direito de auditoria não significa acesso ilimitado. Deve observar necessidade, finalidade, proporcionalidade, minimização e confidencialidade.

## 10. Evidência científica

Proveniência de arquivo não valida claim científico. Todo claim científico mantém trilha própria:

`claim -> hipótese -> método -> dataset -> código -> ambiente -> resultado -> incerteza -> reprodução -> revisão independente`.

## 11. Níveis de força

- `P0_ASSERTION` — alegação sem fonte;
- `P1_SINGLE_SOURCE` — uma fonte identificada;
- `P2_CORROBORATED` — duas fontes concordantes;
- `P3_CONTENT_LINKED` — ligação por texto/path/ID;
- `P4_CRYPTO_LINKED` — SHA/hash/blobs correlacionados;
- `P5_REPRODUCED` — cadeia reproduzida;
- `P6_INDEPENDENT` — verificação por terceiro independente.

Nenhum nível é promovido por quantidade de texto.