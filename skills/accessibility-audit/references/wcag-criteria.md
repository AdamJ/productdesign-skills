# WCAG 2.1 AA Criteria Reference

Quick reference for every criterion checked during an audit. Each entry includes the success
criterion, what it means in practice, common violations, and test method.

---

## Principle 1 — Perceivable

### 1.1.1 Non-text Content (Level A)

All non-text content has a text alternative.

**In practice:**

- `<img>` needs `alt`. Meaningful: describe the content. Decorative: `alt=""`.
- Icon-only `<button>`: needs `aria-label` or `<span class="visually-hidden">`.
- `<input type="image">`: needs `alt`.
- `role="img"` on SVG: needs `aria-label` or `<title>`.
- Charts/graphs: need a text summary or data table alternative.

**Common violations:** `alt` is filename (`alt="button_icon_v2.png"`), missing on icon buttons,
SVG without accessible name.

**Test:** Read DOM with images disabled or inspect alt attributes.

---

### 1.3.1 Info and Relationships (Level A)

Structure and relationships conveyed visually are also in the markup.

**In practice:**

- Visual headings use `<h1>`–`<h6>`, not `<div class="title">`.
- Navigation in `<nav>` with `aria-label` to distinguish multiple navs.
- Lists are `<ul>`/`<ol>`, not bullet characters in `<p>` tags.
- Tables: `<th scope="col|row">`, `<caption>`, or `aria-labelledby`.
- Form fields: `<label for="id">` or `aria-labelledby`/`aria-label`.
- Required fields: `required` or `aria-required="true"`.
- Error states: `aria-invalid="true"` + error message linked via `aria-describedby`.

**Common violations:** Fake headings, navigation in `<div>` soup, tables without headers.

---

### 1.3.3 Sensory Characteristics (Level A)

Instructions don't rely solely on sensory characteristics (shape, color, size, location).

**In practice:** "Click the green button" → bad. "Click Save" → good.
Error indicators must not be color-only.

---

### 1.4.1 Use of Color (Level A)

Color is not the only visual means of conveying information, indicating action, or
distinguishing a visual element.

**In practice:**

- Error states: border color change + icon or label, not red border alone.
- Required field: asterisk + "required" text, not just color.
- Charts: use patterns or labels in addition to color coding.
- Links in body text: underline or other non-color differentiator (unless contrast ratio ≥ 3:1 against surrounding text).

---

### 1.4.3 Contrast (Minimum) (Level AA)

Text and images of text have a contrast ratio of at least 4.5:1 (normal) or 3:1 (large text).

**Thresholds:**

- Normal text (<18pt / <14pt bold): **4.5:1**
- Large text (≥18pt / ≥14pt bold = ≥24px / ≥18.67px bold): **3:1**
- Disabled UI elements: exempt
- Logo text: exempt
- Incidental text (decorative): exempt

**Note:** 18pt = 24px, 14pt bold = ~18.67px bold

---

### 1.4.4 Resize Text (Level AA)

Text can be resized up to 200% without loss of content or functionality.

**In practice:** No `px`-locked containers that clip text. Use `rem`/`em` for font sizes where
possible. Avoid `overflow: hidden` on text containers without adequate space.

---

### 1.4.10 Reflow (Level AA)

Content can be presented without horizontal scrolling at 320px width.

**In practice:** Responsive layouts work at 320px viewport. Data tables may scroll horizontally
but the page itself should not require horizontal scrolling.

---

### 1.4.11 Non-text Contrast (Level AA)

UI components and graphical objects have a contrast ratio of at least 3:1 against adjacent color(s).

**In practice:**

- Input borders vs. background: 3:1
- Focus indicators vs. adjacent color: 3:1
- Icon (when the icon is the only indicator): 3:1
- Chart data points/lines: 3:1

---

### 1.4.12 Text Spacing (Level AA)

No loss of content when user overrides text spacing.

**In practice:** Don't use fixed-height containers where text will overflow if spacing increases.
Avoid `overflow: hidden` on text blocks without room to grow.

---

### 1.4.13 Content on Hover or Focus (Level AA)

Additional content that appears on hover/focus must be: dismissible (Escape), hoverable
(pointer can move to the tooltip without it disappearing), and persistent (stays until dismissed).

