# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [2.1.0] - 2026-09-11

### Added

- `app-store-connect` skill - prepares an iOS, iPadOS, or macOS app's App Store assets and metadata for submission.
  - `skills/app-store-connect/SKILL.md`

## [2.0.0] - 2026-05-27

### Added

- `organizational-docs-writer` skill — creates and updates organizational documents (README, API docs, technical writing, user guides, changelogs, PRDs) with consistent formatting and house style
  — `skills/organizational-docs-writer/SKILL.md`, `skills/organizational-docs-writer/assets/templates/`, `skills/organizational-docs-writer/references/cas-writing-standards.md`
  (four-step workflow: collect metadata → load template + writing standards → dispatch docs-writer subagent → verify output)

## [1.0.2] - 2026-05-07

### Added

- `accessibility-audit` skill — WCAG 2.1 AA audit with prioritized remediation checklist; contrast ratio script; covers React, HTML, CSS tokens, Eleventy
  — `skills/accessibility-audit/`

## [1.0.1] - 2026-04-30

### Added

- `figma-to-code` skill — five-phase workflow using Figma MCP tools; references design-tokens skill for token mapping
  — `skills/figma-to-code/`
- `design-tokens` skill — three-tier token architecture; CSS vars, Tailwind v3/v4, Style Dictionary, JS ESM output formats
  — `skills/design-tokens/`

## [1.0.0] - 2026-04-01

### Added

- Initial skill set: `frontend-design`, `interactive-diagram`, `mcp-builder`, `mcp-server-scaffolding`, `portfolio-case-study-generator`, `synching-project-documentation`
