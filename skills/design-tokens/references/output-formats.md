# Token Output Formats

Reference templates for generating tokens in each target format. Choose based on the project's
stack. Multiple formats can coexist — a project may ship CSS custom properties as the
authoritative source and derive a Tailwind config from the same values.

---

## CSS Custom Properties

The most portable format. Works in any web project regardless of framework.

### File structure

```
/styles
  tokens/
    primitives.css    ← raw values only, no references to other tokens
    semantics.css     ← aliases referencing primitives
    (components.css)  ← optional, component-scoped tokens
  tokens.css          ← barrel file that @imports the above in order
```

### primitives.css

```css
/* ============================================================
   COLOR PRIMITIVES
   ============================================================ */
:root {
  /* Blue */
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

  /* Neutral */
  --color-neutral-0:    #ffffff;
  --color-neutral-50:   #f9fafb;
  --color-neutral-100:  #f3f4f6;
  --color-neutral-200:  #e5e7eb;
  --color-neutral-300:  #d1d5db;
  --color-neutral-400:  #9ca3af;
  --color-neutral-500:  #6b7280;
  --color-neutral-600:  #4b5563;
  --color-neutral-700:  #374151;
  --color-neutral-800:  #1f2937;
  --color-neutral-900:  #111827;
  --color-neutral-950:  #030712;
  --color-neutral-1000: #000000;

  /* Feedback hues */
  --color-red-50:  #fef2f2;
  --color-red-400: #f87171;
  --color-red-500: #ef4444;
  --color-red-600: #dc2626;
  --color-red-700: #b91c1c;

  --color-green-50:  #f0fdf4;
  --color-green-400: #4ade80;
  --color-green-500: #22c55e;
  --color-green-700: #15803d;

  --color-amber-50:  #fffbeb;
  --color-amber-400: #fbbf24;
  --color-amber-500: #f59e0b;
  --color-amber-700: #b45309;

  /* ============================================================
     SPACING PRIMITIVES
     ============================================================ */
  --space-0:    0;
  --space-px:   1px;
  --space-0-5:  0.125rem;
  --space-1:    0.25rem;
  --space-1-5:  0.375rem;
  --space-2:    0.5rem;
  --space-2-5:  0.625rem;
  --space-3:    0.75rem;
  --space-3-5:  0.875rem;
  --space-4:    1rem;
  --space-5:    1.25rem;
  --space-6:    1.5rem;
  --space-7:    1.75rem;
  --space-8:    2rem;
  --space-10:   2.5rem;
  --space-12:   3rem;
  --space-16:   4rem;
  --space-20:   5rem;
  --space-24:   6rem;
  --space-32:   8rem;

  /* ============================================================
     TYPOGRAPHY PRIMITIVES
     ============================================================ */
  --font-family-sans:  ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
                       "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-family-mono:  ui-monospace, SFMono-Regular, "SF Mono", Consolas,
                       "Liberation Mono", Menlo, monospace;

  --font-size-2xs: 0.625rem;
  --font-size-xs:  0.75rem;
  --font-size-sm:  0.875rem;
  --font-size-md:  1rem;
  --font-size-lg:  1.125rem;
  --font-size-xl:  1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  --font-size-5xl: 3rem;
  --font-size-6xl: 3.75rem;

  --font-weight-normal:   400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;

  --line-height-none:    1;
  --line-height-tight:   1.25;
  --line-height-snug:    1.375;
  --line-height-normal:  1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose:   2;

  --letter-spacing-tighter: -0.05em;
  --letter-spacing-tight:   -0.025em;
  --letter-spacing-normal:  0em;
  --letter-spacing-wide:    0.025em;
  --letter-spacing-wider:   0.05em;
  --letter-spacing-widest:  0.1em;

  /* ============================================================
     RADIUS PRIMITIVES
     ============================================================ */
  --radius-none: 0;
  --radius-1:    0.125rem;
  --radius-2:    0.25rem;
  --radius-3:    0.375rem;
  --radius-4:    0.5rem;
  --radius-6:    0.75rem;
  --radius-8:    1rem;
  --radius-12:   1.5rem;
  --radius-full: 9999px;

  /* ============================================================
     SHADOW PRIMITIVES
     ============================================================ */
  --shadow-none: none;
  --shadow-xs:   0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm:   0 1px 3px 0 rgb(0 0 0 / 0.10), 0 1px 2px -1px rgb(0 0 0 / 0.10);
  --shadow-md:   0 4px 6px -1px rgb(0 0 0 / 0.10), 0 2px 4px -2px rgb(0 0 0 / 0.10);
  --shadow-lg:   0 10px 15px -3px rgb(0 0 0 / 0.10), 0 4px 6px -4px rgb(0 0 0 / 0.10);
  --shadow-xl:   0 20px 25px -5px rgb(0 0 0 / 0.10), 0 8px 10px -6px rgb(0 0 0 / 0.10);
  --shadow-2xl:  0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);

  /* ============================================================
     MOTION PRIMITIVES
     ============================================================ */
  --duration-75:   75ms;
  --duration-100:  100ms;
  --duration-150:  150ms;
  --duration-200:  200ms;
  --duration-300:  300ms;
  --duration-500:  500ms;

  --easing-linear:  linear;
  --easing-in:      cubic-bezier(0.4, 0, 1, 1);
  --easing-out:     cubic-bezier(0, 0, 0.2, 1);
  --easing-in-out:  cubic-bezier(0.4, 0, 0.2, 1);
  --easing-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);

  /* ============================================================
     Z-INDEX PRIMITIVES
     ============================================================ */
  --z-below:    -1;
  --z-base:      0;
  --z-raised:   10;
  --z-sticky:   100;
  --z-dropdown: 200;
  --z-overlay:  300;
  --z-modal:    400;
  --z-popover:  500;
  --z-toast:    600;
}
```

