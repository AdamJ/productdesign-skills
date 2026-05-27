---
name: accessibility-audit
description: >
  Audits components, pages, and designs against WCAG 2.1 AA and outputs a prioritized
  remediation checklist with code-level fixes. Use this skill whenever the user asks to
  check accessibility, run a WCAG audit, review color contrast, validate keyboard navigation,
  check screen reader support, or says things like "is this accessible?", "audit this for a11y",
  "check this for WCAG", "does this pass accessibility?", "make this accessible", or
  "review this component for accessibility issues." Also triggers when the user shares a
  React component, HTML file, CSS token set, or design description and asks for feedback —
  if accessibility is even a secondary concern, use this skill. Works across HTML pages,
  React components, Eleventy sites, CSS design tokens, and design mockup descriptions.
---

# Accessibility Audit Skill

## Purpose

Run a structured WCAG 2.1 AA audit on any frontend artifact — React component, HTML page,
CSS token set, Eleventy site, or a design described in prose — and produce a prioritized
remediation report. The goal is not a pass/fail score but a clear action list: what to fix,
why it matters, and exactly how to fix it.

---

## What You Can Audit

- **React components** — `.jsx` / `.tsx` files
- **HTML pages / templates** — including Eleventy `.njk` / `.html` output
- **CSS** — token definitions, stylesheets (especially color pairings and focus states)
- **Design descriptions** — prose or screenshot descriptions of a UI
- **Full pages via URL** — fetch the page and audit the rendered HTML

If the user provides a file path, read it. If they provide a URL, fetch it. If they paste code
inline, work from that. If they describe a design in words, audit the description.

---

## Audit Workflow

### Phase 1 — Scope & Intake

Before running checks, establish:

1. **What's being audited** — file, URL, component, or description?
2. **Target environment** — is this a component in isolation, a full page, or part of a design system?
3. **Known constraints** — does the user have a specific WCAG level target (AA is the standard default)?
4. **Context** — is this a new build or a fix pass on existing work?

Read the input file(s) in full before starting the audit. If reading from a URL, fetch and parse
the HTML. For React, analyze JSX semantics — what renders in the DOM matters most.

### Phase 2 — Run Systematic Checks

Work through the four WCAG principles in order. Don't skip categories even if the user mentions
only one concern — a contrast check often surfaces semantic issues and vice versa.

See `references/wcag-criteria.md` for the full criterion-by-criterion breakdown.

**Quick category guide:**

| Category | What you're checking |
|----------|---------------------|
| **Perceivable** | Contrast ratios, alt text, color independence, text spacing, non-text contrast |
| **Operable** | Keyboard access, focus order, focus visibility, skip links, touch targets |
| **Understandable** | Form labels, error messages, language attributes, input purpose |
| **Robust** | Semantic HTML, ARIA correctness, name/role/value on interactive elements |

### Phase 3 — Contrast Ratio Calculation

When CSS color values are present (hex, rgb, hsl, or CSS custom property references), calculate
contrast ratios programmatically rather than estimating visually. Use the script at
`scripts/contrast_check.py` — pass it pairs of foreground/background values.

```bash
python scripts/contrast_check.py "#1a1a1a" "#ffffff"
# → 19.1:1  ✓ PASS (AA normal, AA large, AAA normal, AAA large)

python scripts/contrast_check.py "#7d94a2" "#1e2a31"
# → 4.9:1   ✓ PASS (AA normal, AA large)

python scripts/contrast_check.py "#666666" "#f5f5f5"
# → 5.7:1   ✓ PASS (AA normal)
```

For CSS custom properties, resolve them to their computed values first (look up the token
definition file, or ask the user to provide the resolved value).

WCAG contrast thresholds:

- **4.5:1** — normal text (< 18pt / < 14pt bold), AA required
- **3:1** — large text (≥ 18pt / ≥ 14pt bold), UI components, AA required
- **7:1** — normal text, AAA (not required but note when achieved)

### Phase 4 — Finding Classification

Classify every finding by severity:

| Severity | Meaning |
|----------|---------|
| **Critical** | Blocks access entirely for some users (no keyboard access to interactive element, contrast below 3:1 for body text, missing required form label) |
| **High** | Significantly impairs experience (contrast 3:1–4.49:1 for body text, missing alt text on meaningful image, no visible focus indicator) |
| **Medium** | Partial barrier or WCAG violation without complete blockage (incorrect ARIA role, missing live region on dynamic update, no skip link on long page) |
| **Low** | Best practice not met, minor friction (missing `lang` attribute, overly generic aria-label, touch target slightly under 44px) |

---

## Output Format

Always produce the audit report in this structure:

```text
## Accessibility Audit — [Component/File Name]

### Summary
[2–3 sentences on overall state. Be direct: "This component has two critical issues that block
keyboard users entirely, plus four contrast failures. Everything else is solid."]

| Severity | Count |
|----------|-------|
| Critical | N |
| High | N |
| Medium | N |
| Low | N |

---

### Findings

#### [CRIT-01] [Short issue name]
**Criterion:** WCAG X.X.X — [Criterion name]
**Location:** [File:line or component/element description]
**Issue:** [What's wrong and why it matters to real users]
**Fix:**
[Code example of the corrected version]

#### [HIGH-01] [Short issue name]
...

---

### Remediation Roadmap

**Do first (Critical):** [Ordered list — address these before shipping]
**Do next (High):** [Ordered list — address in same sprint if possible]
**Do soon (Medium):** [Ordered list — next sprint]
**Backlog (Low):** [Ordered list — good to have]

---

### Passes ✓
[List what's already correct — this matters, it tells the user what not to break]
```

