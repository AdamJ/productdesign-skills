# Product Design Skills

Productdesign-skills is a collection of Claude Code skills for product design and development workflows. Each skill is individually installable via the [productdesigner marketplace](https://github.com/AdamJ/productdesign-marketplace).

## What's Included

| Skill | Description | Category |
| --- | --- | --- |
| [Frontend Design](https://github.com/AdamJ/productdesign-skills/blob/main/skills/frontend-design) | Create distinctive, production-grade frontend interfaces with high design quality. | Design |
| [Accessibility Audit](https://github.com/AdamJ/productdesign-skills/blob/main/skills/accessibility-audit) | Audit components and pages against WCAG 2.1 AA; outputs a prioritized remediation checklist with code-level fixes. | Design |
| [App Store Connect](https://github.com/AdamJ/productdesign-skills/blob/main/skills/app-store-connect-audit) | Prepare an iOS, iPadOS, or macOS app's App Store assets and metadata for submission. | Development |
| [Interactive Architecture Diagram](https://github.com/AdamJ/productdesign-skills/blob/main/skills/interactive-diagram) | Generate interactive HTML architecture diagrams with zoom, click-through, and detail panels. | Development |
| [MCP Builder](https://github.com/AdamJ/productdesign-skills/blob/main/skills/mcp-builder) | Guide for creating high-quality MCP servers in Python (FastMCP) or TypeScript (MCP SDK). | Development |
| [MCP Server Scaffolding](https://github.com/AdamJ/productdesign-skills/blob/main/skills/mcp-server-scaffolding) | Scaffold MCP server projects with correct schema, validation, and deployment configuration. | Development |
| [Portfolio Case Study Writer](https://github.com/AdamJ/productdesign-skills/blob/main/skills/portfolio-case-study-generator) | Write and refine portfolio case studies for designers and PMs targeting founding or startup roles. | Documentation |
| [Syncing Project Documentation](https://github.com/AdamJ/productdesign-skills/blob/main/skills/synching-project-documentation) | Sync README, CLAUDE.md, and CHANGELOG after implementing features or fixes. | Documentation |
| [Organizational Docs Writer](https://github.com/AdamJ/productdesign-skills/blob/main/skills/organizational-docs-writer) | Create and update org documents with consistent formatting and house style. | Documentation |

## Installation

Skills are distributed via the [productdesigner marketplace](https://github.com/AdamJ/productdesign-marketplace). Add the marketplace first:

```
/plugin marketplace add AdamJ/productdesign-marketplace
```

Then install individual skills — no need to take everything at once:

```
/plugin install frontend-design@productdesigner
/plugin install accessibility-audit@productdesigner
/plugin install interactive-arch-diagram@productdesigner
/plugin install mcp-builder@productdesigner
/plugin install mcp-server-scaffolding@productdesigner
/plugin install portfolio-case-study-writer@productdesigner
/plugin install syncing-project-documentation@productdesigner
/plugin install organizational-docs-writer@productdesigner
```

### Verify Installation

Start a new session and make a request that should trigger a skill (e.g. "audit this component for accessibility"). Claude Code will automatically invoke the appropriate skill based on your task context.

## Development Conventions

- Each skill requires at minimum a `SKILL.md` with frontmatter (`name`, `description`)
- Reference files go in `skills/<name>/references/` and are linked from `SKILL.md`
- The `description` frontmatter field is the trigger — write it to match natural language phrases
- New skills should cross-reference related skills where relevant (e.g. `figma-to-code` → `design-tokens`)
- Any new skills or updates should bump the `version` in `.claude-plugin/plugin.json`:
  - New skill → major increment
  - Skill update → minor increment
  - README or CLAUDE.md change → patch increment
- New skills must be added to the table in this README

## Licensing

> MIT License — [LICENSE](https://github.com/AdamJ/productdesign-skills/blob/main/LICENSE)

All skills are subject to their original licensing, where applicable.

Original skills copyright 2026 [Adam J. Jolicoeur](mailto:contact@adamjolicoeur.com)
