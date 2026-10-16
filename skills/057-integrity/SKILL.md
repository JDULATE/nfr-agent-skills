---
name: integrity
description: >-
  Controls unauthorized or unintended alteration when tickets say "stale edits overwrite approved changes", "block updates to protected fields", or "check whether this import was tampered with". Not for factual error (see accuracy), disclosure (see confidentiality), or partial commits (see atomicity).
---
# Integrity

## Definition and scope

Integrity means data or behavior is protected against unauthorized or unintended
alteration. Define permitted transitions and trusted comparison/provenance;
distinguish real-world value error (`accuracy`), disclosure boundaries
(`confidentiality`), all-or-none visibility (`atomicity`), and ordinary representation
agreement (`consistency`).

## Use when / Don't use when

- Apply when protected fields can be overwritten, imported artifacts can change
  without detection, stale updates can replace approved state, or provenance is untrusted.
- Route closeness to a real-world reference to `accuracy`; unchanged data can be
  inaccurate, and an authorized correction may legitimately change a value.
- Route partial commit visibility alone to `atomicity`; a complete commit may
  still contain an unauthorized or unintended alteration.

## Workflow

1. Clarify: Read mutation/import code, allowed-transition rules, provenance and
   version handling, trusted-source docs, and alteration incidents before specifying.
   If the accepted source or permitted transformation is unknown, then Ask the
   user rather than treating the currently stored value or a supplied checksum as authority.

2. Specify: Record protected state/behavior, permitted writers/transitions,
   trusted origin, freshness/version, detection/enforcement point, and response to mismatch.
   If the user wants alteration protection, then propose this transition record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Asset: named fields/artifact/behavior and existing approved transition rule.
   Authority: actual permitted writer, trusted comparison/source, and current version policy.
   Trial gate: 0 accepted prohibited alterations in the agreed tamper/stale-write fixtures.
   Enforcement: inspect the final mutation/import boundary and alternate writers.
   Detection: compare contents and provenance against independently trusted expectations.
   Mismatch: retain known-good state or approved reconciliation; unknown policy stays open.
   Evidence: input origin/version, decision, actual before/after state, and rejected controls.
   Status: proposed scoped integrity checks, not proof that the value is real-world accurate.
   ```

   Ask at most three groups about asset and permitted changes; origin/version and
   trust assumptions; and mismatch, recovery or proposed acceptance behavior.
   Continue to a constrained write/import design without inventing the authoritative value.
   If no criterion exists, then offer the illustrative prohibited-alteration gate
   and confirm with the user/stakeholder before adopting its fixture/threat scope.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [alteration-control practices](./references/design-patterns.md)
   when constraining writes, validating provenance, or rejecting obsolete updates.
   If an importer can change content and its reference together, then identify
   an independent trust anchor; matching attacker-controlled values cannot establish trusted origin.
   If a stale writer can overwrite a newer approved state, then enforce the
   confirmed version/transition rule at the actual mutation boundary, not only in the editor.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Attempt prohibited field changes, altered/untrusted artifacts, stale
   updates, and legitimate corrections; inspect actual state and mismatch evidence.
   If a rejected request still changes protected state through another path,
   then retain the alteration failure even when the response reports an error.

5. Report: Return protected transitions, changed write/import paths, trust/version
   assumptions, actual accepted/rejected effects, and unverified alternate writers.
   If only contents matched a supplied reference, then describe that comparison
   without claiming trusted provenance, freshness, or real-world correctness.

## Specification patterns

- **Protected transition:** For `{asset_and_current_state}`, permit only
  `{approved_writer_and_transition}` under `{version_and_policy_conditions}`,
  verified by `{positive_negative_and_stale_write_effect_checks}`.
- **Trusted import:** Before `{artifact_or_data_use}`, establish `{required_content_origin_and_freshness}`
  against `{independent_trusted_expectation}`, applying `{confirmed_mismatch_response}`
  as verified by `{altered_untrusted_replayed_and_legitimate_input_cases}`.

Use the illustrative prohibited-alteration gate when no criterion exists;
confirm with the user/stakeholder. Ask the user which changes and sources are actually legitimate.

## Rules of thumb

- Do distinguish an authorized correction from an unauthorized overwrite;
  preserving every old byte would defeat a transition policy that permits legitimate repair.
- Don't establish trust by comparing an artifact with a reference supplied through
  the same untrusted alteration path; both may agree while the protected origin is unestablished.
- Do enforce protected-field and transition rules at the final writer, including
  alternate import/admin paths; a restricted editor cannot constrain a bypassing mutation.
- Do bind stale-write decisions to the current approved version at mutation;
  a valid earlier edit must not silently replace a later state the policy protects.
- Do inspect actual protected state after rejected changes; error responses do
  not establish alteration prevention if a side path already committed the forbidden value.
- Don't call unchanged or provenance-checked data accurate; closeness to the
  real-world reference is a separate acceptance question from alteration control.

## Verification

Use write-boundary integration, synthetic tamper/provenance cases, and versioned
state inspection categories. Compare before/after protected fields, attempted
writer/origin, version decisions, and actual effects. Include legitimate correction
as a control, alternate writers, stale/replayed inputs, and mismatch behavior.
Distinguish content equality, provenance, freshness, allowed change, and real-world value error.

## Done checklist

- [ ] Define protected state/behavior and legitimate writers/transitions.
- [ ] Trace the trusted comparison source and its independence from the tested alteration path.
- [ ] Inspect version/freshness rules at final mutation or artifact-use boundaries.
- [ ] Exercise altered, untrusted, stale/replayed, and prohibited-field inputs.
- [ ] Verify actual protected state after both accepted and rejected changes.
- [ ] Confirm legitimate corrections still apply under the approved policy.
- [ ] Inspect alternate writers/importers and record untested origin/version assumptions.

## Failure modes

- Treating matching untrusted content and reference as proof of trusted origin.
- Protecting an editor while another writer can alter the same protected field.
- Accepting a stale valid update that overwrites newer protected state.
- Returning an error after a prohibited state mutation already occurred.
- Blocking legitimate correction or equating preserved bytes with accurate real-world values.

## References

- Read [alteration-control practices](./references/design-patterns.md) when defining
  write authority, independent provenance, version rules, or mismatch handling.
- Read [protected-report example](./references/worked-example.md) when current
  approval state, imported content, and attempted stale edits need different evidence.