Keep findings concrete. "Missing `aria-label` on icon button at line 42" is useful.
"Some ARIA issues exist" is not.

---

## Audit Checklist (Internal — Work Through This)

### Perceivable

- [ ] **1.1.1** All `<img>` elements have meaningful `alt` text; decorative images have `alt=""`
- [ ] **1.1.1** Icon-only buttons have `aria-label` or visually-hidden text
- [ ] **1.3.1** Headings form a logical hierarchy (no skipped levels, no faux headings via bold `<div>`)
- [ ] **1.3.1** Lists use `<ul>` / `<ol>` / `<dl>`, not `<div>` + `<br>`
- [ ] **1.3.1** Tables have `<th>` with `scope`, `<caption>` where helpful
- [ ] **1.3.3** Instructions don't rely on sensory cues only ("click the red button")
- [ ] **1.4.1** Color is not the only means of conveying information (error states, status)
- [ ] **1.4.3** Normal text contrast ≥ 4.5:1
- [ ] **1.4.3** Large text contrast ≥ 3:1
- [ ] **1.4.11** UI components and focus indicators contrast ≥ 3:1 against adjacent colors
- [ ] **1.4.12** No CSS overrides that prevent text-spacing adjustments (line-height, letter-spacing)
- [ ] **1.4.13** Hover/focus-triggered content is dismissible, hoverable, and persistent

### Operable

- [ ] **2.1.1** All interactive elements reachable and operable by keyboard alone
- [ ] **2.1.1** Custom widgets implement expected keyboard patterns (arrow keys for listbox, Esc for modal)
- [ ] **2.1.2** No keyboard traps (except modal dialogs, which correctly trap focus)
- [ ] **2.4.1** Skip navigation link present on pages with repeated navigation
- [ ] **2.4.3** Focus order follows logical reading/interaction order
- [ ] **2.4.7** Focus indicator visible in all interactive states
- [ ] **2.4.7** `outline: none` / `outline: 0` not used without a custom focus style
- [ ] **2.5.3** Touch targets ≥ 44×44px (CSS) for all interactive elements

### Understandable

- [ ] **3.1.1** `<html lang="en">` (or correct language) present
- [ ] **3.3.1** Error messages identify the field and describe what's wrong
- [ ] **3.3.2** All form inputs have associated `<label>` (via `for`/`id` or `aria-labelledby`)
- [ ] **3.3.2** Required fields indicated (not just by color)
- [ ] **3.3.3** Error suggestions provided where possible

### Robust

- [ ] **4.1.1** No duplicate `id` attributes
- [ ] **4.1.2** All interactive elements have accessible name, role, and state
- [ ] **4.1.2** `<button>` used for actions, `<a>` used for navigation
- [ ] **4.1.2** `role="button"` on `<div>`/`<span>` only when truly necessary (and with `tabindex="0"` + keyboard handler)
- [ ] **4.1.2** ARIA attributes are valid and used correctly (no `aria-hidden="true"` on focusable elements)
- [ ] **4.1.3** Dynamic content changes announced via `aria-live` or role `status`/`alert`

---

## Common Fixes Quick Reference

**Icon-only button:**

```jsx
// ✗ No accessible name
<button onClick={onClose}><XIcon /></button>

// ✓ With aria-label
<button onClick={onClose} aria-label="Close dialog"><XIcon aria-hidden="true" /></button>
```

**Visible focus indicator:**

```css
/* ✗ Kills focus visibility */
*:focus { outline: none; }

/* ✓ Custom indicator */
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

**Color-not-only for errors:**

```jsx
// ✗ Color alone indicates error
<input className={errors.email ? 'border-red' : ''} />

// ✓ Icon + text + color
<input
  aria-invalid={!!errors.email}
  aria-describedby="email-error"
  className={errors.email ? 'input--error' : ''}
/>
{errors.email && (
  <span id="email-error" role="alert">
    <ErrorIcon aria-hidden="true" /> {errors.email}
  </span>
)}
```

**Modal focus trap:**

```jsx
// Focus must stay inside modal while open
// On open: move focus to first focusable element inside
// On Escape: close and return focus to trigger
// Tab / Shift+Tab: cycle within modal only
```

**Skip link:**

```html
<a href="#main" class="skip-link">Skip to main content</a>
<main id="main">...</main>
```

```css
.skip-link {
  position: absolute;
  transform: translateY(-100%);
  transition: transform 0.2s;
}
.skip-link:focus { transform: translateY(0); }
```

---

## Related Skills

- **frontend-design** — accessibility patterns and ARIA examples in `references/accessibility.md`
- **design-tokens** — contrast-safe token architecture; ensures semantic color tokens carry intent

When a fix requires adding or changing design tokens (e.g., a new `--color-focus` token for
focus rings), recommend the user run the `design-tokens` skill to integrate the change properly.
