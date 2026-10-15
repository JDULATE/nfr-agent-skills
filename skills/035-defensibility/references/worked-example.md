# Revoked login with an accepted job

This fictional response scope permits an operator to revoke credential `cred-slate`
and interrupt a session, but queued job handling requires a separately granted
control. No actual credential, session or production system is involved.

## Active-path inputs and effects

The modeled adversary has session `session-amber` and previously accepted job
`job-mint` targeting `report-coral`. The declared goal is stopping the scoped
protected effect while preserving unrelated valid work and required evidence.

| Event/control | Observation to check | Carried capability state |
| --- | --- | --- |
| Signal reports modeled activity | Correlate identity/job/resource | Not yet containment |
| Revoke cred-slate | New login behavior | Existing session/job may remain unresolved |
| Interrupt session-amber | Attempt same effect from session | Queued job still needs its own check |
| Granted queued-work intervention | Inspect job-mint actual effect | No unsupported cancellation assumption |
| Normal service healthy | Valid work control result | Does not establish adversarial clearance |

## Proposed response trial

Illustrative timing example; confirm with the user/stakeholder:
Interrupt the agreed capability within 2 minutes after confirmed operator
activation. Confirm which capabilities, action authority and collateral limits
apply; no proposed timing grants permission to execute a live intervention.

## Rehearsal interpretation

A successful revoke receipt plus a continuing job effect fails full containment
of this scoped path. Preserve activity/control/effect records and test reversal
only under confirmed clearance conditions. If queued-work authority is absent,
report that residual capability rather than silently exercising a broader control.
No real containment, incident resolution or external notification occurred here.
