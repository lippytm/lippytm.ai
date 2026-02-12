# API Configuration Example

This example shows how to configure API credentials for different platforms.

```javascript
import { GitHubConnector } from '../src/connectors/github.js';
import { GitLabConnector } from '../src/connectors/gitlab.js';
import { GistConnector } from '../src/connectors/gist.js';

// Note: Current implementation uses environment variables for configuration
// Future versions will support passing configuration objects to constructors

async function setupConnectors() {
  // Create connectors (configuration will be added in future versions)
  const github = new GitHubConnector();
  const gitlab = new GitLabConnector();
  const gist = new GistConnector();
  
  // Connect to all platforms
  await Promise.all([
    github.connect(),
    gitlab.connect(),
    gist.connect()
  ]);
  
  console.log('All platforms connected!');
}

setupConnectors().catch(console.error);
```

## Environment Variables

Create a `.env` file in the project root:

```
GITHUB_TOKEN=your_github_token_here
GITLAB_TOKEN=your_gitlab_token_here
```

**Note:** Never commit your `.env` file to version control!

## Future Configuration

In future versions, you'll be able to pass configuration directly:

```javascript
const github = new GitHubConnector({
  token: process.env.GITHUB_TOKEN,
  apiUrl: 'https://api.github.com'
});
```