### semantics.css

```css
:root {
  /* ============================================================
     COLOR SEMANTICS
     ============================================================ */

  /* Text */
  --color-text-primary:   var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-text-tertiary:  var(--color-neutral-400);
  --color-text-inverse:   var(--color-neutral-0);
  --color-text-disabled:  var(--color-neutral-400);
  --color-text-link:      var(--color-blue-600);
  --color-text-link-hover: var(--color-blue-700);
  --color-text-success:   var(--color-green-700);
  --color-text-warning:   var(--color-amber-700);
  --color-text-danger:    var(--color-red-600);
  --color-text-info:      var(--color-blue-600);

  /* Backgrounds */
  --color-bg-canvas:         var(--color-neutral-0);
  --color-bg-surface:        var(--color-neutral-0);
  --color-bg-surface-raised: var(--color-neutral-50);
  --color-bg-overlay:        var(--color-neutral-100);
  --color-bg-inverse:        var(--color-neutral-900);
  --color-bg-primary:        var(--color-blue-600);
  --color-bg-primary-hover:  var(--color-blue-700);
  --color-bg-success:        var(--color-green-50);
  --color-bg-warning:        var(--color-amber-50);
  --color-bg-danger:         var(--color-red-50);
  --color-bg-info:           var(--color-blue-50);

  /* Borders */
  --color-border-default:  var(--color-neutral-200);
  --color-border-strong:   var(--color-neutral-400);
  --color-border-focus:    var(--color-blue-500);
  --color-border-danger:   var(--color-red-400);
  --color-border-success:  var(--color-green-400);
  --color-border-disabled: var(--color-neutral-200);

  /* Actions */
  --color-action-primary:           var(--color-blue-600);
  --color-action-primary-hover:     var(--color-blue-700);
  --color-action-primary-active:    var(--color-blue-800);
  --color-action-primary-text:      var(--color-neutral-0);
  --color-action-destructive:       var(--color-red-600);
  --color-action-destructive-hover: var(--color-red-700);
  --color-action-destructive-text:  var(--color-neutral-0);

  /* ============================================================
     SPACING SEMANTICS
     ============================================================ */
  --space-component-xs: var(--space-1);
  --space-component-sm: var(--space-2);
  --space-component-md: var(--space-3);
  --space-component-lg: var(--space-4);
  --space-component-xl: var(--space-6);

  --space-gap-xs: var(--space-1);
  --space-gap-sm: var(--space-2);
  --space-gap-md: var(--space-4);
  --space-gap-lg: var(--space-6);
  --space-gap-xl: var(--space-8);

  --space-layout-xs: var(--space-8);
  --space-layout-sm: var(--space-12);
  --space-layout-md: var(--space-16);
  --space-layout-lg: var(--space-24);
  --space-layout-xl: var(--space-32);

  /* ============================================================
     TYPOGRAPHY SEMANTICS
     ============================================================ */
  --font-family-body:    var(--font-family-sans);
  --font-family-heading: var(--font-family-sans);
  --font-family-code:    var(--font-family-mono);

  --font-size-body-sm: var(--font-size-sm);
  --font-size-body:    var(--font-size-md);
  --font-size-body-lg: var(--font-size-lg);
  --font-size-label:   var(--font-size-sm);
  --font-size-caption: var(--font-size-xs);

  --font-size-heading-sm: var(--font-size-lg);
  --font-size-heading-md: var(--font-size-2xl);
  --font-size-heading-lg: var(--font-size-3xl);
  --font-size-heading-xl: var(--font-size-4xl);
  --font-size-display:    var(--font-size-5xl);

  /* ============================================================
     RADIUS SEMANTICS
     ============================================================ */
  --radius-badge:   var(--radius-full);
  --radius-button:  var(--radius-2);
  --radius-card:    var(--radius-4);
  --radius-input:   var(--radius-2);
  --radius-modal:   var(--radius-6);
  --radius-tooltip: var(--radius-2);
  --radius-tag:     var(--radius-full);

  /* ============================================================
     SHADOW SEMANTICS
     ============================================================ */
  --shadow-card:     var(--shadow-sm);
  --shadow-dropdown: var(--shadow-lg);
  --shadow-modal:    var(--shadow-2xl);
  --shadow-raised:   var(--shadow-md);
  --shadow-button:   var(--shadow-xs);

  /* ============================================================
     MOTION SEMANTICS
     ============================================================ */
  --duration-transition-fast:   var(--duration-100);
  --duration-transition-normal: var(--duration-200);
  --duration-transition-slow:   var(--duration-300);
  --duration-enter:             var(--duration-200);
  --duration-exit:              var(--duration-150);

  --easing-transition: var(--easing-out);
  --easing-enter:      var(--easing-out);
  --easing-exit:       var(--easing-in);
  --easing-bounce:     var(--easing-spring);
}

/* Dark mode overrides — semantic layer only */
[data-theme="dark"],
@media (prefers-color-scheme: dark) {
  :root {
    --color-text-primary:      var(--color-neutral-50);
    --color-text-secondary:    var(--color-neutral-400);
    --color-text-tertiary:     var(--color-neutral-600);
    --color-text-inverse:      var(--color-neutral-900);
    --color-bg-canvas:         var(--color-neutral-950);
    --color-bg-surface:        var(--color-neutral-900);
    --color-bg-surface-raised: var(--color-neutral-800);
    --color-bg-overlay:        var(--color-neutral-800);
    --color-bg-inverse:        var(--color-neutral-50);
    --color-border-default:    var(--color-neutral-700);
    --color-border-strong:     var(--color-neutral-500);
  }
}
```

