---
name: frontend-design
description: Creates distinctive, production-grade frontend interfaces with high design quality. Use when building web components, pages, or applications, designing UIs, or when the user asks to create frontend code. Generates creative, polished code that avoids generic AI aesthetics.
---

# Frontend Design Skill

## Core Philosophy

Generate **distinctive, production-ready frontend code** with high design quality that stands out from generic AI-generated interfaces. Focus on creative, thoughtful design decisions that feel intentional and polished.

## Design Principles

### 1. Avoid Generic AI Aesthetics

**Common AI clichés to avoid:**

- Purple/blue gradients everywhere
- Excessive rounded corners (border-radius: 24px on everything)
- Generic card layouts with drop shadows
- Overuse of glassmorphism effects
- Templated hero sections with centered text
- Stock gradient backgrounds

**Instead, create:**

- Intentional color palettes with purpose
- Varied visual hierarchy through scale, weight, and spacing
- Unique layout patterns that serve the content
- Thoughtful use of whitespace and breathing room
- Distinctive typographic treatments
- Purposeful interactive states and transitions

### 2. Production-Grade Quality

Every component should be:

- **Accessible** — WCAG 2.1 AA compliant minimum
- **Responsive** — Mobile-first, graceful scaling
- **Performant** — Optimized CSS, minimal JS overhead
- **Maintainable** — Clean structure, clear naming
- **Polished** — Refined details, smooth interactions

### 3. Visual Sophistication

Create interfaces with:

- **Strong hierarchy** — Clear information architecture through size, weight, color
- **Balanced composition** — Asymmetric layouts when appropriate, intentional symmetry
- **Refined typography** — Scale, line-height, letter-spacing working in harmony
- **Purposeful color** — Limited palettes with clear semantic meaning
- **Subtle motion** — Transitions that enhance, not distract

## Reference Documentation

### CSS Patterns and Methodology

For detailed CSS guidance, see [css-patterns.md](./references/css-patterns.md):

- Naming conventions (element-based, not BEM)
- CSS architecture and organization
- Design tokens and custom properties
- Responsive grid layouts
- Distinctive vs generic examples

### React Component Patterns

For React implementation patterns, see [react-patterns.md](./references/react-patterns.md):

- Functional and class component structure
- State management with Context API
- Common component patterns (Button, Form, Modal)
- Distinctive vs generic examples

### Accessibility Standards

For accessibility requirements, see [accessibility.md](./references/accessibility.md):

- WCAG 2.1 AA compliance
- Semantic HTML patterns
- Keyboard navigation
- ARIA attributes
- Color contrast requirements
- Focus management

## File Organization

Follow standard project structure:

```
/project-root
  /assets
    /images
    /icons
    /fonts
  /components
    /Button
      Button.jsx
      Button.css
      Button.test.js
    /Card
      Card.jsx
      Card.css
  /pages
    HomePage.jsx
    DashboardPage.jsx
  /styles
    reset.css
    variables.css
    global.css
  /utils
    formatDate.js
    api.js
  /config
    constants.js
```

## Design Process

When creating frontend interfaces:

### 1. Understand Context

- What is the component's purpose?
- Who is the user and what's their goal?
- What's the visual hierarchy priority?
- Are there existing design patterns to follow?

### 2. Create Distinctive Visual Direction

**For landing pages:**

- Avoid centered hero sections with generic gradients
- Consider asymmetric layouts, split screens, or editorial-style layouts
- Use typography as a design element (large, bold headlines with purpose)
- Create visual interest through layout, not just color

**For components:**

- Think beyond rounded rectangles with shadows
- Consider how the component draws attention (or doesn't)
- Use whitespace intentionally to create breathing room
- Design interactive states that feel responsive and polished

**For data interfaces:**

- Prioritize scanability over decoration
- Use typographic hierarchy to structure information
- Consider table alternatives (cards, lists, timelines) when appropriate
- Make interactive elements obvious without being loud

### 3. Build with Progressive Enhancement

Start with:

1. **Structure** — Semantic HTML that works without CSS
2. **Style** — CSS that enhances the structure
3. **Behavior** — JavaScript that adds interactivity
4. **Refinement** — Polish details, transitions, states

### 4. Test Accessibility

- Keyboard navigation (Tab, Enter, Escape, Arrow keys)
- Screen reader testing (at least spot check with VoiceOver/NVDA)
- Color contrast validation (use browser DevTools)
- Focus visibility in all states
- Responsive behavior on mobile

## Comments & Documentation

### Large Code Blocks

Use block comments for complex components:

```jsx
/**
 * DataTable Component
 *
 * Displays tabular data with sorting, filtering, and pagination.
 * Uses virtual scrolling for large datasets (1000+ rows).
 *
 * Accessibility: Full keyboard navigation, screen reader support,
 * sortable columns announced via aria-live regions.
 */
```

### Small Changes/Fixes

Use inline comments:

```jsx
// Prevent scroll when modal is open
useEffect(() => {
  if (isOpen) {
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = '';
    };
  }
}, [isOpen]);
```

### Avoid Over-Commenting

```jsx
// ❌ Too much
// This sets the state to true
setState(true);

// ✅ Only comment the non-obvious
// Delay prevents race condition with animation frame
setTimeout(() => setState(true), 0);
```

## Quality Checklist

Before completing any frontend component, verify:

- [ ] **Accessibility**: WCAG 2.1 AA compliant (see [accessibility.md](./references/accessibility.md))
- [ ] **Responsiveness**: Works from 320px to 2560px width
- [ ] **Visual Design**: Distinctive and polished, not generic AI aesthetics
- [ ] **Code Quality**: Clean structure, follows naming conventions
- [ ] **Performance**: Optimized CSS, no unnecessary re-renders

## Integration with Figma

When Figma designs are available:

- **Extract exact values** for spacing, colors, typography
- **Reference design tokens** instead of approximating
- **Ask for clarification** if design values aren't clearly defined
- **Maintain design system consistency** when values are specified

## Output Format

When generating frontend code, provide:

1. **Component file** (`.jsx` or `.js`)
2. **Stylesheet** (`.css`)
3. **Brief technical description** of what was created and key decisions
4. **File locations** where code should be placed
5. **Accessibility notes** if there are complex interactive patterns

Keep explanations concise and technical — let the code speak.

## Final Notes

This skill prioritizes **craftsmanship over speed**. Take time to:

- Consider the user's actual needs
- Design intentionally, not by template
- Create interfaces that feel human and polished
- Write code that others can maintain

The goal is frontend work that stands out for its quality, not blends in with generic AI output.
