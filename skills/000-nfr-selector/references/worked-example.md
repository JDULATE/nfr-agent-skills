# Selection fixtures

These are authored planning fixtures, not executed project results.
Each example keeps the user's scope and labels assumptions before build work.

## Explicit selection request

Input: "Which NFRs matter for this personal-email export? The file goes to an
approved recipient; the known problem is that unused email fields remain in it."
Inspected fixture: export serializer emits `name,email,last_seen`; the agreed
recipient contract needs `name` only. No timing or uptime complaint is supplied.
State: existing recipient permission remains unchanged; retained source data is
outside this export-only request until the user expands it.

Failing plan: select privacy, confidentiality, anonymity, availability, and speed
work merely because the system handles personal data.
Repaired plan: select `privacy` for the export's data-purpose/field boundary.
Assumption shown: permission is already settled, and this change addresses the
recipient payload only. Proposed implementation removes unused serialized fields
through privacy's Workflow; source retention remains explicitly unverified.
Output oracle: export fields equal `name`; no new permission or anonymity claim.

## Broad readiness request

Input: "Make this production-ready." Fixture docs identify an order service whose
only reported release blocker is users losing checkout sessions during deployment.
Current evidence: deployments restart the service; no real outage trace exists.
First question: does readiness mean preserving that checkout journey, or are
there additional blockers? Fixture answer: the checkout journey is the scope.
State carried: existing authentication, database, and deployment route stay fixed.

Failing plan: introduce a new deployment platform, audit stack, and cache before
settling the readiness boundary.
Repaired plan: select `availability` for usable checkout time across the deployment.
Assumptions shown: no other readiness claim is accepted; the deployment mechanism
and recovery behavior remain to be inspected by availability's Workflow.
Output: a journey-specific plan and a deployment rehearsal proposal. No measured
availability improvement or general production-readiness result is asserted.

## Several qualities and a possible conflict

Input: "Improve response time, preserve recipient restrictions, and keep this
easy to maintain. Do not add a service." Fixture proposal: cache report responses.
Existing contract: recipient identity selects report fields; cache keys currently
include the report id only. There is no latency measurement or repair-effort log.
State carried: existing process and permission mechanism remain in use.

Failing plan: add a shared cache and accept speed as the sole success criterion.
Repaired plan: sequence `confidentiality` to establish recipient-specific payload
separation before `performance-efficiency-time-or-space-bounds` trials. Include
`maintainability` for the user's continuing repair-effort concern, with evidence
needed before accepting that claim.
Assumptions shown: caching is a proposal, not a proven speed improvement; no new
service is authorized. Maintainability priority is provisional pending the user's
repair boundary. A paired check compares recipient isolation and response time.
Output oracle: no recipient sees another's restricted fields; timing and ongoing
repair effort remain unverified until their selected checks run.

No fixture establishes that a particular quality always outranks another.
