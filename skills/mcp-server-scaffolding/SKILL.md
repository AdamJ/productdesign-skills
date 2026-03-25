---
name: mcp-server-scaffolding
description: Use when creating MCP servers, adding MCP tools, or deploying MCP services - prevents schema errors, missing validation, and deployment misconfigurations
---

# MCP Server Scaffolding

## Overview

**Build production-ready MCP servers with proper schemas, error handling, and deployment configs from the start.**

MCP servers communicate via stdio (stdin/stdout), not HTTP. They run as background processes or are invoked directly by MCP clients.

## ⚠️ CRITICAL: MCP Servers Are NOT Web Services

**NEVER configure MCP servers as HTTP web services. This is the #1 deployment mistake.**

MCP servers:

- ✅ Run as background workers/processes
- ✅ Use stdio transport (stdin/stdout)
- ✅ Are invoked by MCP clients (Claude Desktop, etc.)

MCP servers DO NOT:

- ❌ Expose HTTP endpoints
- ❌ Need PORT environment variables
- ❌ Have health check endpoints
- ❌ Use `type: web` in deployment configs

**If you're adding a health check endpoint or configuring PORT, you've misunderstood MCP architecture. STOP and review this section.**

## Core Principles

1. **Schemas are mandatory** - Every tool needs fully specified input validation
2. **Validate on startup** - Check environment variables exist before running
3. **Check errors first** - Never access success-path keys without checking for errors
4. **stdio not HTTP** - MCP servers don't expose web endpoints

## When to Use

Use this skill when:

- Creating a new MCP server from scratch
- Adding tools to an existing MCP server
- Preparing MCP server for deployment
- Debugging tool registration errors
- Working with FastMCP (Python) or MCP SDK (TypeScript)

**Don't skip this for "quick scaffolds"** - shortcuts create bugs that take longer to fix.

## Deployment Configurations (Read This First!)

### ❌ WRONG: HTTP Web Service

**This is the most common mistake. DO NOT DO THIS:**

```yaml
# ❌ WRONG - MCP servers don't run as web services
services:
  - type: web # WRONG - should be "worker"
    name: mcp-server
    buildCommand: npm install && npm run build
    startCommand: npm start
    healthCheckPath: /health # WRONG - MCP servers don't expose HTTP
    envVars:
      - key: PORT # WRONG - MCP uses stdio, not ports
        value: 3000
```

**Why this doesn't work:** MCP servers communicate via stdio (stdin/stdout), not HTTP. They can't respond to health check probes or serve HTTP requests.

### ✅ CORRECT: Background Worker

```yaml
# ✅ CORRECT - MCP server as background worker
services:
  - type: worker # Correct - background process
    name: mcp-server
    env: node
    buildCommand: npm install && npm run build
    startCommand: node dist/index.js
    envVars:
      - key: DATABASE_URL
        sync: false
      - key: NODE_ENV
        value: production
    # No PORT, no healthCheckPath
```

**Key differences:**

- `type: worker` not `type: web`
- No `PORT` environment variable
- No `healthCheckPath`
- MCP server runs on stdio, invoked by MCP clients

**Note:** Most MCP servers are NOT deployed as long-running services. They're typically invoked directly by MCP clients (like Claude Desktop) on your local machine or accessed via stdio protocols. Only deploy to platforms like Render if you specifically need remote access to your MCP server.

## Tool Schema Patterns

### TypeScript (MCP SDK)

```typescript
import { z } from 'zod';

// ✅ CORRECT: Fully specified Zod schema
const SearchDocsSchema = z.object({
  query: z.string().min(1).max(500).describe('Search query'),
  doc_set: z.enum(['casim', 'rtu', 'terms']).optional(),
  limit: z.number().min(1).max(50).default(10)
});

server.registerTool(
  'search_docs',
  {
    title: 'Search Documentation',
    description: 'Search for keywords in documentation sets',
    inputSchema: SearchDocsSchema // Pass Zod object directly
  },
  async params => {
    // params is validated and typed
    const { query, doc_set, limit } = params;

    try {
      const results = await searchDocs(query, doc_set, limit);
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(results, null, 2)
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
);
```

### Python (FastMCP)

```python
from fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("Documentation Server")

# ✅ CORRECT: Pydantic model for validation
class SearchDocsArgs(BaseModel):
    query: str = Field(min_length=1, max_length=500, description="Search query")
    doc_set: str | None = Field(default=None, description="Documentation set")
    limit: int = Field(default=10, ge=1, le=50)

@mcp.tool()
def search_docs(args: SearchDocsArgs) -> dict:
    """Search for keywords in documentation sets"""
    try:
        results = perform_search(args.query, args.doc_set, args.limit)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
```

