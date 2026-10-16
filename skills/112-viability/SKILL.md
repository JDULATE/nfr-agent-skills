---
name: viability
description: >-
  Checks continued value when asked "review upkeep at renewal", "compare benefits with ongoing obligations", or "plan service retirement". Ask the user if continued worth vs build feasibility or budget is unclear. Not for initial delivery (see feasibility), spending cap alone (see affordability), or environmental objectives (see sustainability).
---

# Viability

## Definition and scope

Viability means an offering can continue to provide stakeholder value over a
stated horizon under its ongoing obligations. Make the continuation decision
explicit about value evidence, upkeep, ownership, and exit conditions.
Separate continued worth from initial delivery (`feasibility`), spending-cap
fit (`affordability`), and environmental stewardship (`sustainability`).

## Use when / Don't use when

- Apply when an already delivered report service needs a renewal, redesign,
  or retirement decision because recurring obligations may outweigh its accepted value.
- Include repository-visible output scope, upkeep dependencies, ownership records,
  and a stakeholder-approved continuation gate.
- Route whether an initial plan can be delivered to `feasibility`.
- Route a monetary cap alone to `affordability`.
- Route energy, device life, or an environmental objective to `sustainability`;
  do not substitute an unspecified business-value judgment for that objective.

## Workflow

1. Clarify: Read product goals, recipient-use evidence, recurring work,
   maintenance dependencies, ownership docs, and exit plans before specifying.
   Identify the continuation horizon and whose value decision is being made.
   If the user only asks whether to keep it, then Ask the user what continued
   value, obligations, and decision authority should govern that choice.

2. Specify: Record valued outcomes, observation cycles, recurring obligations,
   capacity/funding assumptions, owner, decision gate, and exit constraints.
   If no rule is supplied, then propose a labeled illustrative default:
   recommend continuation only when the selected value and upkeep conditions
   are supported, otherwise request a renewal decision; confirm with the user/stakeholder.
   Ask at most three grouped questions on value/horizon, ongoing obligations,
   and renewal or exit authority before proposing changes.

3. Design/Implement: Read [continuation decisions](./references/design-guide.md)
   when narrowing unvalued output scope or recording renewal evidence.
   If obsolete output consumes upkeep without serving the accepted value model,
   then propose removing that output while preserving valued recipient tasks.
   If ownership or future capacity is unresolved, then keep continuation
   conditional rather than assuming delivery success guarantees ongoing support.

4. Verify: Evaluate the declared value and obligation conditions for each recorded
   cycle or scenario, retaining adverse and missing evidence.
   Separate observed cycles from forecasts and scenario assumptions.
   If only an upkeep reduction was shown, then leave continued value unverified
   until recipient outcome evidence is also available.

5. Report: Return the value/obligation ledger, repository changes, cycle findings,
   recommended renewal state, and unresolved assumptions.
   If retirement or renewal requires stakeholder authority, then present the
   concrete gate evidence for that decision rather than treating the recommendation
   as approval to change service commitments.

## Specification patterns

- **Continuation:** Over `{confirmed_horizon}`, `{offering}` shall support
  `{valued_outcomes}` within `{ongoing_obligations_and_capacity}`, evaluated by
  `{cycle_evidence_and_stakeholder_gate}`.
- **Review/exit:** If `{value_upkeep_or_ownership_condition}` is unmet or unknown,
  `{renewal_record}` shall request `{decision_and_owner}` while preserving
  `{required_exit_or_recipient_obligations}`.

Use the illustrative evidence-based renewal proposal in Specify when numbers
are absent; confirm with the user/stakeholder before accepting the gate or horizon.

## Rules of thumb

- Do not treat successful initial delivery as evidence of continued stakeholder
  value; each renewal horizon needs the value evidence its decision rule names.
- Keep low upkeep distinct from worthwhile operation; a cheap service with no
  required recipient outcome can still fail the chosen continuation gate.
- Evaluate remaining obligations under the continuation model rather than using
  past implementation effort as the sole reason to keep an offering.
- Keep an ownerless renewal conditional; retained code and a running deployment
  do not establish that recurring recipient and support obligations will be met.

## Verification

Use recurring-obligation review, recipient-evidence inspection, and scenario gates.
Capture the value model and horizon with each comparison.
Keep observed outcomes separate from assumed future use or work.
Inspect whether removed outputs support a required recipient task or exit duty.
Retain missing owners, adverse cycles, and unverified capacity assumptions.
Check both value and obligations after a proposed scope reduction.
Do not infer market demand, financial return, or long-term survival from a fixture.

## Done checklist

- [ ] Define whose continued value and which horizon matter.
- [ ] Identify observable valued outcomes and required recipients.
- [ ] Inventory recurring work, dependencies, and ownership.
- [ ] Separate observed cycles from projected scenarios.
- [ ] Evaluate value and obligation conditions together.
- [ ] Check preserved recipient tasks after scope reduction.
- [ ] Record renewal/exit authority and unresolved evidence.
- [ ] Limit recommendations to the supported continuation model.

## Failure modes

- Using initial delivery success as the whole renewal case.
- Calling reduced upkeep proof of continuing value without recipient evidence.
- Treating a future scenario as an observed operating result.
- Assuming a running deployment supplies ownership for future obligations.
- Retiring a service without addressing the stated recipient or exit commitments.

## References

- Read [continuation decisions](./references/design-guide.md) when selecting
  renewal evidence and a bounded upkeep intervention.
- Read [report-service renewal example](./references/worked-example.md) when
  separating past delivery, future scenarios, and continued value.
