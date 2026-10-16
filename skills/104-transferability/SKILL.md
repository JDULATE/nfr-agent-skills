---
name: transferability
description: >-
  Hands assets to recipients when asked "handoff project files", "map recipient owners", or "preserve transfer links". Ask the user: asset ownership, execution hosts, or data exchange? Not for moving execution platforms (see portability), ongoing system exchange (see interoperability), or rebuilding an experiment (see replicability).
---

# Transferability

## Definition and scope

Transferability means a defined asset, responsibility, or state can be handed to
another recipient with its agreed meaning preserved. Specify the handoff package,
recipient mapping, acceptance, and source disposition; distinguish software
platform migration (`portability`), ongoing protocol exchange
(`interoperability`), and independent reconstruction (`replicability`).

## Use when / Don't use when

- Apply when a project export loses linked assets or cannot be used by its recipient.
- Apply when a handoff needs an explicit recipient acceptance and ownership outcome.
- Route moving software between execution environments to `portability`.
- Route a recurring exchange protocol's semantic contract to `interoperability`.
- Ask the user which asset, responsibility, or state changes hands before designing
  a generic "transfer everything" mechanism.

## Workflow

1. Clarify: Read export/import paths, asset references, identity mappings, ownership
   policy, recipient capabilities, and existing handoff documentation first.
   Identify the transferable unit, recipient, allowed data, and copy-versus-handoff intent.
   If responsibility or source disposition is unclear, then Ask the user before
   promising deletion, ownership release, or additional recipient authority.

2. Specify: Record the source unit, referenced-asset closure, semantic mapping,
   recipient prerequisites, acceptance predicate, failure outcome, and source disposition.
   If no handoff contract exists, then propose labeled illustrative defaults:
   stage a recipient-usable package, validate links and meaning, and keep the source
   responsibility unchanged until acceptance; confirm with the user/stakeholder.
   Any final authority change remains governed by the existing confirmed policy.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [handoff decisions](./references/design-guide.md)
   when choosing package closure, mapping, recipient staging, or acceptance evidence.
   If the package references source-only assets, then include or explicitly resolve
   them for the recipient. If identities differ, then use a confirmed mapping rather
   than silently dropping an assignee. If acceptance is absent, then retain the
   declared pending state instead of treating export completion as handoff completion.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Import into the declared recipient context and inspect content, links,
   mapped responsibility, and the usable result. Exercise a missing-asset case.
   If a mapping or asset cannot be validated, then report the handoff incomplete
   and preserve the source under its confirmed policy.
   Retain failed staging, receipt gaps, and unresolved disposition steps.
   Read [project handoff example](./references/worked-example.md) for a filled package.

5. Report: Return the package record, confirmed mappings, recipient acceptance,
   source disposition, and outstanding handoff decisions.
   If only package creation was checked, then report that boundary without
   claiming recipient usability or completed responsibility transfer.

## Specification patterns

- **Asset handoff:** Transfer `{unit_and_reference_closure}` from `{source}`
  to `{recipient_context}` while preserving `{content_units_links_and_meaning}`,
  verified through `{recipient_use_and_comparison}`.
- **Responsibility:** After `{recipient_acceptance_predicate}`, apply
  `{confirmed_source_and_recipient_assignment}` using `{existing_policy}`;
  otherwise retain `{pending_or_uncertain_handoff_state}`.
- **Mapping:** Every `{identity_or_reference}` shall resolve through
  `{approved_mapping}` or produce `{explicit_incomplete_result}`, not
  `{silently_changed_meaning}`.

Use the illustrative handoff record in Specify for missing numeric targets and
confirm with the user/stakeholder. Do not invent a universal transfer deadline.

## Rules of thumb

- Do transfer the referenced-asset closure needed by the recipient, not only the
  root project record; source-only attachment handles do not make a usable handoff.
- Do use recipient acceptance of the transferred unit as the handoff boundary;
  successful package creation alone cannot establish that the recipient can use it.
- Do separate source release from package creation; only the confirmed handoff
  policy can end the source's responsibility after the acceptance condition is met.

## Verification

Use package inventory, recipient-context import, reference resolution, semantic
comparison, and ownership-policy checks.
Inspect assets and links after recipient import rather than reading the export listing only.
Check required recipient capabilities and permissions through the existing policy.
Reconcile source and recipient identities, units, and content meanings.
Inspect recipient-local identifiers for silently changed assignments or units;
an unmapped value must remain incomplete instead of receiving a convenient default.
Keep raw comparisons, failed imports, missing receipts, and partial handoffs visible.
Exercise missing assets and unmapped identities without silently substituting defaults.
A handoff fixture does not establish atomic authority transfer across real systems.

## Done checklist

- [ ] Identify the unit, recipient, and copy-versus-responsibility intent.
- [ ] Include or resolve the required referenced-asset closure.
- [ ] Confirm identity/unit mappings and recipient prerequisites.
- [ ] Inspect recipient usability of content and linked assets.
- [ ] Reject missing assets or mappings as incomplete.
- [ ] Record recipient acceptance separately from package creation.
- [ ] Apply only the confirmed source/recipient responsibility policy.
- [ ] Report pending, uncertain, and partially completed dispositions.

## Failure modes

- Exporting a root record while leaving its assets available only to the source.
- Dropping an unmapped assignee and reporting the project unchanged.
- Calling an archive successfully written a completed recipient handoff.
- Releasing source responsibility before the recipient acceptance condition.
- Claiming a distributed atomic ownership change from a sequential fixture.

## References

- Read [handoff decisions](./references/design-guide.md) when choosing package
  closure, recipient mapping, acceptance, and source disposition boundaries.
- Read [project handoff example](./references/worked-example.md) when validating
  a recipient-usable package without assuming an atomic cross-system handover.
