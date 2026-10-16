# Independent ledger reconstruction

This is an illustrative pair of executor attempts, not an empirical reproduction study.
All ledger values and proposed contracts are illustrative examples;
confirm with the user/stakeholder before using them as project acceptance values.

## Filled handoff record

| Field | Fixture value |
| --- | --- |
| Procedure revision | ledger-sum fern |
| Original executor | Aster, original workspace |
| Independent executor | Bramble, clean workspace without Aster's files |
| Fixture | charge 2 credits; adjustment -1 credit; charge 3 credits |
| Intended semantics | include adjustment rows |
| Original hidden setting | Aster environment sets include_adjustments=true |
| Fresh default | include_adjustments=false |
| Other dependencies | integer arithmetic only; no clock, network, random source, or persisted rows |
| Required capability | read the supplied rows and apply the declared row-selection rule |
| Allowed environment difference | executor and workspace may differ |
| Comparison | exact total in credits |
| Carried state | new output plus effective setup record for each attempt |
| Assistance | none in the constructed before or after attempt |

## Failing handoff before remediation

The initial package contains rows and a procedure that uses its environment's default.
Aster includes the adjustment and produces 2 - 1 + 3 = 4 credits.
Bramble's clean default excludes it and produces 2 + 3 = 5 credits.

The same visible rows are not the same complete semantic input.
The fixture supports the omitted-setting explanation because setting that input
alone changes the selected row population.

## Remediation

Add the semantic setting to the handoff and require it explicitly:
```text
procedure = ledger-sum fern
rows = [(charge, 2), (adjustment, -1), (charge, 3)]
include_adjustments = true
output_unit = credits
comparison = exact total
```

Bramble reconstructs from that package in the clean workspace.
The newly computed output is:
```text
selected_rows = all three declared rows
effective_include_adjustments = true
total = 4 credits
private_author_resources = none
assistance = none
```

Aster's baseline and Bramble's independent result now satisfy the same comparison.
These are illustrative fixture results; confirm with the user/stakeholder before
adopting any number as an acceptance value.

## Failing package probe

Remove include_adjustments from the revised package.
Setup must report a missing semantic input rather than fall back to a private default.
If Bramble receives only a file containing total=4, that is a transferred answer,
not evidence of reconstructed computation.

## Requirement example and limits

The ledger handoff shall let an independent executor compute the exact declared
total from supplied rows and an explicit adjustment policy, without private settings.

This fixture supports only the declared integer procedure and input package.
It does not establish compatibility with every platform or an unassisted real
engineer's outcome. No actual independent executor was engaged in authoring it.
