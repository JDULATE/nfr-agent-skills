---
name: certainty
description: >-
  Bounds confidence when asked "label missing evidence", "show conflicting sources", or "mark unverified results". Ask the user if confidence vs value error is unclear. Not for value error (see accuracy) or formal guarantees (see provability).
---

# Certainty

## Definition and scope

Certainty means stating how strongly the available evidence supports an output
and where knowledge remains unresolved. Use this repository's scoped confidence
meaning rather than promising absolute truth.
Separate support for a claim from observed value error (`accuracy`) and
a formal argument under explicit assumptions (`provability`).

## Use when / Don't use when

- Apply when an output is presented as confirmed despite missing, conflicting,
  stale, or indirect supporting evidence.
- Include claim-level evidence records and propagation of qualified or unknown
  status to the interface that presents the result.
- Route measured deviation from a truth reference to `accuracy`.
- Route a checkable proof obligation to `provability`; a label is not a proof.
- Route delegation or organizational trust decisions to `trustability`.

## Workflow

1. Clarify: Read output generation, evidence retrieval, label assignment,
   cached responses, and interface wording before specifying a confidence policy.
   Identify the exact claim and which evidence supports it.
   If the request is "be certain" without a claim or evidence model, then
   Ask the user what can establish that claim and what must remain unknown.

2. Specify: Record claim scope, evidence authority, matching and freshness rules,
   conflicts, labels, and the allowed action for each evidence state.
   If no policy exists, then propose this labeled illustrative default:
   supported only for a matching authoritative record; otherwise unverified,
   with conflicts exposed separately; confirm with the user/stakeholder.
   Do not invent confidence percentages.
   Ask at most three questions about the claim, supporting sources and validity,
   and how qualified or unknown results should be presented or used.

3. Design/Implement: Read [confidence decisions](./references/design-guide.md)
   when replacing unconditional labels with evidence-dependent states.
   If evidence is absent or outside its validity scope, then preserve an unknown
   result rather than promoting a plausible answer.
   If sources disagree, then carry the conflict to the consumer instead of
   selecting the most reassuring label.

4. Verify: Exercise supported, missing, mismatched, and conflicting evidence
   through the actual output path, including cache and display mapping.
   If a lower-level unknown becomes confirmed downstream, then fail the claim
   propagation check even when the displayed answer happens to be correct.

5. Report: Return the claim/evidence policy, label changes, observed mappings,
   unresolved evidence, and limits of the claim.
   If support only establishes a narrower claim, then state that narrower claim
   rather than implying certainty about the full requested outcome.

## Specification patterns

- **Qualified output:** For `{claim}`, the system shall present `{label_and_limits}`
  from `{evidence_authority_matching_and_validity_rules}`, verified using
  `{supported_missing_and_conflicting_cases}`.
- **Propagation:** When `{claim_evidence}` is `{unknown_or_conflicting}`,
  `{consumer_path}` shall retain `{qualification_and_allowed_action}` without
  asserting `{unsupported_stronger_claim}`, checked by `{end_to_end_output_fixture}`.

Use the illustrative evidence-state policy in Specify when numbers are absent;
confirm with the user/stakeholder. Treat any requested probability as a separate
claim requiring a supplied basis and evaluation method.

## Rules of thumb

- Attach support to the exact claim it establishes; evidence of dispatch must not
  become certainty about delivery merely because the identifiers match.
- Propagate unknown as a meaningful result rather than replacing it with the
  most likely answer and a confirmed label.
- Expose evidence conflicts as conflicts; counting agreeing sources without
  resolving their authority does not establish a warranted certainty level.
- Keep confidence labels weaker than their evidence basis; repetition of the
  same assertion through caches must not make it more established.

## Verification

Use evidence-state decision tests, claim-scope inspection, and output-path review.
Check claim identity, authoritative source, evidence revision, and validity
condition together. Preserve missing records and conflicting observations.
Exercise cached labels after source changes under the declared refresh contract.
Inspect API payload and rendered wording, not just an internal status.
Do not treat a synthetic supported label as proof of real-world truth.
If quantitative confidence is requested, Ask the user for its interpretation,
calibration evidence, and acceptable evaluation procedure before implementing it.

## Done checklist

- [ ] Define the claim and the evidence that can support it.
- [ ] Record authority, identity matching, and validity rules.
- [ ] Check supported, missing, and conflicting evidence states.
- [ ] Test evidence for a related but narrower claim.
- [ ] Inspect propagation through stored or cached output and display.
- [ ] Verify unknown states do not become confirmed defaults.
- [ ] State unestablished claims and any unvalidated probability interpretation.

## Failure modes

- Treating a likely answer as confirmed because the evidence lookup failed.
- Inferring a delivery claim from evidence of dispatch.
- Letting a cached confirmed label survive a disqualifying evidence change.
- Averaging conflicting sources into an invented confidence percentage.

## References

- Read [confidence decisions](./references/design-guide.md) when mapping
  evidence states to claim-level qualifications.
- Read [delivery-label example](./references/worked-example.md) when preserving
  unknown and conflicting evidence through the final response.
