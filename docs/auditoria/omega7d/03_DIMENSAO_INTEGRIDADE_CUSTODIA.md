# Ω7D — Dimensão 3: Integridade e cadeia de custódia

## Objeto
Preservar a identidade dos vestígios históricos e demonstrar cada transformação sem reescrita retroativa.

## Invariante
`original -> hash -> commit -> receipt -> verificação`

## Contrato
1. original histórico é imutável;
2. auditoria posterior gera novo artefato, nunca substitui o vestígio;
3. cada transformação recebe hash, data, ferramenta e responsável;
4. diferença entre hash Git, SHA-256 de arquivo, assinatura e carimbo temporal deve ser explícita;
5. cadeia quebrada reduz o claim ao último elo íntegro demonstrado.

## Receipt mínimo
`proof_id, repo, path, blob_sha, commit_sha, sha256_optional, timestamp_observed, author, committer, agent, source_ref, transformation, verifier, status`.

## Boas práticas
- commits/tags assinados para novos marcos;
- hashes externos para artefatos críticos;
- attestations para builds/releases;
- append-only para ledgers;
- comparação blob-a-blob para detectar reescrita;
- registrar ambiente de reprodução.

## Heurística de força
`custody_strength = min(identity, integrity, chronology, provenance, reproducibility)`

Muitos documentos não compensam um elo essencial ausente.

## TOKEN_VAZIO
Hash, origem ou transformação ausente = gap explícito, não preenchimento estimado.
