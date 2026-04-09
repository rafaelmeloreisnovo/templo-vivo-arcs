# Arquitetura Documental Pós‑Doc (Ultra Técnica)

## 1) Objetivo

Estabelecer uma arquitetura formal para:
1. Navegação de documentos recentes.
2. Refatoração acadêmica com rigor metodológico.
3. Integração entre teoria, dados, hipótese e teste de falsificabilidade.

## 2) Estrutura de diretórios proposta

```text
docs_posdoc_2dias/
├── 00_indice/
│   └── MD_ULTIMOS_2_DIAS.md
├── 01_arquitetura/
│   └── ARQUITETURA_DOCUMENTAL_POSDOC.md
├── 02_metodologia/
│   └── PROTOCOLO_CIENTIFICO_E_FALSIFICABILIDADE.md
├── 03_bibliografia/
│   └── BIBLIOGRAFIA_ACADEMICA_E_REFERENCIAL.md
├── 04_protocolos/
│   └── TEMPLATE_ARTIGO_TECNICO.md
└── 05_rastreabilidade/
    └── MATRIZ_RASTREABILIDADE.md
```

## 3) Camadas formais

- **Camada L0 — Fonte Primária:** arquivos originais (`*.md`) no repositório.
- **Camada L1 — Índice Temporal:** visão por janela de tempo (últimos 2 dias).
- **Camada L2 — Formalização Científica:** hipóteses, métricas, critérios de refutação.
- **Camada L3 — Governança Acadêmica:** bibliografia, versionamento, rastreabilidade.

## 4) Princípios de refatoração profissional

1. **Não destrutivo:** evitar mover/remover documentos originais sem migração assistida.
2. **Auditável:** cada hipótese deve mapear para dados, método e resultado.
3. **Reprodutível:** toda alegação quantitativa deve conter protocolo replicável.
4. **Refutável:** incluir condição objetiva que possa invalidar a tese.
5. **Navegável:** índice principal + índices temáticos + matriz de rastreabilidade.

## 5) Fluxo recomendado

1. Catalogar fontes recentes (feito em `00_indice`).
2. Converter ideias em hipóteses formais (`02_metodologia`).
3. Associar hipóteses às referências (`03_bibliografia`).
4. Produzir texto técnico em template padrão (`04_protocolos`).
5. Registrar matriz de evidência e falsificação (`05_rastreabilidade`).
