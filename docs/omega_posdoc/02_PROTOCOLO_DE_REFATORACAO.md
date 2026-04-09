# Protocolo de Refatoração dos MD recentes

## 1) Escopo

Refatoração dos 16 arquivos recentes com foco em:

- formalidade pós-doc;
- precisão terminológica;
- redução de ambiguidade;
- consistência entre notação e bibliografia.

## 2) Estratégia em 4 fases

### Fase 1 — Saneamento editorial
- Remover redundâncias e trechos meramente conversacionais.
- Uniformizar língua, notação e estilo (voz acadêmica).
- Corrigir títulos para padrão técnico.

### Fase 2 — Estrutura científica
- Converter blocos argumentativos em blocos formais (`definição`, `proposição`, `método`, `resultado`).
- Inserir hipóteses explícitas (H1, H2, H3...).
- Delimitar escopo de validade em cada afirmação.

### Fase 3 — Referenciação e evidência
- Associar cada afirmação central a DOI/preprint/livro técnico.
- Distinguir:
  - evidência de literatura;
  - evidência de simulação;
  - evidência experimental direta.

### Fase 4 — Integração documental
- Criar backlinks entre arquivos por dependência lógica.
- Publicar changelog técnico por versão.
- Consolidar índice e matriz de rastreabilidade.

## 3) Regras de qualidade (obrigatórias)

1. Não declarar validação universal sem condições de teste.
2. Não usar linguagem conclusiva sem métrica associada.
3. Toda hipótese deve ter potencial de refutação explícito.
4. Toda previsão deve definir unidade, escala e tolerância.
5. Toda tabela deve informar fonte e data.

## 4) Matriz de priorização (ordem de refatoração)

1. `Teoremas.md` e `Teoremas2.md` (núcleo formal).
2. `Rafael teoria matemate partícula a matéria.md` (núcleo de integração).
3. `Base academicamente.md` e `Mapate.md` (governança do corpus).
4. `Novo novo.md` (ponte com literatura recente).
5. Documentos de expansão (`Parte*.md`, `Oega3.md`, `Tem ra.md`, `Radoispontozero.md`).

## 5) Definição de pronto (Definition of Done)

Um documento refatorado está pronto quando:

- possui metadados completos;
- possui estrutura formal mínima (definição → hipótese → método → critério de teste);
- possui bibliografia verificável;
- possui seção de limitações e riscos epistemológicos;
- possui versão e histórico de mudanças.
