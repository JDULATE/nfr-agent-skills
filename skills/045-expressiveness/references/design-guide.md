# Representation-capability decisions

Use concrete contrasting intentions before expanding a notation.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Owner-only and everyone rules share the same stored object | Add a subject relation tag with explicit evaluation | Existing readers need defined handling for new tags | Round-trip both forms and evaluate owner/non-owner inputs |
| Explicit denial cannot be distinguished from no matching rule | Add separate deny and absent representations with agreed combination semantics | More states for policy authors and consumers | Evaluate denial and absence under a permissive inherited rule |
| Parser stores a construct but the interpreter discards it | Carry the construct into the semantic evaluation path | Interpreter complexity and test surface grow | Use a distinguishing input where ignoring the construct changes the result |
| Unsupported tags silently become the broadest permission | Refuse unsupported forms rather than guessing their meaning | Some inputs become explicit errors | Parse an unknown tag and inspect refusal before evaluation |

## Subject restriction sketch

Illustrative pseudocode for a local policy fixture, not an authorization standard.

```text
evaluate(rule, actor, resource):
    if rule.kind == "deny":
        return "deny"
    if rule.kind == "absent":
        return "no-decision"
    if rule.kind == "allow" and rule.subject == "everyone":
        return "allow"
    if rule.kind == "allow" and rule.subject == "owner":
        return "allow" if actor == resource.owner else "no-decision"
    return "unsupported-rule"
```

A combining policy must define how no-decision and deny differ.
Do not present this sketch as a complete access-control mechanism.
Security enforcement requires its own scoped controls and evidence.

## Migration boundary

If old forms mean allow-everyone, preserve or explicitly migrate that meaning.
Do not make an old absence suddenly mean denial without stakeholder agreement.