### tokens.css (barrel)

```css
@import "./tokens/primitives.css";
@import "./tokens/semantics.css";
/* @import "./tokens/components.css"; */
```

---

## Tailwind v3

Extend the default theme in `tailwind.config.js`. Tailwind resolves CSS var references at
build time so tokens stay live if also shipped as custom properties.

```js
// tailwind.config.js
const { fontFamily } = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        // Expose semantic tokens as Tailwind color classes
        // Usage: text-text-primary, bg-bg-surface, border-border-default
        text: {
          primary:   "var(--color-text-primary)",
          secondary: "var(--color-text-secondary)",
          tertiary:  "var(--color-text-tertiary)",
          inverse:   "var(--color-text-inverse)",
          disabled:  "var(--color-text-disabled)",
          link:      "var(--color-text-link)",
          success:   "var(--color-text-success)",
          warning:   "var(--color-text-warning)",
          danger:    "var(--color-text-danger)",
          info:      "var(--color-text-info)",
        },
        bg: {
          canvas:        "var(--color-bg-canvas)",
          surface:       "var(--color-bg-surface)",
          "surface-raised": "var(--color-bg-surface-raised)",
          overlay:       "var(--color-bg-overlay)",
          inverse:       "var(--color-bg-inverse)",
          primary:       "var(--color-bg-primary)",
          "primary-hover": "var(--color-bg-primary-hover)",
          success:       "var(--color-bg-success)",
          warning:       "var(--color-bg-warning)",
          danger:        "var(--color-bg-danger)",
          info:          "var(--color-bg-info)",
        },
        border: {
          default:  "var(--color-border-default)",
          strong:   "var(--color-border-strong)",
          focus:    "var(--color-border-focus)",
          danger:   "var(--color-border-danger)",
          success:  "var(--color-border-success)",
          disabled: "var(--color-border-disabled)",
        },
        action: {
          primary:             "var(--color-action-primary)",
          "primary-hover":     "var(--color-action-primary-hover)",
          "primary-active":    "var(--color-action-primary-active)",
          "primary-text":      "var(--color-action-primary-text)",
          destructive:         "var(--color-action-destructive)",
          "destructive-hover": "var(--color-action-destructive-hover)",
          "destructive-text":  "var(--color-action-destructive-text)",
        },
      },

      fontFamily: {
        sans:  ["var(--font-family-body)", ...fontFamily.sans],
        serif: ["var(--font-family-serif)", ...fontFamily.serif],
        mono:  ["var(--font-family-code)", ...fontFamily.mono],
      },

      fontSize: {
        "body-sm": ["var(--font-size-body-sm)", { lineHeight: "var(--line-height-normal)" }],
        body:      ["var(--font-size-body)",    { lineHeight: "var(--line-height-normal)" }],
        "body-lg": ["var(--font-size-body-lg)", { lineHeight: "var(--line-height-relaxed)" }],
        label:     ["var(--font-size-label)",   { lineHeight: "var(--line-height-normal)" }],
        caption:   ["var(--font-size-caption)", { lineHeight: "var(--line-height-normal)" }],
        "heading-sm": ["var(--font-size-heading-sm)", { lineHeight: "var(--line-height-tight)" }],
        "heading-md": ["var(--font-size-heading-md)", { lineHeight: "var(--line-height-tight)" }],
        "heading-lg": ["var(--font-size-heading-lg)", { lineHeight: "var(--line-height-tight)" }],
        "heading-xl": ["var(--font-size-heading-xl)", { lineHeight: "var(--line-height-tight)" }],
        display:      ["var(--font-size-display)",    { lineHeight: "var(--line-height-none)" }],
      },

      borderRadius: {
        badge:   "var(--radius-badge)",
        button:  "var(--radius-button)",
        card:    "var(--radius-card)",
        input:   "var(--radius-input)",
        modal:   "var(--radius-modal)",
        tooltip: "var(--radius-tooltip)",
      },

      boxShadow: {
        card:     "var(--shadow-card)",
        dropdown: "var(--shadow-dropdown)",
        modal:    "var(--shadow-modal)",
        raised:   "var(--shadow-raised)",
        button:   "var(--shadow-button)",
      },

      transitionDuration: {
        fast:   "var(--duration-transition-fast)",
        normal: "var(--duration-transition-normal)",
        slow:   "var(--duration-transition-slow)",
      },

      transitionTimingFunction: {
        DEFAULT: "var(--easing-transition)",
        enter:   "var(--easing-enter)",
        exit:    "var(--easing-exit)",
        bounce:  "var(--easing-bounce)",
      },

      zIndex: {
        below:    "var(--z-below)",
        raised:   "var(--z-raised)",
        sticky:   "var(--z-sticky)",
        dropdown: "var(--z-dropdown)",
        overlay:  "var(--z-overlay)",
        modal:    "var(--z-modal)",
        popover:  "var(--z-popover)",
        toast:    "var(--z-toast)",
      },
    },
  },
};
```

