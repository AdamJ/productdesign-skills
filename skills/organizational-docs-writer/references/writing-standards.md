# Writing Standards

## Voice and Tone

- Use a formal, professional tone throughout all documents.
- Do not use contractions (use "do not" instead of "don't", "will not" instead of "won't").
- Prefer active voice over passive voice.
- Write in present tense for descriptions, instructions, and reference content.
- Write in past tense for changelog entries describing completed changes.
- Address the reader directly as "you" in user-facing guides.
- Use "the user" or "users" in technical and internal documents.

## Grammar and Punctuation

- Always use the Oxford (serial) comma in lists of three or more items.
  - Correct: "The system supports reading, writing, and deleting records."
  - Incorrect: "The system supports reading, writing and deleting records."
- Use em dashes (—) for parenthetical phrases, not hyphens or double hyphens.
- Spell out numbers one through nine; use numerals for 10 and above.
- Spell out numbers at the start of a sentence regardless of value.
- Use title case for all headings.

## Document Metadata

Every document must begin with the following metadata block immediately after the H1 title:

```markdown
**Author:** [Full Name]
**Created:** [Month DD, YYYY]
**Last Updated:** [Month DD, YYYY]
```

Date format: `Month DD, YYYY` — for example, `May 5, 2026`.

---

## Heading Hierarchy

- H1 (`#`): Document title only — one per document.
- H2 (`##`): Major sections.
- H3 (`###`): Subsections within a major section.
- H4 (`####`): Use sparingly for deep nesting; prefer restructuring if needed.
- Never skip heading levels (e.g., do not jump from H2 to H4).

## Lists

- Use **numbered lists** for sequential steps or ranked items.
- Use **bullet lists** for non-sequential items or feature lists.
- Keep list items parallel in grammatical structure.
- Begin each list item with a capital letter.
- Do not end list items with periods unless they are complete sentences.

## Code and Technical Content

- Wrap all code, commands, file paths, and technical strings in backticks or code blocks.
- Use fenced code blocks (triple backtick) with a language identifier for multi-line code.
- Use inline backticks for short code references within prose.
- Always include realistic placeholder values in code examples (not `foo`, `bar`, `test`).

## Tables

- Use tables for structured comparisons, option lists, and parameter references.
- Always include a header row with bold labels.
- Align column content consistently (left-align text, right-align numbers).

## Links

- Use descriptive link text; do not use "click here" or bare URLs in prose.
- Correct: `See the [Authentication Guide](./auth.md) for setup instructions.`
- Incorrect: `Click [here](./auth.md) for setup instructions.`

## Callouts and Notes

Use blockquotes for notes, warnings, and tips:

```markdown
> **Note:** [Content]

> **Warning:** [Content]

> **Tip:** [Content]
```

## Changelog Entries

Follow the [Keep a Changelog](https://keepachangelog.com) format:

- Group entries under: `Added`, `Changed`, `Fixed`, `Removed`, `Deprecated`, `Security`.
- Write entries in past tense.
- Each entry should describe what changed and why it matters to the user.
- Reference issue or PR numbers when available (e.g., `Fixed pagination bug (#42).`).
