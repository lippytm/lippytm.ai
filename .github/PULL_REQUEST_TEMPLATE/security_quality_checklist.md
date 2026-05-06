# Pull Request Security and Quality Checklist

## Summary

Describe the change:

## RiskGate classification

- [ ] Low: docs/copy/checklist/template update
- [ ] Medium: workflow/dependency/website/bot/CRM/affiliate routing change
- [ ] High: secrets/auth/payment/database/deployment/cross-repo automation/autonomous action
- [ ] Critical: incident response, exposed credential, compromised account, major data exposure

## Security checklist

- [ ] No secrets, tokens, private keys, passwords, or `.env` files added
- [ ] No private lead/customer data added
- [ ] No CRM exports added
- [ ] No database dumps added
- [ ] Workflow permissions use least privilege
- [ ] Dependencies are necessary and reviewed
- [ ] Bot/CRM/form changes minimize sensitive data
- [ ] Public claims avoid unsupported guarantees
- [ ] Affiliate disclosures are included where needed
- [ ] Human handoff exists for sensitive bot/AI workflows

## Verification

- [ ] Relevant workflows pass
- [ ] Failed runs are categorized if any fail
- [ ] Documentation updated
- [ ] Fleet security status updated if this affects rollout
- [ ] RiskGate decision logged if medium/high/critical

## Notes