---

## Tailwind v4

Tailwind v4 uses a CSS-first configuration with `@theme`. No `tailwind.config.js` needed.
CSS custom properties defined inside `@theme` are automatically available as Tailwind utilities.

```css
/* app.css or globals.css */
@import "tailwindcss";

/* Primitive tokens (not exposed as utilities, just values) */
@layer base {
  :root {
    --color-blue-500: #3b82f6;
    --color-blue-600: #2563eb;
    --color-neutral-0:   #ffffff;
    --color-neutral-50:  #f9fafb;
    --color-neutral-900: #111827;
    /* ... all primitives */
  }
}

/* Semantic tokens exposed as Tailwind utilities via @theme */
@theme {
  /* Colors — available as text-*, bg-*, border-* utilities */
  --color-text-primary:   var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-bg-surface:     var(--color-neutral-0);
  --color-bg-primary:     var(--color-blue-600);
  --color-border-default: var(--color-neutral-200);

  /* Spacing — available as p-*, m-*, gap-* utilities */
  --spacing-component-sm: var(--space-2);
  --spacing-component-md: var(--space-4);
  --spacing-gap-md:       var(--space-4);
  --spacing-layout-md:    var(--space-16);

  /* Font size — available as text-* utilities */
  --font-size-body:       var(--font-size-md);
  --font-size-heading-lg: var(--font-size-3xl);

  /* Border radius — available as rounded-* utilities */
  --radius-card:   var(--radius-4);
  --radius-button: var(--radius-2);

  /* Shadows — available as shadow-* utilities */
  --shadow-card:     var(--shadow-sm);
  --shadow-dropdown: var(--shadow-lg);
}

/* Dark mode — override semantic tokens */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text-primary: var(--color-neutral-50);
    --color-bg-surface:   var(--color-neutral-900);
  }
}
```

