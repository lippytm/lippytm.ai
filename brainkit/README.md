# AI BrainKit

The **lippytm AI BrainKit** is a standardized set of AI configuration files, connector templates, and automation patterns designed to give every lippytm repository a shared layer of AI intelligence.

## What's in the BrainKit?

| File | Purpose |
|------|---------|
| [`brainkit.json`](./brainkit.json) | Metadata, version, and registry of all connected repositories |
| [`copilot-instructions.template.md`](./copilot-instructions.template.md) | GitHub Copilot instructions template — copy to `.github/copilot-instructions.md` in any repo |
| [`connector.template.js`](./connector.template.js) | ESM connector base class and example — the building block for all platform integrations |

## Applying the BrainKit to a Repository

1. **Copy the Copilot instructions template** into your repository:

   ```bash
   # From within your target repository
   curl -o .github/copilot-instructions.md \
     https://raw.githubusercontent.com/lippytm/lippytm.ai/main/brainkit/copilot-instructions.template.md
   ```

2. **Customize the template** — replace all `{{PLACEHOLDERS}}` with values specific to that repository.

3. **Copy the connector template** if you're building a new platform integration:

   ```bash
   curl -o src/connectors/myplatform.js \
     https://raw.githubusercontent.com/lippytm/lippytm.ai/main/brainkit/connector.template.js
   ```

4. **Update `brainkit.json`** in this hub repository to register the new connector.

## Connected Repositories

All repositories in the lippytm ecosystem that have the BrainKit applied are listed in [`brainkit.json`](./brainkit.json).

## Versioning

The BrainKit follows semantic versioning. The current version is defined in `brainkit.json`. When making breaking changes to templates, increment the major version and update all downstream repositories.
