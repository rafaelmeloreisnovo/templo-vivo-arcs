# Templo Vivo ARCS — Interaction Feedback & Evolution Protocol V1

**status:** DRAFT_REVIEW_REQUIRED  
**claim_allowed:** false  
**mode:** append-only  
**scope:** toda interação relevante que altere entendimento, governança, evidência, prioridade ou próximo passo.

## Princípio

Cada interação deve produzir um delta observável e rastreável:

`INTERAÇÃO → TEMPO → PROVENIÊNCIA → CONFIANÇA → URGÊNCIA → DELTA → GAP → F_NEXT → RECEIPT`

Nenhuma interação deve apagar a anterior. Correções geram supersessão, erratum ou novo estado; nunca reescrita silenciosa da história.

## Registro mínimo por interação

```yaml
interaction_id: TOKEN_VAZIO
observed_at: TOKEN_VAZIO
source_kind: user|github|drive|ci|runtime|external_official|other
source_identity: TOKEN_VAZIO
source_ref: TOKEN_VAZIO
provenance:
  provider: TOKEN_VAZIO
  repo_or_file: TOKEN_VAZIO
  ref_or_revision: TOKEN_VAZIO
  path: TOKEN_VAZIO
  content_hash: TOKEN_VAZIO
confidence:
  level: HIGH|MEDIUM|LOW|TOKEN_VAZIO
  basis: TOKEN_VAZIO
urgency:
  level: P0|P1|P2|P3|TOKEN_VAZIO
  reason: TOKEN_VAZIO
state_before: TOKEN_VAZIO
observation: TOKEN_VAZIO
contradiction_or_noise: TOKEN_VAZIO
delta: TOKEN_VAZIO
uncertainty_change: TOKEN_VAZIO
claim_allowed_change: false
F_ok: TOKEN_VAZIO
F_gap: TOKEN_VAZIO
F_next: TOKEN_VAZIO
receipt_ref: TOKEN_VAZIO
supersedes: TOKEN_VAZIO
```

## Tempo

O tempo é parte da evidência, não decoração. Cada registro deve distinguir:

- **observed_at** — quando o fato foi observado;
- **source_time** — quando o provider diz que o fato ocorreu;
- **persisted_at** — quando o receipt foi gravado;
- **valid_for_ref** — SHA/revision/versão à qual a observação se aplica.

`EVIDÊNCIA_EM_SHA_ANTIGO != EVIDÊNCIA_DO_HEAD_ATUAL`

## Confiança

Confiança não é certeza subjetiva. Deve ser derivada da qualidade da fonte e da reprodutibilidade:

- **HIGH** — provider primário, identidade imutável, conteúdo/hash ou execução diretamente observável;
- **MEDIUM** — fonte confiável, mas sem fechamento completo de identidade/reprodução;
- **LOW** — heurística, documentação autodeclarada, inferência ou fonte indireta;
- **TOKEN_VAZIO** — base insuficiente para classificar.

`DOCUMENTAÇÃO != EXECUÇÃO`

`COMMIT_AUTHOR != PROVA_DE_AUTORIA_INTELECTUAL`

## Urgência

Urgência é função de risco, reversibilidade e capacidade de desbloqueio:

- **P0** — risco jurídico, privacidade/sagrado, perda de custódia, segurança, corrupção de lineage, claim indevido ou bloqueio estrutural;
- **P1** — gap que desbloqueia várias rotas ou fecha uma fronteira crítica;
- **P2** — melhoria de cobertura, indexação, reprodutibilidade ou organização;
- **P3** — refinamento não bloqueante.

`URGÊNCIA != CERTEZA`

Um item pode ser P0 e continuar `TOKEN_VAZIO`.

## Proveniência

Toda afirmação relevante deve apontar, quando disponível, para:

`provider → identity → ref/revision → path/object → hash/digest → observation → receipt`

Se qualquer elo indispensável faltar, a lacuna permanece explícita.

## Evolução

Toda interação deve responder cinco perguntas:

1. O que ficou mais conhecido?
2. O que foi contradito ou reclassificado?
3. Qual incerteza diminuiu ou aumentou?
4. Qual rota ficou mais urgente?
5. Qual é o próximo probe verificável que evita redescoberta inútil?

## Não-regressão

- não transformar `TOKEN_VAZIO` em zero, falso ou inexistente;
- não reutilizar evidência de SHA/revision antiga como atual;
- não apagar contradições históricas;
- não promover documento a execução;
- não promover execução a claim fora do escopo validado;
- não converter confiança em autoridade jurídica automática;
- não expor conteúdo de Privacidade Sagrada para fortalecer receipt quando hash/metadado bastarem.

## Ciclo R₃ por interação

`R₃ = <F_ok, F_gap, F_next>`

- **F_ok:** fatos/evidências agora sustentados;
- **F_gap:** lacunas, contradições e incertezas preservadas;
- **F_next:** próximo passo verificável de maior ganho por custo/risco.

## Índices derivados

A partir dos registros append-only podem ser derivados, sem substituir os receipts originais:

- índice longitudinal — evolução temporal de cada objeto;
- índice de confiança — mudanças de nível e fundamento;
- índice de urgência — P0/P1/P2/P3 por estado atual;
- índice de proveniência — objeto → provider/ref/hash/receipt;
- índice de contradições — claim/observação conflitante e resolução;
- índice de gaps — `TOKEN_VAZIO` aberto, narrowed, blocked ou closed;
- índice de evolução — deltas que realmente reduziram incerteza.

## Gate de persistência

Uma interação merece receipt durável quando pelo menos uma condição ocorrer:

- fecha ou estreita um `TOKEN_VAZIO`;
- altera confiança ou urgência;
- cria/resolve contradição;
- muda autoridade, rota ou prioridade;
- produz execução, evidência, hash, revision ou artifact novo;
- modifica política de privacidade, culto, licença ou integridade;
- identifica risco de regressão.

## Invariantes

`TEMPO != PROVENIÊNCIA`

`CONFIANÇA != AUTORIDADE`

`URGÊNCIA != VERDADE`

`PROVENIÊNCIA != AUTORIA`

`RETROALIMENTAÇÃO != REESCRITA`

`EVOLUIR != PROMOVER CLAIM`

`TOKEN_VAZIO != AUTORIZAÇÃO`

## Próximo passo

Materializar um ledger machine-readable append-only (`interaction-feedback.jsonl`) e validá-lo contra este contrato, de modo que cada ciclo futuro possa acrescentar uma linha com identidade, timestamp, provenance, confidence, urgency, delta, R₃ e receipt sem alterar registros anteriores.
