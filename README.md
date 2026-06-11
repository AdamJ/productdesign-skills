# Product Design Skills

Productdesign-skills is a complete set of skills for incorporating into your agentic workflow to assist in designing and creating products.

## What's Included

| Skill | Description | Category |
| --- | --- | --- |
| [Frontend design](/skills/frontend-design/) | A plugin to assist with frontend design tasks and workflows. | Design |
| [Interactive Architecture Diagram](/skills/interactive-diagram/) | A plugin to generate interactive architecture diagrams based on user input. | Architecture |
| [MCP Builder](/skills/mcp-builder/) | A plugin to guide the user in creating high-quality MCPs with best practices and templates. | Development |
| [MCP Server Scaffolding](/skills/mcp-server-scaffolding/) | A plugin to scaffold MCP server projects based on user input. | Development |
| [Portfolio Case Study Generator](/skills/portfolio-case-study-generator/) | Generate a case study based off of your current code base. | Documentation |
| [Synching Project Documentation](/skills/syncing-project-documentation/) | Sync your docs, README, and CLAUDE files after implementing a feature or fix. | Documentation |
| [Accessibility Audit](/skills/accessibility-audit/) | Audit components, pages, and designs against WCAG 2.1 AA and output a prioritized remediation checklist with code-level fixes. | Design |
| [Organizational Docs Writer](/skills/organizational-docs-writer/) | Creates and updates organizational documents with consistent formatting, visual identity, and house style. | Documentation |

## Installation

To install this marketplace, open Claude Code and enter the following:

```bash
/plugin marketplace add https://github.com/AdamJ/productdesign-marktplace.git
```

1. Once installed, enter the `/plugin` command to manage Claude Code plugins.
2. Cycle to the "Marketplaces" tab and key down to the **productdesign-marketplace**.
  a. Verify that auto-updates are enabled.
3. Enter "Browser Plugins" to review available plugins.
  a. If you have already installed plugins from this marketplace, be sure to enter the "Update marketplace" option first, as skills may have been added or changed.
4. If you ever need to disable/remove the **productdesign-marketplace**, you may do so by selecting "Remove marketplace" and following any subsequent prompts.

### Verify Installation

Start up a new session and ask for something that should trigger the agent to utilize a skill (e.g. "sync my documentation"). The agent should automatically select the proper skill for the request.

## Licensing

> MIT License - [LICENSE](LICENSE)

All skills are subject to their original licensing, where applicable.

Original skills copyright 2026 [Adam J. Jolicoeur](mailto:contact@adamjolicoeur.com)
