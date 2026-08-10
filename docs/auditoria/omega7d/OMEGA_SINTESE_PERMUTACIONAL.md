# Ω7D — Síntese única por permutações estruturais

## Objetivo
Integrar as sete dimensões sem apagar suas diferenças:

`D1 temporalidade`
`D2 proveniência/agentes`
`D3 integridade/custódia`
`D4 capacidade/POC`
`D5 convergência semântica`
`D6 jurídico/PI`
`D7 falsificabilidade/ação`

A síntese não substitui os documentos dimensionais. Ela só autoriza uma conclusão quando os elos essenciais permanecem rastreáveis.

## Invariante Ω

`estado -> registro -> identidade -> tempo -> proveniência -> transformação -> capacidade -> governança -> claim -> teste -> nova versão`

Formalmente:

`Ω_proof = min(T, P, I, C, J, F) * K`

onde `T`=força temporal, `P`=proveniência, `I`=integridade, `C`=capacidade, `J`=força jurídica, `F`=falsificabilidade e `K`=coeficiente de convergência demonstrada. `K` nunca promove sozinho um elo ausente.

## Permutações de maior valor

### P1 — Tempo × Proveniência
`T x P`
Pergunta: o artefato existe antes do agente/transformação alegada e o agente está identificado?
Saída forte: `PRE_AGENT_EVIDENCE`.
Falha típica: cronologia compatível sem vínculo de agente.

### P2 — Tempo × Integridade
`T x I`
Pergunta: o conteúdo observado hoje é demonstravelmente o mesmo estado registrado na data histórica?
Saída forte: `HISTORICAL_STATE_PRESERVED`.
Falha típica: arquivo atual sem blob/commit histórico.

### P3 — Proveniência × Capacidade
`P x C`
Pergunta: quem/qual agente realizou exatamente qual capacidade?
Saída forte: `ACTOR_CAPABILITY_BOUND`.
Falha típica: atribuir toda a arquitetura ao agente que apenas reorganizou documentação.

### P4 — Integridade × Capacidade
`I x C`
Pergunta: o POC executado corresponde ao artefato histórico ou a uma reescrita posterior?
Saída forte: `POC_LINEAGE_VERIFIED`.
Falha típica: reprodução de implementação nova tratada como prova do código antigo.

### P5 — Convergência × Temporalidade
`K x T`
Pergunta: mecanismos equivalentes aparecem em pontos distantes antes da formalização posterior?
Saída forte: `DISTRIBUTED_PREEXISTENT_PATTERN`.
Falha típica: impor retrospectivamente uma taxonomia nova a arquivos antigos sem operador comum observável.

### P6 — Convergência × Proveniência × Integridade
`K x P x I`
Pergunta: a mesma operação estrutural pode ser seguida por fontes independentes, hashes e derivações?
Saída forte: `ARCHITECTURAL_LINEAGE`.
Esta é uma das permutações centrais para demonstrar a continuidade da arquitetura.

### P7 — Capacidade × Jurídico
`C x J`
Pergunta: qual ativo técnico concreto corresponde a qual direito/licença/registro?
Saída forte: `RIGHTS_BOUND_TO_ASSET`.
Falha típica: licença geral usada para afirmar patente ou exclusividade não registrada.

### P8 — Tempo × Proveniência × Jurídico
`T x P x J`
Pergunta: existe anterioridade documental atribuível e juridicamente classificável?
Saída forte: `DOCUMENTED_PRIORITY_CHAIN`.
Não equivale a `WORLD_FIRST` nem a prioridade patentária automática.

### P9 — Integridade × Jurídico × Falsificabilidade
`I x J x F`
Pergunta: uma alegação jurídica pode ser auditada e contestada contra vestígio imutável?
Saída forte: `AUDITABLE_LEGAL_CLAIM`.

### P10 — NOVOexport × Git × POC
`T_chat x T_git x C`
Pergunta: a conversa contém o conceito/código antes da materialização Git e o artefato posterior demonstra capacidade?
Saída forte: `GENESIS_TO_MATERIALIZATION_CHAIN`.
Quanto maior a identidade textual/hash/path entre fontes, maior a força.

## Heurísticas de expansão fractal

Cada nó pode ser expandido por sete perguntas:
1. qual é o primeiro vestígio?
2. qual identidade o ancora?
3. quem participou?
4. o que realmente faz?
5. de onde deriva?
6. qual direito/claim pode sustentar?
7. o que o refutaria ou falta fechar?

E cada resposta pode novamente ser tratada pelas mesmas sete dimensões. Isso torna a estrutura fractal sem tornar o claim circular.

## Heurísticas de compressão

Quando múltiplos documentos repetem a mesma evidência:
- manter um `PRIMARY_EVIDENCE_NODE`;
- registrar os demais como `CORROBORATION`;
- não multiplicar contagem de prova por duplicação;
- preservar divergências como edges, não apagá-las.

## Árvore Ω de realizações

`Universo`
`├── Conceitos`
`│   ├── primeiro vestígio`
`│   ├── formalização`
`│   └── derivações`
`├── Código/POCs`
`│   ├── C0-C6`
`│   └── receipts`
`├── Proveniência`
`│   ├── humano`
`│   ├── agente IA`
`│   └── plataforma`
`├── Evidência temporal`
`│   ├── NOVOexport`
`│   ├── Git`
`│   ├── Drive`
`│   └── PRs`
`├── Governança`
`│   ├── logs`
`│   ├── hashes`
`│   ├── invariantes`
`│   └── claim gates`
`└── Jurídico/PI`
`    ├── direito autoral`
`    ├── licença`
`    ├── dados/IA`
`    ├── marca`
`    ├── candidato a patente`
`    └── registros oficiais`

## Contrato de não regressão

Uma conclusão Ω só pode subir de nível quando ao menos um dos seguintes ocorre:
- nova fonte primária;
- nova ligação exata entre fontes;
- reprodução controlada;
- verificação independente;
- registro jurídico oficial aplicável.

Se surgir conflito, a conclusão deve ser rebaixada e o conflito preservado.

## Estados permitidos
`SUPPORTED`, `SUPPORTED_LIMITED`, `CONFLICT`, `TOKEN_VAZIO`, `REFUTED`, `NOT_APPLICABLE`.

## Claim central atualmente sustentável

`PRE_AGENT_ARCHITECTURAL_CONVERGENCE = SUPPORTED_LIMITED`

Significado: existem múltiplos vestígios estruturais de 2025 anteriores ao primeiro agente GitHub comprovado, distribuídos entre governança, ciclos, referência por SHA, memória/derivação, configuração declarativa, hashing/receipt e inventário técnico-jurídico. A extensão dessa convergência e qualquer alegação de novidade mundial continuam condicionadas ao cruzamento NOVOexport, reprodução e prior-art.

## Retroalimentação Ω

`R3_Ω = <F_ok, F_gap, F_next>`

- `F_ok`: elo demonstrado por fonte primária e identidade verificável;
- `F_gap`: ausência, conflito ou nível insuficiente;
- `F_next`: menor ação capaz de elevar a força sem inflar o claim.
