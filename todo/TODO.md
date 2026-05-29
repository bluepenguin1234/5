# Frontpage Studio — TODO

Open work tracked across sessions. Move items to **Done** when complete (and date them). Add new items at the top of **Open** as they come up.

---

## Open — Brian to do

These need Brian's accounts, payment, or hands-on action. Claude can't do them remotely. Full walkthroughs in `OPERATIONS.md` Appendix A.

- [ ] **Register the domain** (`frontpagestudio.com` or `frontpage.studio`) at Namecheap or Cloudflare
- [ ] **Set up Zoho Mail** for `brian@frontpagestudio.com`
- [ ] **Push this repo to GitHub** under his account
- [ ] **Connect repo to Vercel** for auto-deploy on every push; bookmark the Vercel URL as the live site
- [ ] **Sign up for Formspree**, get the form endpoint, replace `YOUR_FORM_ID` in `index.html`
- [ ] **Activate Stripe**, create the two products (Business Presence Package one-time + Care Plan recurring) and generate the three Payment Links (deposit / launch / subscription)
- [ ] **Build the client-intake Google Form** from `templates/client-intake.md`
- [ ] **Get a Google Places API key** and install Python + scraper requirements so `scraper/find_leads.py` can run
- [ ] **Decide which agency site to ship live**: `index.html` (peach/blue bento) or `index-v2.html` (cream/rust editorial)

---

## Open — Claude to do (waiting on Brian)

Tasks Claude will execute when Brian gives the trigger or unblocks them.

- [ ] **Wire Stripe Payment Links into templates** once Brian has the three URLs:
  - Replace `[STRIPE_DEPOSIT_LINK]` in `templates/proposal.html` and the deposit/proposal emails in `OPERATIONS.md` Part 3
  - Replace `[STRIPE_LAUNCH_LINK]` in `templates/invoice.html` and the final-invoice email in `OPERATIONS.md` Part 3
- [ ] **Wire the Google Form intake link** into the deposit-confirmation email in `OPERATIONS.md` Part 3 §5 once Brian has the form URL
- [ ] **Update `index.html` (or `index-v2.html`)** with Brian's real phone number, email, and any other contact info once he has them

---

## Open — Claude to do (no blockers)

Things Claude can do anytime; Brian just needs to say go.

- [ ] **Build out the demo template library** — add nail salon, landscaper, HVAC, auto repair, florist, chiropractor, cleaning service (each with a distinct aesthetic per the design rules in `CLAUDE.md`). Goal: 6–8 polished templates so personalizing for a new lead is content-swap, not from-scratch.
- [ ] **Build the lead-tracking workflow** — extend the scraper CSV with `status`, `last_contact_date`, `demo_url`, `notes` columns; add chat-driven slash commands like "draft follow-up for [Business]" and "build demo for [Business]"

---

## Done

(Move items here with a completed date as they're finished.)
