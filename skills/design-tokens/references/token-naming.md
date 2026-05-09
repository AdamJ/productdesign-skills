# Token Naming Reference

## Anatomy of a Token Name

```
--[category]-[role]-[variant]-[state]
  │           │       │         │
  │           │       │         └── Optional: hover, active, focus, disabled, placeholder
  │           │       └──────────── Optional: subtle, default, strong, inverse
  │           └──────────────────── What the token is for (text, bg, border, space, ...)
  └──────────────────────────────── The design category (color, space, font-size, ...)
```

**Examples:**
```
--color-text-danger-hover
--color-bg-surface-raised
--space-layout-section
--font-size-heading-xl
--shadow-overlay
--radius-button
--duration-transition-normal
```

---

## Category Prefixes

| Prefix | Covers |
|--------|--------|
| `--color-` | All color tokens |
| `--space-` | All spacing tokens (margin, padding, gap) |
| `--size-` | Non-spacing dimensions (icon sizes, avatar sizes) |
| `--font-family-` | Typeface stacks |
| `--font-size-` | Text size scale |
| `--font-weight-` | Weight values |
| `--line-height-` | Line height values |
| `--letter-spacing-` | Tracking values |
| `--radius-` | Border radius |
| `--shadow-` | Box and drop shadows |
| `--duration-` | Animation/transition durations |
| `--easing-` | Animation timing functions |
| `--z-` | Z-index layers |

---

## Color Tokens

### Primitive color scale

Use numeric steps from 50 to 950. Step 500 is the base/mid hue; lower is lighter, higher is
darker. This matches Tailwind's convention and is universally understood.

```css
/* Hue scales — one set per brand/system hue */
--color-blue-50:  #eff6ff;
--color-blue-100: #dbeafe;
--color-blue-200: #bfdbfe;
--color-blue-300: #93c5fd;
--color-blue-400: #60a5fa;
--color-blue-500: #3b82f6;
--color-blue-600: #2563eb;
--color-blue-700: #1d4ed8;
--color-blue-800: #1e40af;
--color-blue-900: #1e3a8a;
--color-blue-950: #172554;

/* Neutral scale — always include, used for text, borders, surfaces */
--color-neutral-0:   #ffffff;
--color-neutral-50:  #f9fafb;
--color-neutral-100: #f3f4f6;
--color-neutral-200: #e5e7eb;
--color-neutral-300: #d1d5db;
--color-neutral-400: #9ca3af;
--color-neutral-500: #6b7280;
--color-neutral-600: #4b5563;
--color-neutral-700: #374151;
--color-neutral-800: #1f2937;
--color-neutral-900: #111827;
--color-neutral-950: #030712;
--color-neutral-1000: #000000;

/* Semantic feedback hues — red, yellow/amber, green, blue */
--color-red-500: #ef4444;
--color-amber-500: #f59e0b;
--color-green-500: #22c55e;
```

### Semantic color tokens

Organize semantics into functional groups. Each group covers a UI surface or interaction type.

#### Text

```css
--color-text-primary:     var(--color-neutral-900);   /* Default body text */
--color-text-secondary:   var(--color-neutral-600);   /* Supporting/muted text */
--color-text-tertiary:    var(--color-neutral-400);   /* Placeholder, disabled */
--color-text-inverse:     var(--color-neutral-0);     /* Text on dark backgrounds */
--color-text-link:        var(--color-blue-600);
--color-text-link-hover:  var(--color-blue-700);
--color-text-success:     var(--color-green-700);
--color-text-warning:     var(--color-amber-700);
--color-text-danger:      var(--color-red-600);
--color-text-info:        var(--color-blue-600);
--color-text-disabled:    var(--color-neutral-400);
```

#### Backgrounds / Surfaces

