# TOKEN_VAZIO — Utilidade Operacional — Templo Vivo ARCS

**status:** ACTIVE  
**version:** V1  
**date:** 2026-09-22  
**scope:** governança, auditoria, evidência, custódia, ciência e documentação

## Invariante

`TOKEN_VAZIO` é **útil**.

Ele não representa zero, erro, descarte ou ausência de valor. Representa um estado explícito em que a informação necessária ainda não foi demonstrada, medida, localizada, autorizada ou validada.

```text
TOKEN_VAZIO != 0
TOKEN_VAZIO != FALSE
TOKEN_VAZIO != ERRO
TOKEN_VAZIO != AUTORIZAÇÃO
TOKEN_VAZIO != INVENÇÃO
```

Sua utilidade está em impedir que uma lacuna seja silenciosamente preenchida por suposição.

## Função

Quando um campo, claim, fonte, autoria, parâmetro, evidência ou relação ainda não puder ser fechado com prova suficiente, `TOKEN_VAZIO` preserva:

1. **incerteza real** — o desconhecido continua identificado como desconhecido;
2. **proveniência** — não se inventa origem para preencher um campo;
3. **falsificabilidade** — a lacuna pode gerar um teste ou busca verificável;
4. **rollback** — um preenchimento futuro não apaga o estado anterior;
5. **auditabilidade** — é possível distinguir “não sabemos ainda” de “sabemos que é zero/falso”;
6. **segurança de claim** — ausência de evidência não é promovida a conclusão;
7. **priorização** — vazios relevantes viram itens de trabalho rastreáveis.

## TOKEN_VAZIO como estado ativo

Um `TOKEN_VAZIO` útil deve, quando materialmente relevante, apontar para uma rota de fechamento:

```text
gap
-> fonte_esperada
-> ação
-> evidência_mínima
-> critério_de_fechamento
-> critério_de_falha
-> próximo_estado
```

Sem evidência suficiente, o estado continua vazio. O tempo decorrido, repetição textual, coerência narrativa ou plausibilidade não fecham o gap.

## Regra de preenchimento

```text
TOKEN_VAZIO
  + evidência verificável
  + proveniência
  + gate satisfeito
  -> novo estado
```

O novo estado deve ser registrado como evolução append-only; não se reescreve a história como se o vazio nunca tivesse existido.

## Relação com claim gate

```text
SOURCE != ARTEFATO != EXECUÇÃO != EVIDÊNCIA != CLAIM
```

`TOKEN_VAZIO` pode existir em qualquer camada e bloqueia somente a promoção que dependa daquele requisito específico. Ele não invalida automaticamente o restante do sistema.

## Exemplo mínimo

```json
{
  "campo": "autoria_exata_por_linha",
  "estado": "TOKEN_VAZIO",
  "fonte_esperada": "histórico verificável de autoria",
  "evidencia_minima": "registro atribuível e reproduzível",
  "next": "buscar fonte primária",
  "claim_allowed": false
}
```

## Síntese

O valor de `TOKEN_VAZIO` é epistemológico e operacional:

> **preservar o que ainda não sabemos é melhor do que preencher uma lacuna com informação não demonstrada.**

No Templo Vivo ARCS, o vazio governado é informação sobre o estado do conhecimento e pode orientar a próxima ação verificável.

---

### μWRITE

`TVA-MUW-20260922-01 | 2026-09-22T23:00:00-03:00 | source=user_instruction | parent=TOKEN_VAZIO existing contracts | kind=governance_invariant | Δ=TOKEN_VAZIO explicitamente classificado como útil | routes=P,C,R,I,E,A | evidence=repository existing TOKEN_VAZIO controls + this commit | gap=README principal ainda não referencia este documento diretamente | next=referenciar em índice/README quando houver próxima manutenção documental | append_only=true`
