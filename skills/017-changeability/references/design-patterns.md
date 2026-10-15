# Request handoffs and adoption evidence

Model only states that distinguish a real obligation in the inspected process.
The example state names do not impose a universal approval or release procedure.

## Ready versus accepted handoff

- **Use when:** A sender has finished work but responsibility has not transferred.
  Name the receiving owner and the evidence needed to accept or explain a blocker.
- **Trade-off:** Explicit acceptance exposes queues; it can add overhead for trivial
  transitions. Do not add ceremonies where existing evidence already proves receipt.
- **How to verify:** Offer an incomplete request and a ready request, retain receiver
  outcomes, and verify that a sent notification alone advances neither to acceptance.

## Artifact-to-request link

- **Use when:** A request, implementation, and released artifact have different
  identifiers. Connect them through the approved behavior and actual deployed revision.
- **Trade-off:** Link upkeep does not replace checking behavior; an incorrect artifact
  can carry all the expected labels while implementing a different request.
- **How to verify:** Compare the decision's scope with artifact behavior and reject
  a deliberately mismatched revision in the request-to-use trace.

## Audience adoption endpoint

- **Use when:** Deployment, enablement, and actual intended use can diverge. Choose
  an observable endpoint and actor rather than declaring every deployed change adopted.
- **Trade-off:** Production use may be unavailable or inappropriate to observe;
  controlled audience checks need their simulation boundary reported explicitly.
- **How to verify:** Deploy a synthetic artifact with its target-audience switch
  disabled, then enable it through the declared process and run the changed journey.

## Blocked and terminal states

- **Use when:** A request is rejected, superseded, or cannot cross a gate. Retain its
  distinct outcome, blocker owner, and what decision could reopen it, if any.
- **Trade-off:** A complete request history can still lack authority evidence;
  activity records do not authorize the agent to approve its own proposed change.
- **How to verify:** Reconcile abandoned requests separately from adopted ones and
  inspect gate evidence even when a later artifact is already present.

An illustrative handoff-response bound is 1 working day from the agreed ready event;
confirm with the user/stakeholder. Ask the user for calendar, actual states, owners,
and adoption meaning before applying that example to a request.
