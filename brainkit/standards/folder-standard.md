# BrainKit Folder Standard

This document defines the recommended folder and file structure for repositories in the lippytm ecosystem.

The goal is to support:

- innovation without chaos
- diversity without fragmentation
- flexibility without loss of standards
- scalability without loss of operational control

---

## Design principles

### 1. Every repo must explain itself
A repository should make sense to a new human or agent operator within minutes.

### 2. Every repo must be automation-friendly
Folder names and file meanings should be predictable enough for AI agents, scripts, and operators to work safely.

### 3. Every repo must preserve room for experimentation
Standards should create structure, not kill creativity.

### 4. Every repo must separate stable assets from experiments
Production-grade code, documents, prompts, and experiments should not be mixed together carelessly.

---

## Core Standard Layout

```text
/
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── OPERATIONS.md
├── MONETIZATION.md
├── CHANGELOG.md
├── .env.example
├── docs/
├── src/ or app/ or backend/ or frontend/
├── tests/
├── scripts/
├── config/
├── prompts/
├── sandboxes/
├── artifacts/
└── .github/
```

Not every repo must use every top-level folder, but each repo should justify omissions.

---

## Top-Level File Standards

### `README.md`
Required. Explains purpose, major features, quick start, and repo role.

### `ROADMAP.md`
Required for active repos. Defines milestones, phases, and next priorities.

### `ARCHITECTURE.md`
Required for control, swarm, product, and commerce repos. Explains components, flows, boundaries, and integration surfaces.

### `OPERATIONS.md`
Required for anything deployed, scheduled, or operator-managed. Includes commands, environments, recovery steps, and routine maintenance.

### `MONETIZATION.md`
Required for revenue, product, commerce, and knowledge repos. Explains direct or indirect value creation.

### `CHANGELOG.md`
Recommended for active repos. Tracks meaningful architectural, operational, or product changes.

### `.env.example`
Required when runtime configuration exists.

---

## Standard Folder Definitions

### `docs/`
Long-form design, policy, strategy, and system documentation.

Recommended subfolders:

```text
docs/
├── overview/
├── architecture/
├── operations/
├── integrations/
├── quality/
├── security/
├── monetization/
├── product/
├── workflows/
└── research/
```

#### `docs/overview/`
Mission, repo role, glossary, repo map.

#### `docs/architecture/`
System diagrams, responsibilities, data flow, boundaries.

#### `docs/operations/`
Runbooks, on-call notes, operator procedures, maintenance steps.

#### `docs/integrations/`
How the repo connects to other repos, APIs, agents, and workflows.

#### `docs/quality/`
Acceptance criteria, test strategy, quality gates, readiness checks.

#### `docs/security/`
Secrets handling, risk surfaces, trust boundaries, incident response.

#### `docs/monetization/`
Offers, value ladders, packaging, licensing, subscription logic.

#### `docs/product/`
Product surface design, personas, user journeys, interfaces.

#### `docs/workflows/`
Execution flows, automation patterns, triggers, handoffs.

#### `docs/research/`
Exploratory thinking, concepts, notes, experiments, future ideas.

---

### `src/`, `app/`, `backend/`, `frontend/`
Runtime code.

Use the naming pattern that fits the repo:

- `src/` for libraries, services, APIs, generic codebases
- `app/` for application-centric repos
- `backend/` + `frontend/` for full-stack systems
- `contracts/` for smart-contract code when applicable

---

### `tests/`
Required for repos that execute code or automate workflows.

Recommended subdivisions:

```text
tests/
├── unit/
├── integration/
├── regression/
└── fixtures/
```

---

### `scripts/`
Utility scripts for setup, diagnostics, export, validation, rollout, migration, or maintenance.

Examples:

- bootstrap scripts
- migration scripts
- status generators
- dry-run rollout scripts
- data validators

---

### `config/`
Machine-readable configuration and policy files.

Examples:

- YAML configuration
- policy rules
- routing maps
- environment profiles
- repo target lists

Do not store secrets here.

---

### `prompts/`
Reusable AI operating prompts.

Recommended subdivisions:

```text
prompts/
├── architecture/
├── operations/
├── growth/
├── reviews/
├── agents/
└── experiments/
```

Each prompt file should state:

- intended agent or operator
- purpose
- inputs
- constraints
- expected output shape

---

### `sandboxes/`
Safe experimentation and diagnostics.

This is where new concepts can evolve without polluting production paths.

Examples:

- prototype experiments
- scenario drills
- prompt trials
- load tests
- simulation harnesses

A sandbox should be clearly labeled as experimental.

---

### `artifacts/`
Generated outputs or reusable machine-readable deliverables.

Examples:

- reports
- JSON schemas
- exported diagrams
- generated indexes
- build outputs intended for review

Generated artifacts should not replace source-of-truth documents.

---

### `.github/`
Repository automation and collaboration structure.

Recommended structure:

```text
.github/
├── workflows/
├── ISSUE_TEMPLATE/
├── PULL_REQUEST_TEMPLATE.md
└── CODEOWNERS
```

---

## Repo-Type Variants

### Hub Repos
Heavy on standards, docs, policies, contracts, and propagation tooling.

Must include:
- `brainkit/` or equivalent standards folder
- strong `docs/standards/`
- rollout scripts and governance docs

### Control Repos
Heavy on orchestration logic, routes, integrations, policy, and telemetry.

Must include:
- `docs/control/`
- `docs/workflows/`
- `src/fleet/` or equivalent control modules

### Swarm Repos
Heavy on agents, routing, network, memory, and escalation.

Must include:
- `docs/swarm/`
- runtime coordination modules
- routing and failure policy docs

### Revenue Repos
Heavy on offers, funnels, pages, forms, and CTA logic.

Must include:
- `docs/offers/`
- `docs/funnels/`
- page and form assets

### Knowledge Repos
Heavy on canon, educational modules, media assets, and commercialization docs.

Must include:
- `docs/canon/` or `docs/education/`
- product ladder or commercialization path

### Lab Repos
Heavy on experiments, hypotheses, and result tracking.

Must include:
- `EXPERIMENTS.md`
- `docs/hypotheses/`
- `docs/results/`

---

## Minimum Readiness Checklist

A repo is considered BrainKit-aligned when it has:

- a clear README
- a documented repo role
- a predictable folder layout
- a roadmap
- docs for architecture or product intent
- config and scripts separated from runtime code
- tests or a declared reason for absence
- prompts and sandboxes clearly separated from production logic

---

## Anti-patterns to avoid

- putting product strategy only in chat and nowhere in the repo
- mixing production code with unfinished experiments in the same folder
- storing secrets in config files
- using unclear folder names like `misc`, `stuff`, or `temp` for long-lived assets
- burying the core business value where agents cannot find it

---

## Rule of thumb

If an operator cannot identify where to find architecture, prompts, automation, tests, and experimental work in under five minutes, the repo is not yet mass-manufacturing ready.
