# PILOTO PROBATÓRIO Ω — EXCELÊNCIA OPERACIONAL V1

Estado: `ACTIVE_DRAFT / CLAIM_GATE_ON / APPEND_ONLY`
Data de consolidação: 2026-08-10

## 1. Objetivo

Converter o universo documental e técnico RAFAELIA em uma árvore probatória evolutiva, sem promover narrativa, parábola, tradição, hipótese ou associação semântica ao mesmo nível de evidência de artefato, execução ou fonte independente.

A unidade mínima não é “um documento”, mas um evento probatório com identidade, tempo, proveniência, transformação, capacidade, limite e condição de refutação.

## 2. Invariante operacional

`estado -> registro -> identidade -> tempo -> proveniência -> transformação -> capacidade -> governança -> claim -> teste -> receipt -> nova versão`

Nenhum estágio posterior apaga o anterior. Conflitos permanecem registrados. `TOKEN_VAZIO` é um estado auditável, não uma autorização para preencher por inferência.

## 3. Regra geométrica de sustentação

Não existe uma grandeza única que permaneça invariável em toda transformação. Para cada alegação de invariância devem ser declarados: objeto, representação, família de transformações, propriedade preservada e teste de preservação.

Na árvore probatória, a “invariante geométrica” é relacional: o mesmo nó só mantém identidade entre representações quando há um mapa de correspondência verificável (hash, SHA, path, texto exato, ID de mensagem, receipt, ou transformação reproduzível).

## 4. Sete direções Ω

### D1 — Temporalidade e anterioridade
Prova mínima: timestamp interno da fonte + identidade da fonte.
Fortalecimento: NOVOexport -> arquivo -> commit -> PR -> release.
Falha crítica: usar data de upload no Drive como data original da conversa.
Urgência: P0 para conceitos cuja prioridade depende de 2025.

### D2 — Proveniência, autoria e agente
Prova mínima: distinguir autor, committer, agente, plataforma e transformador.
Fortalecimento: task ID, branch de agente, prompt preservado, commit/PR associado.
Falha crítica: inferir GPT/Codex/Copilot por estilo textual.
Urgência: P0 em claims de pré-agente e autoria.

### D3 — Integridade e cadeia de custódia
Prova mínima: path + blob/commit SHA ou hash do artefato.
Fortalecimento: receipt, assinatura, attestation, timestamp externo.
Falha crítica: reescrever o original histórico ou confundir receipt atual com prova temporal retroativa.
Urgência: P0 para todo artefato usado juridicamente.

### D4 — Capacidade e prova de conceito
Classes: C0 textual; C1 formal; C2 estruturado; C3 executável parcial; C4 executável; C5 reproduzido; C6 independente.
Falha crítica: extensão de arquivo ou linguagem de programação não prova execução.
Urgência: P1 para elevar POCs de 2025 de C4 para C5.

### D5 — Convergência semântica e arquitetural
Prova mínima: operações equivalentes descritas por relações explícitas, não apenas vocabulário semelhante.
Fortalecimento: mesma transformação observada em arquivos/repos distintos com ligação temporal e funcional.
Falha crítica: repetir a mesma narrativa em vários documentos e contar como múltiplas confirmações independentes.
Urgência: P1 para FCEA, RAIA, RAFAELIA, hashing/receipt, derivação por SHA e governança.

### D6 — Jurídico, PI e licenciamento
Separar: direito autoral, existência documental, autoria/titularidade, licença, segredo, patente candidata, patente depositada e patente concedida.
Falha crítica: tratar manifesto, README, `Patentes.md` ou licença draft como registro oficial ou decisão jurídica.
Urgência: P0 para ativo comercial ou declaração externa.

### D7 — Falsificabilidade, urgência e ação
Todo claim deve conter: evidência favorável, evidência contrária, lacuna, teste decisivo e próximo ato.
Falha crítica: tempo decorrido ser usado como substituto de evidência.
Urgência: proporcional ao dano de claim errado, não ao desejo de conclusão.

## 5. Contrato TOKEN_VAZIO

Todo vazio deve possuir:
- `gap_id`;
- `claim_id`;
- dimensão afetada;
- prioridade P0/P1/P2;
- fonte primária esperada;
- evidência mínima para fechamento;
- ação verificável;
- critério de falha;
- estado `OPEN | PARTIAL | CLOSED | CONFLICT`.

Um `TOKEN_VAZIO` nunca é eliminado por parábola, tradição, repetição ou coerência interna. Ele fecha apenas com nova evidência apropriada ao claim.

## 6. Fontes canônicas observadas

