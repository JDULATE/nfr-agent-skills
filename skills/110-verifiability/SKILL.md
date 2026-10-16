---
name: verifiability
description: >-
  Designs acceptance evidence when asked "replace an unworkable check", "tie evidence to this claim", or "define the pass decision". Ask the user if acceptance method vs test seams or proof is unclear. Not for adding test seams (see testability), defining units (see measurability), or constructing proofs (see provability).
---

# Verifiability

## Definition and scope

Verifiability means a requirement has a feasible way to decide whether it is met.
Bind each claim to a method, observable evidence, and a decision rule; distinguish
creating control and observation seams (`testability`), defining the measure
(`measurability`), and constructing a formal argument (`provability`) from
designing that acceptance route.

## Use when / Don't use when

- Apply when a requirement sounds desirable but nobody can say what evidence settles it.
- Apply when an acceptance check assumes unavailable data, equipment, or execution access.
- Route a blocked test branch or missing observation seam to `testability`.
- Route an undefined metric or unit to `measurability`.
- Route proof construction for an agreed proposition to `provability`.
- Route an audience capability showing to `demonstrability` when acceptance is already settled.

## Workflow

1. Clarify: Read the requirement source, related code and interfaces, existing
   tests, evidence stores, and environment docs before inventing acceptance checks.
   Identify the claimed behavior, conditions, owner, and actual decision needed.
   If "prove it works" lacks a requirement boundary, then Ask the user whether
   the need is a demonstration, acceptance decision, or universal argument.

2. Specify: Write the claim, conditions, acceptance predicate, evidence method,
   environment, needed access, result artifact, reviewer, and inconclusive rule.
   If numeric targets are absent, then propose labeled illustrative defaults:
   use the requested behavior's explicit success/refusal predicates, select
   feasible evidence for those predicates, and leave an unstated deadline open;
   confirm with the user/stakeholder.
   Never turn the absence of a deadline into permission for arbitrary completion.

3. Design/Implement: Read [acceptance route design](./references/design-guide.md)
   when replacing an unexecutable check or a proxy acceptance criterion.
   If the required evidence is inaccessible, then identify an authorized alternative
   that establishes the same predicate or mark the acceptance route infeasible.
   If control or observation is missing, then specify the seam work for `testability`.
   If a proof is needed, then define its role and hand argument construction to
   `provability` rather than describing a planned argument as discharged.

4. Verify: Rehearse the acceptance procedure against a passing fixture, a failing
   fixture, and missing evidence. Confirm that its inputs are actually obtainable.
   If the procedure cannot distinguish those outcomes, then repair the predicate
   or evidence route before using it as an acceptance gate.
   Read [cancellation acceptance example](./references/worked-example.md) when
   keeping refusal semantics, dispatch evidence, and missing evidence distinct.

5. Report: Return the requirement-to-evidence record, feasibility result,
   exercised acceptance outcomes, and unresolved decisions.
   If the method exists but the product has not been checked, then report
   "acceptance route prepared" rather than "requirement met".

## Specification patterns

- **Acceptance route:** Requirement `{claim}` under `{conditions}` shall be
  decidable using `{method_and_obtainable_evidence}` in `{environment}`,
  with `{pass_fail_and_inconclusive_predicates}` applied by `{reviewer}`.
- **Evidence sufficiency:** Evidence `{artifact}` shall establish
  `{required_observable_or_argument}` for `{claim_scope}`; absent or
  out-of-scope evidence shall produce `{inconclusive_result}`.
- **Feasibility:** Before adopting `{acceptance_gate}`, demonstrate access to
  `{required_inputs_and_resources}` through `{rehearsal}`, documenting
  `{unavailable_parts_and_owners}`.

For a missing threshold, propose the illustrative behavior-predicate default
in Specify and confirm with the user/stakeholder. Ask the user for any deadline
that changes the required outcome; do not replace it with a guessed number.

## Rules of thumb

- Do reject a coverage percentage as the verdict for a behavior requirement;
  executed lines do not supply that requirement's accepted outcome.
- Do distinguish "the acceptance procedure can run" from "the requirement passed";
  preparing a method must not close the product's acceptance decision.
- Do keep an unavailable acceptance input as a feasibility gap; replacing a required
  consequence with an easier proxy changes the requirement's evidence contract.

## Verification

Use acceptance-procedure rehearsal, artifact inspection, integration testing,
and requirement review categories. Trace each required condition to the evidence
that supports its verdict and identify any unsupported qualifier.
Exercise a known failing result so the acceptance route cannot pass everything.
Remove the consequential artifact and verify an inconclusive rather than
successful verdict; no failing artifact found is not evidence of the required behavior.
Check access and resource assumptions with the intended reviewer.
Use an expected-result source independent of the implementation branch under review.
Retain raw observations, incomplete attempts, predeclared exclusions, and the
actual evidence scope. A procedure approved on a fixture still needs execution
against the intended product revision before reporting attainment.

## Done checklist

- [ ] Bind the acceptance decision to a specific requirement and revision.
- [ ] Define the required behavior and conditions without hidden target choices.
- [ ] Obtain the actual evidence inputs in the proposed environment.
- [ ] Identify who can execute and review the acceptance procedure.
- [ ] Distinguish a known passing result from a known failing result.
- [ ] Produce an inconclusive result when the decisive evidence is absent.
- [ ] Record unverified qualifiers, unavailable inputs, and method substitutions.
- [ ] Separate procedure feasibility from measured product attainment.

## Failure modes

- Approving a requirement because a test count or coverage score increased.
- Calling an unexecuted acceptance plan a successful product check.
- Replacing an inaccessible consequence with a convenient but insufficient proxy.
- Passing an acceptance attempt because its evidence collection silently failed.
- Claiming all environments were covered after rehearsing one synthetic fixture.

## References

- Read [acceptance route design](./references/design-guide.md) when selecting
  feasible methods, preserving claim scope, and interpreting incomplete evidence.
- Read [cancellation acceptance example](./references/worked-example.md) when
  rehearsing pass, fail, and inconclusive verdicts for one explicit requirement.
