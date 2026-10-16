# Dependency-organization decisions

Apply the repository's chosen role rules, not an assumed universal architecture.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Domain calculation imports a web-response formatter | Return a domain result and translate it in the web boundary | Boundary code gains translation responsibility | Inspect imports and execute the same request/result fixture |
| Infrastructure is imported directly by a role whose rule forbids it | Introduce a role-owned interface and wire the implementation at composition | More explicit assembly and interface maintenance | Compare dependency direction and inspect actual runtime wiring |
| A static cycle disappears but registration calls back across the forbidden edge | Include registered runtime calls in the organization check | Dynamic inspection requires bounded scenarios | Exercise the callback and record its source/target roles |
| Exceptions apply to an entire package instead of the approved edge | Bind the exception to source, target, edge type, and reason | Exceptions need updates after legitimate moves | Add a different forbidden edge and verify it is not exempt |

## Local organization sketch

Illustrative file roles and pseudocode, not a mandatory architecture pattern.

```text
domain/calculate:
    calculate(input) -> DomainResult
    // no dependency on web modules

web/handler:
    result = domain.calculate(request.input)
    return web.format_response(result)

web/format_response:
    format_response(DomainResult) -> WebResponse
```

Allowed role edges in this fixture: web->domain and web->web.
Forbidden: domain->web. These are selected local rules.
The graph check must inspect actual imports as well as the directory labels.

## Scope caution

Introducing an interface is appropriate only if its ownership preserves the chosen
direction. A new abstract class living in the forbidden role can retain the
same organizational violation.
Do not mistake a compliant graph for proof of behavior or separability.
