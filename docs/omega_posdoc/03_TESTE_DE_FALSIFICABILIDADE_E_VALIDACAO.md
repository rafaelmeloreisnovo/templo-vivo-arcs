# Protocolo de Falsificabilidade, Validação e Reprodutibilidade

## 1. Princípio orientador

Qualquer proposição do corpus deve ser testável por terceiros com:

- dados acessíveis;
- método replicável;
- critérios de decisão definidos antes do teste.

## 2. Esquema padrão de teste

Para cada hipótese `Hk`:

- **Hk (hipótese):** enunciado formal.
- **Pk (predição):** variável observável e intervalo esperado.
- **Mk (método):** procedimento estatístico/numérico.
- **Dk (dados):** origem, janela temporal, limpeza.
- **Fk (falsificação):** condição objetiva de rejeição.

## 3. Exemplo canônico de registro

```text
H1: A métrica espectral S apresenta regime multifractal em escala e.
P1: expoente alpha em [a_min, a_max] com estabilidade > 95%.
M1: ajuste por regressão robusta + validação cruzada temporal.
D1: série temporal pública com N observações, período T.
F1: rejeitar H1 se alpha sair do intervalo em >= q% das janelas.
```

## 4. Métricas mínimas por tipo de estudo

### 4.1 Matemático-formal
- consistência lógica interna;
- rastreabilidade de premissas;
- inexistência de circularidade.

### 4.2 Simulação
- sensibilidade a parâmetros;
- análise de estabilidade numérica;
- benchmark contra baseline conhecido.

### 4.3 Dados reais
- separação treino/validação/teste;
- estimativa de incerteza (IC, bootstrap ou bayesiano);
- teste fora da amostra (out-of-sample).

## 5. Reprodutibilidade operacional

Checklist obrigatório para cada experimento:

- versão do código;
- versão do dataset;
- seed aleatória;
- hardware/ambiente;
- script executável único de reprodução.

## 6. Critérios de qualidade para submissão acadêmica

Um bloco só pode entrar em paper quando cumprir simultaneamente:

1. clareza formal;
2. predição mensurável;
3. teste reprodutível;
4. critério de refutação explícito;
5. discussão de limitações.
