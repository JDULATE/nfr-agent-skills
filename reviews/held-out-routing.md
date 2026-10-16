# Held-out routing findings

H001-H012 scored 11/12 (91.7%) against the unchanged acceptable sets.
All twelve answers were supplied. The other 490 catalogue cases were not part
of this held-out run; their missing answers are not held-out failures.

The single miss was H006: "The same bug keeps coming back every release."
The router chose `maturity`; the acceptable set was `testability`, `stability`,
`maintainability`, or `ask`. Its reported runner-up was `maintainability`,
which was acceptable but earned no credit because only `choice` is scored.

The prompt was judged ambiguous, with `ask` the better answer. It does not
establish whether the requested work concerns regression-test capability,
behavior across releases, or recurring maintenance effort. The observed
`maturity` choice remains a miss under the frozen key.

No description or answer key was changed. These 12 prompts remain held out
from authoring and description tuning, with their `held_out: true` markers
retained. This recorded result is not a description-tuning iteration.

The scored artifact is `evals/results/heldout-1.json`, containing only the
original `id` and `choice` pairs. Extra result fields do not affect scoring;
when present, `runner_up` is shown beside a miss as diagnostic information.
