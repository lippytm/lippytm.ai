# Copilot Instructions for lippytm.ai

## Project Overview

`lippytm.ai` is an AI Web3 connection hub that integrates Gist, Git, GitLab, GitHub, and all of @lippytm's repositories. It serves as the central intelligence layer — the **AI BrainKit hub** — that provides standardized AI configurations, connector templates, and automation across the entire ecosystem.

## Architecture & Conventions

- This repository uses **ES6+ modules** (ESM) throughout — always use `import`/`export`, never `require`.
- **Node.js 18+** is the target runtime.
- The connector pattern: `BaseConnector` → platform-specific connector → `LippyTMHub` orchestrator.
- Zero external runtime dependencies is the goal; use built-in Node.js APIs wherever possible.
- The `brainkit/` directory contains reusable AI BrainKit templates for all repositories.

## AI BrainKit Guidelines

When working on BrainKit-related features:

- Each BrainKit template in `brainkit/` must be self-contained and platform-agnostic.
- `brainkit.json` is the canonical metadata file — keep it up to date when adding features.
- Copilot instruction templates should be generic enough for any lippytm repository but specific enough to add real value.
- Always reference the hub repository (`lippytm.ai`) as the source of truth for BrainKit versions.

## Code Style

- Use descriptive variable and function names that reflect the AI/Web3 domain.
- Document public APIs with JSDoc.
- Prefer `async`/`await` over Promise chains.
- Error messages should be actionable and include context.

## Web3 & AI Integration

- All blockchain interactions should be wrapped in try/catch with meaningful error messages.
- AI model calls should be rate-limited and include retry logic.
- Smart contract ABIs should be stored in `src/contracts/` or `brainkit/contracts/`.

## Repository Links

All lippytm repositories are connected through this hub. When referencing other repositories, use their full GitHub URLs (e.g., `https://github.com/lippytm/<repo>`).
