# Resource-accounting practices

Choose a correct useful output and one resource unit before comparing implementations.

## Functional-unit and resource ledger

- Use when lower consumption might reflect less completed or lower-quality work.
- Trade-off: validating useful results adds accounting work but keeps reduced
  service from masquerading as a resource-per-result improvement.
- Verify: retain correct completed outputs, attempts, failures and resource totals;
  compute the ratio from the agreed useful-result denominator.

## Shared, idle and background allocation

- Use when devices/processes serve several tasks or do work outside the request timer.
- Trade-off: allocation is a modeling choice; excluding shared or idle consumption
  may answer a local question while leaving whole-task resource cost unmeasured.
- Verify: state the boundary and allocation rule, inspect background/retry work,
  and label unobserved consumption rather than silently assigning it no cost.

## Reuse and batching comparison

- Use when repeated computation or transfers suggest cache/reuse/batch candidates.
- Trade-off: fill, invalidation, retained state and delayed completion can move
  resource costs or affect required results; reuse is not automatically a saving.
- Verify: compare the declared warm/cold mix, useful outputs, foreground/background
  resource work and required service constraints over the same accounting horizon.

## Resource dimensions and displacement

- Use when a candidate trades CPU for storage, transfers, another process or parallel work.
- Trade-off: reducing the chosen ratio may be useful while worsening another
  required dimension; resource units cannot be combined into an unexplained score.
- Verify: retain each dimension and displaced work separately, with device/config
  conditions. Do not infer energy, emissions or money without their additional evidence.
