# Matriz de Padrões Contratuais — Microsoft / Oracle / Apple / Google / IBM × RAFCODE-Φ

**Objetivo:** comparar estruturas, não copiar textos nem alegar equivalência de poder econômico ou validação externa.

## 1. Padrões observáveis

| Organização | Padrão público | Lição estrutural para RAFCODE-Φ |
|---|---|---|
| Microsoft | Product Terms universais + termos por produto + DPA + SLA + programas comerciais | separar licença-base, produto, dados, SLA e canal comercial |
| Oracle | Master Agreement/Cloud Agreement + Order Document + Service Policies; licenças de desenvolvimento podem excluir produção comercial | usar Master Terms + Order Form + grants explícitos para dev/test/prod/OEM |
| Apple | Developer Program License + Paid Applications schedules + guidelines + termos de SDK/App Store | separar plataforma, distribuição, monetização, marca e guidelines técnicos |
| Google | API Terms + termos específicos + deveres sobre usuários finais, lei, privacidade e credenciais | tratar APIs, credenciais, end users, privacidade e limites técnicos separadamente |
| IBM | IPLA/base agreement + License Information específica + lifecycle/support | usar acordo-base + ficha de licença por produto/versão + lifecycle e suporte |

## 2. Invariante empresarial

A convergência entre essas empresas não é uma cláusula única. É a arquitetura:

`MASTER/BASE TERMS -> PRODUCT-SPECIFIC TERMS -> ORDER/ENTITLEMENT -> DATA/SECURITY -> SUPPORT/SLA -> POLICIES -> LIFECYCLE`.

A família RAFCODE-Φ segue a mesma forma abstrata, com conteúdo próprio:

`LEGAL_ARCHITECTURE -> SOURCE_AVAILABLE_LICENSE -> COMMERCIAL_ADDENDUM -> DATA_AI_SECURITY_ADDENDUM -> ORDER_FORM -> SECURITY/TRADEMARK/CLA -> VERSION_RECEIPTS`.

## 3. Simetria, não retaliação

O princípio adotado é:

> Uma restrição contratual deve ser suficientemente clara e proporcional para que o próprio titular pudesse aceitá-la se estivesse do outro lado da relação.

Isso evita cláusulas puramente punitivas e melhora previsibilidade.

## 4. Jurisprudência e doutrina úteis — Brasil

### 4.1 Software e contrafação

O STJ, no REsp 1.016.087/RS, envolvendo Microsoft, reconheceu tutela indenizatória por violação de direitos sobre software e destacou que a indenização deve observar parâmetros de razoabilidade, desestímulo à prática ofensiva e vedação ao enriquecimento sem causa.

**Uso no contrato:** remédios proporcionais; evitar multas automáticas ilimitadas sem base jurídica ou econômica.

### 4.2 Violação de cláusula de licença

Em decisão divulgada pelo STJ em 2026, controvérsia sobre violação de cláusula de contrato de software foi tratada como responsabilidade de origem contratual para fins prescricionais, com aplicação do prazo geral de dez anos na situação julgada.

**Uso no contrato:** separar claramente responsabilidade contratual de alegações extracontratuais/autoriais.

### 4.3 Licenciamento e ISS

No Tema 590, o STF assentou a incidência de ISS no licenciamento/cessão de direito de uso de software personalizado.

**Uso empresarial:** contratos comerciais de software têm também consequências tributárias; licença não é apenas documento de PI.

## 5. Referência comparada — Google v. Oracle (EUA)

A Suprema Corte dos EUA decidiu em 2021, no caso Google LLC v. Oracle America, que o uso específico das declarações de APIs Java analisado no caso constituía fair use.

**Limite:** esse precedente não é lei brasileira nem significa que toda API é livre para qualquer uso. Serve como advertência contra redações que tentem transformar interface, ideia ou funcionalidade abstrata em monopólio contratual universal sem considerar exceções legais, interoperabilidade e contexto.

## 6. Cláusulas que grandes estruturas costumam separar

- ownership;
- license grant;
- field/metric of use;
- restrictions;
- third-party components;
- privacy/data processing;
- security;
- confidentiality;
- audit/compliance;
- support/SLA;
- warranties/disclaimers;
- liability/indemnity;
- termination;
- governing law/venue;
- export/sanctions;
- assignment;
- lifecycle/end-of-support;
- product-specific notices.

## 7. O que RAFCODE-Φ acrescenta como diferencial documental

A proposta não é ser “mais legal que Microsoft”. O diferencial pretendido é integrar ao mesmo contrato uma trilha técnica de:

`artifact -> hash -> commit -> provenance -> agent -> capability -> claim gate -> legal entitlement`.

Essa integração pode ser mais adequada ao corpus RAFAELIA porque a obra inclui documentos históricos, agentes de IA, commits, POCs e dados que precisam ser distinguidos juridicamente.

## 8. Regra de não exagero

Nenhum padrão corporativo ou precedente citado:

- valida cientificamente RAFAELIA;
- prova novidade mundial;
- cria direito supralegal;
- permite ignorar direitos do consumidor, LGPD, concorrência ou exceções legais;
- transforma manifesto em contrato sem aceite.

A força vem de **clareza + prova + aceite + proporcionalidade + remédio juridicamente permitido**.