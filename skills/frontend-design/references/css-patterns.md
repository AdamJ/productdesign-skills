# CSS Patterns and Methodology

## Naming Conventions

Use **element-based naming** with clear, descriptive classes:

```css
/* Component naming */
.card {
}
.card-header {
}
.card-body {
}
.card-footer {
}

/* Button variants */
.btn {
}
.btn-primary {
}
.btn-secondary {
}
.btn-icon {
}

/* Layout utilities */
.grid {
}
.grid-2col {
}
.grid-auto {
}

/* State modifiers */
.is-active {
}
.is-disabled {
}
.is-loading {
}
```

**Avoid:**

- BEM notation (unless project specifically requires it)
- Utility-first frameworks like Tailwind (unless project requires it)
- Overly generic names like `.container` or `.wrapper`

## CSS Architecture

Organize styles logically:

```css
/* 1. Custom properties (design tokens) */
:root {
  --color-primary: #1a1a1a;
  --color-accent: #ff6b35;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  --font-primary: 'Inter', system-ui, sans-serif;
  --transition-fast: 150ms ease;
}

/* 2. Base/reset styles */
* {
  box-sizing: border-box;
}
body {
  margin: 0;
  font-family: var(--font-primary);
}

/* 3. Component styles */
.card {
  background: white;
  padding: var(--spacing-lg);
  border: 1px solid #e0e0e0;
  transition: transform var(--transition-fast);
}

/* 4. Interactive states */
.card:hover {
  transform: translateY(-2px);
}
```

## Design Token Best Practices

When creating design systems, use CSS custom properties:

```css
:root {
  /* Color system */
  --color-neutral-100: #f8f9fa;
  --color-neutral-900: #212529;
  --color-primary-500: #0066cc;
  --color-success-500: #28a745;
  --color-error-500: #dc3545;

  /* Spacing scale */
  --space-1: 0.25rem; /* 4px */
  --space-2: 0.5rem; /* 8px */
  --space-3: 0.75rem; /* 12px */
  --space-4: 1rem; /* 16px */
  --space-6: 1.5rem; /* 24px */
  --space-8: 2rem; /* 32px */

  /* Typography scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;

  /* Font weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Border radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.15);
}
```

## Responsive Grid Layouts

```css
.grid {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

/* More control with specific breakpoints */
.grid-adaptive {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .grid-adaptive {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid-adaptive {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## Distinctive vs Generic Design

### Generic AI Pattern (Avoid):

```css
/* Templated, forgettable design */
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 24px;
  padding: 60px;
  text-align: center;
}

.btn {
  border-radius: 999px;
  background: linear-gradient(to right, #667eea, #764ba2);
}
```

### Distinctive Design (Preferred):

```css
/* Unique, intentional layout with personality */
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
  align-items: center;
  padding: var(--space-12) var(--space-6);
  min-height: 600px;
}

.hero-label {
  display: inline-block;
  padding: var(--space-2) var(--space-3);
  background: #f0f7ff;
  color: #0066cc;
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-radius: var(--radius-sm);
  margin-bottom: var(--space-4);
}

.hero-title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: var(--font-bold);
  line-height: 1.1;
  color: var(--color-neutral-900);
  margin-bottom: var(--space-4);
}

.hero-highlight {
  display: block;
  color: #0066cc;
  position: relative;
}

/* Subtle underline effect instead of gradient */
.hero-highlight::after {
  content: '';
  position: absolute;
  bottom: 0.1em;
  left: 0;
  right: 0;
  height: 0.15em;
  background: currentColor;
  opacity: 0.2;
  border-radius: var(--radius-sm);
}

.hero-description {
  font-size: var(--text-lg);
  line-height: 1.6;
  color: var(--color-neutral-700);
  margin-bottom: var(--space-6);
  max-width: 540px;
}

.hero-actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
}

.btn-primary,
.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-5);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
}

.btn-primary {
  background: #0066cc;
  color: white;
  border: 2px solid #0066cc;
}

.btn-primary:hover {
  background: #0052a3;
  border-color: #0052a3;
  transform: translateY(-1px);
}

.btn-secondary {
  background: transparent;
  color: var(--color-neutral-900);
  border: 2px solid var(--color-neutral-300);
}

.btn-secondary:hover {
  border-color: var(--color-neutral-900);
}

@media (max-width: 768px) {
  .hero-split {
    grid-template-columns: 1fr;
    gap: var(--space-6);
  }

  .hero-visual {
    order: -1;
  }
}
```

## Focus Management

```css
/* Visible focus indicators */
button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Don't remove focus entirely */
*:focus {
  outline: none; /* ❌ Never do this */
}
```
