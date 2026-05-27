# productdesigner — Agent Notes

## What this repo is

A Claude Code skills marketplace for product design workflows. Skills live in `skills/<name>/SKILL.md`
with optional reference files in `skills/<name>/references/`.

Plugin metadata: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

---

## Skills status

### Shipped (in `main`)

| Skill | Directory | Notes |
|-------|-----------| ----- |
| frontend-design | `skills/frontend-design/` | |
| interactive-diagram | `skills/interactive-diagram/` | |
| mcp-builder | `skills/mcp-builder/` | |
| mcp-server-scaffolding | `skills/mcp-server-scaffolding/` | |
| portfolio-case-study-generator | `skills/portfolio-case-study-generator/` | |
| synching-project-documentation | `skills/synching-project-documentation/` | |
| design-tokens | `skills/design-tokens/` | Three-tier token architecture; CSS vars, Tailwind v3/v4, Style Dictionary, JS ESM output formats |
| figma-to-code | `skills/figma-to-code/` | Five-phase workflow using Figma MCP tools; references design-tokens skill for token mapping |
| accessibility-audit | `skills/accessibility-audit/` | WCAG 2.1 AA audit with prioritized remediation output; contrast script; covers React, HTML, CSS tokens, Eleventy |
| organizational-docs-writer | `skills/organizational-docs-writer/` | Creates/updates org docs (README, API docs, user guides, changelogs, PRDs) with consistent formatting via subagent dispatch; templates in `assets/templates/`; writing standards in `references/cas-writing-standards.md` |

### Proposed (not yet implemented)

These were brainstormed and agreed upon — implement in priority order:

| Skill | Purpose | Priority |
|-------|---------|----------|
| ~~**accessibility-audit**~~ | ~~Audit components against WCAG 2.1 AA; output prioritized remediation checklist~~ | ~~High~~ → **Shipped** |
| **mcp-test-suite** | Generate evaluation harness (tool call stubs, edge case fixtures, prompt tests) for an MCP server | High |
| **data-visualization** | Self-contained D3.js/Observable charts (bar, line, scatter, sankey) with proper scales and responsive behavior | Medium |
| **motion-design** | Purposeful CSS/JS animations and transitions with easing curves and timing guidelines | Medium |
| **ux-copywriting** | UI microcopy — labels, empty states, error messages, onboarding tooltips — aligned to product voice | Medium |
| **changelog-generator** | Structured CHANGELOG entry from git log, formatted by conventional commits or custom schema | Low |

---

## Development conventions

- Each skill needs at minimum: `SKILL.md` with frontmatter (`name`, `description`)
- Reference files go in `skills/<name>/references/` and are linked from SKILL.md
- The `description` frontmatter field is the trigger — write it to fire on natural language phrases
- New skills should cross-reference related skills (e.g. figma-to-code → design-tokens)
- Any new skills or updates to skills should increment the version numbers found in the `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` files.
- New skills are a major increment, updates to skills are a minor increment, and changes to `CLAUDE.md` or `README.md` are patch increments.
- New skills need to be added to the README.md file, in the "What's Included" section.
