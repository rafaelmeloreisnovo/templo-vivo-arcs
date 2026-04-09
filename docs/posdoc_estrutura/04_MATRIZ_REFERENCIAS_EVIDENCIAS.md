# Matriz Referências ↔ Evidências ↔ Afirmações

## Finalidade

Garantir que cada afirmação técnica/teórica relevante tenha:

1. fundamento bibliográfico;
2. vínculo com evidência observável;
3. status epistemológico claro.

## Taxonomia de status epistemológico

- **E0 — Intuição/ensaio:** sem teste formal.
- **E1 — Hipótese operacional:** testável, mas sem validação robusta.
- **E2 — Evidência inicial:** teste executado com suporte parcial.
- **E3 — Evidência robusta:** replicação e consistência estatística.
- **E4 — Consenso provisório:** múltiplas validações independentes.

## Template de matriz (preencher continuamente)

| ID | Afirmação | Documento fonte | Referência bibliográfica | Evidência empírica | Status |
|----|-----------|-----------------|--------------------------|--------------------|--------|
| A-01 | ... | `DISSERTACAO_ACADEMICA.md` | Autor, ano | Dataset X + experimento Y | E1 |
| A-02 | ... | `Teoremas.md` | Autor, ano | Simulação Z | E0/E1 |
| A-03 | ... | `EXEMPLOS_PRATICOS.md` | Autor, ano | Execução reproduzível | E2 |

## Regras de preenchimento

1. **Documento fonte:** apontar arquivo de origem da afirmação.
2. **Referência bibliográfica:** priorizar fonte primária (artigo, livro, padrão).
3. **Evidência empírica:** descrever dataset, script e métrica.
4. **Status:** atualizar após cada ciclo de teste.

## Critério de maturidade científica

Uma linha só alcança E3+ se cumprir simultaneamente:

- metodologia explicitada;
- dados auditáveis;
- teste estatístico adequado;
- replicação por equipe ou ambiente independente.

## Integração com os documentos existentes

- Use `BIBLIOGRAFIA.md` como base de referência canônica.
- Use `INDICE_NAVEGACAO.md` para conectar contextos de leitura.
- Use `SUMMARY_OF_CHANGES.md` para rastrear evolução argumentativa.
