# 01 — Arquitetura Estrutural (Pós-Doc)

## 1) Camadas formais do projeto

### Camada A — Ontologia documental
- **Manifestos e visão**: textos fundacionais e de posicionamento epistemológico.
- **Teoria e formalização**: teoremas, modelos e propostas matemáticas.
- **Aplicação e dados**: CSV/XLSX, scripts, app Flutter/Android.
- **Governança e validade**: metodologia, bibliografia, critérios de teste.

### Camada B — Pipeline científico
1. **Hipótese** (declaração formal).
2. **Modelagem** (equações/axiomas/operadores).
3. **Implementação** (código e instrumentação).
4. **Teste** (falsificação, sensibilidade, erro).
5. **Reprodutibilidade** (dados, scripts, versão, logs).
6. **Síntese** (limites, implicações, revisão).

### Camada C — Entregáveis auditáveis
- Documento técnico primário.
- Caderno de experimentos.
- Dataset versionado com dicionário de dados.
- Relatório de robustez estatística.
- Quadro de limitações e ameaças à validade.

## 2) Estrutura de diretórios recomendada

```text
/docs
  /posdoc_2dias
    README.md
    01_Arquitetura_Estrutural.md
    02_Formalismo_Matematico_e_Hipoteses.md
    03_Protocolo_Falsificabilidade.md
    04_Bibliografia_Curadoria.md
    05_Mapa_Ultimos_MD_2_Dias.md

/data
  /raw
  /processed
  /reference

/experiments
  /hypotheses
  /results
  /replication
```

## 3) Princípios de qualidade acadêmica

- **Rastreabilidade**: cada afirmação forte deve apontar para evidência.
- **Separação entre tese e evidência**: evitar mistura de opinião com resultado medido.
- **Comensurabilidade**: usar métricas comparáveis entre ciclos experimentais.
- **Reprodutibilidade**: todo resultado deve ser reproduzível por terceiro independente.
- **Clareza epistemológica**: declarar fronteiras entre metáfora, modelo e evidência.

## 4) Refatoração proposta para os MD recentes

- Consolidar documentos dispersos em trilhas: **teoria**, **método**, **teste**, **síntese**.
- Remover duplicação conceitual entre manifestos e seções de dissertação.
- Converter afirmações não-testáveis em hipóteses operacionais quando possível.
- Definir uma taxonomia única para termos centrais (entropia, malha, coerência, etc.).
