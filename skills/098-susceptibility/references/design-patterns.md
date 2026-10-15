# Exposure-path practices

Locate a scoped adverse influence without inventing vulnerability or exploitability facts.

## Entry-to-effect precondition ledger

- Use when the same operation is reached through different interfaces or capabilities.
- Trade-off: a minimal path is readable but can hide prerequisites in configuration,
  identity or another service; unsupported prerequisites must remain unknown.
- Verify: record source, entrypoint, caller capability, trust/config conditions,
  invocation and affected result, with evidence for every blocked or reachable classification.

## Three-state classification

- Use when some deployment or permission facts cannot be observed.
- Trade-off: unknown is less decisive but avoids interpreting missing evidence
  as either guaranteed exposure or guaranteed protection.
- Verify: distinguish source-possible paths, observed conditions and missing facts;
  exercise known precondition changes in synthetic fixtures before changing the classification.

## Alternative invocation review

- Use when a public route is disabled but workers, imports or administration can reach the effect.
- Trade-off: expanded review costs effort and requires authorized scope; a hidden
  interface does not establish that its underlying path is unreachable.
- Verify: inspect declared internal/background routes and actual permissions;
  do not assume an invocation succeeds merely because a function exists.

## Exposure change record

- Use when removing a prerequisite or changing configuration is proposed as a fix.
- Trade-off: blocking one path can affect useful behavior while leaving another
  enabling route; narrow reductions are not universal class-exclusion guarantees.
- Verify: rewalk affected/alternative paths, retain valid-use controls and reopen
  classifications when capability, configuration or dependency assumptions change.
