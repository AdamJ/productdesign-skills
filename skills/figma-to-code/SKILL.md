---
name: figma-to-code
description: >
  Converts Figma designs into production-ready code adapted to the project's stack, components,
  and design token system. Use when the user shares a figma.com URL (design, board, slides, or
  make file), asks to implement a Figma design, or says "build this" while sharing a Figma link.
  Coordinates the Figma MCP tools, the design-tokens skill, and the frontend-design skill into
  a single structured workflow.
---

# Figma-to-Code Skill

## Core Philosophy

The Figma MCP returns **reference code** — a starting point enriched with design intent, not
final output. Treat it like a senior designer's redline annotation: precise on values, agnostic
about your stack. Your job is adaptation, not transcription.

Three things to never do with raw Figma output:
- Copy hardcoded hex values into component styles (map them to tokens instead)
- Use absolute positioning from a Figma auto-layout conversion verbatim (rewrite as flexbox/grid)
- Paste generated JSX without checking it against the project's existing component library

---

## URL Parsing

Before calling any tool, extract the `fileKey` and `nodeId` from the URL:

| URL pattern | fileKey | nodeId |
|-------------|---------|--------|
| `figma.com/design/:fileKey/...?node-id=1-2` | `:fileKey` | `1:2` (replace `-` with `:`) |
| `figma.com/design/:fileKey/branch/:branchKey/...` | `:branchKey` | from `node-id` param |
| `figma.com/make/:makeFileKey/...` | `:makeFileKey` | from `node-id` param |
| `figma.com/board/:fileKey/...` | `:fileKey` | from `node-id` param — use `get_figjam` |
| `figma.com/slides/:fileKey/...` | `:fileKey` | from `node-id` param |

If no `node-id` is present in the URL, call `get_metadata` with the fileKey and root nodeId
(`0:1`) to list the page structure, then identify the correct node to target.

---

## Workflow

### Phase 1 — Read the design

**Step 1: Call `get_design_context`** (always first, always required)

This is the primary tool. It returns:
- Generated reference code (React + Tailwind by default)
- A screenshot of the node
- Code Connect snippets if the file has mappings set up
- Design annotations and constraints from the designer
- Asset download URLs for images and icons

Pass `clientFrameworks` and `clientLanguages` based on what the project uses. This affects
how the returned code hints are shaped.

**Step 2: Read the screenshot**

Before touching the code output, study the screenshot to understand:
- Overall layout direction (vertical stack, horizontal row, grid, overlay)
- Visual hierarchy (what's prominent, what's secondary)
- Interactive affordances (what looks clickable, what's a label)
- Spacing rhythm and density

The screenshot is ground truth. If the generated code conflicts with what the screenshot
shows, trust the screenshot.

**Step 3: Call `get_variable_defs`** (when the file uses Figma variables)

If `get_design_context` returns values that look like token references (e.g., color names
rather than hex codes, or variable IDs), call `get_variable_defs` to resolve them. This
returns the full variable collection for the node — the foundation for token mapping in
Phase 3.

See [figma-mcp-tools.md](./references/figma-mcp-tools.md) for when to use other tools.

---

### Phase 2 — Audit context

Before writing any code, answer these questions:

**Does this file have Code Connect mappings?**
If `get_design_context` returned Code Connect snippets (not raw JSX), use those component
imports directly. Code Connect is the authoritative mapping from Figma component → codebase
component. Skip generating that component from scratch.

**Does the project have a design token system?**
Check for `tokens/`, `styles/tokens.css`, Tailwind config with token-named keys, or any CSS
custom property file. If tokens exist, every design value must map through them.
If tokens don't exist yet, invoke the **design-tokens skill** before continuing —
implement the token system first, then resume this workflow.

**What is the target stack?**
Confirm: framework (React/Vue/Svelte/plain HTML), styling approach (CSS modules/Tailwind/
styled-components/CSS custom properties), component library if any. This determines the
adaptation patterns to apply in Phase 4.

**What is the scope?**
A single component, a full page, or a design system batch? For full pages, break the work
into sections and implement each section as a separate component.

---

### Phase 3 — Map tokens

This is the bridge between Figma and the project's design-tokens system.

**If `get_variable_defs` returned data:**
Map each Figma variable to its project token equivalent using the naming conventions from
the design-tokens skill:

```
Figma variable name              → Project token
────────────────────────────────────────────────
color/text/primary               → --color-text-primary
color/background/surface         → --color-bg-surface
color/brand/action               → --color-action-primary
spacing/component/md             → --space-component-md
typography/size/heading-lg       → --font-size-heading-lg
radius/card                      → --radius-card
```

Figma variable collections map to token tiers:
- "Primitives" or "Core" collection → Tier 1 primitives
- "Semantic" or "Alias" collection → Tier 2 semantics
- "Component" collection → Tier 3 component tokens

**If Figma returned raw hex values (no variables):**
Reverse-map each hardcoded value to the nearest primitive token, then check if a semantic
token covers its purpose in context. See [adaptation-guide.md](./references/adaptation-guide.md)
for the full reverse-mapping process.

**Token gap report:**
Any Figma value that has no project token equivalent is a gap. Do not silently approximate it
with a nearby token. Surface the gap explicitly:

```
Token gaps found:
- Figma uses #7C3AED (violet-600) for the badge background — no --color-* token covers
  this. Options: (a) add --color-bg-badge to semantics, (b) add violet primitives,
  (c) confirm this is a one-off and use the primitive directly.
```

Ask the user to resolve gaps before finalizing the implementation, or propose a resolution
and note it clearly.

---

### Phase 4 — Adapt the code

Never use Figma's generated code verbatim. Apply all of the following:

**Token substitution** (see [adaptation-guide.md](./references/adaptation-guide.md))
Replace every hardcoded value with the token reference identified in Phase 3.

**Layout rewrite**
Figma auto-layout converts to absolute positioning or inline styles. Rewrite as semantic
CSS layout:
- Vertical stacks → `display: flex; flex-direction: column; gap: var(--space-gap-md)`
- Horizontal rows → `display: flex; align-items: center; gap: var(--space-gap-sm)`
- Grids → `display: grid; grid-template-columns: ...`
- Overlays → `position: relative` on parent, `position: absolute` only for genuinely
  positioned elements (badges, tooltips, floating actions)

**Component substitution**
Where the Figma design uses components that exist in the project's library (Button, Input,
Badge, Icon, Avatar, etc.), use the project's component — not a reimplementation. Only build
net-new components.

