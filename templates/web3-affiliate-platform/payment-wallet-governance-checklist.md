# Payment and Crypto Wallet Governance Checklist

## Before accepting payment

- [ ] Product/offer is clearly described.
- [ ] Price is clearly shown.
- [ ] Refund/cancellation terms are documented.
- [ ] Customer support contact is documented.
- [ ] Affiliate/partner disclosure is included where needed.
- [ ] No income, funding approval, investment, or crypto gain guarantee is made.

## Stripe / fiat payment checklist

- [ ] Use Stripe Checkout, Payment Links, Billing, or Invoicing.
- [ ] Test mode completed.
- [ ] Webhook events documented before automation.
- [ ] Payment events logged to CRM/GitHub/Zapier as needed.
- [ ] Human approval required before price or payout changes.

## Crypto wallet checklist

- [ ] Never collect private keys or seed phrases.
- [ ] Collect only public wallet addresses when required.
- [ ] Confirm chain/network.
- [ ] Validate wallet address format.
- [ ] Prefer a reputable crypto payment processor for production flows.
- [ ] Document refund and support policy.
- [ ] Require human approval before live crypto payment launch.

## Data fields

- payment_provider
- payment_status
- amount
- currency
- product_id
- customer_email
- public_wallet_address, if required
- wallet_network, if required
- transaction_hash, if applicable
- github_issue_url
- zapier_run_id
