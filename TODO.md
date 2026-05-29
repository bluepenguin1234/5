# Frontpage Studio — TODO

## This week (do all four or stop)

These four make the difference between "I have docs" and "I can take a customer."

- [ ] **Stripe deposit Payment Link** ($299.50 one-time). Activate Stripe at stripe.com, create the Business Presence Package product, generate the deposit link. Save URL.
- [ ] **Google Voice phone number.** Free at voice.google.com. Use it in the agency site footer and email signature. Don't give clients your personal cell.
- [ ] **Vercel deploy of the agency site.** Push the repo to GitHub, connect to Vercel, bookmark the live URL. Auto-deploys on every commit going forward.
- [ ] **Command-center Google Sheet.** Import the four CSVs in `templates/sheets/` per the `templates/sheets/README.md` walkthrough (~8 minutes). Open this every morning.

When all four are checked, start calling. The cold-call script lives in `OPERATIONS.md` Part 2 §2.

---

## Phase 2 (revisit after 3 paying clients)

Everything below earns its place after revenue, not before. Don't touch any of it until clients 4 and 5 are signed.

- Activate Stripe **subscription** product + launch Payment Link + Customer Portal
- Build the **client-intake Google Form** from `templates/client-intake.md`
- **Calendar reminder routine** at every launch (month 11 / month 12 / quarterly maintenance)
- **Form an LLC** + business insurance (E&O)
- **Terms of Service + Privacy Policy** on the agency site itself
- **MSA** (`templates/msa.html`) introduced as standard practice
- **Google Places API key** + Python scraper setup
- **Expand demo template library** from 3 to 6–8
- **Chat-driven personalized-demo + email workflow**
- **Scraper deduplication + revisit logic** vs the Leads sheet

---

## Always-pending (Claude executes when Brian unblocks)

- Replace `[STRIPE_DEPOSIT_LINK]` in `templates/proposal.html` + `templates/invoice.html` + OPERATIONS.md once Brian has the URL
- Replace `YOUR_FORM_ID` in `index.html` once Formspree is active
- Replace `[Your Phone]` placeholders in `templates/proposal.html` once Brian has Google Voice
