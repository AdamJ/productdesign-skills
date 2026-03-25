---
name: interactive-arch-diagram
description: "Generates a fully self-contained interactive HTML architecture diagram for a software project. Use this skill whenever the user asks to \"visualize the architecture\", \"create a diagram of the project\", \"make an interactive map of the codebase\", \"diagram the system\", \"show how the pieces fit together\", or any request to produce an explorable/interactive visualization of a project's components, services, agents, APIs, or data flows. Also triggers on \"zoom into the architecture\", \"interactive diagram\", \"clickable diagram\", \"architecture overview with details\", \"show me the tech stack visually\", or \"I want to explore the codebase structure\". Always use this skill when the user wants something richer than a static diagram — especially if they mention zoom, click-through, detail panels, or multiple layers of information."
---
 
# Interactive Architecture Diagram
 
This skill produces a fully self-contained, interactive HTML file that lets users explore a software project's architecture through pan/zoom navigation, color-coded zones, and clickable nodes with rich detail panels.
 
## What the output looks like
 
- **D3.js pan/zoom canvas** — scroll to zoom, drag to pan, double-click to reset
- **Color-coded zones** — logical groupings (e.g., Frontend, Backend, External Services, Storage) each with a distinct color band
- **Clickable nodes** — every component, service, endpoint, or agent is a node; clicking opens a detail panel on the right
- **Detail panels** — description, responsibilities, code snippets, example prompts/requests, configuration notes, status indicators
- **Light/dark mode toggle** — respects system preference, persists to localStorage
- **Toolbar** — zoom in/out buttons, reset view, theme toggle
- **No external dependencies at runtime** — D3 is loaded from cdnjs; everything else is inline
 
## Clarifying questions (always ask before starting)
 
Before reading any files or building the diagram, ask the user these three questions in a single message. Use the AskUserQuestion tool with multiple choice options where applicable.
 
1. **Output scope** — Full technical deep-dive (all components, APIs, data flows, config) or a lighter overview (major zones and key flows only)?
2. **Visual style** — Dark mode default, light mode default, or use system preference? (Theme toggle is always included regardless.)
3. **Any specific areas to emphasize?** — Are there particular agents, services, or flows they want highlighted or given more detail?
 
## Step-by-step workflow
 
### 1. Read project documentation
 
Start with the key files that describe the project's architecture. Always read:
- `CLAUDE.md` or `README.md` at the repo root — these are gold; they often describe every module, environment variable, and pattern
- The main backend controller(s) — these reveal actual API endpoints and their logic
- The main frontend entry point / routing file — reveals pages, agents, and UI structure
- Any `.env.example` or documented environment variables
 
Use Glob to discover files if you're unsure of the structure:
```
CLAUDE.md, README.md, backend/src/**/*.controller.ts, frontend/src/App.tsx,
frontend/src/pages/*.tsx, backend/src/**/*.module.ts
```
 
Read selectively — you need enough to understand the system's shape, not every line of every file.
 
### 2. Identify the zones and nodes
 
After reading, mentally map the project into 3–6 logical zones. Common patterns:
- **Browser / Client** — what the user's browser runs (pages, components, hooks)
- **Frontend App** — the SPA framework layer (routing, state, SDK config)
- **Backend API** — controllers, services, middleware
- **External Services** — third-party APIs, AI platforms, auth providers
- **Storage** — databases, file stores, queues, logs
 
Within each zone, identify **nodes**: discrete components, endpoints, agents, or services. A node is anything a developer or architect would want to understand individually. Aim for 20–60 nodes depending on scope.
 
For each node capture:
- **id** — unique kebab-case identifier
- **label** — short display name (≤ 25 chars)
- **type** — `component`, `service`, `agent`, `endpoint`, `store`, `external`
- **description** — 1–3 sentence explanation of what it does
- **details** — deeper info: responsibilities, config, code snippet (optional), example inputs/outputs
- **status** — `active`, `wip`, `disabled`, or `missing`
 
**Important: flag incomplete configurations.** When reading project files, watch for features that are referenced in one place but not wired up in another — for example, an agent card in the frontend UI that has no corresponding entry in the backend type union or workflow ID map. Mark these with `status: "missing"` and include a ⚠ indicator in the diagram. This surfaces real gaps to the team and is one of the highest-value things the diagram can communicate.
 
