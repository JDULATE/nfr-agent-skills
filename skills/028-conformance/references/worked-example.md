# Event envelope against chosen local rules

This synthetic local rule set is supplied by the fixture, not proposed as an
external standard. Acceptance defaults are illustrative; confirm with the
user/stakeholder before adopting them.

## Filled checking record

| Input | Value |
| --- | --- |
| Selected rule set | event-envelope revision birch |
| Artifact under review | producer event revision cedar |
| Applicability | both rules apply to every event in this fixture |
| required-kind | event must contain a text field named kind |
| kind-spelling | kind must contain lowercase ASCII letters in nonempty words separated by single underscores |
| Valid name example | task_started |
| Invalid name example | TaskStarted |
| Other fields | unrestricted by this selected rule set |
| Exception state | none |
| Initial check inventory | required-kind only; kind-spelling unchecked |
| Result states | pass, fail, unknown, not-applicable, exempted |
| Rule owner | event-contract maintainer role |

## Before: partial checker overclaims

Input artifact is `{kind: "TaskStarted", task_key: "cedar"}`.
The old checker sees kind present and returns success.
Its report says event-envelope birch passed.
But kind-spelling was not executed; under the supplied predicate the name fails.

The fixture identifies an omitted check, not a disputed convention selection.

## Remediation

Add the selected spelling predicate and enumerate both rule results.
Require text kind for required-kind.
For kind-spelling, accept a nonempty sequence of lowercase-letter words
joined by single underscores; reject uppercase, empty words, and nontext values.
Report findings with the rule identity and artifact path.

## After outputs

| Artifact | required-kind | kind-spelling | Evidence |
| --- | --- | --- | --- |
| {kind: "task_started", task_key: "cedar"} | pass | pass | both predicates executed |
| {kind: "TaskStarted", task_key: "cedar"} | pass | fail | kind path violates kind-spelling |
| {task_key: "cedar"} | fail | unknown | missing kind; spelling cannot be evaluated |
| {kind: "task__started"} | pass | fail | empty word between underscores |
| {kind: 7} | fail | fail | nontext kind violates both supplied predicates |

The numeric value is an illustrative invalid fixture input; confirm with the
user/stakeholder before adopting these acceptance fixtures.

Each run starts with an empty finding list and no exceptions.
Carried result state contains event-envelope/birch, artifact/cedar, and the
per-rule statuses above; it never inherits another run's pass.

## Default-insertion negative

Start with {task_key: "cedar"} and no kind field.
A mutating checker inserts kind=task_started before validating and then passes.
That result describes a repaired artifact; the original still fails required-kind.
The corrected check records the original failure before offering a repair.

## Exception control

Add a fixture exception for artifact cedar with name TaskStarted,
rule kind-spelling, approved by event-contract maintainer.
The spelling result becomes exempted with its violation retained, not pass.
The same name in artifact maple has no matching exception and still fails.

## Limits

These results check the selected local schema and naming predicates only.
Other semantic event obligations are not part of the supplied rules.
An empty finding list does not establish an external certification,
legal conclusion, or adoption decision.
