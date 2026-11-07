---
name: review-triage
version: 1.0.0
pack: 1
description: Use when a repository or fleet has accumulated open pull requests, branches, or issues that need to be reviewed, closed, split, or merged in a bounded, auditable order — especially when the backlog has grown past what one person can hold in their head, or when automated agents keep reopening the same work. Do not use to author new features.
compatibility: Created for Zo Computer and GitHub Copilot coding agents
metadata:
  author: lippytmai.zo.computer
  canonical_repo: lippytm/lippytm.ai
  created: 2026-11-07
---

# Review Triage

## Why this pack exists

A backlog is not a storage problem, it is a decision debt problem. Every open pull request is a question somebody has to answer. When the questions outnumber the capacity to answer them, the repository stops being a place where work happens and becomes a place where work is parked.

The failure this pack prevents is specific and it has already happened in this fleet. An automated agent opened seven pull requests across AI-Time-Machines (#39, #42, #43, #44, #45, #46, #47) that all reach for the same MyClaw/GitHub/OpenClaw integration from slightly different angles. None of them were reviewed. The main branch moved on beneath all seven. Months later each one is still open, each one alone, and none of them can be merged without re-doing the work against a base that no longer exists.

The lesson is not "review faster." It is **decide on purpose, and write the decision where the next agent will find it.** A closed PR with a recorded reason is a finished decision. An open PR is an undecided one, and undecided work compounds.

## When to use this skill

Use it when any of these is true:

- A repository carries more open pull requests than can be read carefully in one sitting.
- Several open PRs appear to address the same problem.
- A PR has been open for longer than the code around it has been stable.
- Automated agents (Copilot, Dependabot, or your own) have produced more proposals than decisions.
- Someone asks "what should I do with all of these?"

Do **not** use this skill to write new features, to refactor, or to merge anything. It produces decisions and one bounded action per item. Merging remains a human action.

## The three gates

Every item gets exactly one of three verdicts. There is no fourth verdict, and "leave it open for now" is not one of them.

| Gate | Meaning | Action |
|---|---|---|
| **MERGE-READY** | Addresses a real, current problem; base is current; checks pass; review found nothing blocking. | Hand to the owner for merge. Never auto-merge. |
| **REVIVE** | Right problem, stale base or incomplete work. | Rebase onto current default branch, resolve conflicts, re-run checks, then re-enter triage. |
| **CLOSE** | Superseded, duplicate, already implemented on the default branch, or the problem is no longer real. | Close with a recorded reason naming the PR that supersedes it, or the commit/file that already solves it. |

A PR with no test evidence is never MERGE-READY. A PR whose stated problem you cannot observe anywhere in the current codebase is a CLOSE candidate, not a REVIVE one.

## Procedure

### Step 1 — Establish the real inventory

Do not trust a search count. Search endpoints return platform-wide results and will hand you other people's repositories.

- For each repository you actually own, list open PRs **per repository**.
- Record for each: number, title, author, `draft` flag, age in days, head branch, base branch.
- Record the base branch's current SHA. Every later judgement depends on it.

Write this to a file before making any judgement: `review-triage/inventory.md`.

### Step 2 — Classify before reading

Sort the inventory into four kinds. Each has a different default gate.

| Kind | How to recognise it | Default gate |
|---|---|---|
| **Dependency bump** | Author is a dependency bot; title begins "Bump" / "chore(deps)" | MERGE-READY if it is a patch or minor and checks are green and the lockfile is consistent. **REVIVE or CLOSE if it crosses a major version** — a major bump is a behaviour change, not a chore. |
| **Agent-proposed feature** | Author is a coding agent; description restates a problem the agent inferred | REVIVE at best. Agent PRs are proposals. They are almost never MERGE-READY on arrival. |
| **Workflow / documentation** | Docs, CI, instructions, READMEs, templates | MERGE-READY if it matches what the code actually does today. CLOSE if it describes a state that no longer exists. |
| **Human-designed change** | You wrote the design, an agent or person implemented it | Evaluate on its own merits; this is where MERGE-READY is genuinely available. |

### Step 3 — Look for clusters before you look at items

Group PRs by the problem they claim to solve, not by their titles. Two PRs touching the same three files are usually one decision, not two.

For every cluster of two or more:

- Pick **one** to revive or merge — the one whose base is closest to current and whose diff is smallest.
- The others are CLOSE, with the reason naming the surviving PR.

This is the single highest-value step. Seven agent PRs reaching for the same integration are one decision and six closures, not seven reviews.

### Step 4 — Read each survivor properly

For each non-clustered survivor, read in this order and stop at the first blocker:

1. **The diff against the current base**, not the PR page. A diff viewed against a stale base tells you nothing about whether it still applies.
2. **The rebase result.** If it does not apply cleanly, that is the finding. Gate REVIVE, do not read further.
3. **The checks.** A red or missing check run is the finding. Never reason around a failing check; report it.
4. **The claims in the description.** For each claim of verification, find the artifact. A claim of "tests pass" with no check run is not evidence.
5. **The blast radius.** Note every file whose change affects something already running: workflow permissions, authentication, installers, deploy steps, environment files, money paths, credential handling.

### Step 5 — Write the decision where it will be found

Produce one row per item in `review-triage/decisions.md`:

```
| PR | Repo | Kind | Gate | One-line reason | Evidence read | Superseded by |
```

Then produce the actions. Each action is bounded to one item and is one of:

- `close <pr> --reason "<specific>"`
- `rebase <pr> onto <branch>@<sha>`
- `hand to owner for merge: <pr>`

Nothing else. No "consider," no "maybe later."

### Step 6 — Bound the blast radius

Before any action on a PR that touches workflow permissions, authentication, installers, deployment, environment files, credentials, or anything revenue-related:

- Record the current state of the affected file **before** the change, so the action is reversible.
- Name the specific human approval needed.
- If that approval is not present, the item's gate is **REVIVE** or **hand to owner**, never an applied action.

### Step 7 — Publish the decision in the place the next agent looks first

A closed PR is not discoverable. Write the outcome where the work happens:

- Close each CLOSE item with its reason in the closing comment.
- Add one line to the repository's own backlog note (an issue, or `review-triage/decisions.md` committed to the default branch).
- If the same decision will recur, propose it as an amendment to `.github/copilot-instructions.md` so the next agent inherits it instead of rediscovering it.

## Hard rules

1. **Never merge.** This skill produces hand-offs, not merges. Merging is a human action, always.
2. **Never close a revenue-critical or governance-tier item without a recorded human reason.** If you are an agent reading this, your role for those tiers is to *describe* and *recommend*, never to act.
3. **Never treat a stale base as a detail.** Age is not the problem; divergence is the problem. A two-day-old PR against a branch that moved yesterday is staler than a two-month-old PR against a quiet branch.
4. **Never review a claim of testing without the check run.**
5. **Never use a platform-wide search count as a backlog number.** Count per repository, or say you did not count.
6. **Never revive more than one PR per cluster.** Reviving duplicates recreates the problem you are solving.
7. **Record the base SHA for every item, including the ones you close.** The next agent needs to know what the world looked like when you decided.

## Refusal conditions

Return the item to the owner and stop, stating which condition fired, if:

- The item's purpose cannot be determined from its description and diff.
- The item touches authentication, credentials, money movement, or live deployment and no human approval is recorded.
- The correct gate depends on a fact only the owner holds (a product decision, an account state, a customer commitment).
- Two items in the inventory contradict each other and you cannot tell which reflects current intent.

A refusal is a valid output. Guessing is not.

## Output format

For a triage run, produce exactly this:

```
## Inventory
- Repository, open PR count, default branch SHA observed

## Clusters
- Problem, members, survivor, closures

## Decisions
| PR | Kind | Gate | Reason | Evidence | Superseded by |

## Actions
- One bounded action per line, or "hand to owner"

## Refusals
- Item and the condition that fired

## Blast radius
- Files whose change affects something already running, with required approvals

## Next triage target
- The repository and the reason it is next
```

## Acceptance test

A triage run is complete and correct when all of the following hold, each checkable by a second person:

1. Every open PR in the chosen repository appears exactly once in the Decisions table.
2. Every row has a gate, and the gate is one of the three — no blanks, no "TBD."
3. Every CLOSE row names what supersedes it.
4. Every MERGE-READY row has a green check run recorded.
5. Every row records the base SHA it was judged against.
6. No merge was performed.
7. Every refusal names its condition.
8. The clusters section shows at least the grouping attempt, even when every cluster has one member.

## Worked example — the shape of a real run

The pattern below is the expected shape, using placeholder counts. Replace them with what you actually count; do not reuse these numbers.

```
## Inventory
- repo/A — 12 open PRs — default branch base sha <sha>

## Clusters
- MyClaw + GitHub integration: #39 #42 #43 #44 #45 #46 #47 → survivor #42
  (smallest diff, closest base). Six closures, each naming #42.
- Dependency bumps: #75 #76 #79 #80 #81 → five separate items, no cluster.

## Decisions
| PR | Kind | Gate | Reason | Evidence | Superseded by |
| #39 | agent feature | CLOSE | duplicate of #42 | diff overlap 3 files | #42 |
| #42 | agent feature | REVIVE | base 4 months stale | rebase conflict in src/index.js | - |
| #75 | dependency | MERGE-READY | patch bump, checks green | check run <id> success | - |
| #81 | dependency | REVIVE | major version jump | eslint 8 → 10 | - |

## Actions
- close #39 --reason "superseded by #42"
- rebase #42 onto main@<sha>
- hand to owner for merge: #75
- rebase #81 onto main@<sha>

## Refusals
- #42 depends on whether MyClaw or OpenClaw is the intended target — owner decision.

## Blast radius
- #75 changes only package.json and lockfile — no approval needed.
- #81 changes eslint config used by CI — requires owner approval before merge.

## Next triage target
- repo/B — highest issue count with no triage note.
```
