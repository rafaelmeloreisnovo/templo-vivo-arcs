# Licensing & Rights Matrix — V1

## Regra central
Uma licença só alcança direitos que o licenciante efetivamente possui. Visibilidade pública não é sinônimo de domínio público.

| Classe | Tratamento padrão | Evidência necessária | Observação |
|---|---|---|---|
| Código original | RAFCODE Proprietary V1, salvo aviso diferente | histórico Git + autoria/proveniência | separar dependências |
| Documentação original | RAFCODE Proprietary V1 | commit/blob + cadeia | ideias/fatos não monopolizados por copyright |
| Dados próprios | contrato específico por dataset | origem + consentimento + schema | avaliar LGPD e direitos de terceiros |
| Dados de terceiros | licença/origem do fornecedor | LICENSE/terms/source | não relicenciar sem poder jurídico |
| Outputs de IA | revisar caso a caso | prompt/proveniência/modelo/data | autoria/proteção pode variar por jurisdição e contribuição humana |
| Marcas/símbolos | reserva separada | uso + eventual registro | licença copyright não basta |
| Invenções | política patentária separada | disclosure + prior art + depósito | publicação pode afetar estratégia de patente conforme jurisdição |
| Segredos | não publicar | controles de confidencialidade | Git público é incompatível com segredo do material publicado |

## Arquivos normativos
- `LICENSE-RAFCODE-PROPRIETARY-V1.md`: licença prospectiva para material coberto.
- `docs/legal/CADEIA_PROBATORIA_FORMAL_V1.md`: governança de evidência.
- `LICENSE`: arquivo histórico preservado como evidência; não deve ser silenciosamente reinterpretado como licença jurídica tecnicamente adequada.

## Política de conflitos
1. licença específica de arquivo/componente prevalece para aquele componente;
2. direitos de terceiros permanecem intactos;
3. material sem titularidade/proveniência suficiente entra em `RIGHTS_REVIEW_REQUIRED`;
4. nenhuma cláusula pretende eliminar direitos obrigatórios previstos em lei;
5. mudança de licença não reescreve retroativamente direitos já validamente concedidos sob licença anterior.

## Gate antes de release
- inventário SPDX/licenças;
- scan de dependências e notices;
- classificação de dados pessoais/confidenciais;
- separação de outputs de IA e contribuição humana quando material;
- prior-art antes de claims patentários;
- preservar SHAs/receipts do release.
