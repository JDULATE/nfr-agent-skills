# Stakeholder-authored artifact patterns

Inspect the real grammar and host boundary. These choices do not establish an
existing plugin facility or support for an arbitrary scripting language.

## Authored artifact separated from presets

- **Use when:** Stakeholders need results beyond built-in choices. Store the
  author-owned content and select it through the same normal feature invocation.
- **Trade-off:** Authoring creates compatibility and ownership obligations beyond
  selecting a preset; a hardcoded customer branch does not remove those obligations.
- **How to verify:** Edit content independently of host source and compare the
  normal result with that content's expected result, including a non-preset difference.

## Declared authoring inputs and operations

- **Use when:** Custom artifacts read host fields or request actions. Provide only
  the agreed public data and explicit supported operations through the boundary.
- **Trade-off:** Restricting inputs can make a desired custom result impossible;
  expose the missing capability instead of silently accessing private host state.
- **How to verify:** Exercise available fields and a forbidden/unsupported expression;
  check the declared rejection without presenting partial output as authored success.

## Revision selection and validation

- **Use when:** Saved drafts, previews, and active artifacts can diverge. Define
  which revision each invocation uses and how invalid edits affect prior selection.
- **Trade-off:** Keeping a previous revision may preserve use but conceal a failed
  edit if fallback is not explicit. The author needs its invalid-result evidence.
- **How to verify:** Save a changed draft, preview it, invoke normally, and compare
  revision traces; select the changed revision under the agreed activation policy.

For an illustrative starting scope, demonstrate 1 user-authored artifact;
confirm with the user/stakeholder. Obtain actual grammar, allowed data, authoring
rights, result contract, failure behavior, revision lifecycle, and host-change scope.
