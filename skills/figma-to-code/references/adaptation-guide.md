# Adaptation Guide

Concrete rules for converting Figma MCP output into project-appropriate code. Apply every
section in this guide to every component — none are optional.

---

## Token Substitution

### Color reverse-mapping

When Figma returns raw hex values, map them to tokens in two steps:

**Step 1 — Find the primitive.** Match the hex to the nearest primitive token scale.
Use the numeric scale (50–950) from `skills/design-tokens/references/token-naming.md`:

```
#ffffff  →  --color-neutral-0
#f9fafb  →  --color-neutral-50
#111827  →  --color-neutral-900
#3b82f6  →  --color-blue-500
#2563eb  →  --color-blue-600
#ef4444  →  --color-red-500
#dc2626  →  --color-red-600
```

**Step 2 — Find the semantic.** Determine purpose from context, then use the semantic token:

```
Body text on white     →  --color-text-primary      (not --color-neutral-900)
Secondary label        →  --color-text-secondary     (not --color-neutral-600)
Card background        →  --color-bg-surface         (not --color-neutral-0)
Page background        →  --color-bg-canvas          (not --color-neutral-50)
Primary button fill    →  --color-action-primary     (not --color-blue-600)
Button text on primary →  --color-action-primary-text
Danger text            →  --color-text-danger        (not --color-red-600)
Input border           →  --color-border-default
Focus ring             →  --color-border-focus
```

**Rule:** Always go primitive → semantic. Never use a primitive directly in a component style.

### Spacing reverse-mapping

```
2px   →  --space-px + 1  (rare; use sparingly)
4px   →  --space-1  →  semantic: --space-component-xs or --space-gap-xs
8px   →  --space-2  →  semantic: --space-component-sm or --space-gap-sm
12px  →  --space-3  →  semantic: --space-component-md
16px  →  --space-4  →  semantic: --space-component-lg or --space-gap-md
24px  →  --space-6  →  semantic: --space-component-xl or --space-gap-lg
32px  →  --space-8  →  semantic: --space-gap-xl or --space-layout-xs
48px  →  --space-12 →  semantic: --space-layout-sm
64px  →  --space-16 →  semantic: --space-layout-md
96px  →  --space-24 →  semantic: --space-layout-lg
```

Determine which semantic category based on role:
- Inside a single component (padding, icon gap) → `--space-component-*`
- Between sibling items in a list or row → `--space-gap-*`
- Between sections on a page → `--space-layout-*`

### Typography reverse-mapping

```
10px / 0.625rem  →  --font-size-2xs
12px / 0.75rem   →  --font-size-xs  →  semantic: --font-size-caption
14px / 0.875rem  →  --font-size-sm  →  semantic: --font-size-label or --font-size-body-sm
16px / 1rem      →  --font-size-md  →  semantic: --font-size-body
18px / 1.125rem  →  --font-size-lg  →  semantic: --font-size-body-lg or --font-size-heading-sm
24px / 1.5rem    →  --font-size-2xl →  semantic: --font-size-heading-md
30px / 1.875rem  →  --font-size-3xl →  semantic: --font-size-heading-lg
36px / 2.25rem   →  --font-size-4xl →  semantic: --font-size-heading-xl
48px / 3rem      →  --font-size-5xl →  semantic: --font-size-display
```

For line height: Figma often shows computed px values. Convert to unitless ratios:
```
line-height: 20px on 14px text  →  20/14 = 1.43  →  --line-height-normal (1.5)
line-height: 28px on 24px text  →  28/24 = 1.17  →  --line-height-tight (1.25)
line-height: 32px on 24px text  →  32/24 = 1.33  →  --line-height-snug (1.375)
```

### Radius reverse-mapping

```
0px     →  --radius-none
2px     →  --radius-1   →  semantic: --radius-tooltip
4px     →  --radius-2   →  semantic: --radius-button or --radius-input
6px     →  --radius-3
8px     →  --radius-4   →  semantic: --radius-card
12px    →  --radius-6   →  semantic: --radius-modal
16px    →  --radius-8
9999px  →  --radius-full →  semantic: --radius-badge or --radius-tag
```

### Shadow reverse-mapping

```
No shadow                                  →  --shadow-none
Subtle (0 1px 2px, low opacity)           →  --shadow-xs  →  --shadow-button
Light (0 1px 3px + 0 1px 2px)            →  --shadow-sm  →  --shadow-card
Medium (0 4px 6px + 0 2px 4px)           →  --shadow-md  →  --shadow-raised
Heavy (0 10px 15px + 0 4px 6px)          →  --shadow-lg  →  --shadow-dropdown
Strong (0 20px 25px + 0 8px 10px)        →  --shadow-xl
Maximum (0 25px 50px, high opacity)      →  --shadow-2xl →  --shadow-modal
```

