# Livro Vivo — Rotas Humanas Lúdicas — V1

**natureza:** parábolas didáticas contemporâneas  
**estado:** PARABOLA_DIDATICA  
**claim_allowed:** false

Estas narrativas ajudam a explicar governança, dignidade, liberdade, cuidado, proteção infantil, rastreabilidade e rollback. Não são citações históricas, escrituras, normas jurídicas nem evidência técnica. Tradições humanas aparecem apenas como inspiração hermenêutica; quando uma regra real depender de lei, tratado ou standard, a rota deve apontar para a fonte oficial/versionada e para a evidência aplicável.

## O Mestre das Sete Lanternas

Um mestre tinha sete lanternas. O discípulo perguntou qual mostrava o caminho verdadeiro.

O mestre acendeu todas. Uma mostrava as pedras, outra as árvores, outra os rostos, outra as pegadas, outra o precipício, outra a ponte e a última a própria mão do discípulo.

— Qual é a correta?

— Aquela que mostra o que as outras não conseguem ver.

**Rota:** pluralismo → múltiplas fontes → evidência específica → decisão humana.

## A Árvore que Guardava os Caminhos

Uma criança perguntou à anciã a quem pertencia uma árvore.

— Aos que vieram antes de nós e aos que ainda não nasceram.

— Então ela não pertence a ninguém?

— Agora começaste a entender.

Antes de cortar um galho, perguntavam: **o que receberá quem vier depois de mim?**

**Rota:** decisão presente → impacto → reversibilidade → gerações futuras.

## O Pedreiro e a Pedra Imperfeita

Um aprendiz disse que uma pedra torta estava errada. O mestre virou a pedra, e ela encaixou no arco.

— Há diferença entre algo não servir e nós ainda não sabermos onde serve.

O aprendiz passou a marcar as pedras como USAR, REPARAR ou AINDA_NAO_SEI.

**Invariante:** TOKEN_VAZIO != 0.

## O Mestre do Rio Reversível

Um governante pediu uma barragem impossível de desfazer.

— Então não me pedes engenharia. Pedes uma aposta.

O mestre construiu primeiro uma pequena comporta, mediu, abriu, fechou e mediu de novo.

— Uma mudança que não sabemos desfazer ainda não conhecemos completamente.

**Rota:** before_state → mudança mínima → after_state → replay → rollback_test.

## O Cartógrafo que Não Mandava

Os mapas de um cartógrafo diziam: este caminho é curto; este é seguro na chuva; este atravessa a montanha; aqui ainda não sabemos.

O rei perguntou por que o mapa não mandava qual estrada seguir.

— Para que quem caminhe continue sendo dono dos próprios pés.

**Invariante:** informar melhor != decidir pelo outro.

## A Mestra dos Três Espelhos

Uma mestra possuía três espelhos.

CORPO perguntava: **o que fizeste?**  
ALMA perguntava: **por que fizeste e de onde veio?**  
ESPÍRITO perguntava: **quem pode ser afetado e como preservar dignidade, liberdade e reversibilidade?**

**Rota:** execução → proveniência/contrato → impacto/ética → evidence gate.

## O Guardião da Porta Pequena

Na cidade havia muitos portões, mas o mais vigiado era uma pequena porta.

— Por que justamente esta?

— Porque é por aqui que passam as crianças.

O guardião não exigia que as crianças fossem mais fortes; exigia que a porta fosse mais segura.

**Rota:** menor poder → maior dever de cuidado → child-safety fail-closed.

## O Jardim sem Bandeiras

Uma placa dizia: “Aqui cresce apenas a planta correta.” Nada floresceu.

Depois escreveram: “Aqui cuidamos de cada planta segundo aquilo de que ela necessita.”

O jardim floresceu não porque tudo ficou igual, mas porque diferenças puderam coexistir sem destruir umas às outras.

**Rota:** pluralismo → proporcionalidade → dignidade → coexistência.

## O Mestre que Não Entregava Respostas

— Quero construir uma máquina que saiba o melhor caminho para cada pessoa.

— Constrói antes uma máquina que mostre caminhos sem roubar os pés de ninguém.

— Como saberei se fiz certo?

— Quando ela souber dizer: **isto eu sei; isto eu não sei; e a escolha continua sendo sua.**

**Invariante:** conhecimento + compaixão + liberdade + responsabilidade.

## Fronteira operacional

- parábola orienta compreensão;
- fonte e evidência sustentam afirmações;
- norma só entra com identidade, versão, escopo e aplicabilidade;
- divergência cultural não autoriza desrespeito;
- proteção não deve virar coerção indevida;
- criança e pessoa vulnerável recebem maior dever de cuidado;
- correção cria sucessor e preserva predecessor;
- replay e rollback fazem parte da responsabilidade de engenharia.

```yaml
route_id: LIVRO-VIVO-ROTAS-HUMANAS-V1
source_kind: contemporary_didactic_parables
epistemic_class: PARABOLA_DIDATICA
historical_quote: false
normative_authority: false
technical_evidence: false
child_safety_priority: true
human_autonomy_priority: true
cultural_pluralism: true
replay: follow_mapped_gate_to_source_and_evidence
rollback: supersede_without_rewriting_history
claim_allowed: false
```
