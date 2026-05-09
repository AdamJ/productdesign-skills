---
name: design-tokens
description: >
  Creates and manages design token systems — the single source of truth for visual decisions
  (color, spacing, typography, shadow, radius, motion, z-index). Use when setting up a design
  system, defining CSS custom properties, generating a Tailwind theme config, extracting tokens
  from Figma, auditing inconsistent hardcoded values, or migrating scattered magic numbers into
  a structured token architecture.
---

# Design Tokens Skill

## Core Philosophy

Design tokens are **named design decisions**, not just variables. Every token carries intent:
`--color-text-danger` explains *purpose*; `#ef4444` explains nothing. A well-structured token
system lets a codebase change its visual language by editing one file — and lets a team
communicate in shared vocabulary instead of hex codes.

The goal is a **layered system** where primitive values feed semantic aliases, which feed
component-level overrides. Never skip layers to add speed — a flat list of hex codes is not
a token system.

---

## Token Architecture

### Three-Tier Model

```
Primitives  →  Semantics  →  (Components)
──────────────────────────────────────────
Raw values     Purpose-         Scoped
(no context)   named aliases    overrides
```

**Tier 1 — Primitives**: Every raw value the design uses, named by *what it is*.
```css
--color-red-500: #ef4444;
--space-4: 1rem;
--font-size-lg: 1.125rem;
```

**Tier 2 — Semantics**: Aliases that express *how* a primitive is used. This tier is what
components consume. Never consume primitives directly in component styles.
```css
--color-text-danger: var(--color-red-500);
--space-component-gap: var(--space-4);
```

**Tier 3 — Component tokens** (optional, for large systems): Scoped overrides per component.
Add this tier only when a semantic token doesn't cover a specific component need without
becoming too narrow to share.
```css
/* In button context */
--button-bg-destructive: var(--color-bg-danger);
```

---

## Workflow

### Step 1 — Audit the context

Before writing any tokens, answer:
- Does a Figma file exist? → Use the Figma MCP to extract exact values with `get_variable_defs`
  or `get_design_context`. Don't approximate.
- Is there an existing codebase? → Grep for hardcoded hex values, `px` sizes, and
  font stacks. These are your primitive candidates.
- What is the target output? → CSS custom properties, Tailwind config, Style Dictionary JSON,
  or a combination. See [output-formats.md](./references/output-formats.md).
- What framework? → Affects token consumption patterns (CSS vars vs. JS objects vs. theme keys).

### Step 2 — Build primitives

Define every raw value first. Include the full scale for each category — don't pre-filter
based on assumed usage.

| Category   | Scale strategy                                          |
|------------|---------------------------------------------------------|
| Color      | Per-hue numeric scale (50–950), plus neutrals           |
| Space      | Powers-of-two rem scale (0.25rem → 4rem), then named    |
| Font size  | Modular scale (1.125 ratio or custom)                   |
| Font weight | Named weights only (400, 500, 600, 700)                |
| Line height | Unitless values (1, 1.25, 1.5, 1.75)                   |
| Radius     | Named scale (none, sm, md, lg, full)                    |
| Shadow     | Named scale (none, sm, md, lg, xl)                      |
| Duration   | Named scale (instant, fast, normal, slow)               |
| Easing     | Named functions (ease-in, ease-out, spring)             |
| Z-index    | Named layers (base, raised, dropdown, modal, toast)     |

### Step 3 — Build semantics

Map primitives to semantic roles. For each category, define:
- **Default/base** state
- **Emphasis** variants (subtle, strong)
- **Interactive** states (hover, active, focus, disabled)
- **Feedback** roles (success, warning, danger, info)
- **Brand** roles (primary, secondary, accent)

### Step 4 — Output

Generate output in the target format(s). See [output-formats.md](./references/output-formats.md)
for complete templates covering:
- CSS custom properties (`:root` + scoped layers)
- Tailwind v3 `theme.extend` and v4 `@theme`
- Style Dictionary W3C DTCG JSON

### Step 5 — Validate

Before completing:
- [ ] All semantic tokens reference primitives — no raw values in semantics
- [ ] Color pairs (foreground + background) pass WCAG AA contrast (4.5:1 for text, 3:1 for UI)
- [ ] Every semantic name describes purpose, not appearance
- [ ] No orphan primitives (every primitive is referenced by at least one semantic token)
- [ ] Dark mode semantic tokens are defined if the project requires them

---

## Naming Conventions

See [token-naming.md](./references/token-naming.md) for the complete naming reference.

**Quick rules:**
- Format: `--[category]-[role]-[variant]-[state]`
- Describe *purpose*, not *appearance*: `--color-text-secondary` not `--color-gray`
- Use numeric scales for primitives (300, 500, 700), semantic names for semantics (subtle, default, strong)
- State suffixes: `-hover`, `-active`, `-focus`, `-disabled`, `-placeholder`
- Dark mode: prefer semantic inversion over separate token sets

---

## Figma Integration

When a Figma file is available, extract tokens rather than authoring them:

1. Use `get_variable_defs` to pull the file's variable collections directly.
2. Map Figma variable collections to token tiers: Figma "Primitives" collection → Tier 1,
   "Semantic" or "Alias" collection → Tier 2.
3. Preserve the exact values — don't round or approximate Figma values.
4. If Figma variables don't exist, use `get_design_context` on representative frames and
   extract colors, spacing, and type styles from the generated code hints.
5. Note any Figma tokens that have no codebase equivalent — surface these as gaps, not errors.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Semantic names describing appearance (`--color-blue-button`) | Rename to describe purpose (`--color-action-primary`) |
| Components consuming primitives directly | Add a semantic alias; components reference semantics only |
| Flat list of variables with no tier separation | Restructure into primitives + semantics files |
| Missing interactive states in semantics | Add `-hover`, `-focus`, `-disabled` variants for interactive tokens |
| Color-only token system | Add spacing, typography, radius, shadow, motion — incomplete systems breed hardcoded values |
| Separate dark mode token files | Use CSS `[data-theme="dark"]` or `@media (prefers-color-scheme: dark)` to override semantic tokens only; primitives don't change |

---

## Output Format

For a new token system, deliver:

1. **Primitive tokens file** — all raw values, organized by category
2. **Semantic tokens file** — all purpose-named aliases referencing primitives
3. **Integration note** — how to import/use in the target stack (one paragraph)
4. **Gap report** — any category missing from the provided design (e.g., "no motion tokens found in Figma — recommend adding")

For an audit of an existing codebase, deliver:

1. **Inventory** — all hardcoded values found, grouped by category and frequency
2. **Proposed primitives** — consolidated unique values
3. **Proposed semantics** — purpose-named aliases for the inventory
4. **Migration path** — file-by-file replacement plan, starting with highest-frequency values