---

## Layout Rewriting

Figma's code generation converts auto-layout to flexbox but often adds unnecessary
`position: absolute`, fixed `width`/`height`, or duplicated sizing. Rewrite layout
from the screenshot rather than from the generated code.

### Vertical stacks

```jsx
/* Figma output (do not use verbatim) */
<div style={{ display: 'flex', flexDirection: 'column', gap: '16px', width: '320px' }}>

/* Adapted */
<div className="stack">   {/* or use CSS module / Tailwind */}
```
```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-gap-md);
  /* width comes from the container, not this component */
}
```

### Horizontal rows

```css
.row {
  display: flex;
  align-items: center;   /* or flex-start / flex-end from screenshot */
  gap: var(--space-gap-sm);
  flex-wrap: wrap;       /* add if items can overflow */
}
```

### Grid layouts

When Figma shows a repeating grid of cards or items:
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: var(--space-gap-lg);
}
```

For fixed column counts:
```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-gap-md);
}
```

### Overlays and positioned elements

Only use `position: absolute` for genuinely overlapping elements:
- Badge counts on avatars or icons
- Floating action buttons
- Tooltips and popovers (managed by a positioning library)
- Decorative background shapes

Everything else in a Figma "overlay" is usually a semantic stack, not an overlay.

### Fixed dimensions

Remove explicit `width` and `height` from most elements. Let content and containers
determine size. Exceptions:
- Avatar/icon containers (must be a fixed square)
- Progress bar tracks (fixed height)
- Thumbnail images (fixed aspect ratio via `aspect-ratio`)

```css
/* Avoid */
.card { width: 320px; height: 180px; }

/* Prefer */
.card { width: 100%; }  /* or max-width on the container */
.card-image { aspect-ratio: 16/9; width: 100%; object-fit: cover; }
```

---

## Component Identification

Before implementing any element from Figma, check if the project already has it.

### Check in this order:

1. **Code Connect response** — if `get_design_context` returned a component import, use it
2. **Project component directory** — grep for likely names (`Button`, `Badge`, `Avatar`, `Tag`,
   `Input`, `Select`, `Modal`, `Toast`, `Tooltip`)
3. **UI library** — if the project uses a component library (shadcn/ui, Radix, MUI, etc.),
   check whether the Figma component maps to a library component
4. **Design system docs** — if Code Connect returned a documentation link, read it

If a match is found, use the existing component with the correct props. Only build new
components for genuinely novel UI patterns.

### Figma component → common code equivalent

| Figma component name | Likely project equivalent |
|---------------------|--------------------------|
| Button / CTA / Action | `<Button>`, `<button>` |
| Icon Button | `<IconButton>`, `<button aria-label="...">` |
| Input / TextField | `<Input>`, `<input>` |
| Dropdown / Select | `<Select>`, `<select>`, Radix `<Select>` |
| Checkbox | `<Checkbox>`, `<input type="checkbox">` |
| Toggle / Switch | `<Switch>`, `<input type="checkbox" role="switch">` |
| Avatar | `<Avatar>`, `<img>` with rounded-full |
| Badge / Chip / Tag | `<Badge>`, `<Tag>`, `<span>` with pill styles |
| Card | `<Card>`, `<article>`, `<section>` |
| Modal / Dialog | `<Dialog>`, `<dialog>`, Radix `<Dialog>` |
| Toast / Snackbar | `<Toast>`, `<output role="status">` |
| Tooltip | `<Tooltip>`, Radix `<Tooltip>` |
| Tabs | `<Tabs>`, Radix `<Tabs>`, `<nav role="tablist">` |
| Progress / Loader | `<Progress>`, `<progress>`, animated `<div role="progressbar">` |
| Breadcrumb | `<nav aria-label="Breadcrumb">` with `<ol>` |
| Pagination | `<nav aria-label="Pagination">` |

---

## Interactive State Implementation

Figma designs show one static state. For every interactive component, implement all states.

### Color token pattern for interactive states

```css
.btn-primary {
  background-color: var(--color-action-primary);
  color: var(--color-action-primary-text);
  transition: background-color var(--duration-transition-fast) var(--easing-transition);
}

.btn-primary:hover {
  background-color: var(--color-action-primary-hover);
}

.btn-primary:active {
  background-color: var(--color-action-primary-active);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}

