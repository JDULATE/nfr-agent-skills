# Synthetic installation lifecycle

This is an illustrative target and package model, not an actual installer result.
All fixture revisions and proposed policies are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled lifecycle record

| Field | Fixture value |
| --- | --- |
| Target | target-elm, supports the declared staging and activation operations |
| Package revisions | app-fern followed by app-moss |
| Prerequisites | runtime capability present; app area writable; startup registry writable |
| App-owned paths | app/bin, app/defaults, app/stage, active-entry |
| Startup registration | launcher-elm -> active-entry |
| User-owned path | projects/draft-ash, content user-note |
| Fresh start | app paths and launcher absent; user project already present |
| Existing start | app-fern active, complete owned artifact set and launcher |
| User-data policy | retain projects during install, upgrade, failure, and removal |
| Schema change | none in this fixture |
| Activation predicate | complete package set and successful installed-entrypoint startup |
| Failure point | new binary staged but new defaults not yet staged |
| Carry | user project persists; active version remains identifiable |

## Before remediation: failing lifecycle

The original setup marks extraction complete as success even when launcher-elm is absent.
The app cannot be started through its declared installed entrypoint.

Its upgrade writes app-moss binary over app-fern before copying new defaults.
Failure at the stated point leaves a mixed binary/default set.

Its removal deletes the common root holding app and projects.
That also removes projects/draft-ash, violating the supplied retention policy.

These are constructed defects in this lifecycle model, not observed repository bugs.

## Fresh installation after remediation

Check the declared prerequisites and stage app-fern binary plus defaults.
Activate the complete set and register launcher-elm.
Invoke the installed entrypoint: it returns ready using the installed defaults.
The ownership record names the app paths and launcher only.
projects/draft-ash still contains user-note.

## Interrupted upgrade and retry

Start with complete app-fern and stage app-moss in app/stage.
Inject failure after staging the new binary but before new defaults.
Expected state:
```text
active = app-fern
active_artifacts = complete app-fern set
staged = partial app-moss set, explicitly owned
launcher = launcher-elm -> active-entry
projects/draft-ash = user-note
result = upgrade incomplete, not activated
```

A retry inspects the owned partial set, completes app-moss staging, and activates it.
The installed entrypoint now returns ready with the complete app-moss set.
This example has no data-schema migration to reverse.

## Removal case

Remove the recorded app files, active entry, staged remnants, and launcher-elm.
Inspect the result: app resources and launcher absent; projects/draft-ash unchanged.
A new unowned projects/note-birch with content keep-me must also remain.

If launcher removal fails, report partial removal rather than "uninstalled".
The fixture does not authorize deleting arbitrary unknown resources.

## Requirement example and limits

On target-elm, lifecycle operations shall activate only a complete owned package
and retain the declared user project through install, interrupted upgrade, and removal.

This model does not establish real package-manager behavior, filesystem atomicity,
service uptime, schema rollback, or support for another execution platform.
