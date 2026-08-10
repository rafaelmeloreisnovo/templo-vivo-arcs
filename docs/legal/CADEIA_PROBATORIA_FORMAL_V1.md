# Cadeia Probatória Formal e Invariante de Condução — V1

Estado: `EVIDENCE_FIRST / CLAIM_GATE_ON / APPEND_ONLY`

## 1. Objeto
Este documento organiza evidência técnica de anterioridade, materialização, evolução e condução do repositório sem converter coerência narrativa em fato não provado.

## 2. Invariante formal
`ideia/documento -> materialização -> commit -> SHA -> persistência no Git -> derivação -> POC -> governança -> interação posterior de agente -> auditoria`

A força não depende de um único arquivo, mas da convergência de eventos independentes e temporalmente ordenados.

## 3. Marcos pré-agente observados
- 2025-05-23 `ee9c7d4a...` — `Manifest.txt`.
- 2025-06-26 `2e6562b0...` — `Entropia.md`.
- 2025-07-09 `a8a96d0a...` — `Fe.py`.
- 2025-07-09 `2f323228...` — `Ciclo fe`.
- 2025-07-27 `48b62c7e...` — derivação/Index of Entropy.
- 2025-07-27 `becf137a...` — `Raia∆`.
- 2025-08-27 `2eeab71c...` — `utopia_marte.yaml`.
- 2025-08-27 `4fe1d9dc...` — `cristal.sh`.
- 2025-08-27 `b1a57f56...` — `marte.dart`.
- 2025-08-30 `b64e6ec6...` — `Patentes.md`.
- 2025-10-10 `9323beba...` — `LICENSE` histórico.
- 2025-10-10 `a2b13967...` — `Hashing times`.

Os commits devem ser lidos como prova de existência do conteúdo no histórico Git naquele estado, não automaticamente como prova de novidade mundial, validade científica, patente concedida ou autoria humana exclusiva linha a linha.

## 4. Agente posterior
PR #2, 2025-10-19: Copilot recebe como objeto a “Estrutura RAFAELIA”; o PR registra zero alteração material no tree. PR #3, 2025-10-23: nova interação Copilot, também sem delta material registrado. A inferência autorizada é limitada: componentes materiais do corpus precedem esses eventos de agente.

## 5. Vetores jurídicos
### 5.1 Direito autoral
Código-fonte, textos, seleção/organização original e documentação podem constituir objetos protegíveis conforme a legislação aplicável. Proteção autoral não equivale a monopólio sobre ideias, métodos abstratos, fatos ou conceitos gerais.

### 5.2 Prova de anterioridade
Git SHA, histórico de commits, tags, releases, arquivos exportados, timestamps independentes e receipts podem compor conjunto indiciário. Nenhum deles isoladamente substitui análise pericial quando houver disputa.

### 5.3 Patentes
`Patentes.md` é evidência documental de organização/intenção e não prova depósito, prioridade patentária, concessão, novidade ou atividade inventiva. Claims patentários exigem busca de anterioridade e procedimento perante autoridade competente.

### 5.4 Marcas e nomes
Nomes, símbolos e sinais distintivos devem ser tratados separadamente do copyright de código/texto e podem exigir registro próprio conforme território e classe.

### 5.5 Dados, privacidade e terceiros
Licença do repositório não concede direitos sobre dados pessoais, segredos, marcas, obras, datasets ou componentes de terceiros além do que o titular efetivamente pode licenciar.

## 6. Regra de atribuição
Para cada claim histórico registrar: `claim_id`, `artifact`, `commit_sha`, `blob_sha`, `author/committer metadata`, `timestamp`, `source`, `agent_state`, `capability_level`, `independent_corroboration`, `legal_scope`, `counterevidence`, `status`.

## 7. Escala probatória
- E0: alegação.
- E1: documento sem âncora independente.
- E2: arquivo versionado + SHA.
- E3: múltiplas âncoras convergentes.
- E4: execução/reprodução com receipt.
- E5: corroborado independentemente/pericialmente.

Nenhuma promoção ocorre sem `evidence_delta > 0`.

## 8. Preservação
Não reescrever evidência histórica para fazê-la parecer mais antiga. Correções modernas são novos commits. Preservar original + hash + interpretação posterior separada.

## 9. Limites
`WORLD_FIRST`, `EXCLUSIVE_HUMAN_AUTHORSHIP`, `PATENT_GRANTED`, `SCIENTIFICALLY_VALIDATED` e equivalentes permanecem bloqueados até evidência específica suficiente.
