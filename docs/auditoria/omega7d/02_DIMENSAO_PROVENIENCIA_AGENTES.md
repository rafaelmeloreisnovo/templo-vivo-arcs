# Ω7D — Dimensão 2: Proveniência, autoria e agentes

## Objeto
Separar criação intelectual, operação da plataforma e participação de agentes humanos/IA.

## Invariante
`entidade -> atividade -> agente -> transformação -> entidade derivada`

## Papéis que nunca devem ser fundidos
- autor intelectual declarado;
- autor Git;
- committer técnico (`web-flow`, bot ou usuário);
- agente IA (`Copilot`, `Codex`, outro);
- plataforma hospedeira;
- revisor/maintainer;
- titular jurídico.

## Regra de atribuição
`AGENT_IDENTITY` só pode ser preenchido por evidência explícita: usuário/bot, branch, task ID, PR body, commit metadata, log ou registro de conversa que vincule o agente ao ato.

Estilo textual, semelhança linguística ou cronologia compatível não bastam.

## Vetor de proveniência
`P = (source_id, path, blob_sha, commit_sha, author, committer, agent, activity, derived_from, claim_status)`

## Heurísticas
- `web-flow` prova infraestrutura de commit, não autoria intelectual.
- PR de agente com `changed_files=0` prova participação/evento, não incorporação material.
- Material anterior ao agente posterior não pode ser retroativamente atribuído ao agente sem elo documental.
- Toda derivação deve apontar para fonte anterior quando identificável.

## TOKEN_VAZIO
Agente desconhecido permanece `TOKEN_VAZIO`; nunca preencher por plausibilidade.

## Saída
`ARTIFACT -> SOURCE -> ACTIVITY -> AGENT -> DERIVED_ARTIFACT -> CONFIDENCE`
