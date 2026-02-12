# Examples

This directory contains examples demonstrating how to use lippytm.ai.

## Available Examples

### 1. Basic Usage (`basic-usage.js`)
Demonstrates the fundamental usage of the lippytm.ai hub:
- Creating a hub instance
- Initializing connectors
- Checking connector status
- Using individual connectors

**Run it:**
```bash
node examples/basic-usage.js
```

### 2. Configuration (`configuration.md`)
Shows how to configure API credentials for different platforms:
- Setting up environment variables
- Configuring GitHub, GitLab, and Gist tokens
- Using configuration objects

## Running Examples

All examples can be run from the project root:

```bash
# From the project root
node examples/basic-usage.js
```

## Prerequisites

- Node.js >= 18.0.0
- npm or yarn

## Getting API Tokens

### GitHub
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `gist`
4. Copy the token to your `.env` file

### GitLab
1. Go to https://gitlab.com/-/profile/personal_access_tokens
2. Create a new token with `api` scope
3. Copy the token to your `.env` file

## Need Help?

- Check the [Development Guide](../docs/DEVELOPMENT.md)
- Review the [API Documentation](../docs/API.md) (when available)
- Open an issue on GitHub
