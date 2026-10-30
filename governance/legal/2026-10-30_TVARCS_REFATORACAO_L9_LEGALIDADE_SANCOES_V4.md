# TEMPLO VIVO ARCΣ / ARCS — RAFAELIA
## Plano de refatoração jurídico-institucional L9, responsabilidade e sanções — V4
Data: 2026-10-30 | Escopo: diagnóstico comparado / proposta documental | STATUS: REVIEW_ONLY / CLAIM_ALLOWED=false / PROMOTION=HOLD
Fonte produtora: https://github.com/rafaelmeloreisnovo/templo-vivo-arcs
HEAD de partida: 11552fee066ce2c5631f331c574546de72ed0021
Predecessores: PR#44 (8 jurisdições), PR#45 (jurisprudência US/UK), PR#46 (matriz 24 jurisdições): **todos MERGED no estado observado em 2026-10-30**. Estados "DRAFT" escritos dentro de documentos são marcas HISTÓRICAS, não o estado presente dos PRs. V4 não reescreve licenças ou commits anteriores.

> Este registro estuda **o que refatorar**, não atesta conformidade legal, personalidade jurídica, registro de culto, validade de um parecer judicial, sucesso de sanção contra terceiros ou segurança absoluta. Regras materialmente aplicáveis requerem fatos reais sobre o operador, atividade, jurisdição, usuários e estrutura econômica. Cada número monetário abaixo é **teto legal condicionado**, jamais multa aplicada ao Templo.

## 1. Diagnóstico do material real — atenção à apresentação
Observado em README.md atual:
- A primeira abertura em inglês explica a governança, mas em seguida permanece um longo manifesto misto (espiritualidade, app, ciência, mercado e direito), com SEGUNDO título do projeto, marca "hi" junto ao selo e rótulo legado "ACTIVE".
- Afirmação histórica "Σ-Seal assegura autenticidade, autoria e provas públicas" **é forte demais** sem certificado de autenticação, cadeia de titularidade e validação externa. Reformular futuramente como "o sistema busca registrar integridade e proveniência, sujeito a testes, identidade e validação".
- Afirmação histórica de "estrutura completa de dissertação" não é parecer acadêmico independente. Dividir documento produzido, grau acadêmico, avaliação por pares e evidência executada.
- Links legais V3 dizem "proposed / not yet effective" embora PR#46 esteja MERGED. CORREÇÃO sem apagar história: **documento presente no branch principal ≠ licença comercial automática ≠ revisão jurídica concluída**.
- Mistura de software, pesquisas, atividade espiritual e dados de trading no mesmo texto público pode fazer leitores inferirem aconselhamento médico/financeiro ou validação científica sem base. Inserir delimitadores e não-promessa de resultados, consentimento para serviços reais, se houver.
- Fonte técnica e jurídica do escopo licenciado está corretamente segmentada em LICENSE_POLICY.md e RIGHTS_NOTICE...V3; preservar. LICENSE root histórico e demais direitos de terceiros **não modificar** por refatoração visual.

### Refatoração mínima proposta para a próxima PR (NÃO implementada em V4)
1. README de entrada com duas camadas: pt-BR principal + resumo EN (mais versões apenas se verificadas). Título único, metadados atualizados, sem poluição de manifesto ou "hi"; texto histórico preservado em anexo e com link estável/commit.
2. Criação futura de `docs/LEGAL_START_HERE.md` ou ponte para índice já existente, **só após deduplicação de índice**: identidade do operador, objeto, direitos/licenças, política de privacidade, proteção infantil, jurisdições aplicáveis, fontes autoritativas, contatos legítimos e procedimento de revisão de reivindicações.
3. Separar `MANIFESTO_HISTORICO`, `RESEARCH_HYPOTHESES`, `SOFTWARE_STATUS`, `LEGAL_GOVERNANCE`, `EVIDENCE_RECEIPTS`, `PRIVACY_AND_CHILD_SAFETY`, `PUBLIC_NOTICES`. Navegação por links versionados; não mover nem destruir documento histórico automaticamente.
4. Antes de traduzir: revisão por pessoa competente, glossário de "templo", "culto", "instituto", "religião", "licença", "autoria", "selo", "validação", "sanção" e delimitação jurisdicional.
5. Evidência antes de logomarca/selo: autoridade do operador, prova de cadeia de titularidade, fontes e testes reproduzíveis.
6. Não publicar emails privados, credenciais, dados de crianças, declarações de fé individuais ou contratos internos.