## Error Handling Pattern

**Always check for errors before accessing success-path keys:**

```python
# ❌ WRONG: Assumes success
@mcp.tool()
def get_model(model_id: str):
    result = db.query("SELECT * FROM models WHERE id = ?", model_id)
    return {"model_id": result["model_id"]}  # Crashes if query fails

# ✅ CORRECT: Check errors first
@mcp.tool()
def get_model(model_id: str):
    result = db.query("SELECT * FROM models WHERE id = ?", model_id)

    if "error" in result:
        return {"error": result["error"]}

    if not result.get("model_id"):
        return {"error": f"Model {model_id} not found"}

    return {
        "model_id": result["model_id"],
        "name": result.get("name", "Unknown")
    }
```

## Environment Variable Validation

**Validate on startup, not at first use:**

```python
import os
import sys

# ✅ CORRECT: Validate before server runs
required_env_vars = ["DATABASE_URL", "API_KEY"]
missing = [var for var in required_env_vars if not os.getenv(var)]

if missing:
    print(f"ERROR: Missing required environment variables: {', '.join(missing)}", file=sys.stderr)
    sys.exit(1)

# Now safe to use
DATABASE_URL = os.getenv("DATABASE_URL")
```

## Common Mistakes

| Mistake                                       | Why It's Wrong                                         | Fix                                                       |
| --------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| `inputSchema: {}`                             | Empty dict is invalid, causes tool registration errors | Use Zod (TypeScript) or Pydantic (Python) for full schema |
| Accessing `result['key']` without error check | Crashes when query/API call fails                      | Check for `error` key first, use `.get()` with defaults   |
| Configuring as HTTP web service               | MCP uses stdio, not HTTP endpoints                     | Use `type: worker` or background process config           |
| Hardcoded database engine assumptions         | Fails when env changes (SQLite → SQL Server)           | Read from environment, validate on startup                |
| Copying existing tool patterns blindly        | Propagates bugs from "working" code                    | **Review patterns for correctness before copying**        |

## Red Flags - STOP and Review

These thoughts mean you're about to make a critical mistake:

| Rationalization                       | Reality                                     | Correct Action                         |
| ------------------------------------- | ------------------------------------------- | -------------------------------------- |
| "I'll add proper schemas later"       | Takes 2 minutes now, hours to debug later   | Add Zod/Pydantic schemas immediately   |
| "Just copying the existing pattern"   | Existing code may have bugs                 | Review patterns for correctness first  |
| "Quick scaffold, will iterate"        | Shortcuts create deeper bugs                | Follow checklist, saves time overall   |
| "Health checks keep Render happy"     | **MCP servers don't use HTTP**              | Use `type: worker`, no health checks   |
| "Need PORT for deployment"            | **MCP uses stdio, not ports**               | Remove PORT env var entirely           |
| "Maybe just one health endpoint"      | **This breaks MCP architecture**            | No HTTP server, period                 |
| "Skipping env var validation for now" | Will fail in production with cryptic errors | Validate on startup before server runs |

**If you're adding healthCheckPath, PORT, or type: web → You've fundamentally misunderstood MCP. Re-read the CRITICAL section above.**

## Checklist for New MCP Tools

- [ ] Input schema fully specified (Zod/Pydantic, not empty dict)
- [ ] Error handling checks errors before accessing success keys
- [ ] Try/catch around external calls (database, API, file system)
- [ ] Input validation (string length, numeric ranges, required fields)
- [ ] Tool description clearly explains what it does
- [ ] Test with MCP Inspector before deploying

## Checklist for MCP Server Deployment

- [ ] Environment variables validated on startup
- [ ] Configured as background worker/process (not web service)
- [ ] No HTTP endpoints, PORT, or healthCheckPath
- [ ] Build command installs dependencies and compiles
- [ ] Start command runs the built server
- [ ] Database connections use environment variables (no hardcoded values)

## Real-World Impact

**Before this skill (baseline tests):**

- Deployment configs for HTTP web services (non-functional)
- Empty `inputSchema: {}` dicts causing MCP Inspector errors
- Runtime crashes from missing error handling
- Blindly copied buggy patterns from existing code

**After applying this skill:**

- Correct stdio-based worker configurations
- Fully validated input schemas catching errors early
- Graceful error handling with clear messages
- Critical review of existing patterns before copying

**Time saved:** 15 minutes upfront prevents hours debugging deployment issues and runtime crashes.