```css
--color-bg-canvas:        var(--color-neutral-0);     /* Page background */
--color-bg-surface:       var(--color-neutral-0);     /* Card/panel background */
--color-bg-surface-raised: var(--color-neutral-50);  /* Slightly elevated surfaces */
--color-bg-overlay:       var(--color-neutral-100);   /* Hover states, selections */
--color-bg-inverse:       var(--color-neutral-900);

--color-bg-primary:       var(--color-blue-600);      /* Brand/action fill */
--color-bg-primary-hover: var(--color-blue-700);
--color-bg-success:       var(--color-green-50);
--color-bg-warning:       var(--color-amber-50);
--color-bg-danger:        var(--color-red-50);
--color-bg-info:          var(--color-blue-50);
```

#### Borders

```css
--color-border-default:   var(--color-neutral-200);
--color-border-strong:    var(--color-neutral-400);
--color-border-focus:     var(--color-blue-500);      /* Focus rings */
--color-border-danger:    var(--color-red-400);
--color-border-success:   var(--color-green-400);
--color-border-disabled:  var(--color-neutral-200);
```

#### Interactive / Action

```css
--color-action-primary:           var(--color-blue-600);
--color-action-primary-hover:     var(--color-blue-700);
--color-action-primary-active:    var(--color-blue-800);
--color-action-primary-text:      var(--color-neutral-0);

--color-action-secondary:         var(--color-neutral-0);
--color-action-secondary-hover:   var(--color-neutral-100);
--color-action-secondary-border:  var(--color-neutral-300);

--color-action-destructive:       var(--color-red-600);
--color-action-destructive-hover: var(--color-red-700);
--color-action-destructive-text:  var(--color-neutral-0);
```

### Dark mode

Override only semantic tokens inside a dark-mode selector. Primitives never change.

```css
[data-theme="dark"],
@media (prefers-color-scheme: dark) {
  --color-text-primary:     var(--color-neutral-50);
  --color-text-secondary:   var(--color-neutral-400);
  --color-bg-canvas:        var(--color-neutral-950);
  --color-bg-surface:       var(--color-neutral-900);
  --color-bg-surface-raised: var(--color-neutral-800);
  --color-border-default:   var(--color-neutral-700);
  /* ... continue for all semantics */
}
```

---

## Spacing Tokens

### Primitive spacing scale

Base unit: `0.25rem` (4px). Each step is the previous × 2 until step 8 (2rem), then grows
more slowly for layout-scale values.

```css
--space-0:    0;
--space-px:   1px;
--space-0-5:  0.125rem;   /*  2px */
--space-1:    0.25rem;    /*  4px */
--space-1-5:  0.375rem;   /*  6px */
--space-2:    0.5rem;     /*  8px */
--space-2-5:  0.625rem;   /* 10px */
--space-3:    0.75rem;    /* 12px */
--space-3-5:  0.875rem;   /* 14px */
--space-4:    1rem;       /* 16px */
--space-5:    1.25rem;    /* 20px */
--space-6:    1.5rem;     /* 24px */
--space-7:    1.75rem;    /* 28px */
--space-8:    2rem;       /* 32px */
--space-10:   2.5rem;     /* 40px */
--space-12:   3rem;       /* 48px */
--space-16:   4rem;       /* 64px */
--space-20:   5rem;       /* 80px */
--space-24:   6rem;       /* 96px */
--space-32:   8rem;       /* 128px */
```

### Semantic spacing tokens

Map scale steps to named purposes. Components consume these — never raw `--space-N` directly.