## 2. L9 — Causas, correções e medição de progresso

| Eixo | Fonte/gap | Refatoração de maior valor | Evidência/gate |
|---|---|---|---|
| L longitudinal | PRs #44–46 mergidos, arquivos dizem DRAFT | Ponto de situação separado de disclaimer histórico por documento | IDs, GH HEAD, data e parent/supersedes |
| O ortogonal | fé/tecnologia/jurisprudência/negócios mesclados | Identidade e produtos separados por domínio | nenhum domínio empresta prova ao outro |
| T transversal | autoria, dados, menores, terceiros | Política comum de dignidade + escopo por fluxo | testes de exclusão e não coerção |
| P proveniência | hash/selo usado como prova ampla | Integridade ≠ titularidade ≠ tempo ≠ autoria ≠ registro | hash de conteúdo + prova independente |
| C contexto | regras brasileiras/US/UK/EU sem fatos operacionais | `country_scope`, operador, público, modo de serviço | mapa de dados e legal nexus |
| R relacional | links para 24 países sem confirmação completa | relação tipada: lei→obrigação→risco→controle→evidência→sanção | nenhum "precedente universal" |
| I índice | README duplicado/manifesto longo | START_HERE mínimo, profundo só por rota | navegação humana/IA testada |
| E evidencial | revisão local e CI ausentes | controlar `VERIFIED_SOURCE/ANALYZED/IMPLEMENTED/TESTED/APPROVED` | checklist e receipts |
| A adaptativa | novos precedentes/modificação de normas | atualizações *append-only* de índices jurídicos, substituições legíveis | before/after, idempotência, rollback |

## 3. Sanções não são um bloco único
Separe três sistemas:
A) **Consequências legais por infração do operador**, regulatórias, civis ou criminais, segundo a lei aplicável e os fatos.
B) **Remédios civis do titular** (indenização, tutela judicial, remoção ou reparação) mediante prova e processo, não multas automáticas por declaração no README.
C) **Regimes econômicos/financeiros de sanções** (OFAC, OFSI, UE/ONU) ligados a transações, pagamentos, pessoas designadas e território; **não** são multas genéricas por copiar um texto ou discordar do projeto. Ativar apenas com atividade, jurisdição e risco identificado.