---

## Principle 2 — Operable

### 2.1.1 Keyboard (Level A)

All functionality is operable via keyboard.

**In practice:**

- Every `<a>`, `<button>`, `<input>`, `<select>`, `<textarea>` is keyboard accessible by default.
- Custom interactive elements (drag-and-drop, sliders, carousels) need keyboard equivalents.
- Expected keyboard patterns:
  - **Modal/dialog**: Tab/Shift+Tab cycles inside; Escape closes; focus returns to trigger.
  - **Dropdown/menu**: Arrow keys navigate; Enter/Space selects; Escape closes.
  - **Tabs (ARIA)**: Arrow keys switch tabs; Tab moves to content panel.
  - **Combobox**: Arrow keys navigate list; Enter selects; Escape dismisses.

**Common violations:** `onClick` on `<div>` with no `tabindex` or keyboard handler.

---

### 2.1.2 No Keyboard Trap (Level A)

Keyboard focus doesn't get stuck (modal dialogs are the intentional exception — they trap focus,
but Escape exits).

---

### 2.4.1 Bypass Blocks (Level A)

Skip navigation link at the top of the page, targeting `<main id="main">`.

**In practice:** Visually hidden by default, visible on focus. Present on every page that
has repeated navigation blocks.

---

### 2.4.3 Focus Order (Level A)

Focusable components receive focus in an order that preserves meaning and operability.

**In practice:** DOM order = visual order where possible. Avoid `tabindex > 0`. If visual layout
differs from DOM order, use `tabindex="0"` carefully or restructure the DOM.

---

### 2.4.7 Focus Visible (Level AA)

Any keyboard-operable interface has a visible focus indicator.

**In practice:**

- Never `outline: none` or `outline: 0` without a replacement.
- `:focus-visible` is the modern approach — shows for keyboard, hides for mouse.
- Focus ring should be ≥ 2px and contrast ≥ 3:1 against adjacent colors (2.4.11 at AAA, but
  treat as best practice).

---

### 2.5.3 Label in Name (Level A)

Accessible name of interactive element contains the visible label text.

**Common violation:** Button visually says "Submit" but `aria-label="Send form"` — screen reader
announces "Send form" but voice control user says "click Submit" and nothing happens.

---

### 2.5.8 Target Size (Level AA, WCAG 2.2)

Interactive targets are at least 24×24px. Recommended: 44×44px.

---

## Principle 3 — Understandable

### 3.1.1 Language of Page (Level A)

`<html lang="en">` (or correct BCP 47 language code) present.

---

### 3.3.1 Error Identification (Level A)

If an input error is detected, the item is identified and described in text.

**In practice:**

```html
<input aria-invalid="true" aria-describedby="email-error" />
<span id="email-error" role="alert">Enter a valid email address</span>
```

---

### 3.3.2 Labels or Instructions (Level A)

Labels or instructions provided when content requires user input.

**In practice:** Every `<input>`, `<select>`, `<textarea>` has an associated `<label>`.
Placeholder text is not a label — it disappears and fails when the input is focused.

---

## Principle 4 — Robust

### 4.1.1 Parsing (Level A)

No duplicate IDs in the same document. Elements properly nested.

---

### 4.1.2 Name, Role, Value (Level A)

All UI components: accessible name, role, and states/properties are programmatically determinable
and set when changed.

**In practice:**

- Interactive elements have accessible names (via content, `aria-label`, `aria-labelledby`).
- Use native HTML elements when possible — `<button>`, `<a>`, `<input>` have roles built in.
- Custom widgets declare role: `role="dialog"`, `role="tablist"`, `role="combobox"`, etc.
- States set correctly: `aria-expanded`, `aria-selected`, `aria-checked`, `aria-disabled`.
- `aria-hidden="true"` never on a focusable element.

---

### 4.1.3 Status Messages (Level AA)

Status messages (success, error, progress) conveyed to assistive technologies without
receiving focus.

**In practice:**

```html
<div role="status" aria-live="polite">3 items added to cart</div>
<div role="alert" aria-live="assertive">Error: session expired</div>
```

Use `polite` for non-urgent updates, `assertive` for errors that need immediate attention.
