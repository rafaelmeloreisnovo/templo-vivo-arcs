# 03 — Protocolo de Falsificabilidade Acadêmica

## 1) Pré-registro interno

Antes de executar qualquer experimento:

1. Registrar hipótese.
2. Definir métrica primária e secundárias.
3. Declarar baseline(s) obrigatório(s).
4. Definir janela temporal de treino/validação/teste.
5. Congelar critérios de aceitação/rejeição.

## 2) Pipeline experimental

1. **Ingestão**: versionar datasets e dicionário de variáveis.
2. **Validação de dados**: missing, outliers, drift de distribuição.
3. **Treinamento**: logs completos de parâmetros e seeds.
4. **Avaliação**: comparação contra baseline e intervalos de confiança.
5. **Estresse**: testes de regime (alta/baixa volatilidade; choques exógenos).
6. **Replicação**: rerun independente com ambiente limpo.

## 3) Matriz de decisão

- **Aceita provisoriamente**: melhora significativa + robustez + replicação.
- **Inconclusiva**: melhora sem robustez ou sem significância.
- **Refutada**: sem melhora ou com degradação robusta.

## 4) Ameaças à validade

- Viés de seleção de amostra.
- Vazamento temporal (look-ahead bias).
- Sobreajuste por tuning extensivo.
- Dependência de regime específico de mercado.

## 5) Deliverable obrigatório

Cada ciclo deve produzir:

- relatório técnico curto;
- tabela de métricas comparativas;
- artefatos de reprodução (comando, versão, seed, hash de dados);
- seção explícita “o que pode estar errado”.
