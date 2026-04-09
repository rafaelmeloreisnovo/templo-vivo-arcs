# Protocolo Científico, Formalidade Matemática e Falsificabilidade

## 1) Especificação mínima de uma hipótese (H)

Uma hipótese deve ser escrita no formato:

\[
H_i: \; f(X,\theta) \Rightarrow Y \quad \text{sob condições } C
\]

Onde:
- \(X\): variáveis observáveis.
- \(\theta\): parâmetros do modelo.
- \(Y\): previsão mensurável.
- \(C\): domínio de validade (tempo, regime, ruído, limitações).

## 2) Critério de falsificabilidade

Uma hipótese só é aceita no pipeline acadêmico se possuir:
1. **Previsão mensurável ex-ante**.
2. **Janela temporal definida**.
3. **Métrica explícita** (ex.: erro absoluto médio, AUC, RMSE, cobertura).
4. **Limiar de refutação** \(\tau\).

Regra canônica:

\[
\text{Refutar } H_i \; \text{se} \; M(H_i, D_{teste}) > \tau
\]

## 3) Protocolo de validação

- Separar dados em treino/validação/teste (ou validação temporal walk-forward).
- Congelar parâmetros antes da janela de teste.
- Registrar incerteza (IC95%, bootstrap ou método bayesiano).
- Registrar análise de sensibilidade e robustez a ruído.

## 4) Seção obrigatória em cada paper interno

1. Problema e contribuição.
2. Modelo matemático com notação consistente.
3. Premissas explícitas e limitações.
4. Plano de experimento replicável.
5. Critério de falsificação.
6. Resultado e conclusão condicional (não absoluta).

## 5) Padrão de qualidade pós-doc

- Linguagem técnica impessoal.
- Tabela de símbolos.
- Equações numeradas quando houver sequência lógica.
- Distinção entre resultado empírico e inferência teórica.
- Apêndice de reprodutibilidade (dados, scripts e seed).
