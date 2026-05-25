# ChatGPT Business to Zo API Setup

## Purpose

Use this only when Charles wants ChatGPT Business or a Custom GPT to send structured task packets to Zo Computer through an API bridge.

## Setup

1. Create a Zo access token in [Settings > Advanced](/?t=settings&s=advanced).
2. Save the token as a Zo secret, for example `CHATGPT_ZO_BRIDGE_SECRET`.
3. Create a secured Zo Space API route such as `/api/chatgpt-bridge`.
4. Configure a Custom GPT Action using `custom-gpt-action-openapi-template.yaml`.
5. Test with draft-only packets first.

## Approval boundaries

ChatGPT may submit internal draft task packets. It should not directly:

- publish public pages
- send external messages
- move money
- perform crypto wallet transactions
- change payment settings
- delete files
- commit to GitHub without Zo-side review

Those actions require Zo-side review and approval.