### Matriz legal de possíveis exposições — teto não é penalidade aplicada
| Sistema / autoridade | Gatilho potencial *condicional* | Consequências possíveis e parâmetro legal | Controle mínimo / estado |
|---|---|---|---|
| Brasil LGPD, art.52, ANPD | tratamento de dados pessoais no escopo da lei; violação comprovada no procedimento | advertência; multa simples até **2% do faturamento no Brasil**, teto **R$50 milhões por infração**; diária; publicização, bloqueio/eliminação e outras sanções do art.52 | dados sensíveis de religião, minimização, retenção, direitos do titular, resposta a incidentes; **aplicabilidade e cumprimento TOKEN_VAZIO** |
| Brasil ECA Digital Lei 15.211/2025 art.35, ANPD | serviço TIC direcionado ou de acesso provável por menores; obrigação descumprida; lei vigente **17/03/2026** | advertência; multa até **10% do faturamento do grupo no Brasil**, ou fórmula legal por usuário cadastrado sem faturamento, teto **R$50 milhões por infração**; suspensão/proibição de atividades | avaliação REAL de acesso provável, idade, riscos, mecanismos proporcionais, comunicação e segurança infantil; **nexo e implementação TOKEN_VAZIO** |
| Brasil Marco Civil da Internet, arts.10–12 + STF Temas 987/533 (2026) | guarda/divulgação de dados e atuação como provedor; conteúdo de terceiros e risco sistêmico se factual e juridicamente aplicável | art.12 prevê advertência, multa de até **10% do faturamento do grupo no Brasil** para hipóteses arts.10/11, suspensão/proibição conforme lei; responsabilidade civil de conteúdo depende da tese STF ajustada e dos fatos | trilha de notificações e resposta diligente, distinção publicação própria/UGC; **regras jurídicas distintas e NÃO somar tetos como multa prevista** |
| Brasil direitos autorais Lei 9.610/1998 arts.102–110 | violação de obra efetivamente protegida e direitos demonstrados | apreensão, suspensão de divulgação, indenização, e demais remédios judiciais condicionados; direitos de terceiros também protegidos | cadastro por ativo, titular, autorização, exceções, restrições, prova original; sem ameaça de penalidade automática |
| Brasil CDC arts.30,37,39,56 se relação de consumo | app, subscrição, doação associada a oferta de bens/serviços, publicidade/atividade comercial real | multa administrativa, suspensão de serviços e outras medidas proporcionais, além de reparação civil, se os requisitos legais forem preenchidos | publicidade não enganosa, preço e escopo dos serviços, canais de reclamação e provas de entrega |
| Brasil Lei 7.716/1989 art.20 e Código Penal, se fatos típicos | incitação a discriminação religiosa e outras condutas definidas em lei | resposta penal/pessoal e remoção/interdição judicial nos termos legais; proibição de discurso discriminatório não é proibição de crença | não coerção, moderação legítima, discurso respeitoso, apuração individual; não antecipar culpabilidade |
| UK UK GDPR / DPA 2018, ICO | processamento em alcance territorial e material das normas | patamar superior **£17,5 milhões ou 4% do faturamento mundial** de undertaking, o que for maior, conforme o tipo de infração e regime aplicável | country/data map, privacy-by-design, direitos, incidentes, lawful basis; se UK nexus desconhecido => TOKEN_VAZIO |
| UK Online Safety Act 2023, Ofcom, Sch.13 | serviço regulado sob a lei e deveres concretos aplicáveis | máximo **£18 milhões ou 10% da receita mundial qualificável**, o maior; depende categoria/regime, proporção e processo | avaliação de serviços com UGC, denúncias e riscos infantis; não aplicar automaticamente a repo estático |
| EUA COPPA, FTC | serviço online direcionado a menores de 13 anos ou conhecimento efetivo de coleta nos termos do COPPA | multas civis por violação conforme teto periodicamente ajustado, além de ordens e remédios; **não congelar valor monetário sem tabela vigente** | identificar público, dados, regras de pais e coleta; leis estaduais adicionais conforme nexus |
| EUA OFAC / UK OFSI | pagamento/transferência/negócio real envolvendo jurisdição e pessoa/território listado | bloqueio, reportes e multas financeiras ou criminais no regime aplicável; valores e critérios variam por programa | triagem proporcional *somente se transações/compliance exigirem*; nada de acusar pessoas sem evidência |
| União Europeia GDPR art.83 / DSA | processamento/serviços cobertos por regras UE e nexo territorial | GDPR categoria superior até **€20 milhões ou 4% do volume mundial** (o que for maior); DSA máx. até **6% da receita mundial** em casos pertinentes | escopo UE, tipo de plataforma e data, supervisionamento e garantias; **não são multas do Templo verificadas** |

**Regra:** sanção aplicada requer infração, agente competente, rito, defesa, gradação e decisão conforme lei. A multa máxima **não é condenação provável nem orçamento financeiro**. Não ameaçar terceiros com multas legislativas como se houvesse poder de punição privada.

## 4. Normas e precedentes a governar por domínio

**Brasil:** CF arts.5º IV, V, VI, IX, X, XXVII-XXIX, LXXIX; art.19(I); art.227. LGPD Lei 13.709/2018; ECA 8.069/1990; ECA Digital 15.211/2025 (vigência mar/2026); MCI Lei 12.965/2014; Lei 9.610/1998; Lei 9.609/1998; CDC 8.078/1990 se comércio; Lei 7.716/1989 em ilícitos discriminatórios. Repercussão geral STF **Temas 987/533**, sessão de 17/06/2026 sobre responsabilidade de plataformas e atualização do art.19 do MCI; incidência requer classificação real do serviço e do conteúdo.

**EUA:** 1ª/4ª/5ª Emendas e lei federal/estadual aplicáveis; *Lukumi* (1993), *Smith* (1990), *Fulton* (2021), *Moody* (2024), *Riley* (2014), *Carpenter* (2018), *Braswell* (1988). Artigos do Bill of Rights não dão imunidade a organização privada; discriminação, proteção de crianças, IP e contratos permanecem temas próprios.

**Inglaterra e País de Gales / Reino Unido:** Human Rights Act 1998, Data Protection Act 2018 / UK GDPR, Online Safety Act 2023 conforme serviço; *Hodkin* (2013), *Shergill* (2014), *Bank Mellat* (2013) e *Eweida* (ECtHR, não UKSC). Diferenciar precedentes Inglaterra/País de Gales, Escócia/Irlanda do Norte e Tribunal Europeu dos Direitos Humanos.

**Internacional:** Convenção de Berna e WIPO Lex, PIDCP, Convenção dos Direitos da Criança; distinguir tratado, soft law, transposição, ratificação, reservas e regra territorial. Pesquisa V3 de 24 jurisdições contém **15 rotas de pesquisa** sem texto/casos completos; não promover a 24 pareceres nacionais. UE DSA e GDPR só mediante conexão factual.

