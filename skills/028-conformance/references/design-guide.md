# Selected-rule checking decisions

Use supplied local rules here; do not invent external obligations.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Event payload omits a field the selected schema requires | Add a schema gate for the actual required-field predicate | Previously tolerated artifacts may now fail | Submit the missing-field and complete-field fixtures |
| Event name violates the chosen naming rule | Implement the supplied lexical predicate with rule-specific output | Naming exceptions require explicit treatment | Exercise accepted and violating names at the predicate boundary |
| A checker loads a different rule revision than the report states | Bind the result to the loaded rule identity and revision | Reports must carry revision metadata | Substitute a changed rule fixture and inspect the reported identity |
| Some applicable rules have no implemented check | Enumerate rule results and retain unknown/manual status | No single unqualified green result | Remove a check and verify that the omitted rule appears unknown |
| An exception is approved for a violating artifact | Record exempted status with unmet-rule evidence and authority | More result states for consumers | Check that the same violation outside exception scope still fails |

## Local predicate sketch

Illustrative pseudocode; these local names are not standard identifiers.

```text
check_event(event):
    findings = []
    if not event.contains("kind") or not is_text(event.kind):
        findings.append({rule: "required-kind", path: "kind"})
    if event.contains("kind") and not lower_snake_name(event.kind):
        findings.append({rule: "kind-spelling", path: "kind"})
    return findings
```

Use lower_snake_name only when the supplied naming rule actually selects it.
The fixture defines its accepted characters and separator behavior explicitly.
The spelling predicate returns false for nontext values.
Do not add a preferred style as an unstated obligation.

## Scope of results

The sketch checks two predicates only.
Its empty finding list says nothing about additional selected rules.
Combine it with a rule-to-check inventory before producing a whole-scope result.
