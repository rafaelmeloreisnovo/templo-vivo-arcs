# RAFCODE-Φ — Arquitetura Jurídica em Camadas V1

**Status:** DRAFT_GOVERNED  
**Natureza:** engenharia jurídica/documental; não substitui revisão por advogado habilitado.  
**Regra de preservação:** nenhum artefato histórico é reescrito para fabricar anterioridade. Novos atos jurídicos recebem data e versão próprias.

## 1. Objetivo

Organizar a obra em uma família contratual modular, distinguindo direitos autorais, software, dados, marcas, patente/know-how, uso comercial, IA, segurança, proveniência e auditoria.

A estrutura segue um princípio comum em licenciamento empresarial: **termo-base + termos específicos + políticas + anexos + ordem comercial**, em vez de concentrar tudo em um manifesto único.

## 2. Pirâmide de autoridade

1. **Lei imperativa aplicável** — Constituição, leis brasileiras, tratados incorporados, normas de ordem pública, direitos do consumidor quando aplicáveis, LGPD e demais normas cogentes.
2. **Contrato comercial assinado / Order Form** — preço, escopo, prazo, SLA, território, usuários, ambientes, suporte e direitos adicionais.
3. **Licença-base RAFCODE-Φ** — direitos mínimos de uso, reservas, restrições, propriedade intelectual e rescisão.
4. **Adendos específicos** — dados/IA, segurança, enterprise, pesquisa, APIs, distribuição, marca, contribuições.
5. **Políticas técnicas** — SECURITY, provenance, disclosure, acceptable use, retention, incident response.
6. **Documentação do produto** — versões, compatibilidade, requisitos e limites técnicos.
7. **Manifestos simbólicos/éticos** — orientam interpretação cultural e de propósito, mas não ampliam direitos contra normas imperativas.

**Invariante:** uma camada inferior não pode anular direito obrigatório da camada superior.

## 3. Famílias de ativos

### A. Código-fonte e código-objeto
- Proteção principal: Lei 9.609/1998 + Lei 9.610/1998, conforme aplicável.
- Registro no INPI pode reforçar prova de autoria/titularidade.
- Versionar por hash, tag e commit.

### B. Documentação, textos, diagramas e imagens
- Direitos autorais sobre a forma de expressão original.
- Ideias, fatos, métodos abstratos e resultados não recebem automaticamente a mesma exclusividade da expressão textual.

### C. Dados e bases
- Distinguir: dado factual; dado pessoal; base organizada; segredo de negócio; dataset licenciado de terceiro.
- Dados pessoais obedecem LGPD independentemente da licença de software.

### D. Marcas e identidade
- `RAFAELIA`, `RAFCODE-Φ`, selos e nomes devem ter política de marca separada.
- Licença de código não implica licença de marca.

### E. Patentes / pedidos / know-how
- Nenhuma patente é presumida por README ou commit.
- Direitos patentários só são concedidos expressamente.
- Segredo de negócio exige medidas reais de confidencialidade; publicação aberta pode eliminar sigilo sobre o conteúdo divulgado.

### F. Contribuições
- Contribuições externas precisam de regra `inbound → outbound` ou CLA/DCO explícito.
- Autor, committer, agente e plataforma permanecem campos separados na proveniência.

## 4. Matriz de direitos de uso

| Classe | Visualizar | Fork no GitHub | Executar localmente | Modificar privado | Redistribuir | Produção comercial | Treino de IA comercial |
|---|---:|---:|---:|---:|---:|---:|---:|
| Público/GitHub mínimo | conforme ToS GitHub | conforme ToS GitHub | não presumido além da licença | não presumido | não presumido | não presumido | sujeito a lei, ToS e licença aplicável |
| Avaliação RAFCODE-Φ | sim | sim no serviço | sim, teste limitado | sim, avaliação | não | não | não concedido |
| Pesquisa não comercial | sim | sim | sim | sim | somente conforme termo específico | não | somente mediante autorização específica |
| Comercial | conforme Order Form | conforme política | sim | conforme escopo | conforme escopo | sim | conforme adendo |
| Enterprise/OEM | conforme contrato | conforme contrato | conforme contrato | conforme contrato | conforme contrato | conforme contrato | conforme contrato |

**Nota:** tornar um repositório público no GitHub já concede aos usuários certos direitos de visualização e fork dentro do serviço segundo os Termos do GitHub. A licença RAFCODE-Φ regula direitos adicionais e não pode fingir que essa concessão da plataforma nunca ocorreu.

## 5. Contratos especializados

- `RAFCODE_PHI_SOURCE_AVAILABLE_LICENSE_V1.md` — licença-base proprietária/source-available.
- `COMMERCIAL_ENTERPRISE_ADDENDUM_V1.md` — produção, monetização, OEM, suporte, auditoria e SLA.
- `DATA_AI_SECURITY_PROVENANCE_ADDENDUM_V1.md` — dados, IA, segurança, cadeia de custódia e incidentes.
- Futuro: `TRADEMARK_POLICY.md`, `CONTRIBUTOR_AGREEMENT.md`, `SECURITY.md`, `PRIVACY_NOTICE.md`, `ORDER_FORM_TEMPLATE.md`.

## 6. Cláusulas inegociáveis por padrão

1. Preservação de autoria, avisos e proveniência.
2. Nenhuma transferência de titularidade por simples acesso.
3. Uso comercial somente com grant expresso.
4. Nenhuma sublicença, OEM, SaaS ou redistribuição fora do escopo contratado.
5. Nenhuma licença de marca ou patente implícita além do mínimo exigido pela lei.
6. Proteção de segredos somente para material efetivamente confidencial e submetido a controles de sigilo.
7. Dados pessoais tratados sob base legal e finalidade definida.
8. Segurança e notificação de incidentes proporcionais ao risco.
9. Auditoria limitada, proporcional e com salvaguardas de confidencialidade.
10. Nenhuma cláusula pretende afastar direito inderrogável por lei.

## 7. Cadeia de custódia contratual

Cada versão jurídica deve gerar:

`LEGAL_VERSION -> file SHA -> commit SHA -> UTC -> branch/tag -> reviewer -> adoption event -> signature/timestamp (quando aplicável)`

Adoção de uma nova licença não altera retroativamente o regime jurídico de versões distribuídas sob termos anteriores.

## 8. Força jurídica e claim gate

### Permitido
- afirmar titularidade/autoria quando sustentada por prova;
- reservar direitos não concedidos;
- condicionar uso comercial a contrato;
- definir escopo, auditoria, segurança e rescisão dentro da lei;
- separar marca, software, dados e patente.

### Bloqueado
- declarar-se “acima da lei” ou “supra-legal”;
- usar tratados sem relação material como se criassem direitos autorais adicionais;
- proibir direitos obrigatórios previstos em lei;
- chamar licença restritiva de `open source`;
- alegar patente concedida sem registro oficial;
- transformar política interna em obrigação contra terceiro que nunca a aceitou.

## 9. Princípio de engenharia jurídica

A força não vem do número de proibições. Vem da combinação:

`titularidade + escopo claro + aceite + integridade + proveniência + proporcionalidade + remédio + lei aplicável`.

Quanto mais verificável e específico for o contrato, menor o espaço para ambiguidade.