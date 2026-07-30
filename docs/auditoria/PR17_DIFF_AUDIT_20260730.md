# Auditoria do diff — PR #17

**Repositório:** `rafaelmeloreisnovo/templo-vivo-arcs`  
**PR auditado:** `#17`  
**Data de decisão:** `2026-07-30`  
**Decisão:** `CLOSED_WITHOUT_MERGE`  
**claim_allowed:** `false`

## Âncoras de rastreabilidade

| Objeto | Valor |
|---|---|
| Base | `main` |
| Base commit | `ade5948b1487a50130e9dd3336d96d93b3e6c4da` |
| README original blob | `f577635b08e5a9c3ffff1458b6c85dd5b430c46d` |
| Branch auditado | `claude/readme-analise-refatoracao-vl6t6l` |
| Head auditado | `fb42bdaba38914ca151312fe2c1bb63ac51f37cc` |
| Arquivos alterados | `2` |
| Adições | `57` |
| Exclusões | `1163` |
| Workflow runs no head | `0` |
| Review de auditoria | `4814755866` |

## Resultado do diff

### `LITURGIA.md`

- 23 linhas adicionadas no PR original;
- preservava a oração inicial;
- não preservava o restante do conteúdo espiritual, científico, jurídico, acadêmico e declaratório removido do README;
- continha o erro textual `lituúrgico`.

### `README.md`

- 34 linhas adicionadas;
- 1.163 linhas removidas;
- a nova entrada técnica era mais legível, mas a migração não possuía mapa origem → destino;
- links acadêmicos relevantes foram removidos da navegação, incluindo:
  - `INDICE_NAVEGACAO.md`;
  - `EXEMPLOS_PRATICOS.md`;
  - `BIBLIOGRAFIA.md`;
  - `docs/posdoc_estrutura/*`.

## Contradição material

A descrição do PR declarava “conteúdo preservado 100%”. O tree proposto preservava apenas a oração de abertura em arquivo dedicado. O restante continuava acessível no histórico Git, mas não estava preservado nem navegável no novo tree. Portanto:

```text
preservação histórica no Git != preservação integral no tree
oração preservada != corpus preservado
README menor != migração concluída
```

## Achado lateral

O README de `main` cita `MANIFEST-SEAL.md`, porém a consulta direta ao caminho retornou `404 Not Found`. O estado correto é:

```text
MANIFEST-SEAL.md = TOKEN_VAZIO_PATH_NOT_FOUND
```

Nenhuma afirmação de hashes ativos, assinatura ou carimbo de tempo deve depender desse caminho até sua materialização e validação.

## Ação aplicada

1. PR #17 fechado sem merge.
2. Branch e commits mantidos para auditoria e recuperação.
3. Nova branch criada: `docs/pr17-safe-preservation-20260730`.
4. `LITURGIA.md` adicionado de forma classificada e não destrutiva.
5. `docs/README_TECNICO.md` adicionado como entrada paralela.
6. README original mantido intacto.

## Gate para futura refatoração do README

A refatoração somente pode ser promovida quando existir receipt contendo:

- contagem de blocos de origem e destino;
- hashes ou blobs de cada fonte;
- tabela origem → destino;
- classificação epistemológica de cada bloco;
- verificação de links;
- comprovação de que nenhum conteúdo ficou órfão;
- CI ou auditoria reproduzível no head final.

## Retroalimentação

- `F_ok`: intenção de separar navegação técnica e liturgia é coerente.
- `F_gap`: preservação integral não foi materializada no tree e não houve CI.
- `F_next`: classificar e migrar o README por blocos, com receipt de equivalência antes de qualquer exclusão.
