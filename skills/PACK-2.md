# Pack 2 — Sandboxed skill evaluation and agent-assisted review

Pack 2 answers the two questions that followed pack 1: do agents help the skill improvement engine, and what does a sandbox add.

## The files

| File | What it is |
|---|---|
| `skills/sandboxed-skill-evaluation/SKILL.md` | Runs a revised skill against a frozen fixture in an isolated cell and compares it with the unchanged version. This is the test the library has never had. |
| `skills/agent-assisted-skill-review/SKILL.md` | Bounds what an agent may do in the improvement loop: trigger collection, failure-class diagnosis, and overlap detection. It may not author changes. |

## Why these two, and not a third

Pack 1 added `review-triage`. Pack 2 needed the two pieces named in the answer to the question "would agents help, and what about a sandbox".

- **The sandbox matters more than the agents.** Without it, `skill-improvement-engine` can change an instruction and bump a version but cannot tell whether the change worked. An acceptance test checkable only by reading is not a test.
- **The agents matter in three places and none of them is authoring.** An agent that both collects triggers and applies fixes drifts toward finding whatever it can fix. The version-bump requirement is the defence, and it only works if the trigger came from a real event rather than from the agent's own prior output.

## What already existed

This is a wiring job, not a new sandbox.

Tower Control already holds a sandbox architecture with four layers (lesson, workflow, blockchain, reflection), a promotion scorecard scored out of 35, a cross-sandbox reuse model, per-system lineage records, a sandbox-to-platform promotion matrix, and builder and register templates. `Chatlippytm.ai.Bots` already holds `SandboxAgent`, which provisions and assists inside isolated environments but which its own docstring notes is simulated in-process.

What none of it did was evaluate a skill. Twenty-two skills, zero tests. Pack 2 supplies the missing use case and reuses the existing scorecard bands rather than inventing a parallel scale.

## Related repository work worth knowing

`chatgpt-business-import-automation` and `chatgpt-business-export-automation` already define a package-and-receipt flow: staged directories, a manifest, a returned package, and review before anything durable is written. That is the same shape a sandbox evaluation needs, so the receipt vocabulary here follows it rather than introducing another.

## Honest limits

- Neither skill runs itself. Something else must invoke them.
- The sandbox evaluation produces a recommendation and a receipt. It never edits the default branch, and a human still promotes.
- The agent-assist skill bounds an agent; it does not schedule one or grant one access. Nothing in this pack gives an agent write access to `skills/`.
- No fixture in this pack has been run. The worked example uses declared placeholders, and no evaluation result is claimed anywhere in these files.
