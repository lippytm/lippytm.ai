# Copilot Instructions for {{REPO_NAME}}

## Project Overview

`{{REPO_NAME}}` is part of the **lippytm AI ecosystem** — a collection of AI, Web3, and automation repositories connected through [lippytm.ai](https://github.com/lippytm/lippytm.ai).

{{REPO_DESCRIPTION}}

## AI BrainKit

This repository uses the **lippytm AI BrainKit** (v{{BRAINKIT_VERSION}}) sourced from [lippytm.ai](https://github.com/lippytm/lippytm.ai/tree/main/brainkit). The BrainKit provides standardized AI configuration, connector patterns, and automation templates across all lippytm repositories.

## Architecture & Conventions

- **Language/Runtime**: {{LANGUAGE_RUNTIME}}
- **Module system**: {{MODULE_SYSTEM}}
- **Key patterns**: {{KEY_PATTERNS}}

## Code Style

- Use descriptive variable and function names that reflect the AI/Web3 domain.
- Prefer `async`/`await` over raw Promise chains.
- Wrap all external API/blockchain calls in try/catch with meaningful error messages.
- Document public APIs with JSDoc (JavaScript) or docstrings (Python).

## AI & Web3 Guidelines

- AI model calls should be rate-limited and include retry logic. Use exponential backoff:
  ```js
  // Simple retry with exponential backoff (no external deps)
  async function withRetry(fn, retries = 3, delayMs = 500) {
    for (let i = 0; i < retries; i++) {
      try { return await fn(); } catch (err) {
        if (i === retries - 1) throw err;
        await new Promise(r => setTimeout(r, delayMs * 2 ** i));
      }
    }
  }
  ```
- All blockchain interactions must handle network failures gracefully.
- Store contract ABIs in a dedicated `contracts/` or `abis/` directory.

## Related Repositories

This project connects to other lippytm repositories via the hub at [lippytm.ai](https://github.com/lippytm/lippytm.ai):

- **Hub**: [lippytm.ai](https://github.com/lippytm/lippytm.ai) — Central AI connection hub
- **Web3AI**: [Web3AI](https://github.com/lippytm/Web3AI) — Web3 AI integrations
- **Factory.ai**: [Factory.ai](https://github.com/lippytm/Factory.ai) — Workflow automation
- **AI-Time-Machines**: [AI-Time-Machines](https://github.com/lippytm/AI-Time-Machines) — AI agents

## Development Notes

{{DEVELOPMENT_NOTES}}
