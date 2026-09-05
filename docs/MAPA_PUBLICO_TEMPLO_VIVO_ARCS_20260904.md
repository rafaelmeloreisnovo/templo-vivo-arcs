# MAPA PÚBLICO — TEMPLO VIVO ARCS

Data: 2026-09-04
Escopo: projeção pública navegável do Templo Vivo Arcs.
Visibilidade: PUBLIC
Estado: OBSERVED + PARTIAL

## Finalidade

Este mapa organiza os lugares públicos do repositório sem declarar equivalência entre metáfora, tradição, hipótese, experimento e evidência.

Regra epistemológica:

```text
=   igualdade no domínio declarado
≈   aproximação / analogia contextual
≠   distinção relevante
?   relação ainda não estabelecida
TOKEN_VAZIO   lacuna válida e auditável
```

## Lugares observados no repositório

| Lugar | Tipo | Função observável | Estado | Próxima ação verificável |
|---|---|---|---|---|
| ` LIVROS/` | diretório | superfície de livros/corpus | OBSERVED | inventariar títulos e proveniência sem presumir autoria/status |
| `.github/` | diretório | automação/governança GitHub | OBSERVED | ler workflows/policies antes de classificar |
| `.lux/` | diretório | namespace próprio do projeto | OBSERVED | `TOKEN_VAZIO`: significado interno ainda não revalidado |
| `00000/` | diretório | agrupamento/corpus | OBSERVED | `TOKEN_VAZIO`: finalidade semântica ainda não revalidada |
| `Amor.html` | arquivo | artefato HTML público | OBSERVED | classificar relação com os arcos após leitura específica |
| `Anexo_Legal_Manifesto_RafaelIA.docx` | arquivo | anexo/manifesto | OBSERVED | verificar versão e relação com eventual duplicata |
| `Anexo_Legal_Manifesto_RafaelIA_1.docx` | arquivo | possível duplicata/versão | OBSERVED | comparar hashes/conteúdo antes de declarar equivalência |
| `Ativos_20_Puros_Estatisticas_Completas.xlsx` | arquivo | planilha pública | OBSERVED | validar proveniência/metodologia antes de qualquer claim |
| `docs/MAPA_PUBLICO_TEMPLO_VIVO_ARCS_20260904.md` | arquivo | índice público de lugares | ACTIVE | evoluir por leitura comprovada e append de estados |

## Contrato de publicação

O repositório público recebe somente informação que possa ser exposta com segurança e contexto suficiente.

Cada arco/lugar deve poder carregar:

```yaml
arc:
  name: TOKEN_VAZIO
  kind: text|book|image|code|dataset|metaphor|legal|other
  status: observed|interpreted|tested|evidenced|TOKEN_VAZIO
  provenance: []
  semantics: []
  analogy_links: []
  evidence_links: []
  rights_or_license: TOKEN_VAZIO
  public_safe: TOKEN_VAZIO
  next_verifiable_action: TOKEN_VAZIO
```

## Grafo do Logos — regra de relação

Relações não são achatadas em igualdade:

```text
SEMENTE 🌱 --pode_evoluir--> ÁRVORE
CHAVE 🔑 --pode_abrir--> PORTA 🚪
FLECHA 🏹 --direciona_para--> ALVO 🎯
HIPÓTESE --testada_por--> EXPERIMENTO
METÁFORA --é_analógica_a--> CONCEITO
METÁFORA ≠ EVIDÊNCIA EXPERIMENTAL
```

A perspectiva religiosa, filosófica, científica ou agnóstica pode coexistir no grafo desde que o tipo da relação permaneça explícito.

## Google Drive público-operacional

Foi observada uma pasta Drive `templo-vivo-arcs` criada em 2026-09-02 e vazia na leitura desta sessão. Ela pode receber o espelho deste mapa como índice operacional, sem importar automaticamente conteúdo privado.

## Gaps atuais

- `TOKEN_VAZIO`: inventário completo dos subdiretórios ainda não executado nesta sessão.
- `TOKEN_VAZIO`: autoria/licença/proveniência de cada artefato não inferida apenas pelo nome.
- `TOKEN_VAZIO`: relação entre arquivos potencialmente duplicados requer comparação de conteúdo/hash.
- `TOKEN_VAZIO`: classificação de `.lux/` e `00000/` requer leitura específica.

## Próximo ciclo

`observar → classificar → relacionar → verificar → registrar → publicar somente o demonstrado`.
