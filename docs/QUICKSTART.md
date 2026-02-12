# Quick Start Guide

Get up and running with lippytm.ai in 5 minutes!

## Prerequisites

- Node.js 18.0.0 or higher
- npm (comes with Node.js)
- Git

Check your Node.js version:
```bash
node --version
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lippytm/lippytm.ai.git
cd lippytm.ai
```

### 2. Install Dependencies

```bash
npm install
```

Currently, there are no external dependencies, but this step is important for future updates.

### 3. Set Up Environment (Optional)

For API integration (coming soon):

```bash
cp .env.example .env
# Edit .env and add your API tokens
```

## Usage

### Run the Hub

```bash
npm start
```

Expected output:
```
🚀 Initializing lippytm.ai Connection Hub...
Connecting to GitHub...
✓ github connector initialized
Connecting to GitLab...
✓ gitlab connector initialized
Connecting to Gist...
✓ gist connector initialized
✨ Hub ready for creative development!
```

### Run Examples

```bash
# Basic usage example
node examples/basic-usage.js
```

### Development Mode

Run with auto-reload on file changes:

```bash
npm run dev
```

## What's Next?

### Learn More
- Read the [Development Guide](DEVELOPMENT.md)
- Check out the [Architecture](ARCHITECTURE.md)
- Review the [Roadmap](ROADMAP.md)

### Explore the Code
- `src/index.js` - Main hub implementation
- `src/connectors/` - Platform connectors
- `examples/` - Usage examples

### Contribute
- Read [Contributing Guidelines](../CONTRIBUTING.md)
- Check [open issues](https://github.com/lippytm/lippytm.ai/issues)
- Join discussions

## Common Tasks

### Adding a New Connector

1. Create a new file in `src/connectors/`
2. Extend `BaseConnector` class
3. Implement platform-specific methods
4. Add to hub in `src/index.js`

Example:
```javascript
import { BaseConnector } from './base.js';

export class BitbucketConnector extends BaseConnector {
  constructor() {
    super('Bitbucket');
  }

  async connect() {
    await super.connect();
    // Add Bitbucket-specific logic
  }
}
```

### Running Tests

```bash
npm test
```

### Running Linter

```bash
npm run lint
```

## Troubleshooting

### Node.js Version Error
If you see "SyntaxError: Cannot use import statement":
- Ensure you're using Node.js 18.0.0 or higher
- The project uses ES Modules

### Permission Errors
On Unix-like systems, you may need to use `sudo`:
```bash
sudo npm install
```

### Module Not Found
Make sure you're in the project directory:
```bash
cd /path/to/lippytm.ai
npm install
```

## Get Help

- 📖 [Full Documentation](DEVELOPMENT.md)
- 🐛 [Report a Bug](https://github.com/lippytm/lippytm.ai/issues)
- 💬 [Ask a Question](https://github.com/lippytm/lippytm.ai/discussions)

## Next Steps

1. ✅ You've got lippytm.ai running!
2. 📚 Read the [Development Guide](DEVELOPMENT.md) to understand the creative development process
3. 🎯 Check the [Roadmap](ROADMAP.md) to see what's planned
4. 🤝 Start [Contributing](../CONTRIBUTING.md)!

Happy coding! 🚀