```css
/* Component internal spacing */
--space-component-xs:    var(--space-1);
--space-component-sm:    var(--space-2);
--space-component-md:    var(--space-3);
--space-component-lg:    var(--space-4);
--space-component-xl:    var(--space-6);

/* Gaps between related items */
--space-gap-xs:    var(--space-1);
--space-gap-sm:    var(--space-2);
--space-gap-md:    var(--space-4);
--space-gap-lg:    var(--space-6);
--space-gap-xl:    var(--space-8);

/* Layout / section-level spacing */
--space-layout-xs:  var(--space-8);
--space-layout-sm:  var(--space-12);
--space-layout-md:  var(--space-16);
--space-layout-lg:  var(--space-24);
--space-layout-xl:  var(--space-32);

/* Inline padding inside interactive elements */
--space-inset-xs:  var(--space-1) var(--space-2);
--space-inset-sm:  var(--space-1-5) var(--space-3);
--space-inset-md:  var(--space-2) var(--space-4);
--space-inset-lg:  var(--space-3) var(--space-6);
```

---

## Typography Tokens

### Font family

```css
/* Primitives */
--font-family-sans:  ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
                     "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-family-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
--font-family-mono:  ui-monospace, SFMono-Regular, "SF Mono", Consolas,
                     "Liberation Mono", Menlo, monospace;

/* Semantics */
--font-family-body:    var(--font-family-sans);
--font-family-heading: var(--font-family-sans);
--font-family-code:    var(--font-family-mono);
```

### Font size

Use a modular scale (1.25 ratio "major third" by default, or match Figma type styles exactly).

```css
/* Primitives */
--font-size-2xs: 0.625rem;   /* 10px */
--font-size-xs:  0.75rem;    /* 12px */
--font-size-sm:  0.875rem;   /* 14px */
--font-size-md:  1rem;       /* 16px — base */
--font-size-lg:  1.125rem;   /* 18px */
--font-size-xl:  1.25rem;    /* 20px */
--font-size-2xl: 1.5rem;     /* 24px */
--font-size-3xl: 1.875rem;   /* 30px */
--font-size-4xl: 2.25rem;    /* 36px */
--font-size-5xl: 3rem;       /* 48px */
--font-size-6xl: 3.75rem;    /* 60px */

/* Semantics */
--font-size-body-sm:   var(--font-size-sm);
--font-size-body:      var(--font-size-md);
--font-size-body-lg:   var(--font-size-lg);
--font-size-label:     var(--font-size-sm);
--font-size-caption:   var(--font-size-xs);
--font-size-heading-sm:  var(--font-size-lg);
--font-size-heading-md:  var(--font-size-2xl);
--font-size-heading-lg:  var(--font-size-3xl);
--font-size-heading-xl:  var(--font-size-4xl);
--font-size-display:     var(--font-size-5xl);
```

### Font weight, line height, letter spacing

```css
/* Font weight primitives */
--font-weight-normal:   400;
--font-weight-medium:   500;
--font-weight-semibold: 600;
--font-weight-bold:     700;

/* Line height primitives */
--line-height-none:    1;
--line-height-tight:   1.25;
--line-height-snug:    1.375;
--line-height-normal:  1.5;
--line-height-relaxed: 1.625;
--line-height-loose:   2;

/* Letter spacing primitives */
--letter-spacing-tighter: -0.05em;
--letter-spacing-tight:   -0.025em;
--letter-spacing-normal:  0em;
--letter-spacing-wide:    0.025em;
--letter-spacing-wider:   0.05em;
--letter-spacing-widest:  0.1em;

/* Semantic typography composites (use in component styles) */
--font-size-body:       var(--font-size-md);
--line-height-body:     var(--line-height-normal);
--font-weight-body:     var(--font-weight-normal);

--font-size-heading-lg:    var(--font-size-3xl);
--line-height-heading-lg:  var(--line-height-tight);
--font-weight-heading:     var(--font-weight-bold);
--letter-spacing-heading:  var(--letter-spacing-tight);
```

---

## Radius Tokens