## 5. Matriz de risco com fonte, disparador, sanção e método de prova
| ID | Severidade condicional | Risco/observação | Próxima ação reversível | Teste / estado |
|---|---|---|---|---|
| P0-A | Operacional confirmado | GitHub `main` sem proteção obrigatória observado no HEAD de 30/10 | revisão de regras do provedor, permissões, PR review, required checks; administrador autorizado | readback protection + tentativa negativa em ambiente seguro; NOT_DONE |
| P0-B | Condicional, dados infantis | inexistência de classificação serviço/acesso provável menores sob ECA Digital | levantar app público/privado, público-alvo e fluxos, sem coletar dados pessoais novos | ficha factual por serviço; TOKEN_VAZIO |
| P0-C | Condicional, segredo | credencial histórica apontada em receipt, status de rotação desconhecido | revogação/rotação em canal seguro, varredura sem divulgar valor | atestado de provedor, sem log de segredo; TOKEN_VAZIO |
| P1-D | Documental confirmado | README mistura narrativa, claims técnico-científicos, links jurídicos e duplicação | reorganização aditiva em PR separado após approval | testes de links + revisão humana |
| P1-E | Governança de conteúdo | escopo de UGC/denúncias é desconhecido apesar da mudança STF 2026 | mapear conteúdo próprio vs terceiros, avisos, responsividade e abuso | evidência funcional; TOKEN_VAZIO |
| P1-F | Dados sensíveis | fé, menores, pesquisa científica poderiam envolver dados pessoais, mas isso não prova coleta | mapa de dados mínimos e tratamento local/crossborder | lawful basis e direitos; TOKEN_VAZIO |
| P1-G | Titularidade | direitos/ligações AI + terceiros tratados abstratamente | matriz por ativo/autor/versão/license/consent | clearance explícito; TOKEN_VAZIO |
| P1-H | Entidade/operador | identidade societária e eventual registro religioso ausentes dos artefatos checados | ficha factual segura com documentação legal sob revisão humana | registro, capacidade, jurisdição; TOKEN_VAZIO |
| P1-I | Serviços e promessas | texto de trading/pesquisa/saúde pode sugerir aconselhamento ou valoração de resultados | classificar quais serviços de fato são oferecidos e revisar afirmações | evidência de uso/autorizações; TOKEN_VAZIO |
| P2-J | Jurisprudência | 24 países listados, 15 ainda como rotas | priorizar apenas país onde existe nexo operacional, validar julgados e sua atualidade | pin cite e contraditório em cada jurisdição |

Se qualquer risco for marcado alto sem atividade comprovada, registrar `CONDITIONAL / TOKEN_VAZIO` e não anunciar infração. Exposição estimada em dinheiro = `TOKEN_VAZIO` até dados factuais.

## 6. Plano de testes falsificadores para refatoração jurídica
- F01 apresentação distinguir natureza espiritual, pesquisa, software e eventual organização formal.
- F02 pessoa ateia/outra fé pode acessar documentação e discordar sem exclusão/retaliação.
- F03 cada alegação forte tem fonte, data, nível de teste e limitação; nenhum selo substitui prova de autoria.
- F04 `LICENSE_POLICY` e licenças de terceiros não mudam por harmonização visual.
- F05 24 países no índice NÃO são interpretados como 24 pareceres jurídicos.
- F06 teto legal nunca aparece como multa automaticamente aplicada, sanção penal jamais atribuída a alguém sem processo.
- F07 dispositivo de privacidade atende retificação/eliminação legal, ainda que hash/receipt seja append-only.
- F08 se há acesso provável por menores, ECA Digital/idade/risco são examinados antes de promoção.
- F09 serviço de UGC? checar STF Tema 987/533 2026, notificação, tempo razoável e falha sistêmica.
- F10 reclamações de pessoas afetadas com avaliação individual, recurso e não coerção.
- F11 licença de software por ativo continua `TOKEN_VAZIO / DECISION_REQUIRED` se não decidida.
- F12 branch principal sem proteção => nenhuma afirmação `SECURE_GOVERNANCE_PASS`.
- F13 fonte EU/US/UK só se aplica após `GEO_GATE` fundamentado; jurisprudência estrangeira é persuasiva, não vinculante no Brasil.
- F14 sem prova de pessoa jurídica/registro não alegar entidade religiosa oficial, charity, imunidade tributária ou incentivo fiscal.
- F15 não publicar material privado para demonstrar sanitização ou auditoria.
- F16 verificação de links, exact-HEAD CI, revisão humana independente e status do provider ANTES de merge.
- F17 denúncia de ameaça/abuso infantil pede procedimento legal proporcional, não vigilância massiva, retaliação, censura indiscriminada ou ocultamento de provas.
- F18 revisar controle aplicável após alteração normativa ou decisão judicial; nova linha successor sem apagar histórico.