---

## Style Dictionary JSON (W3C DTCG Format)

Use when tokens need to be consumed by multiple platforms (web, iOS, Android) or when
integrating with tools like Tokens Studio, Supernova, or Specify.

The W3C Design Token Community Group (DTCG) format uses `$value` and `$type` keys.

### tokens/primitives.json

```json
{
  "color": {
    "blue": {
      "500": { "$value": "#3b82f6", "$type": "color" },
      "600": { "$value": "#2563eb", "$type": "color" },
      "700": { "$value": "#1d4ed8", "$type": "color" }
    },
    "neutral": {
      "0":   { "$value": "#ffffff",  "$type": "color" },
      "50":  { "$value": "#f9fafb",  "$type": "color" },
      "900": { "$value": "#111827",  "$type": "color" },
      "950": { "$value": "#030712",  "$type": "color" }
    },
    "red": {
      "600": { "$value": "#dc2626", "$type": "color" }
    }
  },
  "space": {
    "2": { "$value": "0.5rem",  "$type": "dimension" },
    "4": { "$value": "1rem",    "$type": "dimension" },
    "8": { "$value": "2rem",    "$type": "dimension" },
    "16": { "$value": "4rem",   "$type": "dimension" }
  },
  "fontSize": {
    "sm": { "$value": "0.875rem", "$type": "dimension" },
    "md": { "$value": "1rem",     "$type": "dimension" },
    "2xl": { "$value": "1.5rem",  "$type": "dimension" }
  },
  "fontWeight": {
    "normal":   { "$value": 400, "$type": "fontWeight" },
    "semibold": { "$value": 600, "$type": "fontWeight" },
    "bold":     { "$value": 700, "$type": "fontWeight" }
  }
}
```

