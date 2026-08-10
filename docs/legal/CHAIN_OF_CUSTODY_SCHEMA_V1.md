# Chain of Custody Schema V1

Para cada evidência relevante, registrar ao menos:

```text
record_id
asset_id
repository
path
blob_sha
commit_sha
parent_sha
author_identity_observed
committer_identity_observed
author_time
committer_time
ref_or_branch
pr_number_or_null
tag_or_null
release_or_null
external_source_pointer_or_null
external_source_hash_or_null
agent_identity_or_null
agent_event_pointer_or_null
tree_delta_summary
execution_status
execution_environment_or_null
receipt_path_or_null
receipt_sha256_or_null
claim_status
limitations[]
next_gate
```

## Estados permitidos

- `OBSERVED`
- `HASH_VERIFIED`
- `HISTORY_LINKED`
- `AGENT_EVENT_LINKED`
- `MECHANICS_REPRODUCED`
- `HISTORICALLY_REPRODUCED`
- `INDEPENDENTLY_VALIDATED`

Estados não podem ser promovidos sem evidência adicional preservada.

## Invariante

`SOURCE -> CONTENT_HASH -> GIT_OBJECT -> HISTORY_EVENT -> EXECUTION_RECEIPT -> CLAIM`

Cada registro deve permitir voltar do claim ao objeto original sem depender exclusivamente de narrativa humana.