### Google Drive
- `RAFAELIA — Implementação Latentes e Papers — Drive GitHub V1`: contrato operacional Drive <-> GitHub; registra gaps de execução real, cobertura total, schemas e validações.
- `RAFAELIA — Invariante Geométrica Coerente e Coesão Real — V1`: exige objeto, representação, família de transformações e propriedade preservada; rejeita identidade geométrica sem mapa de colagem/correspondência.
- `RAFAELIA_GOVERNANCE_PROVENANCE_URGENT_LEDGER_V1`: ledger append-only e claim gate.
- `RAFAELIA — Master Navigation Registry V1`: navegação entre invariantes, ledgers e fontes.
- `NOVOexport`: fonte primária para timestamps e conteúdo de conversas; checkpoints são auxiliares.

### GitHub
- PR #21: camada de anterioridade, cadeia de custódia, POCs, licença e timeline multi-fonte — mergeada, preservada.
- PR #22: refinamento Ω7D pós-merge.
- Artefatos de 2025 já catalogados: `Manifest.txt`, `Entropia.md`, `Fe.py`, `Ciclo fe`, derivação por SHA, RAIA, YAML de invariantes, `cristal.sh`, POC Flutter e `00000/Patentes.md`.

## 7. Vetores de sustentação

`V_temporal = fonte_original + timestamp_interno + ligação_artefato`

`V_prov = autor + committer + agente + transformação`

`V_integridade = hash/SHA + path + preservação + receipt`

`V_capacidade = implementação + execução + reprodução + limite`

`V_convergência = operação_equivalente + independência_de_fonte + ligação_funcional`

`V_jurídico = titularidade + escopo + aceite + prova + proporcionalidade`

`V_falsificação = hipótese + contraevidência + teste_decisivo + critério_de_rebaixamento`

A força do claim é limitada pelo elo essencial mais fraco; volume documental não compensa ausência de proveniência ou integridade.

## 8. Heurísticas de permutação úteis

1. `Tempo x Proveniência` -> anterioridade perante agente.
2. `Tempo x Integridade` -> preservação do estado histórico.
3. `Proveniência x Capacidade` -> quem participou e o que efetivamente fez.
4. `Integridade x Capacidade` -> o binário/código testado corresponde ao artefato alegado.
5. `Convergência x Tempo` -> a estrutura aparece antes de sua formalização posterior.
6. `Convergência x Proveniência x Integridade` -> linhagem arquitetural.
7. `Capacidade x Jurídico` -> direito associado a ativo técnico específico.
8. `NOVOexport x Git x POC` -> gênese conversacional -> materialização -> execução.
9. `Drive x Git x Receipt` -> observações independentes de um mesmo estado.
10. `Falsificabilidade x Jurídico` -> claims públicos limitados ao que pode ser sustentado.

## 9. Fila de urgência sem regressão

### P0
- Extrair do NOVOexport a primeira ocorrência de cada núcleo de 2025 e ligar por message/conversation ID.
- Produzir receipts dos artefatos históricos sem modificar os originais.
- Distinguir agente comprovado de assistência de IA não identificada.
- Preservar status legal real: `PATENT_GRANTED=false` salvo fonte oficial.
- Fixar cada claim comercial/licenciável a uma versão de licença e ativo.

### P1
- Reproduzir `cristal.sh` e outras POCs executáveis em ambiente controlado.
- Cruzar FCEA/RAIA/RAFAELIA/RAFCODE em múltiplos repositórios e Drive.
- Deduplicar documentos derivados para evitar contagem artificial de evidência.
- Construir matriz de prior art por mecanismo técnico.

### P2
- Verificação independente por terceiro.
- Assinaturas/attestations para novos releases.
- Consolidação de registro de software, marcas ou depósitos de PI quando adequado.

## 10. Claims atuais permitidos

`PRE_AGENT_ARCHITECTURAL_CONVERGENCE = SUPPORTED_LIMITED`

`2025_INTERNAL_ANTERIORITY = SUPPORTED_FOR_CATALOGUED_ARTIFACTS`

`CHAIN_OF_CUSTODY = PARTIAL_STRONG / EXPANDING`

`POC_CAPABILITY = PER_ARTIFACT_ONLY`

Bloqueados sem nova prova:
- `WORLD_FIRST`;
- `NEW_PHYSICS`;
- `OPENAI_VALIDATED`;
- `PATENT_GRANTED`;
- identidade de agente não documentada;
- extrapolação de uma POC para toda a arquitetura.

## 11. Retroalimentação

F_ok: já existe uma base multi-fonte, append-only, com commits, Drive, NOVOexport, POCs e contratos de claim.
F_gap: extração bruta do NOVOexport, reprodução C5, prior art e validação independente ainda não estão completos.
F_next: preencher a árvore probatória por conceito e não por narrativa; cada nó deve sair de `TOKEN_VAZIO` apenas por evidência adequada.