### tokens/semantics.json

References use `{path.to.token}` syntax.

```json
{
  "color": {
    "text": {
      "primary":   { "$value": "{color.neutral.900}", "$type": "color" },
      "secondary": { "$value": "{color.neutral.500}", "$type": "color" },
      "danger":    { "$value": "{color.red.600}",     "$type": "color" },
      "inverse":   { "$value": "{color.neutral.0}",   "$type": "color" }
    },
    "bg": {
      "surface":  { "$value": "{color.neutral.0}",   "$type": "color" },
      "primary":  { "$value": "{color.blue.600}",    "$type": "color" },
      "canvas":   { "$value": "{color.neutral.50}",  "$type": "color" }
    },
    "border": {
      "default": { "$value": "{color.neutral.200}", "$type": "color" },
      "focus":   { "$value": "{color.blue.500}",    "$type": "color" }
    },
    "action": {
      "primary":       { "$value": "{color.blue.600}", "$type": "color" },
      "primary-hover": { "$value": "{color.blue.700}", "$type": "color" }
    }
  },
  "space": {
    "component": {
      "sm": { "$value": "{space.2}", "$type": "dimension" },
      "md": { "$value": "{space.4}", "$type": "dimension" }
    },
    "layout": {
      "md": { "$value": "{space.16}", "$type": "dimension" }
    }
  }
}
```

### style-dictionary.config.js

```js
import StyleDictionary from "style-dictionary";

export default {
  source: ["tokens/primitives.json", "tokens/semantics.json"],
  platforms: {
    css: {
      transformGroup: "css",
      prefix: "",
      buildPath: "dist/",
      files: [
        {
          destination: "tokens.css",
          format: "css/variables",
          options: { outputReferences: true },
        },
      ],
    },
    js: {
      transformGroup: "js",
      buildPath: "dist/",
      files: [
        {
          destination: "tokens.js",
          format: "javascript/esm",
        },
      ],
    },
  },
};
```

---

## JavaScript / ES Module

Use when tokens need to be consumed in JavaScript (e.g., charting libraries, Canvas rendering,
React Native StyleSheet, or Storybook theme).

```js
// tokens/primitives.js
export const color = {
  blue: {
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
  },
  neutral: {
    0:   "#ffffff",
    50:  "#f9fafb",
    900: "#111827",
    950: "#030712",
  },
  red: {
    600: "#dc2626",
    700: "#b91c1c",
  },
};

export const space = {
  2: "0.5rem",
  4: "1rem",
  8: "2rem",
  16: "4rem",
};

// tokens/semantics.js
import { color, space } from "./primitives.js";

export const text = {
  primary:   color.neutral[900],
  secondary: color.neutral[500],
  danger:    color.red[600],
  inverse:   color.neutral[0],
};

export const bg = {
  surface: color.neutral[0],
  canvas:  color.neutral[50],
  primary: color.blue[600],
};

export const border = {
  default: color.neutral[200],
  focus:   color.blue[500],
};

export const component = {
  gap:     { sm: space[2], md: space[4] },
  padding: { sm: space[2], md: space[4] },
};
```

---

## Choosing a Format

| Situation | Recommended format |
|-----------|-------------------|
| Pure HTML/CSS project | CSS custom properties |
| React/Vue/Svelte with Tailwind v3 | CSS custom properties + Tailwind config |
| React/Vue/Svelte with Tailwind v4 | CSS custom properties + `@theme` |
| Multi-platform (web + mobile) | Style Dictionary JSON → generates all outputs |
| Canvas / chart library / React Native | JavaScript ES module |
| Tokens Studio / Supernova / Specify | W3C DTCG JSON |
| Storybook design system documentation | CSS custom properties + JS module |

When in doubt, ship CSS custom properties first — every other format can be derived from them,
and they work everywhere without a build step.
