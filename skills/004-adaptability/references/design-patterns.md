# Accommodation boundary decisions

Treat these as design options for the reported external delta, not claims about a
real partner. Establish input meaning from inspected examples and the owner.

## Normalize external representations

- **Use when:** Old and changed representations express the same accepted domain
  fact. Put the mapping at the integration boundary and preserve a domain result
  that downstream consumers already understand.
- **Trade-off:** Normalization can discard source distinctions that some consumers
  actually require; record them before declaring the representations equivalent.
- **How to verify:** Pair source messages with their expected domain result, replay
  both through the boundary, and inspect downstream writes as well as parsed fields.

## Explicit condition selection

- **Use when:** Multiple external variants remain supported. Select a mapping from
  documented revision evidence or a confirmed distinguishing feature.
- **Trade-off:** Structural detection can be ambiguous. A renamed field alone may
  not establish the revision or the meaning of its value.
- **How to verify:** Supply each recognized variant, conflicting selection evidence,
  and a missing discriminator. Inspect selected mapping and accepted rejection behavior.

## Unknown-meaning boundary

- **Use when:** A new source value lacks an approved domain interpretation. Keep
  that case outside the successful-accommodation set pending a mapping decision.
- **Trade-off:** Rejection can delay required work; a guessed default can instead
  create accepted-looking wrong results. Ask the user which consequence is permitted.
- **How to verify:** Send an unmapped value through the real path; inspect that it
  cannot become a normal result silently. Replay mapped controls to expose over-rejection.

## Mapping record

Retain external condition evidence, old/new field meanings, normalized result,
permitted loss, continued support, negative cases, and the mapping owner.
As an illustrative paired-fixture bound, propose 0 unexplained semantic differences;
confirm with the user/stakeholder. This bound does not establish environment coverage.
A changed representation can be mapped while changed meaning remains unresolved;
keep those outcomes separate rather than reporting a single adapter-success flag.
