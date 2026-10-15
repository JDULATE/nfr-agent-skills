# Threat-path practices

Select controls for an explicit adversary-to-asset path inside the authorized scope.

## Asset, capability, and trust crossing

- Use when a feature accepts data or requests from a less-trusted actor/component.
- Trade-off: a model broad enough to include every hypothetical actor becomes
  unreviewable; a narrow model must disclose capabilities and effects it excludes.
- Verify: trace the exact attacker-controlled values and preconditions through
  the boundary to a protected action; do not infer authority from valid syntax.

## Control placement and bypass review

- Use when an interface or normal route is the only apparent gate.
- Trade-off: central controls can reduce duplicate policy logic but may be bypassed
  by alternate workers/imports or fail differently when dependencies are unavailable.
- Verify: inspect all modeled entrypoints to the same effect, exercise the confirmed
  control-failure behavior, and retain actual bypass effects as counterexamples.

## Prevention versus observation

- Use when logging, alerts, or retained evidence are proposed as mitigation.
- Trade-off: detection supports a response but may occur after the protected effect;
  prevention and detection need distinct evidence and residual exposure statements.
- Verify: trace event, effect, log, and responder-visible observation separately;
  an observed alert cannot prove the action was denied before effect.

## Valid-use and residual conditions

- Use when a candidate control blocks misuse by restricting legitimate behavior too.
- Trade-off: narrower capability can be acceptable only through a confirmed product
  decision; switching the feature off is not automatically a preserved security requirement.
- Verify: run legitimate and misuse controls, record unmet use constraints, and
  assign residual paths/assumptions instead of hiding them in an aggregate green verdict.

## Tool findings and path evidence

- Use when a scan or dependency inventory supplies leads for review.
- Trade-off: findings can miss modeled paths or lack relevant preconditions;
  neither a long findings list nor an empty one decides exploitability or security.
- Verify: connect each investigated item to source, capability, precondition, and
  actual effect evidence; retain unresolved items without inventing a successful attack.
