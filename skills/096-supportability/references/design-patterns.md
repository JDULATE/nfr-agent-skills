# Repository-backed support decisions

Keep case evidence, support access, and remedy authority explicit. A runbook entry
is useful only if the support provider can follow its evidence-to-action path.

## Case-bound diagnostic artifact

- **Use when:** Support lacks the revision, actor context, or reason that distinguishes
  likely causes. Add a scoped collector or diagnostic branch tied to that case question.
- **Trade-off:** More fields can expose unapproved data without distinguishing any
  action. Ask the user which fields and collection context are permitted.
- **How to verify:** Generate a synthetic bundle under the support actor's actual
  access; compare allowed fields and forbidden markers with the agreed collection schema.

## Remedy with prerequisites and outcome oracle

- **Use when:** A known case branch has a documented action. Record what makes that
  action applicable and the affected actor's expected result afterward.
- **Trade-off:** Retry/reset may erase a symptom without resolving its cause;
  broad access can make an admin demonstration pass while the user's issue remains.
- **How to verify:** Exercise matching and mismatched case preconditions, apply only
  the permitted remedy, and replay the user's task with unchanged actor constraints.

## Unresolved branch and escalation proposal

- **Use when:** Available evidence cannot distinguish the branch or support lacks
  remedy authority. Identify missing facts, owning role, and minimal reproducible context.
- **Trade-off:** A detailed proposal does not establish that another owner accepts
  the case. No external contact or permissions change follows from creating the record.
- **How to verify:** Supply an unknown reason or unavailable evidence source and
  inspect that the result names what is missing instead of claiming resolution.

An illustrative starting scope is 1 synthetic case bundle;
confirm with the user/stakeholder. Actual case classes, collection rights, permitted
remedies, resolution criteria, and escalation ownership need a supplied policy.
Code/config/test/runbook changes should enable that path, not manufacture extra
status records without a reproducible support decision.
