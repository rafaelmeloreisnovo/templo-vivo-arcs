# RAFCODE-Φ — Commercial & Enterprise Addendum V1 — DRAFT

## 1. Finalidade

Este adendo regula direitos que **não** são concedidos pela licença de avaliação/source-available: produção comercial, SaaS, OEM, distribuição, suporte, SLA, auditoria de uso, indenizações e condições econômicas.

## 2. Ordem comercial obrigatória

Cada contratação deve possuir `Order Form` ou instrumento equivalente contendo, no mínimo:

- partes e CNPJ/identificação;
- produto/versão/SKU;
- território;
- prazo;
- usuários, dispositivos, workloads ou outra métrica de licença;
- ambientes autorizados: dev/test/staging/prod;
- direitos de distribuição/OEM, se houver;
- suporte e SLA;
- preço, impostos e reajuste;
- dados tratados e papéis LGPD;
- anexos incorporados;
- assinatura e data de vigência.

## 3. Direitos comerciais possíveis

Os direitos abaixo só existem quando marcados expressamente no Order Form:

`PRODUCTION_USE`, `HOSTED_SERVICE`, `SaaS`, `OEM`, `EMBEDDED`, `REDISTRIBUTION`, `SUBLICENSE`, `API_RESALE`, `MODEL_TRAINING`, `DATASET_USE`, `TRADEMARK_USE`, `PATENT_GRANT`, `SOURCE_ESCROW`.

Ausência de marcação = direito não concedido.

## 4. Métrica e escopo

A métrica deve ser objetiva e auditável: usuário, instância, dispositivo, CPU/core, organização, volume, chamada API, receita atribuível, unidade OEM ou outra métrica especificada. Não se admite obrigação econômica baseada em conceito impossível de medir.

## 5. Auditoria proporcional

Quando prevista no Order Form, a auditoria de conformidade:

- ocorrerá em frequência razoável, salvo indício material de violação;
- terá aviso prévio razoável, exceto fraude ou urgência legal;
- limitar-se-á aos registros necessários para aferir o uso licenciado;
- respeitará confidencialidade, segurança, LGPD e segredo de terceiros;
- poderá usar relatório independente ou evidência automatizada em vez de acesso irrestrito;
- não autoriza coleta de dados desconectados da finalidade da auditoria.

Diferenças materiais confirmadas poderão gerar regularização, taxas contratuais e remédios permitidos pela lei; não há penalidade automática ilimitada.

## 6. SLA e suporte

SLA só existe quando contratado. Deve definir disponibilidade, janela de manutenção, severidade, tempo de resposta, créditos de serviço e exclusões. Documentação pública ou POC não cria SLA implícito.

## 7. Segurança enterprise

Contratos de produção devem definir, conforme risco:

- controle de acesso e MFA;
- gestão de segredos;
- SBOM e dependências críticas;
- atualização e vulnerabilidades;
- logs e retenção;
- backup e recuperação;
- notificação de incidente;
- provenance/attestation de releases;
- separação de ambientes;
- subprocessadores quando houver dados pessoais.

## 8. Propriedade intelectual

Cada parte mantém seus ativos preexistentes (`Background IP`). Entregáveis específicos (`Foreground IP`) devem ter titularidade ou licença expressamente definida.

Feedback não transfere automaticamente invenções, código ou datasets. Contribuições devem ser tratadas por contrato de contribuição/cessão/licença apropriado.

## 9. Indenização

Indenizações devem ser recíprocas e delimitadas por matéria, incluindo quando negociado: violação de PI de terceiro, violação de confidencialidade, tratamento ilícito de dados, fraude, dolo ou uso fora do escopo.

Defesa e acordo exigem notificação, controle razoável da defesa e cooperação.

## 10. Limitação de responsabilidade

O contrato comercial deve definir `liability cap` proporcional ao valor e risco, com `carve-outs` para matérias que não possam ser limitadas por lei ou que as partes negociem separadamente. Nenhum cap é presumido neste draft.

## 11. Confidencialidade

Informação confidencial deve ser identificável por natureza ou marcação e protegida com diligência razoável. Não inclui informação que já era pública, legitimamente conhecida, recebida de terceiro sem dever de sigilo ou desenvolvida independentemente, sujeito a prova.

## 12. Rescisão e saída

O Order Form deve prever:

- hipóteses de rescisão;
- prazo de cura para inadimplemento sanável;
- exportação/retorno de dados;
- eliminação certificada quando aplicável;
- sobrevivência de confidencialidade, PI, pagamento e auditoria de período anterior;
- transição técnica quando contratada.

## 13. Governo e setor regulado

Contratações públicas ou reguladas exigem adendo próprio; esta licença não prevalece sobre regras de contratação pública, soberania de dados, saúde, financeiro, defesa ou outras normas específicas.

## 14. Regra de interpretação

O objetivo não é maximizar restrições, mas tornar cada direito **mensurável, verificável e executável**:

`grant explícito + métrica + evidência + remédio proporcional + limite legal`.