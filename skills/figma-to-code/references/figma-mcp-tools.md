# Figma MCP Tools Reference

Quick reference for every Figma MCP tool available in this environment, when to call each,
and what to do with the response.

---

## Primary Tool

### `get_design_context`

**When:** Always — this is the first call in any figma-to-code workflow.

**What it returns:**
- `code` — reference React + Tailwind (or framework-matched) implementation
- `screenshot` — rendered PNG of the node; read this before the code
- Code Connect snippets if the file has mappings (component imports from your codebase)
- Asset download URLs for images and icons
- Design annotations from the designer
- Token/variable references if the file uses Figma variables

**Parameters to set:**
- `nodeId` — extracted from URL (convert `-` to `:` in node-id)
- `fileKey` — extracted from URL
- `clientFrameworks` — e.g. `"react"`, `"vue"`, `"svelte"`, `"unknown"`
- `clientLanguages` — e.g. `"typescript"`, `"javascript,css"`, `"unknown"`
- `excludeScreenshot: false` — always keep screenshot; it's the ground truth
- `disableCodeConnect: false` — always allow Code Connect; it maps to real components

**Do not set:**
- `forceCode: true` — only if explicitly asked; large nodes may return metadata-only by default
  for good reason (too large to be useful as a single block)

**After calling:**
1. Read the screenshot first
2. Check if Code Connect snippets are present — if so, use mapped components directly
3. Check for designer annotations — these are requirements
4. Then read the generated code as reference

---

## Token Extraction

### `get_variable_defs`

**When:** Call after `get_design_context` if:
- The generated code references variable names rather than raw hex values
- You need to build or update the project's design token system from this file
- The user asks to "extract tokens" or "sync tokens from Figma"

**What it returns:**
A map of variable names to resolved values, e.g.:
```
{ "color/text/primary": "#111827", "spacing/component/md": "16px" }
```

**How to use:**
Map each variable name to a project token using the naming conventions in
`skills/design-tokens/references/token-naming.md`. The `/` separators in Figma variable
names correspond to `-` separators in CSS custom property names.

```
Figma: color/text/primary  →  CSS: --color-text-primary
Figma: spacing/layout/lg   →  CSS: --space-layout-lg
Figma: radius/card         →  CSS: --radius-card
```

**Note:** `get_variable_defs` resolves variables for the given node's scope. For a full
file token extraction, call it with the root page node ID (`0:1` or the page node).

---

## Structure Exploration

### `get_metadata`

**When:** Use only when you need to understand the file's layer structure without generating
code. Common cases:
- No `node-id` in the URL — need to find the right node to target
- A frame is too large and `get_design_context` returns metadata-only — use this to identify
  child sections to call individually
- Verifying layer names before batch-processing multiple nodes

**What it returns:** XML describing node IDs, types, names, positions, and sizes. Does not
include styles, colors, or code.

**After calling:** Use the returned node IDs to make targeted `get_design_context` calls on
individual sections.

**Do not use for:**
- Figma Make files (not supported)
- Getting actual design values — use `get_design_context` for that

---

## Screenshots

### `get_screenshot`

**When:** Use only if you need a standalone screenshot of a node without triggering full code
generation. Use cases:
- Comparing before/after states by capturing two nodes separately
- Getting a higher-resolution render of a detail (`maxDimension: 2048`)
- Inspecting a node that `get_design_context` can't process (very large frames)

**Parameters:**
- `maxDimension` — default 1024. Increase to 2048+ when inspecting fine detail (typography,
  icon paths, subtle shadows). Decrease to 256–512 for thumbnails.
- `enableBase64Response: false` — keep false unless you cannot fetch URLs from the environment

**Note:** `get_design_context` already includes a screenshot. Only call `get_screenshot`
separately when you have a specific reason.

---

## Code Connect Workflow

Code Connect links Figma components to real codebase components so `get_design_context`
returns actual component imports instead of generated JSX. Setting it up is a one-time
investment that permanently improves design-to-code accuracy.

### `get_code_connect_suggestions`

**When:** The project has an established component library and you want to link its components
to their Figma counterparts.

**What it returns:** AI-suggested mappings between Figma component nodes and candidate
codebase components, with confidence scores.

**Workflow:**
1. Call `get_code_connect_suggestions` with the frame or component set node
2. Review suggestions with the user — confirm or correct each mapping
3. Call `send_code_connect_mappings` to save approved mappings to Figma

### `get_code_connect_map`

**When:** Checking what Code Connect mappings already exist for a file before deciding
whether to generate code or use existing mappings.

### `get_context_for_code_connect`

**When:** Building or updating Code Connect definitions — returns the context needed to
write a `.figma.tsx` (or equivalent) Code Connect file for a component.

### `send_code_connect_mappings`

**When:** Saving approved Code Connect mappings after reviewing `get_code_connect_suggestions`.
This writes the mappings back to Figma so future `get_design_context` calls return the
mapped imports.

### `add_code_connect_map`

**When:** Manually adding a Code Connect mapping for a specific node-to-component pair,
without going through the suggestions flow.

---

## Design System Search

### `search_design_system`

**When:** You know a component exists in the design system but don't have its node ID.
Search by component name (e.g., "Button", "Avatar", "Tag") to find the relevant node,
then call `get_design_context` on it.

### `get_libraries`

**When:** The file uses shared library components and you need to identify which library
they come from — useful when Code Connect mappings reference library components that live
in a different file.

---

## FigJam

### `get_figjam`

**When:** The URL is `figma.com/board/...`. FigJam files are whiteboards, not design files —
use `get_figjam` instead of `get_design_context`. Returns the board's content (sticky notes,
shapes, connectors, text) as structured data.

**Common use:** Reading flow diagrams, user journey maps, brainstorming boards to understand
design intent before implementing.

---

## Tool Decision Tree

```
User shares a Figma URL
        │
        ├─ figma.com/board/...  ──────────────────→  get_figjam
        │
        ├─ figma.com/design/... or /make/... or /slides/...
        │         │
        │         ├─ Has node-id?  ──── Yes ──→  get_design_context  ──→  Phase 2
        │         │
        │         └─ No node-id  ────────────→  get_metadata (root)
        │                                              │
        │                                        Find target node
        │                                              │
        │                                       get_design_context
        │
        └─ After get_design_context:
                  │
                  ├─ Response has variable references?  ──→  get_variable_defs
                  │
                  ├─ Response too large / metadata-only?  ──→  get_metadata → section by section
                  │
                  └─ Need to set up Code Connect?  ──→  get_code_connect_suggestions
```

---

## What the `get_design_context` Response Tells You

| Response characteristic | What it means | Action |
|------------------------|---------------|--------|
| Imports from `@/components/...` or project paths | Code Connect is set up | Use those imports; don't reimplement |
| Raw JSX with inline styles | No Code Connect; loosely structured file | Full adaptation required |
| `var(--color-...)` in styles | File uses CSS variable tokens | Map to project's token system |
| `#xxxxxx` hardcoded colors | File uses no variables | Reverse-map to tokens manually |
| `position: absolute` with specific px offsets | Auto-layout not used or overlay element | Rewrite as flex/grid unless truly an overlay |
| Designer annotation blocks | Explicit constraints from designer | These are requirements — implement exactly |
| Asset URL entries | Icons or images in the design | Download and place; do not inline temp URLs |
| `forceCode` returned metadata only | Node is very large | Break into sub-nodes via `get_metadata` |
