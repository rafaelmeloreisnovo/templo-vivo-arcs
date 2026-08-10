# Ω7D — Dimensão 4: Capacidade e prova de conceito

## Objeto
Distinguir o que foi dito, formalizado, estruturado, executado, reproduzido e validado independentemente.

## Escala
- C0_TEXTUAL: descrição/manifesto;
- C1_FORMAL: fórmula, algoritmo ou estados definidos;
- C2_STRUCTURED: schema, YAML, configuração, contrato de dados;
- C3_EXECUTABLE_PARTIAL: código com placeholder/dependência não fechada;
- C4_EXECUTABLE: mecanismo implementado;
- C5_REPRODUCED: execução atual com receipt e ambiente;
- C6_INDEPENDENT: reprodução por terceiro/ambiente independente.

## Invariante
`claim de capacidade <= maior nível demonstrado por evidência executável`

## Procedimento
1. identificar artefato;
2. classificar linguagem e dependências;
3. verificar se o diff contém ação real;
4. executar somente em ambiente controlado quando aplicável;
5. registrar stdout/stderr, exit code, hashes e ambiente;
6. separar resultado do programa de interpretação científica do resultado.

## Heurísticas
- extensão `.py` não prova executabilidade;
- README não prova implementação;
- script executável não prova validade científica do modelo;
- benchmark sem dataset/ambiente/receipt não sobe para C5;
- placeholder deve permanecer visível.

## Exemplo de arco
`Manifest.txt (C0/C1) -> YAML (C2) -> Flutter parcial (C3) -> cristal.sh (C4) -> reprodução controlada (C5)`.
