---
name: docs-writer
description: Creates and updates organizational documents with consistent formatting, visual identity, and house style. Supports READMEs, API documentation, technical writing, user guides, changelogs, and PRDs. Use when a user asks to write or update documentation, needs a document created, requests any of the supported document types, or invokes the /docs-writer command.
---

# Document Writer

Creates documents with consistent formatting, metadata, and house style by dispatching
the `docs-writer` subagent with the appropriate template and writing standards.

## Step 1 — Collect Metadata

Before doing anything else, ask the user for:

1. **Author name** — Always prompt; never assume or skip.
2. **Document type** — README, API docs, technical writing, user guide, changelog, or PRD.
3. **Target file path** — Where the document will be written (e.g., `docs/user-guide.md`).
4. **Content scope** — What the document should cover.

Set **Created** and **Last Updated** to today's date. For updates to existing documents,
keep the original Created date and update only Last Updated.

## Step 2 — Load Resources

Read both files before dispatching the subagent:

- **Template**: Load the matching file from `assets/templates/` (see table below).
- **Writing standards**: Read `references/cas-writing-standards.md`.

| Document Type     | Template File                           |
| ----------------- | --------------------------------------- |
| README            | `assets/templates/readme.md`            |
| API Docs          | `assets/templates/api-docs.md`          |
| Technical Writing | `assets/templates/technical-writing.md` |
| User Guide        | `assets/templates/user-guide.md`        |
| Changelog         | `assets/templates/changelog.md`         |
| PRD               | `assets/templates/prd.md`               |

## Step 3 — Dispatch the Subagent

Use the `docs-writer` subagent (via the Agent tool with `subagent_type: "docs-writer"`).

Structure the prompt as follows:

```text
Write a [document type] for [project/feature name] and save it to [target file path].

Metadata:
- Author: [name]
- Created: [date]
- Last Updated: [date]

Content requirements:
[user's content requirements]

Use this template structure exactly:
[full template content]

Apply these writing standards:
[key standards from writing-standards.md]
```

## Step 4 — Verify

After the subagent completes:

1. Confirm the file exists at the target path.
2. Verify the metadata block (Author, Created, Last Updated) is present and correct.
3. Report the completed file path to the user.