```css
/* Primitives */
--radius-none: 0;
--radius-1:    0.125rem;   /* 2px */
--radius-2:    0.25rem;    /* 4px */
--radius-3:    0.375rem;   /* 6px */
--radius-4:    0.5rem;     /* 8px */
--radius-6:    0.75rem;    /* 12px */
--radius-8:    1rem;       /* 16px */
--radius-12:   1.5rem;     /* 24px */
--radius-full:  9999px;

/* Semantics */
--radius-badge:   var(--radius-full);
--radius-button:  var(--radius-2);
--radius-card:    var(--radius-4);
--radius-input:   var(--radius-2);
--radius-modal:   var(--radius-6);
--radius-tooltip: var(--radius-2);
--radius-tag:     var(--radius-full);
```

---

## Shadow Tokens

```css
/* Primitives */
--shadow-none: none;
--shadow-xs:   0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-sm:   0 1px 3px 0 rgb(0 0 0 / 0.10), 0 1px 2px -1px rgb(0 0 0 / 0.10);
--shadow-md:   0 4px 6px -1px rgb(0 0 0 / 0.10), 0 2px 4px -2px rgb(0 0 0 / 0.10);
--shadow-lg:   0 10px 15px -3px rgb(0 0 0 / 0.10), 0 4px 6px -4px rgb(0 0 0 / 0.10);
--shadow-xl:   0 20px 25px -5px rgb(0 0 0 / 0.10), 0 8px 10px -6px rgb(0 0 0 / 0.10);
--shadow-2xl:  0 25px 50px -12px rgb(0 0 0 / 0.25);
--shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);

/* Semantics */
--shadow-card:    var(--shadow-sm);
--shadow-dropdown: var(--shadow-lg);
--shadow-modal:   var(--shadow-2xl);
--shadow-input-focus: 0 0 0 3px rgb(var(--color-blue-500-rgb) / 0.4);
--shadow-button:  var(--shadow-xs);
--shadow-raised:  var(--shadow-md);
```

---

## Motion Tokens

```css
/* Duration primitives */
--duration-instant:  0ms;
--duration-75:       75ms;
--duration-100:      100ms;
--duration-150:      150ms;
--duration-200:      200ms;
--duration-300:      300ms;
--duration-500:      500ms;
--duration-700:      700ms;
--duration-1000:     1000ms;

/* Easing primitives */
--easing-linear:     linear;
--easing-in:         cubic-bezier(0.4, 0, 1, 1);
--easing-out:        cubic-bezier(0, 0, 0.2, 1);
--easing-in-out:     cubic-bezier(0.4, 0, 0.2, 1);
--easing-spring:     cubic-bezier(0.34, 1.56, 0.64, 1);   /* Slight overshoot */
--easing-anticipate: cubic-bezier(0.36, 0, 0.66, -0.56);  /* Pull-back before forward */

/* Semantic motion tokens */
--duration-transition-fast:   var(--duration-100);   /* Hover states, color changes */
--duration-transition-normal: var(--duration-200);   /* Most UI transitions */
--duration-transition-slow:   var(--duration-300);   /* Expanding panels, drawers */
--duration-enter:             var(--duration-200);
--duration-exit:              var(--duration-150);   /* Exits feel snappier */

--easing-transition:  var(--easing-out);      /* Default for most transitions */
--easing-enter:       var(--easing-out);      /* Elements entering the page */
--easing-exit:        var(--easing-in);       /* Elements leaving the page */
--easing-bounce:      var(--easing-spring);   /* Playful interactions */
```

---

## Z-Index Tokens

```css
/* Named layers — never use raw numbers in components */
--z-below:    -1;     /* Behind everything (e.g., background fills) */
--z-base:      0;
--z-raised:   10;     /* Slightly raised cards */
--z-sticky:   100;    /* Sticky headers, sidebars */
--z-dropdown: 200;    /* Menus, popover triggers */
--z-overlay:  300;    /* Semi-transparent page overlays */
--z-modal:    400;    /* Dialog/modal windows */
--z-popover:  500;    /* Tooltips, rich popovers above modals */
--z-toast:    600;    /* Notifications — always on top */
--z-max:      9999;   /* Emergency override — use sparingly */
```
