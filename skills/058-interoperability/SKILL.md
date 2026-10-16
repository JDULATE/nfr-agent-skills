---
name: interoperability
description: >-
  Aligns exchanged meaning when asked "agree on timestamp units", "fix payload interpretation", or "distinguish queued from completed". Ask the user if meaning vs connection setup is unclear. Not for assembly effort (see integratability).
---

# Interoperability

## Definition and scope

Interoperability means participants exchange information and use it with the
agreed interaction meaning. Specify units, field interpretation, outcomes, and
responsibilities on both sides of the boundary.
Separate semantic exchange from assembly work (`integratability`) and from
noninterfering coexistence (`compatibility`).

## Use when / Don't use when

- Apply when a receiver accepts a payload but interprets its units or fields
  differently, or a sender misreads what a response promises.
- Include supported participant revisions and refusal semantics for unsupported
  representations; parse success alone does not establish agreement.
- Route missing bindings or excessive glue edits to `integratability`.
- Route independent tools overwriting shared resources to `compatibility`.

## Workflow

1. Clarify: Read sender construction, receiver parsing, response handling,
   interface docs, contract fixtures, and revision negotiation before specifying.
   Follow a payload through the receiver's resulting action and the sender's
   interpretation of the response.
   If either party's intended meaning is missing, then Ask the user for its
   authoritative contract rather than inferring semantics from a field name.

2. Specify: Record participants, supported representations, units, optional-field
   meaning, accepted/refused outcomes, and the effect each acknowledgement promises.
   If targets are absent, then propose a labeled illustrative default:
   agreed values retain meaning end to end, unsupported units are refused, and
   acceptance is distinct from completed application; confirm with the user/stakeholder.
   For a change request, ask at most three questions on participant contracts,
   permitted conversions, and response/effect obligations before designing.

3. Design/Implement: Read [exchange decisions](./references/design-guide.md)
   when adding unit adapters, response states, or representation gates.
   If units differ, then convert at a declared boundary using confirmed context;
   refuse when conversion information is unavailable.
   If a response only means queued, then preserve that status through the caller
   rather than presenting the requested effect as complete.

4. Verify: Send complete contract fixtures through real serializers, receiver
   actions, and caller response handling; check the resulting domain values.
   If only a parser or stub transport was tested, then mark end-to-end exchange
   meaning unverified and retain failed and refused interactions in the record.

5. Report: Return the agreed exchange table, mapping changes, participant matrix,
   domain effects, and unsupported representations.
   If an interpretation remains disputed, then show the differing meanings and
   withhold the affected interoperability claim.

## Specification patterns

- **Value meaning:** For `{participant_pair_and_representations}`, exchanging
  `{fields_and_units}` shall yield `{agreed_domain_value}` after
  `{declared_conversion}`, verified by `{sender_to_receiver_effect_fixture}`.
- **Outcome meaning:** Responses to `{interaction}` shall distinguish
  `{accepted_completed_and_refused_states}` and cause `{caller_behavior}`,
  checked against `{receiver_state_and_caller_result}`.
- **Unsupported representation:** On `{unknown_unit_or_representation}`, the
  receiver shall produce `{agreed_refusal}` without `{forbidden_effect}`,
  verified by `{negative_contract_case}`.

Use the illustrative semantic-preservation default in Specify if no numbers are
given; confirm with the user/stakeholder instead of substituting a latency target.

## Rules of thumb

- Carry the unit and conversion context across the exchange boundary; a numeric
  payload that parses successfully may still request a different domain amount.
- Map acknowledgements by the effect they promise, not by a generic success flag;
  queued acceptance must not become a completed business result at the caller.
- Distinguish absent, empty, and explicitly cleared fields when the participants
  assign different effects to them; normalizing them can change the exchanged intent.
- Refuse unsupported representations explicitly rather than silently interpreting
  them as the receiver's default; defaulting can fabricate agreement between peers.

## Verification

Use producer-consumer contract tests, serialization round trips, and domain-effect
inspection. Check direction-specific mappings rather than assuming an inverse.
Cover supported unit conversions, unknown units, absent/empty fields when in scope,
and caller behavior after queued, applied, and refused responses.
Keep participant revisions, original payloads, and receiver effects together.
Separate transport failures from semantic refusal in the reported outcomes.
A mocked success flag cannot demonstrate the receiver's actual business effect.

## Done checklist

- [ ] Identify both participants and supported representations.
- [ ] Resolve field and unit meaning against their contracts.
- [ ] Observe a domain effect after supported exchange.
- [ ] Check caller interpretation of acceptance versus completion.
- [ ] Exercise unsupported representation refusal without a domain effect.
- [ ] Record any untested field-presence or direction-specific behavior.
- [ ] Bound conclusions to the participant combinations actually exercised.

## Failure modes

- Treating parseable data as semantically agreed data.
- Assuming a field named quantity always uses the same unit.
- Reporting a queued request as a completed effect.
- Replacing an unknown representation with a convenient receiver default.

## References

- Read [exchange decisions](./references/design-guide.md) when selecting conversion,
  representation, and response-state mappings.
- Read [stock exchange example](./references/worked-example.md) when tracing a
  concrete payload into domain effects and caller-visible status.
