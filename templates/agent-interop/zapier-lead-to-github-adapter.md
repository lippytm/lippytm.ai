# Adapter Template — Zapier Lead to GitHub Issue

## Purpose

Route GetBizFunds and AI Business Funding eBook leads into GitHub issues and follow-up workflows.

## Input

- name
- email
- phone
- business name
- website/social
- primary interest
- funding range
- urgency
- source page
- campaign source

## Output

- GitHub issue title
- GitHub issue body
- lead log row
- next follow-up action
- notification message

## Steps

1. Receive lead from form or webhook.
2. Normalize lead fields.
3. Add row to lead log.
4. Create GitHub issue in the correct repo.
5. Notify Charles.
6. Send or draft first follow-up depending on approval setting.

## Approval gates

Draft external follow-up before sending unless Charles has explicitly approved the live automation.
