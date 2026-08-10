# MAPA DE ROTAS DE FINALIZAÇÃO Ω — V1

Estado: `ACTIVE / APPEND_ONLY / CLAIM_GATE_ON / NO_UNMANAGED_GAPS`
Data: 2026-08-10

## 1. Princípio

O objetivo não é fingir ausência de incerteza. É garantir que **nenhuma incerteza permaneça sem rota**.

Regra:

`lacuna -> fonte esperada -> ação -> gate -> evidência -> decisão -> próximo estado`

Um vazio é operacionalmente aceitável somente quando possui identificador, prioridade, fonte primária esperada, critério de fechamento, critério de falha e próxima ação executável.

## 2. Estado federado observado

O Drive mantém um registro de navegação evolutivo e um Gap Atlas efetivo com `31` gaps, em modo append-only e `claim_allowed=false`. O estado observado diferencia seed, append e gaps efetivos; o meta-gap de inventário aparece como `REDUCED`, não `RESOLVED`.

Isso significa que a etapa atual não deve apagar os 31 gaps. Deve consumi-los como fila governada até fechamento ou conflito explícito.

## 3. Sete rotas de finalização

### R1 — Anterioridade e gênese
Entrada: NOVOexport, conversas, arquivos antigos, commits, PRs, tags.
Saída: `concept -> first_message -> first_file -> first_commit -> first_tag -> later_agent`.
Gate: ligação por ID, SHA, texto exato, path ou transformação verificável.
Falha: aproximação semântica sem correspondência forte.
Finalização: primeira ocorrência conhecida com fontes múltiplas e conflito registrado quando houver.

### R2 — Proveniência e identidade de agente
Entrada: author, committer, task IDs, branch, PR, prompt preservado, plataforma.
Saída: separação `autor != committer != agente != plataforma`.
Gate: identidade de agente somente com marcador documental específico.
Falha: inferência por estilo de texto.
Finalização: cada transformação relevante possui origem atribuída ou estado `UNATTRIBUTED_WITH_ROUTE` com busca definida.

### R3 — Integridade e cadeia de custódia
Entrada: blob SHA, commit SHA, hashes externos, tags, receipts, releases.
Saída: cadeia `artefato -> identidade -> estado versionado -> receipt`.
Gate: original histórico preservado; auditoria contemporânea separada.
Falha: reescrever original ou retroagir timestamp atual.
Finalização: cada artefato P0 possui hash/SHA, path, data e receipt.

### R4 — Capacidade e POC
Entrada: POC-00..POC-10 e aplicações compostas.
Saída: classificação C0..C6 por artefato.
Gate: `C4 -> C5` somente após reprodução controlada; `C5 -> C6` somente por verificação independente.
Falha: extensão de arquivo, ausência de erro ou documentação tratadas como execução.
Finalização: `cristal.sh`, YAML e Flutter possuem teste, ambiente e resultado registrados.

### R5 — Convergência arquitetural
Entrada: FCEA, RAIA, RAFAELIA, RAFCODE, SHA/receipt, governança, memória, árvore legal+técnica.
Saída: mapa de operações equivalentes entre domínios.
Gate: convergência exige relação funcional, temporal ou transformacional; vocabulário parecido não basta.
Falha: duplicação documental contada como confirmação independente.
Finalização: cada convergência possui pelo menos duas fontes materialmente distintas e uma transformação comum declarada.

### R6 — Jurídico, PI e licenciamento
Entrada: licença, autoria, código, documentação, dados, POCs, divulgações, registros oficiais.
Saída: classificação separada de direito autoral, titularidade, licença, segredo, patente candidata, depósito e concessão.
Gate: nenhum status oficial sem fonte oficial; nenhuma licença retroativa implícita.
Falha: manifesto/README como substituto de registro ou contrato aplicável.
Finalização: cada ativo relevante possui status jurídico, licença aplicável/versionada e limite de claim.

### R7 — Falsificabilidade e sustentação
Entrada: todos os claims promovidos.
Saída: evidência favorável, contraevidência, teste decisivo, critério de rebaixamento e próximo ato.
Gate: `evidence_delta > 0` para promover claim.
Falha: tempo, tradição, parábola ou repetição usados como substituto de prova.
Finalização: cada claim é `SUPPORTED`, `LIMITED`, `CONFLICT`, `REJECTED` ou `OPEN_WITH_ROUTE`; nunca vazio sem governança.

