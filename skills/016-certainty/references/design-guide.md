# Confidence-state decisions

Choose labels from the evidence model agreed for the exact claim.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Evidence lookup fails but the UI still says confirmed | Use an explicit unverified state instead of a confirmed default | Consumers must handle unknown outcomes | Remove the supporting record and inspect the final response and display |
| A dispatch event is used to confirm delivery | Match the evidence claim type as well as subject identity | Related evidence no longer supplies a convenient answer | Provide dispatch-only evidence and verify delivery remains unverified |
| Authoritative records disagree for the same claim | Preserve a conflict state with source attribution | Some decisions remain unresolved | Supply the disagreeing records and inspect conflict propagation |
| A cached label outlives the evidence policy that justified it | Store the policy/evidence revision with the qualified result and re-evaluate under the agreed refresh rule | Refresh work and potentially less cached certainty | Change the relevant revision and inspect whether the old label can still be presented |

## Claim qualification sketch

Illustrative pseudocode for a qualitative policy, not a probability estimator.

```text
qualify(claim, evidence):
    matching = authoritative_valid_records_for(claim, evidence)
    if matching is empty:
        return {state: "unverified", claim: claim}
    if matching contains incompatible assertions:
        return {state: "conflicting", claim: claim}
    if matching contradicts claim:
        return {state: "contradicted", claim: claim, sources: matching.identities}
    return {state: "supported", claim: claim, sources: matching.identities}
```

The helper's authority, claim match, and validity rules require a supplied policy.
Do not turn "supported" into an unconditional factual guarantee.

## Narrower evidence

Keep related evidence visible without promoting it to the requested claim.
A dispatch record can support dispatch while delivery remains unverified.
If the user requests numerical confidence, this qualitative sketch is insufficient;
obtain a justified numerical interpretation and evaluation method first.
