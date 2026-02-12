# API Configuration Example

This example shows how to configure API credentials for different platforms.

```javascript
import { GitHubConnector } from '../src/connectors/github.js';
import { GitLabConnector } from '../src/connectors/gitlab.js';
import { GistConnector } from '../src/connectors/gist.js';

// Configuration object
const config = {
  github: {
    token: process.env.GITHUB_TOKEN,
    apiUrl: 'https://api.github.com'
  },
  gitlab: {
    token: process.env.GITLAB_TOKEN,
    apiUrl: 'https://gitlab.com/api/v4'
  },
  gist: {
    token: process.env.GITHUB_TOKEN // Gist uses GitHub token
  }
};

async function setupWithConfig() {
  // Create connectors with configuration
  const github = new GitHubConnector(config.github);
  const gitlab = new GitLabConnector(config.gitlab);
  const gist = new GistConnector(config.gist);
  
  // Connect to all platforms
  await Promise.all([
    github.connect(),
    gitlab.connect(),
    gist.connect()
  ]);
  
  console.log('All platforms connected!');
}

setupWithConfig().catch(console.error);
```

## Environment Variables

Create a `.env` file in the project root:

```
GITHUB_TOKEN=your_github_token_here
GITLAB_TOKEN=your_gitlab_token_here
```

**Note:** Never commit your `.env` file to version control!