.btn-primary:disabled,
.btn-primary[aria-disabled="true"] {
  background-color: var(--color-bg-overlay);
  color: var(--color-text-disabled);
  pointer-events: none;
}
```

### Form input states

```css
.input {
  border: 1px solid var(--color-border-default);
  color: var(--color-text-primary);
  background: var(--color-bg-surface);
}

.input::placeholder {
  color: var(--color-text-tertiary);
}

.input:hover {
  border-color: var(--color-border-strong);
}

.input:focus {
  border-color: var(--color-border-focus);
  box-shadow: var(--shadow-input-focus);
  outline: none;
}

.input:disabled {
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  background: var(--color-bg-overlay);
}

.input[aria-invalid="true"] {
  border-color: var(--color-border-danger);
}
```

### Motion: enter/exit

For components that appear or disappear (modals, toasts, dropdowns):

```css
/* Enter */
@keyframes fade-in {
  from { opacity: 0; transform: translateY(-4px); }
  to   { opacity: 1; transform: translateY(0); }
}

.dropdown {
  animation: fade-in var(--duration-enter) var(--easing-enter);
}

/* Exit — apply class before unmounting */
@keyframes fade-out {
  from { opacity: 1; transform: translateY(0); }
  to   { opacity: 0; transform: translateY(-4px); }
}

.dropdown.is-exiting {
  animation: fade-out var(--duration-exit) var(--easing-exit);
}
```

---

## Accessibility Adaptation

Figma designs are visual — accessibility semantics must be added during adaptation.

### Landmark and semantic HTML

| Figma frame | Semantic element |
|-------------|-----------------|
| Nav / Navigation | `<nav aria-label="...">` |
| Header / Top bar | `<header>` |
| Footer | `<footer>` |
| Sidebar | `<aside aria-label="...">` |
| Main content area | `<main>` |
| Article / Post card | `<article>` |
| Section with heading | `<section aria-labelledby="...">` |
| Form | `<form>` with `<label>` for every input |
| List of items | `<ul>` / `<ol>` with `<li>` |

### Icon-only controls

Every icon-only button or link needs an accessible label:
```jsx
<button aria-label="Close dialog">
  <CloseIcon aria-hidden="true" />
</button>
```

### Color contrast verification

Before finalizing, check every foreground/background pair from the design:
- **Text on background:** must be ≥ 4.5:1 (WCAG AA)
- **UI elements (borders, icons):** must be ≥ 3:1
- **Large text (≥18pt or ≥14pt bold):** must be ≥ 3:1

Quick check: the token pairings defined in the design-tokens skill are pre-verified.
Any pairing that uses a non-standard color combination from Figma must be manually verified
using browser DevTools or a contrast checker before shipping.

### Keyboard navigation

For any interactive component:
- `Tab` — moves focus between controls
- `Enter` / `Space` — activates buttons and checkboxes
- `Escape` — closes dialogs, dropdowns, and popovers
- Arrow keys — navigates within a group (tabs, radio buttons, listbox options, menu items)

Add `role`, `aria-expanded`, `aria-haspopup`, and `aria-controls` to disclosure patterns.

---

## Asset Handling

`get_design_context` returns temporary asset URLs. These expire — do not reference them in
committed code.

### Icons
1. Download the SVG from the asset URL during implementation
2. Place in `/assets/icons/` or the project's icon directory
3. Use inline or via an `<img>` tag or `<use>` sprite reference
4. Set `aria-hidden="true"` on decorative icons; `aria-label` or `<title>` on semantic icons

### Images
1. Download from the asset URL
2. Place in `/assets/images/` or the public directory
3. Always add `alt` text — describe the image's content or leave `alt=""` if purely decorative
4. Use `aspect-ratio` + `object-fit: cover` to prevent layout shift

### Fonts
Figma shows the font name. Verify the project already loads it (check `<link>` tags,
`@font-face` rules, or `next/font`). If not, add the font load before using the font family
token.

---

## Delivery Checklist

Before marking a figma-to-code task complete:

- [ ] Screenshot read and understood before writing code
- [ ] Code Connect mappings checked — existing components used where mapped
- [ ] All hardcoded values replaced with semantic tokens
- [ ] No primitive tokens used directly in component styles
- [ ] Layout rewritten from scratch (not verbatim from Figma output)
- [ ] All interactive states implemented (hover, focus, active, disabled)
- [ ] Semantic HTML used throughout
- [ ] Icon-only controls have `aria-label`
- [ ] Token gaps reported explicitly with proposed resolutions
- [ ] Asset checklist provided (icons and images to download and place)
- [ ] Integration note included (how to import and use the component)
