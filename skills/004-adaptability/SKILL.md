---
name: adaptability
description: >-
  Specifies accommodation of a named external environment change when users
  say "the partner feed changed", "support new operating conditions", or "keep
  this working after the environment changes". Accepts preserved required
  behavior across old and changed conditions. Not for choosing already
  supported task alternatives (see flexibility), moving execution platforms
  alone (see portability), or a configuration transition alone (see
  reconfigurability).
---
# Adaptability

## Definition and scope

Adaptability means accommodating a named external change while retaining required
behavior. Compare original and changed conditions; separate supported alternatives
(`flexibility`), execution-platform movement (`portability`), and applying a changed
operating arrangement (`reconfigurability`) under this repository's conventions.

## Use when / Don't use when

- Apply to a changed partner payload, external contract, or operating condition
  that threatens an existing required result.
- Route choosing already supported task routes to `flexibility`.
- Route the impact of one proposed adapter edit to `modifiability`; that impact
  does not establish that the environmental delta is actually accommodated.

## Workflow

1. Clarify: Read integration code, environment assumptions, deployment docs,
   partner examples, and consumer contracts before defining accommodation.
   If the external delta is unknown, then Ask the user for observable before/after
   conditions rather than guessing a vendor behavior or internal remedy.

2. Specify: Pair conditions with retained outputs, accepted differences, detection
   evidence, unsupported variants, and an integration owner.
   If the request is a practical fix, then propose this full adaptation record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Delta: reported condition reproduced from inspected old/new examples.
   Retained result: documented domain meaning and accepted rejection behavior.
   Example bound: 0 unexplained semantic differences on paired supported fixtures.
   Action: agreed adapter/mapping; unknown meanings remain unresolved.
   Support: old conditions retained only where still promised.
   Evidence: condition selection, paired outcomes, unsupported-condition counterexample.
   Status/owner: proposed bound and mappings; existing integration owner.
   ```

   Ask at most three questions: what changed outside; which outcomes must stay or
   may differ; and which variants, rollout constraints, or defaults need revision.
   Proceed to adapter design while unknown meanings remain open.
   If no formal target is given, then use the labeled proposal above and confirm
   with the user/stakeholder before accepting its fixture bound.

3. Design/Implement: Read [adaptation patterns](./references/design-patterns.md) when
   choosing a normalization boundary or an unsupported-condition response.
   If representations differ but meanings agree, then normalize at that boundary.
   If meanings differ, then obtain a mapping or accepted loss decision instead
   of carrying forward an old-looking but misleading value.

4. Verify: Replay old/new conditions through the actual integration and compare
   domain results, rejection behavior, and selection evidence.
   If only the replacement fixture passes, then replay the still-supported old
   condition before claiming accommodation across both environments.

5. Report: Return the external delta, accepted mappings, paired results, and
   conditions that remain unsupported or untested.
   If evidence came only from a simulation, then disclose that boundary rather
   than claiming verified behavior of the real partner or deployment.

## Specification patterns

- **Accommodation:** Under `{changed_condition}`, `{integration}` shall retain
  `{required_result}` within `{confirmed_difference_bound}`, verified by
  `{paired_environment_fixtures}` using `{approved_semantic_mapping}`.
- **Unknown condition:** For `{unrecognized_variant}`, the boundary shall perform
  `{approved_rejection_or_escalation}`, evidenced by `{negative_fixture}` instead
  of inventing `{missing_meaning}` from a convenient default.

Use the illustrative fixture target above only as a proposal;
confirm with the user/stakeholder. Ask the user which conditions remain supported.

## Rules of thumb

- Do name the external assumption an adapter removes; internal cleanup alone
  cannot demonstrate accommodation of the reported environmental delta.
- Do compare normalized meanings, not accepted payload shapes; parsing both
  variants with different downstream interpretations fails the retained-result claim.
- Do select variants from agreed evidence; guessing a condition from missing
  fields can disguise unsupported input as a successful adaptation.
- Do pair retained old conditions with the changed condition under the same domain
  obligation; a new-condition-only suite cannot show what adaptation preserved.
- Don't propagate vendor-shape branches into unrelated consumers; inspect the
  boundary output so the same external change cannot acquire conflicting mappings.

## Verification

Use paired-environment integration tests, semantic mapping review, and adapter
selection inspection. Exercise changed representation, unknown meaning, and a
still-supported original condition. Inspect rejected variants and selection
mismatches; fewer rejections may reflect permissive guessing rather than adaptation.
Reconcile retained outcomes with source conditions and the accepted mapping.

## Done checklist

- [ ] Reproduce the external delta from inspected old/new evidence.
- [ ] Compare paired domain results under the approved mapping and bound.
- [ ] Exercise condition selection without guessed input meaning.
- [ ] Reject or escalate an unsupported variant under its accepted rule.
- [ ] Replay an original condition whose support continues.
- [ ] Inspect consumers for leaked environment-specific interpretations.

## Failure modes

- Calling an internal refactor adaptation without reproducing the external delta.
- Accepting a new field name with the wrong domain interpretation.
- Removing old-condition tests while that condition remains supported.
- Counting a guessed default as successful handling of an unknown environment.

## References

- Read [adaptation patterns](./references/design-patterns.md) when selecting boundary
  mappings, variant evidence, or unsupported-condition behavior.
- Read [feed example](./references/worked-example.md) when turning an external
  payload delta into paired outcomes and a scoped requirement.
