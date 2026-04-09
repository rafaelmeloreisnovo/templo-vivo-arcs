# Protocolo de Falsificabilidade Acadêmica

## Objetivo

Converter hipóteses amplas em enunciados **testáveis, refutáveis e reproduzíveis**, respeitando rigor estatístico e epistemológico.

## 1) Estrutura formal da hipótese

Para cada hipótese `H`, registrar:

- **H0 (nula):** não há efeito/associação acima do acaso.
- **H1 (alternativa):** há efeito/associação sob condições explicitadas.
- **Escopo:** em quais contextos `H` é válida.
- **Predições observáveis:** quais sinais devem surgir se `H1` for verdadeira.

## 2) Critério mínimo de testabilidade

Uma hipótese só entra no ciclo experimental se houver:

1. Variáveis mensuráveis;
2. Instrumento de medição definido;
3. Janela temporal explícita;
4. Critério de decisão (`p`, intervalo de confiança, erro predefinido, ou métrica bayesiana);
5. Procedimento de replicação independente.

## 3) Modelo de tabela de validação

| ID | Hipótese | Métrica | Regra de decisão | Resultado | Status |
|----|----------|---------|------------------|-----------|--------|
| H-01 | Exemplo | MAE/RMSE | `RMSE < baseline` | ... | Aceita provisoriamente / Refutada |

## 4) Ameaças à validade

### 4.1 Interna
- Viés de seleção;
- sobreajuste;
- variáveis de confusão;
- erro de instrumentação.

### 4.2 Externa
- Baixa generalização temporal/geográfica;
- dependência de cenário de mercado específico;
- não replicabilidade por terceiros.

### 4.3 Construto
- Métrica não representa adequadamente o fenômeno;
- definição ambígua de variáveis latentes.

## 5) Regra de publicação responsável

- Alegações extraordinárias exigem evidência extraordinária.
- Sem replicação externa, resultado permanece **provisório**.
- Afirmações de fronteira devem ser claramente rotuladas como exploratórias.

## 6) Checklist de submissão acadêmica

- [ ] Hipótese formalizada (H0/H1)
- [ ] Base de dados identificada e versionada
- [ ] Código/procedimento de replicação disponível
- [ ] Limitações explicitadas
- [ ] Referências primárias suficientes
- [ ] Conclusão sem extrapolação indevida
