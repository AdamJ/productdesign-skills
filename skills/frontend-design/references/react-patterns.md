# React Component Patterns

## Component Structure

Both functional and class components are acceptable — choose based on context:

### Functional Components (preferred for new development)

```jsx
import React, { useState, useEffect } from 'react';
import './ComponentName.css';

/**
 * ComponentName - Brief description of purpose and behavior
 *
 * @param {Object} props
 * @param {string} props.title - Title to display
 * @param {Function} props.onAction - Callback when action occurs
 */
function ComponentName({ title, onAction }) {
  const [state, setState] = useState(initialValue);

  useEffect(() => {
    // Side effects
  }, [dependencies]);

  return <div className="component-name">{/* Component JSX */}</div>;
}

export default ComponentName;
```

### Class Components (when stateful logic or lifecycle methods are complex)

```jsx
import React, { Component } from 'react';
import './ComponentName.css';

/**
 * ComponentName - Brief description
 */
class ComponentName extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // Initial state
    };
  }

  componentDidMount() {
    // Lifecycle logic
  }

  render() {
    return <div className="component-name">{/* Component JSX */}</div>;
  }
}

export default ComponentName;
```

## State Management with Context API

```jsx
// contexts/ThemeContext.js
import React, { createContext, useState, useContext } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}
```

## Common Component Patterns

### Button Component with Variants

```jsx
function Button({
  children,
  variant = 'primary',
  size = 'medium',
  icon,
  onClick,
  disabled = false,
  type = 'button',
  ...props
}) {
  const classNames = [
    'btn',
    `btn-${variant}`,
    `btn-${size}`,
    icon && !children ? 'btn-icon' : '',
    disabled ? 'is-disabled' : ''
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <button
      type={type}
      className={classNames}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {icon && (
        <span className="btn-icon-wrapper" aria-hidden="true">
          {icon}
        </span>
      )}
      {children && <span className="btn-text">{children}</span>}
    </button>
  );
}
```

### Form with Validation

```jsx
function ContactForm() {
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  const validate = () => {
    const newErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = e => {
    e.preventDefault();
    if (validate()) {
      // Submit logic
    }
  };

  const handleBlur = field => {
    setTouched({ ...touched, [field]: true });
    validate();
  };

  return (
    <form onSubmit={handleSubmit} className="form" noValidate>
      <div className="form-field">
        <label htmlFor="name" className="form-label">
          Name
        </label>
        <input
          id="name"
          type="text"
          className="form-input"
          value={formData.name}
          onChange={e => setFormData({ ...formData, name: e.target.value })}
          onBlur={() => handleBlur('name')}
          aria-invalid={touched.name && errors.name ? 'true' : 'false'}
          aria-describedby={
            touched.name && errors.name ? 'name-error' : undefined
          }
        />
        {touched.name && errors.name && (
          <span id="name-error" className="form-error" role="alert">
            {errors.name}
          </span>
        )}
      </div>

      <button type="submit" className="btn-primary">
        Submit
      </button>
    </form>
  );
}
```

### Modal Component

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

  // Prevent scroll when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.overflow = '';
      };
    }
  }, [isOpen]);

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

## Distinctive vs Generic Example

### Generic AI Pattern (Avoid):

```jsx
// Templated, forgettable design
<div className="hero">
  <h1
    style={{
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      borderRadius: '24px',
      padding: '60px',
      textAlign: 'center'
    }}
  >
    Welcome to Our Product
  </h1>
  <p style={{ textAlign: 'center', fontSize: '18px' }}>
    The best solution for all your needs
  </p>
  <button
    style={{
      borderRadius: '999px',
      background: 'linear-gradient(to right, #667eea, #764ba2)'
    }}
  >
    Get Started
  </button>
</div>
```

### Distinctive Design (Preferred):

```jsx
// Unique, intentional layout with personality
<section className="hero-split">
  <div className="hero-content">
    <span className="hero-label">Product Launch 2025</span>
    <h1 className="hero-title">
      Built for teams who
      <span className="hero-highlight">move fast</span>
    </h1>
    <p className="hero-description">
      Collaborative project management that adapts to your workflow, not the
      other way around.
    </p>
    <div className="hero-actions">
      <a href="/signup" className="btn-primary">
        Start free trial
      </a>
      <a href="/demo" className="btn-secondary">
        Watch demo
        <svg className="btn-icon" aria-hidden="true">
          <use href="#icon-play" />
        </svg>
      </a>
    </div>
  </div>
  <div className="hero-visual">
    <img
      src="/dashboard-preview.png"
      alt="Dashboard showing project timeline and team activity"
      className="hero-image"
    />
  </div>
</section>
```