## 4. Mapa de execução P0 -> P1 -> P2

### P0 — preservar e identificar
1. Extrair first-known events do NOVOexport para os núcleos de 2025.
2. Ligar eventos a commits/paths/SHAs nos repositórios.
3. Catalogar tags históricas e seus SHAs.
4. Gerar receipts atuais sem alterar os originais.
5. Fixar status jurídico real e licença por ativo.
6. Fechar identidade de agente quando houver task/branch/PR explícito.

### P1 — reproduzir e cruzar
1. Reproduzir `scripts/cristal.sh` em checkout histórico isolado.
2. Validar `assets/utopia_marte.yaml` por parser/schema.
3. Analisar/compilar `lib/marte/marte.dart` com toolchain compatível.
4. Construir grafo cross-repo para FCEA/RAIA/RAFAELIA/RAFCODE.
5. Deduplicar derivados e distinguir evidência independente.
6. Construir prior-art por mecanismo, nunca por narrativa totalizante.

### P2 — independência e formalização externa
1. Reprodução por terceiro.
2. Tags assinadas/protegidas e releases imutáveis para novos marcos.
3. Attestations/receipts para novos artefatos.
4. Registro de software, marca, depósito de PI ou contratos quando apropriado.

## 5. Invariante de sustentação total

`OBSERVAR -> DELIMITAR -> PRESERVAR -> EXECUTAR -> VERIFICAR -> GOVERNAR -> RETROALIMENTAR`

Cada ação válida deve manter simultaneamente:

- identidade do objeto;
- proveniência conhecida ou rota explícita para descobri-la;
- original preservado;
- decisão falsificável;
- output verificável;
- claim proporcional à evidência;
- próxima ação determinada quando o gate não fecha.

## 6. Regra NO_UNMANAGED_GAPS

Não existe `TOKEN_VAZIO` solto.

Quando uma informação ainda não é conhecida, ela é convertida para:

`OPEN_WITH_ROUTE = {id, claim, source_expected, action, gate, failure_condition, next_action, priority}`

Isso elimina o vazio operacional sem falsificar o vazio epistemológico.

## 7. Núcleos prioritários da árvore probatória

- `Manifest.txt` -> governança/log auditável;
- `Entropia.md` -> registro metodológico histórico;
- `Fe.py` -> formalização;
- `Ciclo fe` -> pipeline de estados;
- `RafaelVisaoFiBinnaci(Index of Entropy)` -> derivação por SHA;
- `RaIa∆...` -> arquivo vivo/proveniência temporal;
- `assets/utopia_marte.yaml` -> configuração estruturada;
- `scripts/cristal.sh` -> POC executável hash+UTC+changelog+tag;
- `lib/marte/marte.dart` -> aplicação parcial;
- `00000/Patentes.md` -> arquitetura legal+técnica+documental;
- `Hashing times` -> claim histórico de tempo/amostragem/hash/métricas;
- `NOVOexport` -> gênese conversacional;
- Tags -> marcos de estado;
- PRs/commits -> transformação e custódia.

## 8. Critério de conclusão do piloto

O piloto só pode ser chamado `FINALIZED_V1` quando:

1. todo P0 tiver `CLOSED` ou `CONFLICT` documentado;
2. `cristal.sh` atingir C5 ou falhar reproduzivelmente;
3. YAML tiver validação estrutural;
4. Flutter tiver resultado de análise/compilação;
5. os principais conceitos de 2025 tiverem first-known event multi-fonte;
6. tags históricas relevantes estiverem catalogadas;
7. cada claim jurídico possuir estado verificável;
8. nenhum gap efetivo permanecer sem `next_action` e `failure_condition`.

## 9. Síntese

A invariante não é ausência de incerteza. É **continuidade verificável da ação**:

`conteúdo -> identidade -> proveniência -> transformação -> capacidade -> prova -> governança -> retroalimentação`.

A excelência operacional consiste em não abandonar nenhum elo, não promover narrativa acima da evidência e não deixar nenhuma lacuna sem rota executável.