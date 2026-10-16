---
name: formality
description: >-
  Defines precise notation when asked "define allowed transitions", "give states one meaning", or "specify missing values". Ask the user if notation precision vs explanation clarity is unclear. Not for proving the stated property (see provability) or choosing acceptance evidence (see verifiability).
---

# Formality

## Definition and scope

Formality means giving a specification an explicit level of notation and
interpretation precision. Define terms, domains, states, and transition meanings
so a reader can distinguish valid statements from ambiguous ones; keep this
notation contract separate from proving a property (`provability`) or choosing
how to establish a requirement (`verifiability`).

## Use when / Don't use when

- Apply when the same state label or conditional rule admits conflicting readings.
- Apply when prose, transition tables, and executable checks disagree about a symbol.
- Route a universal argument over an already defined model to `provability`.
- Route unclear explanatory wording without a notation decision to `comprehensibility`.
- Route selection of acceptance evidence to `verifiability`.

## Workflow

1. Clarify: Read requirement text, schemas, enums, transition code, tests, and
   existing notation conventions before introducing a new representation.
   Identify the precise disagreement and the decision it changes.
   If the problem is missing domain meaning rather than notation, then Ask the user
   to resolve that meaning before encoding an arbitrary interpretation.

2. Specify: Record the artifact, vocabulary, variable domains, event meanings,
   boundary conventions, and interpretation of omitted cases.
   If the required precision is unspecified, then propose labeled illustrative
   defaults: a typed state vocabulary, explicit transition table, and rejection
   meaning for unlisted transitions; confirm with the user/stakeholder.
   Do not imply that adopting this notation establishes implementation correctness.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [notation decisions](./references/design-guide.md)
   when selecting prose constraints, a transition table, or a stricter grammar.
   If readers disagree about a boundary, then define its inclusion explicitly.
   If the same symbol has incompatible meanings, then separate the names or scopes.
   If a checker forces a new semantic decision, then surface that decision instead
   of treating its default as the stakeholder's requirement.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Interpret concrete valid, invalid, boundary, and omitted cases using
   only the notation record. Compare the readings with source contracts.
   If two readers or representations yield different allowed transitions, then
   record the discrepancy and resolve it before claiming the artifact is precise.
   Read [cancellation notation example](./references/worked-example.md) when
   documenting a terminal-state meaning without turning it into a proof.

5. Report: Deliver the vocabulary, interpretation rules, chosen representation,
   resolved ambiguities, and remaining semantic decisions.
   If implementation checks or proof work were not performed, then keep those
   outcomes unverified even when the notation itself is consistent.

## Specification patterns

- **Interpretation:** The specification for `{artifact}` shall define
  `{symbols_and_domains}`, `{event_meanings}`, and `{omitted_case_policy}`
  so `{review_cases}` have the unique allowed interpretations in `{answer_record}`.
- **Boundary:** For `{predicate_or_transition}`, the representation shall state
  `{endpoint_and_ordering_conventions}`; prose, tables, and checks shall give
  `{agreed_result}` for `{boundary_cases}`.

For absent precision targets, use the illustrative notation default in Specify
and confirm with the user/stakeholder; choose precision to remove the actual ambiguity.

## Rules of thumb

- Do give every state label one declared meaning within its scope; don't let
  "done" mean both a terminal outcome and an operation still awaiting confirmation.
- Do distinguish an undefined expression from a false predicate; missing notation
  meaning must not silently become a valid refusal rule.
- Do state whether an omitted transition is forbidden, allowed, or unspecified;
  a blank table cell must not acquire meaning only from a particular reader.
- Do choose the least elaborate representation that resolves the identified
  interpretation conflict; stricter syntax without defined semantics adds ceremony.

## Verification

Use specification review, schema validation, and transition-table check categories.
Enumerate the declared state and event vocabulary and find every use in the
representations being reconciled.
Evaluate a terminal-state attempt and an unlisted event, not just valid transitions.
Check endpoint inclusion, event order, and absent-value meanings explicitly.
Compare each formalized rule with the original requirement to detect a silently
added restriction. Preserve unresolved alternatives in the decision record.
Treat parser acceptance as evidence of syntax only; it cannot select domain meaning
or show that the running system obeys the table.

## Done checklist

- [ ] Locate the interpretation conflict and its affected decision.
- [ ] Define each symbol, domain, and event used in the chosen representation.
- [ ] Give omitted transitions or cases an explicit interpretation.
- [ ] Resolve endpoint and ordering conventions with concrete boundary readings.
- [ ] Compare prose and table interpretations for valid and invalid cases.
- [ ] Record added restrictions and obtain the intended semantic decision.
- [ ] Separate notation findings from unperformed proof or implementation checks.

## Failure modes

- Introducing mathematical symbols while leaving their domains undefined.
- Reading a blank transition cell as permission in one artifact and refusal in another.
- Calling a model precise because a parser accepts its syntax.
- Encoding a tool's default semantics as if the stakeholder had chosen them.

## References

- Read [notation decisions](./references/design-guide.md) when choosing a
  representation and resolving undefined, omitted, or conflicting meanings.
- Read [cancellation notation example](./references/worked-example.md) when
  checking concrete readings before making proof or implementation claims.
