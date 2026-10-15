# Fixed-handler exclusion claim

This fictional local claim excludes caller text being interpreted as commands
through the specified dispatch boundary. It does not claim exclusion of all
injection, malicious handlers or runtime faults.

## Declared candidate and assumptions

The candidate dispatcher accepts only declared operation names mapped to fixed
handlers. Payload text remains data to those handlers. The proposed argument
requires that no reachable handler or loader interprets that caller text as commands.
Actual handler behavior and dependency closure must be inspected, not assumed.

| Input/path | Candidate outcome/evidence | Carried claim state |
| --- | --- | --- |
| Allowed operation name | Fixed handler receives data | Required legitimate use preserved |
| Unknown operation name | No handler invocation | Test result, not universal exclusion proof |
| Payload text on normal path | Inspect every reachable use | No command interpretation assumed without source evidence |
| Alternate loader interprets payload | Counterexample enabling path | Scoped exclusion defeated |
| Configuration enables such a loader | Assumption no longer holds | Old claim reopened |

## Proposed counterexample gate

Illustrative example; confirm with the user/stakeholder:
Require 0 unresolved counterexamples to the exact scoped exclusion argument.
Confirm the class, handler/loader boundary and enforceable configuration premises.

## Interpretation

Many rejected payload examples do not repair the alternate-loader counterexample.
A candidate can remove that route or narrow the claim to an environment where
its absence is verified. A timeout after interpretation bounds behavior but does
not demonstrate exclusion of interpretation itself. No real command execution,
structural proof or universal security property was established in this example.
