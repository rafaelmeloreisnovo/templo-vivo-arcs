# TEMPLO VIVO ARCΣ — V5 | Matriz jurídico-evidencial verificável

**2026-10-30 · Status:** IMPLEMENTED_UNTESTED_CI (até existir execução exata) · PROMOTION=HOLD · claim_allowed=false.  
**Autoridade de execução:** repositório produtor `rafaelmeloreisnovo/templo-vivo-arcs`; não uma entidade jurídica formal comprovada.  
**Âncoras históricas:** PR#44 (oito países), #45 (EUA/Reino Unido), #46 (24 jurisdições), #47 (L9/sanções) — todos MERGED no HEAD de partida `67379c81c8c1dfdcbf74beece46502a929ecda19`. Documentos com marca `DRAFT` são *históricos*; merge NÃO comprova revisão jurídica.  
**Invariantes:** `SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM`; `TOKEN_VAZIO ≠ 0`; `PASS_SCOPED ≠ COMPLIANCE`.

## 1. O que foi efetivamente implantado nesta branch isolada
- `evidence_register.json`: **13 casos** Brasil/EUA/Reino Unido, com autoridade, data, fonte, questão central, interpretação estreita, limite contrário e condição de aplicação; **5 regimes de sanções**, todos condicionais e **nenhuma sanção aplicada**.
- `check_evidence.py`: validador determinístico Python stdlib. Falha se houver alegação de validade automática, multas aplicadas, evidência inventada, duplicidade, fonte fora da allowlist, lacuna convertida em `0`, ausência de argumento adverso, revisão jurídica presumida ou arquivo modificado fora do escopo da V5.
- `test_check_evidence.py`: **15 testes**, com casos positivos e controles adversariais, executáveis pelo próprio Python.
- `.github/workflows/tvarcs-legal-evidence-v5.yml`: PR-only, permissões `contents:read`, escopo de caminhos restrito, `checkout` sem credenciais persistentes, sem publicação/merge/secret scanning remoto; validador + testes + verificação das alterações em relação ao base SHA. **A existência do YAML não prova execução.**

## 2. Como testar de maneira reprodutível
```sh
python3 governance/legal/v5/check_evidence.py
python3 -m unittest discover -s governance/legal/v5 -p 'test_check_evidence.py' -v
```
Resultado admitido: `PASS_SCOPED_RESEARCH_ONLY` com SHA-256 do JSON, número de casos/sanções e contagem de lacunas. Nunca `LEGAL_PASS`, `SIX_SIGMA` ou `FULL_COMPLIANCE`. Erro → saída diferente de zero, `FAIL_CLOSED`. CI só passa a contar após identificador de execução, conclusão, status e HEAD verificados via GitHub. Revisão humana ainda obrigatória.

## 3. Casos estruturantes, inclusive os contrários
| Âncora | Questão jurídica e uso restrito | Falsificador essencial |
|---|---|---|
| STF Temas 987/533 (2026) | Responsabilidade de certos provedores por conteúdo de terceiros, atualização do MCI | O Templo efetivamente hospeda UGC e qual modalidade? Texto consolidado e deveres concretos verificados? |
| STF ADI 4439 (2017) | Ensino religioso confessional facultativo em escolas públicas | Não confundir com credenciamento do Templo ou obrigatoriedade de adesão |
| STF RE 494601 (2019) | Liberdade de culto no contexto de lei gaúcha sobre rito | Não converter em isenção geral de outras normas |
| STF ADPF 130 (2009) | Liberdade de imprensa; reparação posterior e direitos da personalidade | Diferenciar publicação e violação de imagem/honra |
| STJ Súmula 403 (2009) | Imagem usada sem autorização para fins econômicos/comerciais | STJ não emitiu “súmula vinculante do STF”; verificar aplicação aos fatos |
| US *Lukumi* (1993) vs *Smith* (1990) | Tratamento estatal discriminatório vs leis neutras e gerais | Controle estatal provado? Norma geral? Exceções específicas? |
| US *Moody* (2024) | Curadoria expressiva em plataforma; julgamento remeteu impugnações | Jamais declarar vitória irrestrita da plataforma |
| US *Braswell* (1988) | Limites do privilégio contra autoincriminação de custodiantes corporativos | Não alegar imunidade jurídica da organização |
| UK *Hodkin* (2013) | Conceito de religião em regime estatutário específico | Não registrar o Templo apenas por citação |
| UK *Shergill* (2014) | Questões religiosas vs direitos civis, propriedade e trusts | Não impedir apreciação de litígios civis por invocar fé |
| UK *Bank Mellat* (2013) | Proporcionalidade de medida estatal | Não aplicar automaticamente a toda decisão privada |

**Nota de autoridade:** STF, STJ, SCOTUS, UKSC e ECtHR têm forças jurídicas diferentes. Um precedente estrangeiro é, em regra, argumento comparado, não norma vinculante no Brasil. A lista não certifica exame do inteiro teor, pinpoints, superação posterior ou aderência a um litígio concreto; os campos permanecem `TOKEN_VAZIO`.

