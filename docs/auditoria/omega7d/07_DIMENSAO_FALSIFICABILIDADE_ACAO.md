# Ω7D — Dimensão 7: Falsificabilidade, urgência e ação

## Objeto
Converter cada afirmação em uma unidade auditável que tenha prova esperada, condição de refutação e próximo ato executável.

## Invariante
`claim -> evidência -> teste adversarial -> resultado -> próximo estado`

## Contrato de claim
Cada claim deve possuir:
- `claim_id`;
- formulação precisa;
- evidências favoráveis;
- evidências contrárias;
- condição que o refutaria;
- nível temporal T0–T6;
- capacidade C0–C6;
- nível jurídico J0–J6;
- `claim_allowed`;
- urgência;
- próxima ação;
- critério de fechamento.

## Urgência
- U0: informativo;
- U1: melhora documental;
- U2: lacuna que limita claim;
- U3: risco de integridade/proveniência;
- U4: prazo jurídico, segurança ou risco de perda de evidência.

## TOKEN_VAZIO como estado ativo
`TOKEN_VAZIO` não é apagado. Deve ser transformado em contrato de busca:
`gap -> fonte esperada -> ação -> responsável -> evidência mínima -> deadline se houver -> resultado`.

## Regra anti-regressão
Nenhuma conclusão anterior pode ser promovida sem nova evidência; pode ser rebaixada se aparecer conflito, artefato anterior, falha de reprodução ou erro de atribuição.

## Retroalimentação
`R3 = <F_ok, F_gap, F_next>` deve acompanhar cada ciclo e gerar alteração somente quando existe ganho verificável de informação.
