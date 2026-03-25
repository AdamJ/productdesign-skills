---
name: syncing-project-documentation
description: Use when updating project documentation files (README, CLAUDE.md, CHANGELOG) after code changes, architectural updates, or feature additions. CRITICAL triggers: (1) After implementing any feature or fix, (2) When user asks to "update docs" or "update README", (3) Before creating PRs, (4) When you notice documentation is outdated. Prevents partial completion where only one file is updated under time pressure.
---

# Syncing Project Documentation

## Overview

**Core principle:** All three documentation files must be updated together to maintain consistency. Updating only one file creates documentation drift.

## The Rule

When code changes, **all three files get updated in the same session**:

1. README.md - User-facing: architecture, setup, usage
2. CLAUDE.md - Agent-facing: conventions, patterns, commands
3. CHANGELOG.md - History: what changed, where, why

**No exceptions for time pressure or "existing docs."**

- "Quick PR update" means update all files quickly, not skip files
- "README already has basics" means UPDATE the basics with new info
- "Existing docs are sufficient" is never true when code changed

## What Goes Where

| File             | Audience                       | Content                                                                                               |
| ---------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **README.md**    | External users, new developers | Project overview, architecture, setup instructions, usage examples, features                          |
| **CLAUDE.md**    | Future Claude instances        | Coding conventions, file organization, tech stack details, common commands, project-specific patterns |
| **CHANGELOG.md** | All developers                 | Recent changes with file paths, context, and dates                                                    |

## Process

For any code change:

1. **README.md**: User-facing changes (features, architecture, setup, usage)
2. **CLAUDE.md**: Developer-facing changes (conventions, patterns, commands, tech stack)
3. **CHANGELOG.md**: Change entry in `[Unreleased]` with file paths and context
4. **Verify**: Architecture in README matches conventions in CLAUDE.md; all features logged in CHANGELOG

## Red Flags - STOP and Update All Files

- "I'll just update the CHANGELOG"
- "Quick PR, only need README"
- "CLAUDE.md is internal, can skip"
- "Documented the main part, good enough"
- "Already updated one file, that's sufficient"
- **"Existing README is sufficient/good enough/has basics"**
- **"Minimal docs already present, just adding CHANGELOG"**
- "This change doesn't need CLAUDE.md updates"

**All of these mean: Go back and update all three files.**

**When code changes, existing docs are NEVER sufficient - they need updates.**

## Common Mistakes

| Mistake                                                  | Fix                                                    |
| -------------------------------------------------------- | ------------------------------------------------------ |
| Only update CHANGELOG under time pressure                | Update all three - "quick" doesn't mean "partial"      |
| **Claim existing README "has basics" and skip update**   | **Existing docs must be updated when code changes**    |
| README has new architecture, CLAUDE.md has old patterns  | Sync conventions in CLAUDE.md with README architecture |
| Feature in README, missing from CHANGELOG                | Add CHANGELOG entry with files and context             |
| **Only update CHANGELOG, claim other docs "sufficient"** | **All three files must reflect the change**            |
| Setup steps in README don't match CLAUDE.md commands     | Verify commands and update both for consistency        |

## Example: Adding OAuth2 Authentication

**README.md update:**

```markdown
## Authentication

This project uses OAuth2 with JWT tokens for authentication.

### Setup

1. Configure OAuth provider in `.env`:

    ```env
    OAUTH_CLIENT_ID=your_client_id
    OAUTH_CLIENT_SECRET=your_secret
    ```

2. Supported providers: Google, GitHub

### Usage
Users authenticate via `/api/auth/login` endpoint.
```

**CLAUDE.md update:**

```markdown
## Authentication Patterns

- OAuth2 flow implemented in `/src/auth/oauth.js`
- JWT validation uses `jsonwebtoken` library
- Token expiry: 24 hours
- Refresh token expiry: 7 days

### Common Commands

- Test auth: `npm run test:auth`
- Generate test token: `npm run auth:token`
```

**CHANGELOG.md update:**

```markdown
### Added

- OAuth2 authentication with JWT tokens
  — `/src/auth/oauth.js`, `/api/auth/login`, `.env.example`
  (Google and GitHub providers; 24hr token expiry)
```

Notice all three files updated with consistent, cross-referenced information.

## Verification Checklist

Before marking documentation complete:

- [ ] README.md updated with user-facing changes
- [ ] CLAUDE.md updated with conventions and patterns
- [ ] CHANGELOG.md updated with change entry and file paths
- [ ] All three files have consistent information
- [ ] No conflicting architecture or patterns between files
