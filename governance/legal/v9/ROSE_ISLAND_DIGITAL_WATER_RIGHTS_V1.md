# Ilha das Rosas, infraestrutura digital, água e Estado de Direito — estudo adversarial V9

**2026-10-30 · DRAFT RESEARCH_ONLY · claim_allowed=false · não é parecer jurídico nem projeto de soberania.**
**Fonte autoritativa de implementação:** `rafaelmeloreisnovo/templo-vivo-arcs`. Referências externas são fontes, não certificados.

## 1. A hipótese e seu contraponto
H1 (investigar): uma comunidade digital voluntária pode ter normas próprias de participação, proteção cultural e governança distribuída, conectadas a uma infraestrutura material.
H0 (controle): servidores, cabos, energia, água, nomes de domínio, membros e um manifesto **não** geram soberania estatal por si mesmos.
Resultado permitido hoje: **governança associativa/contratual potencial**, sujeita a direito estatal, direitos humanos e leis territoriais; **estatalidade e reconhecimento=TOKEN_VAZIO/NÃO COMPROVADOS**.

## 2. Caso histórico — Isola delle Rose (Giorgio Rosa)
- A autoproclamada República Esperantista da Ilha das Rosas surgiu numa plataforma artificial no mar Adriático em 1968, sem reconhecimento estatal; ocupação italiana em junho de 1968, demolição em fevereiro de 1969. [Rai Teche](https://www.teche.rai.it/2018/05/lisola-delle-rose-sogno-della-repubblica-esperantista-indipendente/) e [Biblioteca Salaborsa, Bologna](https://www.bibliotecasalaborsa.it/bolognaonline/cronologia-di-bologna/1968/lisola_delle_rose).
- **Montevidéu 1933, art. 1**: população permanente, território definido, governo e capacidade de relações exteriores: [Office of Historian, EUA](https://history.state.gov/historicaldocuments/frus1933v04/d134).
- **CNUDM/UNCLOS 1982, art. 60(8)**: ilhas artificiais não têm mar territorial próprio: [ONU, Parte V](https://www.un.org/Depts/los/convention_agreements/texts/unclos/part5.htm). É norma posterior aos fatos da Ilha das Rosas; não retroprojetar automaticamente para 1968.
- **Falsificadores**: prova de território soberano, reconhecimento, capacidade interestatal, governo legítimo, regras então vigentes, oposição estatal, decisões e tratados aplicáveis. Moeda/selo/esperanto/platforma NÃO são prova isolada de reconhecimento.

## 3. Da água ao data center: o território material do digital
- Não é verdadeiro que **todo** data center necessite de uma **entrada direta de água**: refrigeração seca pode consumir pouca ou nenhuma água local; energia, fabricação e cadeia de fornecimento têm pegada hídrica indireta. [Comissão Europeia, análise 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026DC0500), [IEA](https://www.iea.org/reports/powering-artificial-intelligence/executive-summary), [UNECE](https://unece.org/environmental-policy/water-convention-and-protocol-water-and-health/sustainable-data-centres).
- **Direito humano à água e ao saneamento**: Assembleia Geral da ONU, [A/RES/64/292 (2010)](https://digitallibrary.un.org/record/687002); isso não é escritura territorial nem autorização para fundar Estado.
- **Águas transfronteiriças**: Convenção da UNECE sobre águas transfronteiriças; deveres de cooperação dependem de Partes, bacias compartilhadas e fatos [UNECE FAQ](https://unece.org/environment-policy/water/about-the-convention/faqs/5).
- **Indicadores e regulação**: [Comissão Europeia — desempenho e pegada hídrica de data centers](https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficiency-targets-directive-and-rules/energy-efficiency-directive/energy-performance-data-centres_en). Não presume obrigação de qualquer operador fora do escopo.
- Para cada infraestrutura real: `physical_site_id | country | lawful_operator | provider | cooling_type | direct_water | indirect_water | electricity_origin | water_rights | local_impact | legal_basis | vendor_contract | data_flows | source | verified_at | gaps`.
- **Gatilho P0** se houver operação física identificada e risco a água potável/localidade; sem operador ou instalação demonstrados, marcar `TOKEN_VAZIO`.

## 4. Estado de Direito digital sem falsa soberania
Uma comunidade pode adotar uma **carta interna voluntária** com: transparência, não discriminação, livre crença/não crença, direito de saída, devido processo procedimental dentro da organização, mecanismos humanos de recurso, proteção infantil, tratamento legítimo de dados, prestação de contas, acessibilidade, respeito cultural e remediação.
**Isso não constitui Constituição estatal, tratado entre Estados, tribunal soberano, direito de expropriar recursos naturais nem imunidade das leis do país.**
- [Princípios Orientadores da ONU sobre Empresas e Direitos Humanos](https://international-partnerships.ec.europa.eu/eu-due-diligence-navigator-partner-countries/un-guiding-principles-business-and-human-rights-ungps_en): proteger, respeitar e remediar; padrões orientadores, não tratado constitutivo.
- [UNESCO 2005, art. 2](https://www.unesco.org/en/legal-affairs/convention-protection-and-promotion-diversity-cultural-expressions): diversidade cultural condicionada ao respeito aos direitos humanos.
- Brasil: [Lei 15.211/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm) (ECA Digital, vigente desde 17-03-2026) para serviços concretamente abrangidos. Incluir revisão de decretos e regulações atuais.
- Proteção de dados pessoais e crença religiosa: LGPD/GDPR quando aplicáveis; retenção append-only de provas **não** afasta direitos de exclusão/correção de dados pessoais. Conservar commitments não identificadores quando possível.
- Contratos de nuvem, DNS, IP, localização de usuários, sede jurídica, terceiros e lei aplicável criam nexos, não soberania.

## 5. Tabela de falsificação jurídica
| Claim hipotético | Contraexemplo/falsificador | Regra |
| --- | --- | --- |
| "Hospedar dados cria um país" | Montevidéu art. 1 sem território/povo/governo/capacidade | CLAIM_BLOCKED |
| "Uma plataforma criou mar territorial" | UNCLOS art. 60(8), com limite temporal para 1968 | CLAIM_BLOCKED |
| "Todo data center recebe água diretamente" | refrigeração a ar/seca; pegada indireta ≠ captação direta | CLAIM_REFUTED_GENERALITY |
| "Declaração da ONU entrega direito ao uso de água" | direito humano à água não é concessão de outorga/posse | CLAIM_BLOCKED |
| "Uma licença privada proíbe qualquer análise/cópia" | exceções autorais, acessibilidade, licenças prévias e titularidade | CLAIM_BLOCKED |
| "Carta interna cria imunidade penal/infantil" | normas obrigatórias e proteção da criança | CLAIM_BLOCKED |
| "A política é operacional" | falta de proprietário, fluxo de dados, auditoria e testes de incidentes | HOLD |

## 6. Itens deliberadamente separados (lacunas negligenciadas)
1. **Personalidade jurídica da associação/fundação** ≠ governo nacional; eventual registro nacional exige rito próprio.
2. **Domicílio digital/domínio** ≠ território; DNS e domínios dependem de contratos e entidades de registro.
3. **Infraestrutura e poder estatal**: competências fiscal, urbanística, ambiental, hídrica, trabalhista e energética continuam territoriais; identificar fornecedor/operador, sem inventar país.
4. **Competência jurisdicional** ≠ escolha unilateral de foro; contratos, consumo, serviços digitais e tratados processuais podem limitar escolha.
5. **Custódia histórica**: hash vincula bytes conhecidos; não comprova autoria, titularidade ou instante histórico sem fontes independentes.
6. **Ritos e tradições**: consultas e titularidade coletiva; evitar apropriação de culturas ancestrais.
7. **Direitos humanos universais**: liberdade de sair e de não crer, proteção de minorias, igualdade, acesso à crítica, mecanismos de reparação.
8. **Segurança e crianças**: manter P0/HOLD enquanto operador, dados sensíveis, canal de denúncias, credenciais e branch protection permanecerem não comprovados.
9. **Sustentabilidade medida**: sem métrica local de água/energia, custo ambiental = TOKEN_VAZIO, não ZERO.

## 7. Critérios de promoção e retorno
Uma tese só avança se `fonte oficial + versão temporal + objeto + sujeito + nexo territorial + autoridade competente + regra aplicável + decisão favorável/contrária + exceções + evidência + revisão independente` estiverem demonstrados. O contrário permanece `TOKEN_VAZIO`.
**Sem licenciamento novo, exploração de menores, coleta de crenças, implementação de supostas prerrogativas estatais ou promoção de claims sem revisão.**
F_ok=roteiro documental e limites tipados; F_gap=operador/infrastrutura efetiva, direitos de água, legislação local, titularidade, reconhecimento e revisão independente; F_next=inventário mínimo de operação e falsificação de direitos aplicáveis por jurisdição.
