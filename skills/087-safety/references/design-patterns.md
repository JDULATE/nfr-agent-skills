# Harm-control practices

Start with the stakeholder's harm/context model; do not assume a domain safety standard.

## Harm and unsafe-control ledger

- Use when an action, omission, or timing condition can produce a named harm.
- Trade-off: a narrow ledger is inspectable but may omit interacting hazards;
  the intended operating boundary and responsible reviewer must be explicit.
- Verify: connect loss, hazardous condition, unsafe action, causal path, constraint,
  control owner, evidence, and residual paths; do not substitute generic error labels.

## Enforcement at the effect boundary

- Use when interface confirmation alone cannot constrain all ways to issue an action.
- Trade-off: a shared gate reduces bypass paths but its own state and failure
  behavior become part of the harm analysis; a gate name proves no enforcement.
- Verify: trace every in-scope entrypoint to the actual effect and exercise a
  bypass attempt; inspect final effects, not merely a warning or rejected interface call.

## State validity at commitment

- Use when a decision depends on evidence that may change before the effect occurs.
- Trade-off: rechecking or serializing decisions can delay a needed action; the
  allowed timing and consequences of delay must be justified for the named harm.
- Verify: change the relevant state between decision and commit; inspect how the
  implementation binds the checked evidence to the effect without assuming atomicity.

## Unknown, missing, or stale evidence policy

- Use when a controller lacks the evidence needed to choose safely.
- Trade-off: proceed, pause, refuse, or switch modes can each create a competing
  harm. The correct choice is a stakeholder/domain decision, not a generic fail-closed rule.
- Verify: exercise missing and stale evidence under the confirmed policy and
  inspect both prohibited effects and harms caused by omitted or late required actions.

## Control defeat and residual review

- Use when overrides, alternate commands, recovery, or control failure can bypass protection.
- Trade-off: an override may serve a legitimate mission need but reopens an
  explicitly owned path; logs and approval labels alone do not prevent the effect.
- Verify: exercise allowed and forbidden bypass paths, retain counterexamples,
  and assign residual decisions to the responsible owner without inferring certification.
