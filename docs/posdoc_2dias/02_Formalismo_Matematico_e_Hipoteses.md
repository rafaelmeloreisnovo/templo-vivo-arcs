# 02 — Formalismo Matemático e Hipóteses

## 1) Objetos formais mínimos

Defina explicitamente:

- Espaço de estados \(\mathcal{S}\)
- Vetor de observáveis \(\mathbf{x}_t \in \mathbb{R}^n\)
- Operador de evolução \(\mathcal{F}_\theta\)
- Função de energia/informação \(\mathcal{E}(\mathbf{x}_t)\)
- Ruído \(\epsilon_t\) com hipótese distribucional declarada

Modelo base:

\[
\mathbf{x}_{t+1} = \mathcal{F}_\theta(\mathbf{x}_t) + \epsilon_t
\]

## 2) Hipóteses científicas falsificáveis

- **H1 (Predição)**: o modelo reduz erro fora da amostra versus baseline estatístico.
- **H2 (Robustez)**: o ganho de desempenho persiste sob perturbação de hiperparâmetros.
- **H3 (Estabilidade)**: métricas não colapsam em janelas temporais distintas.
- **H4 (Transferência)**: desempenho mantém-se em domínios correlatos (ações/índices/commodities).

## 3) Métricas e critérios

- Erro: MAE, RMSE, MAPE.
- Dependência temporal: autocorrelação de resíduos, Ljung-Box.
- Significância: teste Diebold-Mariano para comparação preditiva.
- Robustez: bootstrap de blocos e análise de sensibilidade global.

## 4) Notas de formalidade avançada

- Diferenciar rigorosamente **postulado**, **teorema**, **heurística** e **metáfora**.
- Especificar domínio de validade de cada proposição.
- Declarar quando uma expressão é analogia e não lei física inferida.