### 3. Identify edges (data flows)
 
Map the connections between nodes. For each edge:
- **source / target** — node IDs
- **label** — short verb phrase (e.g., "POST /session", "streams tokens", "writes to")
- **color** — use the zone color of the source node for visual coherence
- **style** — `solid` for primary flows, `dashed` for optional/async/disabled flows
- **overTop** — set `true` for edges that cross zones in a way that would visually tangle (route them as arcs above the canvas)
 
### 4. Build the HTML file
 
Use the template below as the structural foundation. Fill in the `ZONES`, `NODES`, `EDGES`, `NODE_DETAILS`, and `AGENT_DETAILS` data structures.
 
**Key implementation details:**
 
#### Zone layout
Zones are rendered as labeled background rectangles. Lay them out left-to-right or in a logical spatial arrangement (client → frontend → backend → external). Calculate zone widths proportional to node count.
 
```javascript
const ZONES = [
  { id: 'frontend', label: 'Frontend', color: '#3B82F6', x: 20, y: 60, w: 300, h: 520 },
  { id: 'backend',  label: 'Backend',  color: '#10B981', x: 340, y: 60, w: 300, h: 520 },
  // ...
];
```
 
#### Node types and visual styles
Use a `NODE_STYLES` map keyed by `type` to assign fill, stroke, and text colors. In dark mode these are set via D3 `.attr()` as presentation attributes; in light mode they're overridden by CSS class rules (`.ntype-{type} .node-bg { fill: ...; stroke: ...; }`). This lets CSS handle theme switching without a full re-render.
 
```javascript
const NODE_STYLES = {
  component: { fill: '#1e3a5f', stroke: '#3B82F6', textColor: '#93c5fd' },
  agent:     { fill: '#2d1b69', stroke: '#8B5CF6', textColor: '#c4b5fd' },
  endpoint:  { fill: '#1a3a2a', stroke: '#10B981', textColor: '#6ee7b7' },
  store:     { fill: '#2d1f00', stroke: '#F59E0B', textColor: '#fcd34d' },
  external:  { fill: '#1e1a2e', stroke: '#6366F1', textColor: '#a5b4fc' },
  service:   { fill: '#1a2a1a', stroke: '#22C55E', textColor: '#86efac' },
};
```
 
#### Light/dark mode theming
The theme is controlled by `data-theme` on `<html>`. CSS custom properties handle backgrounds, text, and panel colors. SVG presentation attributes (set by D3) are overridden by CSS class selectors for node fills and zone fills in light mode.
 
Arrow marker colors require special handling — CSS can't easily target SVG `<defs>`. Store D3 selection references to each marker's `<path>` and update `fill` in JavaScript when the theme changes:
 
```javascript
const markerPaths = {};
function updateMarkerColors() {
  const LIGHT_EDGE_COLORS = { '#3B82F6': '#2563eb', '#10B981': '#059669', ... };
  Object.entries(markerPaths).forEach(([origColor, sel]) => {
    const col = currentTheme === 'light' ? (LIGHT_EDGE_COLORS[origColor] || origColor) : origColor;
    sel.attr('fill', col);
  });
}
```
 
#### Node hover (CSS only, no JS handlers)
```css
.node-group .node-bg { transition: filter 0.12s, stroke-width 0.12s; }
.node-group:hover .node-bg { filter: brightness(1.18); stroke-width: 2.5px; }
```
 
#### Detail panel
The right-side panel renders NODE_DETAILS on click. Structure it with sections: Overview, Responsibilities (if present), Code Snippet (collapsible `<pre>` block), Examples, Tags. For agents specifically, render AGENT_DETAILS with example prompts and workflow status.
 
**Agent detail panels must include example prompts** — 2–4 concrete example questions a user would type to that agent. This is the most useful thing the panel can show for AI agents.
 
Status indicators: use colored dots — green for `active`, yellow for `wip`, red for `disabled`, orange/⚠ for `missing`.
 
#### D3 zoom setup
```javascript
const zoom = d3.zoom()
  .scaleExtent([0.25, 3])
  .on('zoom', (event) => { mainGroup.attr('transform', event.transform); });
svg.call(zoom);
// Reset on double-click
svg.on('dblclick.zoom', () => {
  svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity);
});
```
 