**Interaction and state**
Figma only shows static states. For interactive components, implement:
- Hover state using the corresponding `-hover` token
- Focus state using `--color-border-focus` and `--shadow-input-focus`
- Disabled state using `-disabled` tokens and `pointer-events: none`
- Loading state if the component can load data

**Accessibility**
Follow the standards from the frontend-design skill:
- Semantic HTML (`<button>`, `<nav>`, `<article>`, `<label>`, not `<div>` for everything)
- ARIA labels on icon-only controls
- Keyboard navigation (Tab, Enter, Space, Escape)
- Color contrast: verify Figma's color pairs pass WCAG AA (4.5:1 text, 3:1 UI elements)

**Assets**
For images and icons returned in the `get_design_context` asset URLs:
- Icons: prefer SVG inline or sprite; download from the asset URL
- Images: reference by path; note that the asset URL is temporary and must be downloaded
- Do not embed base64 images in component code unless the asset is a tiny icon (<1 KB)

---

### Phase 5 — Deliver

Provide:

1. **Component file(s)** — adapted, production-ready code in the project's stack
2. **Token mapping summary** — table of Figma values → project tokens used
3. **Gap report** — any unmapped values with proposed resolutions
4. **Asset checklist** — list of images/icons to download and where to place them
5. **Integration note** — how to import and use the new component (one paragraph)

If the scope was a full page, additionally provide a brief **component tree** showing how the
pieces compose.

---

## Handling Different Response Types from `get_design_context`

The Figma MCP response varies based on how the file is set up. Know how to read each:

### Code Connect snippets present
The response includes imports from your actual codebase. This means the designer has linked
Figma components to real components via Code Connect.
→ Use those imports directly. Do not reimplement the component.
→ Focus adaptation effort on the surrounding layout and composition, not the mapped components.

### Component documentation links present
The response references external docs for a component.
→ Follow the link to understand usage constraints before implementing.
→ The designer may have specified props or variants — honor them.

### Design annotations present
The response includes notes or constraints from the designer (e.g., "minimum touch target
44px", "do not truncate this label", "this padding is intentional for optical alignment").
→ These are requirements, not suggestions. Implement them exactly.

### Raw hex / absolute positioning only
The file uses no variables and no Code Connect.
→ This is a loosely structured design. The screenshot is the primary reference.
→ Apply full adaptation: reverse-map values to tokens, rewrite layout, use project components.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using Figma output as final code | Always adapt — at minimum replace hardcoded values with tokens |
| Silently approximating unmapped tokens | Surface every gap explicitly; ask or propose a resolution |
| Reimplementing mapped components | Check Code Connect response first; use existing components |
| Ignoring the screenshot | Read the screenshot before reading the code; it shows true intent |
| Building the whole page in one component | Break into sections; compose components |
| Skipping interactive states | Hover, focus, disabled are required for any interactive element |
| Using absolute positioning from Figma output | Rewrite as flex/grid with token-based gaps |
| Downloading assets manually in code | List assets in the delivery checklist; don't embed temp URLs |

---

## Integration with Other Skills

**design-tokens** (this repo):
Always invoke before this skill if the project has no token system yet. Once tokens exist,
Phase 3 of this workflow maps Figma variables directly to the token file.
See: `skills/design-tokens/SKILL.md`

**frontend-design** (this repo):
Apply its design principles during Phase 4 adaptation — particularly the guidance on avoiding
generic AI aesthetics, building with progressive enhancement, and meeting the quality checklist.
See: `skills/frontend-design/SKILL.md`

**Code Connect** (Figma MCP):
If the project has a component library worth linking, consider setting up Code Connect
mappings after implementing components. See [figma-mcp-tools.md](./references/figma-mcp-tools.md)
for the Code Connect workflow.
