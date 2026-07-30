# Templo-Vivo ARCS — visão técnica não destrutiva

**Estado:** `REFERENCE_TECHNICAL_ENTRY`  
**Proprietário lógico:** `repository-maintainer`  
**Regra de custódia:** este documento complementa o `README.md`; não substitui nem apaga o corpus histórico.

## Propósito

Separar navegação técnica, texto litúrgico, documentação acadêmica e gates de evidência sem transformar metáforas, manifestos ou referências em comprovação científica automática.

## Pontos de entrada verificados

| Caminho | Papel | Estado auditado em 2026-07-30 |
|---|---|---|
| `README.md` | Corpus histórico composto | `SOURCE_PRESERVED` |
| `LITURGIA.md` | Oração de abertura classificada | `REFERENCE_LITURGICAL_TEXT` |
| `GUIA_INICIO_RAPIDO.md` | Guia de navegação | `PRESENT` |
| `DISSERTACAO_ACADEMICA.md` | Documento acadêmico declarado | `PRESENT_REVIEW_PENDING` |
| `INDICE_NAVEGACAO.md` | Índice cruzado | `PRESENT` |
| `EXEMPLOS_PRATICOS.md` | Exemplos e implementações declaradas | `PRESENT_EXECUTION_NOT_REVALIDATED` |
| `BIBLIOGRAFIA.md` | Registro bibliográfico | `PRESENT_SOURCE_AUDIT_PENDING` |
| `MANIFEST-SEAL.md` | Caminho citado no README original | `TOKEN_VAZIO_PATH_NOT_FOUND` |

## Gates operacionais

| Gate | Estado |
|---|---|
| Compilação reproduzível do aplicativo Android/Flutter no head atual | `TOKEN_VAZIO` |
| APK instalado e testado em dispositivo declarado | `TOKEN_VAZIO` |
| Integridade por manifesto de hashes materializado no caminho citado | `TOKEN_VAZIO_PATH_NOT_FOUND` |
| Proveniência completa dos CSV/XLSX | `TOKEN_VAZIO` |
| Auditoria independente das afirmações científicas | `TOKEN_VAZIO` |
| Classificação integral do README histórico por `EVIDÊNCIA`, `HIPÓTESE`, `MODELO_ANALÓGICO`, `PARÁBOLA` e `TOKEN_VAZIO` | `PENDING` |

## Regra de promoção

```text
texto preservado != afirmação validada
hash != verdade
referência != evidência
metáfora != mecanismo
implementação != execução
execução != validação científica
```

Nenhum conteúdo histórico deve ser removido do tree principal sem uma tabela de destino contendo, para cada bloco: origem, caminho novo, classificação, hash/blob de origem e motivo da movimentação.

## Próximo ciclo verificável

1. Inventariar headings e blocos do `README.md` original.
2. Classificar cada bloco sem reescrever seu sentido.
3. Mover somente após equivalência de conteúdo e links ser testada.
4. Gerar receipt de preservação com contagem de linhas, hashes e mapa origem → destino.
5. Substituir o README composto apenas quando o corpus estiver integralmente navegável no novo tree.
