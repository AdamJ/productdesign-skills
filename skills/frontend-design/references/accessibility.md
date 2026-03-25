# Accessibility Patterns

## WCAG 2.1 AA Requirements

Every component must meet accessibility standards.

## Semantic HTML

```jsx
// Good - semantic elements
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>

// Bad - div soup
<div className="nav">
  <div className="nav-item">Home</div>
</div>
```

## Keyboard Navigation

All interactive elements must be keyboard accessible:

```jsx
function Modal({ isOpen, onClose, children }) {
  useEffect(() => {
    if (!isOpen) return;

    // Trap focus within modal
    const handleKeyDown = e => {
      if (e.key === 'Escape') onClose();
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  return isOpen ? (
    <div
      className="modal"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div className="modal-content">
        <h2 id="modal-title">Modal Title</h2>
        {children}
        <button onClick={onClose} aria-label="Close modal">
          ×
        </button>
      </div>
    </div>
  ) : null;
}
```

## Color Contrast

Ensure minimum contrast ratios:

```css
/* Ensure minimum 4.5:1 contrast for normal text */
.text-on-dark {
  background: #1a1a1a;
  color: #ffffff; /* 21:1 contrast */
}

/* 3:1 minimum for large text (18pt+) */
.heading-on-light {
  background: #ffffff;
  color: #666666; /* 5.7:1 contrast */
}
```

## ARIA Attributes

### Loading States

```jsx
<button disabled aria-busy="true">
  Loading...
</button>
```

### Form Validation

```jsx
<input
  type="email"
  aria-invalid={errors.email ? 'true' : 'false'}
  aria-describedby={errors.email ? 'email-error' : undefined}
/>;
{
  errors.email && (
    <span id="email-error" role="alert">
      {errors.email}
    </span>
  );
}
```

### Interactive Widgets

```jsx
<div role="tablist" aria-label="Account settings">
  <button
    role="tab"
    aria-selected={activeTab === 'profile'}
    aria-controls="profile-panel"
  >
    Profile
  </button>
</div>
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

## Accessibility Testing Checklist

Before completing any frontend component, verify:

- [ ] **Semantic HTML** - Using appropriate HTML5 elements
- [ ] **Keyboard navigation** - All interactive elements reachable and operable via keyboard
- [ ] **Color contrast** - Minimum 4.5:1 for normal text, 3:1 for large text
- [ ] **ARIA attributes** - Used where needed for complex interactions
- [ ] **Focus indicators** - Visible on all interactive elements
- [ ] **Screen reader** - Content makes sense when read aloud (test with VoiceOver/NVDA)
- [ ] **Alt text** - All images have descriptive alt attributes
- [ ] **Form labels** - All inputs properly labeled
- [ ] **Error messages** - Clear, associated with inputs via aria-describedby

## Common Accessibility Patterns

### Skip Navigation Link

```jsx
<a href="#main-content" className="skip-link">
  Skip to main content
</a>

<main id="main-content">
  {/* Page content */}
</main>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--color-primary);
  color: white;
  padding: 8px;
  text-decoration: none;
}

.skip-link:focus {
  top: 0;
}
```

### Accessible Dropdown

```jsx
function Dropdown({ label, items }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="dropdown">
      <button
        aria-expanded={isOpen}
        aria-haspopup="true"
        onClick={() => setIsOpen(!isOpen)}
      >
        {label}
      </button>
      {isOpen && (
        <ul role="menu">
          {items.map(item => (
            <li key={item.id} role="menuitem">
              <button onClick={item.onClick}>{item.label}</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

### Live Region for Dynamic Updates

```jsx
function StatusMessage({ message, type }) {
  return (
    <div
      role="status"
      aria-live={type === 'error' ? 'assertive' : 'polite'}
      className={`status-${type}`}
    >
      {message}
    </div>
  );
}
```

## Touch Targets

Ensure minimum size for mobile:

```css
/* Minimum 44×44px touch targets */
.btn {
  min-width: 44px;
  min-height: 44px;
  padding: var(--space-3) var(--space-4);
}
```

## Reduced Motion

Respect user preferences:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
