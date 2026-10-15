# Worked example: checkout disappears during deployment

Treat this as a hypothetical illustration, not an inspection of the user's system.

## Read and clarify

Start with the request: "Keep checkout usable while we deploy."
Read the checkout route, shutdown handler, deployment configuration, and incident
timeline. Suppose those artifacts show incoming traffic reaching a retiring worker
before it finishes existing orders. Record that as the example's stated condition;
in a real project, verify it before choosing a fix.

Ask the user which order result counts as successful, when checkout is required,
which locations matter, and how long an order attempt may take. Ask whether an
order queued but not accepted counts as usable service. Do not decide that from
a successful response code alone.

## Draft the requirement

Propose: "During a checkout deployment, the system shall accept an order through
the ordinary public route and return its recorded acceptance within
`{confirmed_deadline}` during `{service_calendar}` from `{agreed_locations}`,
meeting `{confirmed_good_time_ratio}` over `{agreed_window}` under
`{agreed_bin_and_unknown_policy}`."

Illustrative example only: propose 99.9% good eligible time as the ratio;
confirm with the user/stakeholder. Leave the requirement proposed while the
deadline, calendar, locations, window, or accounting policy is unresolved.

## Change and exercise

Evaluate traffic draining and the shutdown order against the observed retiring
worker path. Keep the required order acceptance behavior as the success boundary.
If a proposed fallback only displays a saved basket, classify checkout as
unavailable unless the stakeholder explicitly changes that boundary.

In a controlled environment, prepare distinguishable synthetic orders, start
the journey probe through ordinary routing, and trigger a deployment. Inspect
whether existing orders finish and new orders reach a serving worker. Check
recorded order acceptance as well as responses; inspect for duplicate orders
introduced by retries rather than reporting a retry as an unqualified success.

Repeat the journey with the mandatory order store unavailable. Expect the probe
to classify checkout as bad when the required result cannot be produced; a green
process health check must not change that classification. Stop the probe stream
in a separate rehearsal and confirm missing bins remain visible as unknown.

## Interpret evidence

| Example observation | Classify under the proposed boundary | Keep as evidence |
| --- | --- | --- |
| Order accepted within the agreed deadline during handoff | Good observed bin under the agreed bin rule | Order reference, timing, route, and deployment revision |
| Page renders but the order store cannot accept the order | Bad | Failed business assertion and dependency timeline |
| No trustworthy journey sample is available | Unknown | Missing-sample interval and monitor status |

Recompute good, bad, unknown, and excluded time using the measurement contract.
Do not claim this hypothetical exercise passed in an actual deployment. Report
the requirement as proposed, the rehearsal results as observed only if executed,
and attainment as unverified until the agreed measurement window is covered.