## 4. Sanções: dois polos, não ameaças
A) **Dever do operador:** LGPD art.52 (dados pessoais), ECA Digital art.35 (serviços abrangidos), Marco Civil art.12 (privacidade/dados, hipóteses dos arts.10/11); UK Online Safety Act Sch.13 e UK GDPR em caso de alcance territorial/material.  
B) **Direito de terceiros e autores:** violação de direitos autorais, imagem, contratos, publicidade e direitos fundamentais só gera tutela/sanção na forma de legislação, provas e procedimento próprios. *Um aviso no README não cria pena, multa privada ou tribunal universal.*

O teto é limite legal condicionado a tipo de infração, faturamento ou regra alternativa; **exposição financeira do Templo = `TOKEN_VAZIO_UNMEASURED`**. Distinga indenização civil, tutela inibitória, multa administrativa, responsabilidade penal pessoal e sanções econômicas OFAC/OFSI; não some tetos nem presuma infrações. Nunca divulgar credenciais/dados para demonstrar auditoria.

## 5. Lacunas operacionais: tipagem e rota sem invenção
| Campo | Estado | Ação autorizável após apuração |
|---|---|---|
| Identidade legal do operador | TOKEN_VAZIO_UNKNOWN | Comprovar entidade/CPF/CNPJ de maneira reservada; revisar representação sem publicar dados pessoais |
| Serviço real, público-alvo, moderação e UGC | TOKEN_VAZIO_UNKNOWN | Inventário por URL/app/feature, categorizar conteúdo próprio vs terceiros |
| Acesso provável por crianças/adolescentes | TOKEN_VAZIO_UNKNOWN | Avaliar critérios ECA Digital, medidas proporcionais e riscos reais |
| Tratamento de dados pessoais/religiosos | TOKEN_VAZIO_UNKNOWN | Fluxo minimizado, fundamento legal, retenção, privacidade e direitos de eliminação |
| Nexo territorial US/UK | TOKEN_VAZIO_UNKNOWN | Dados de negócio/usuários/servidores e aconselhamento local |
| Rotação da credencial histórica | TOKEN_VAZIO_UNKNOWN | Administrador verifica revogação sem revelar segredo |
| Revisão jurídica independente | TOKEN_VAZIO_UNKNOWN | Advogado competente registra parecer e escopo |
| Proteção de `main` | FAIL_OBSERVED | Admin autoriza regraset/required checks, verifica com readback |

**IMPORTANTE:** append-only de recibos não obriga retenção perpétua de dados pessoais. Retificação, exclusão e outros direitos legalmente aplicáveis exigem protocolo próprio.

## 6. Recibos, testes falsificadores e não-regressão
- **Sem alterar:** raiz `LICENSE`, `LICENSE_POLICY.md`, licença RAFCODE original, README legado, código Android/Flutter, dados privados, histórico e proteção administrativa do provedor.
- **Diferenças autorizadas nesta PR:** somente os arquivos explicitados no validador `ALLOWED_FILES`.
- **Falhas controladas:** multa indevidamente marcada aplicada, claim=true, fonte fictícia, duplicidade, dado desconhecido=0, tese sem limite contrário, caso indevidamente revisado, modificação de licença/README e falso PASS do provedor devem ser recusados.
- **Gates ainda externos:** testes completos do aplicativo e E2E, conselho jurídico, atualidade completa dos precedentes, maturidade técnica, controle de menores e provedor. `IMPLEMENTED_UNTESTED` permanece distinto de `PASS`.
- **Rollback:** fechar PR V5 sem merge. Após eventual merge, correção por commit sucessor, preservando histórico; nunca reescrever provas antigas.

## 7. Fontes oficiais principais / rotas
- STF Tema 987: https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=987
- STF ADI 4439: https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=4439
- STJ Súmula 403: https://scon.stj.jus.br/SCON/sumstj/doc.jsp?b=SUMU&i=1&l=10&livre=%22403%22+INPATH%28NUM%29&operador=AND&ordenacao=-%40NUM&p=false
- ECA Digital ANPD: https://www.gov.br/anpd/pt-br/assuntos/eca-digital/
- Lei 15.211/2025: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm
- LGPD art.52: https://legis.senado.gov.br/norma/27457334/publicacao/27459584
- US *Lukumi*: https://www.law.cornell.edu/supremecourt/text/508/520
- US *Smith*: https://www.law.cornell.edu/supremecourt/text/494/872
- US *Moody*: https://www.supremecourt.gov/docket/docketfiles/html/public/22-277.html
- UK *Hodkin*: https://www.supremecourt.uk/cases/uksc-2013-0030
- UK *Shergill*: https://www.supremecourt.uk/cases/uksc-2012-0234
- UK Online Safety sanctions: https://www.legislation.gov.uk/ukpga/2023/50/schedule/13/paragraph/4

**R3:** F_ok = documentação versionada + validador estático + testes adversariais e CI proposto; F_gap = execução real, fatos operacionais, revisão jurídica, proteção de branch; F_next = conferir exact-head tests, categorizar serviços reais e submeter parecer humano antes de qualquer promoção ou merge.
