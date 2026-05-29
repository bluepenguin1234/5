# Frontpage Studio — Todo

Tracked items for Brian and Claude to pick up in future sessions.

---

## Open

### Update proposal and invoice templates with the Stripe acceptance flow
**Files:** `templates/proposal.html`, `templates/invoice.html`

What to do:
- Add a clear "How to accept" section at the bottom of `proposal.html` with two explicit steps: (1) reply to the email with "I accept", (2) click the Stripe Payment Link for the deposit
- Add a `[STRIPE_DEPOSIT_LINK]` placeholder in the proposal where Brian will paste the live link
- Update `invoice.html` similarly with `[STRIPE_LAUNCH_LINK]` for the balance + first month Care Plan payment
- Update the email templates in `sop/email-templates.md` so the proposal-send and final-invoice emails reference the same placeholders consistently

Why: Brian is setting up Stripe Payment Links. Every proposal he generates should already have the simple email-reply + Stripe-link acceptance flow baked in so he just pastes the URL per client.

---

## Done

(Move items here as they get completed.)
