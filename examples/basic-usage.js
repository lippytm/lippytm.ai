// Example: Basic Hub Usage
// This example demonstrates how to use the lippytm.ai connection hub.

import LippyTMHub from '../src/index.js';

async function main() {
  // Create a new hub instance
  const hub = new LippyTMHub();
  
  // Initialize all connectors
  await hub.initialize();
  
  // Check status of all connectors
  const status = hub.getStatus();
  console.log('Connector Status:', status);
  
  // Use individual connectors (these will return empty arrays for now)
  const githubRepos = await hub.connectors.github.listRepositories();
  console.log('GitHub Repositories:', githubRepos);
  
  const gitlabProjects = await hub.connectors.gitlab.listProjects();
  console.log('GitLab Projects:', gitlabProjects);
  
  const gists = await hub.connectors.gist.listGists();
  console.log('Gists:', gists);
}

main().catch(console.error);