## 7. Proposta de contrato legal para cada item do ATLAS
```yaml
legal_node_v4:
  claim_id: "TVARCS-LEGAL-ITEM-..."
  country: "BR|US|UK|EU|OTHER|TOKEN_VAZIO"
  subject: "expression|privacy|child|consumer|copyright|licensing|sanctions|other"
  operator_legal_identity: "TOKEN_VAZIO"
  actual_activity: "TOKEN_VAZIO"
  source_type: "STATUTE|DECISION|TREATY|GUIDANCE|PROJECT"
  source_url: "authoritative-url"
  source_date: "YYYY-MM-DD"
  operative_period: "TOKEN_VAZIO"
  elements_for_application: []
  contrary_authorities: []
  exposure_kind: "ADMIN|CIVIL|CRIMINAL|FINANCIAL_SANCTIONS|NONE|TOKEN_VAZIO"
  max_penalty_if_applicable: "NOT_AUTO_APPLIED"
  control_owner: "TOKEN_VAZIO"
  implementation_receipt: "TOKEN_VAZIO"
  counsel_approval: "NOT_DONE"
  claim_allowed: false
  rollback: "close draft PR / successor"
```

## 8. Fontes oficiais verificadas (consultas 2026-10-30; verificação local antes de uso jurídico)
- Constituição BR: https://www4.planalto.gov.br/legislacao/legis-federal/constituicao
- LGPD art.52: https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-republicacao-156210-pl.html
- ANPD dosimetria Res.4/2023: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-regulamento-de-dosimetria
- ECA Digital vigência e orientações: https://www.gov.br/anpd/pt-br/assuntos/eca-digital/
- ECA Digital art.35: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm
- Marco Civil art.12: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm
- STF Temas 987/533 e revisão 2026: https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=5160549&numeroTema=987 ; https://noticias.stf.jus.br/postsnoticias/plataformas-terao-60-dias-para-implementar-medidas-estruturais-decide-stf/
- Direitos autorais arts.102–110: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm
- CDC art.56: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- Lei 7.716 art.20: https://www.planalto.gov.br/ccivil_03/leis/l7716.htm
- ICO UK GDPR teto: https://ico.org.uk/about-the-ico/our-information/policies-and-procedures/data-protection-fining-guidance/statutory-background/the-maximum-amount-of-a-fine-under-uk-gdpr-and-dpa-2018/
- UK OSA Schedule 13: https://www.legislation.gov.uk/ukpga/2023/50/schedule/13
- FTC COPPA: https://search.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- OFAC (sanções econômicas): https://ofac.treasury.gov/recent-actions/20190502_33
- OFSI (sanções econômicas): https://www.gov.uk/government/publications/financial-sanctions-enforcement-and-monetary-penalties-guidance/financial-sanctions-enforcement-and-monetary-penalties-guidance
- UE DSA enforcement: https://digital-strategy.ec.europa.eu/en/policies/dsa-enforcement
- WIPO Berna: https://www.wipo.int/en/web/treaties/ip/berne

## 9. Governança da execução
SOURCE = arquivos reais GitHub + lei/jurisprudência primária; ARTIFACT = este estudo documental; EXECUTION = escrita em branch isolada, nenhuma refatoração da apresentação implantada; EVIDENCE = blob Git e readback do PR; CLAIM = `false` até revisão e implantação verificada. Não abrir, copiar nem listar segredos históricos. Não alterar proteção do provedor sem autoridade administrativa e readback.
Próxima ação de alto valor: (1) verificar segmentação dos serviços e segurança infantis; (2) revisar tutela de dados/direitos e segredos; (3) abrir PR mínimo e distinto para apenas a apresentação após revisão. Reverter este estudo = fechar PR draft; nenhum auto-merge.
R3 = <F_ok: comparativo/revisão/risco/sanções documentados; F_gap: factos operacionais, jurisdição, proteção provider, revisão independente; F_next: medir produto/fluxos e autorização dos controles, somente então implementar>.