### 5. Data integrity check
 
Before saving, run a quick internal consistency check:
- Every node ID referenced in edges exists in the nodes array
- Every zone ID referenced by a node exists in the zones array
- No duplicate node IDs
- Detail entries exist for all nodes that have a `details` property
 
### 6. Save and share
 
Save the file to the workspace folder:
```
/sessions/{session-id}/mnt/{workspace-name}/{project-name}-architecture.html
```
 
Provide a `computer://` link so the user can open it directly. The file should be entirely self-contained — no separate CSS/JS files needed.
 
## HTML file template structure
 
```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <title>{Project Name} Architecture</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
  <style>
    /* CSS custom properties for theming */
    :root[data-theme="dark"]  { --bg: #080d1a; --panel-bg: #0f172a; --text: #e2e8f0; ... }
    :root[data-theme="light"] { --bg: #eef2f7; --panel-bg: #ffffff; --text: #1e293b; ... }
 
    /* Light mode SVG overrides (higher specificity than D3 .attr() presentation attributes) */
    [data-theme="light"] .ntype-component .node-bg { fill: #eff6ff; stroke: #2563eb; }
    [data-theme="light"] .zone-frontend .zone-bg   { fill: rgba(59,130,246,0.07); stroke: rgba(59,130,246,0.35); }
 
    /* Hover effects (CSS only) */
    .node-group .node-bg { transition: filter 0.12s, stroke-width 0.12s; }
    .node-group:hover .node-bg { filter: brightness(1.18); stroke-width: 2.5px; }
  </style>
</head>
<body>
  <div id="header">...</div>
  <div id="main">
    <div id="canvas-wrapper">
      <svg id="main-svg">
        <defs><!-- arrow markers --></defs>
        <g id="main-group"><!-- zones, edges, nodes rendered by D3 --></g>
      </svg>
      <div id="toolbar"><!-- zoom/reset/theme buttons --></div>
    </div>
    <div id="detail-panel"><!-- node details rendered on click --></div>
  </div>
  <script>
    // Data: ZONES, NODES, EDGES, NODE_DETAILS, AGENT_DETAILS
    // Theme: init from localStorage / prefers-color-scheme
    // D3: render zones → edges → nodes
    // Interactions: click nodes, zoom/pan, theme toggle
  </script>
</body>
</html>
```
 
## Quality checklist before delivering
 
- [ ] All nodes are clickable and show a non-empty detail panel
- [ ] Agent detail panels include 2–4 example prompts (not just config metadata)
- [ ] Features referenced in one layer but missing in another are flagged as `status: "missing"` with ⚠
- [ ] Light mode and dark mode both look good (check contrast, readable labels)
- [ ] Zone labels are visible and not overlapping nodes
- [ ] Edge arrows render correctly in both themes
- [ ] Double-click resets the view
- [ ] File is self-contained (no broken external refs beyond D3 CDN)
- [ ] File saved to workspace and linked with computer:// URL
 
## Notes on common pitfalls
 
**Over-top edges**: When an edge would draw directly through an intermediate zone (e.g., frontend → external AI API, crossing the backend zone visually), route it with a cubic Bezier that arcs above the canvas top. Use a flag like `overTop: true` and compute the path as `M${sx},${sy} C${sx},-35 ${dx},-35 ${dx},${dy}`.
 
**SVG defs and CSS**: Arrow marker fills can't be styled purely with CSS. Store D3 path element references and imperatively update them in your `updateMarkerColors()` function when the theme changes.
 
**Node label truncation**: For long node names, either wrap text or truncate with ellipsis. SVG `text` elements don't word-wrap natively — use tspan elements or truncate to ~20 chars with a tooltip showing the full name.
 
**Zone sizing**: Don't hardcode pixel positions for zones if possible. Calculate them based on the number of nodes in each zone, with a minimum height. Nodes should be positioned in a grid within their zone with consistent margins.
 
**Endpoint granularity**: When asked for full technical depth, represent individual API endpoints as their own nodes (not a single "Controller" node). Each endpoint node should show its HTTP method, path, and brief description. This is the difference between a diagram that's actually useful for onboarding vs. one that just shows high-level boxes.
 
## Reminder
 
Always check for agents/features referenced in the frontend but missing from the backend type union.
