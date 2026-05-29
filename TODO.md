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
- [ ] **Set up the Stripe Customer Portal** (Stripe dashboard → Settings → Customer Portal → enable + configure). Grab the portal URL and paste it into the launch email template so clients can self-serve subscription management (update card, view history). Removes most billing-support requests.
- [ ] **Build the client-intake Google Form** from `templates/client-intake.md`
- [ ] **Build the "command center" Google Sheet.** One sheet, multiple tabs:
  - **Leads** — scraper writes here. Columns: Business Name, Phone, Address, Type, Date Added, Status (new/called/VM/emailed/interested/closed/dead), Last Contact Date, Next Action Date, Notes, Demo URL.
  - **Active Builds** — clients between deposit and launch. Columns: Client, Deposit Date, Day of Build (1–7), Content Received?, Staging URL, Launch Target.
  - **Care Plan Clients** — Columns: Client, Launch Date, Month-11 Reminder Date, Month-12 Renewal Date, Hours Used This Month, Last Edit Date, Domain Renewal Date.
  - **Revenue** — monthly totals (build fees + Care Plan + add-ons + domain pass-through). For taxes and visibility.
- [ ] **Set up the launch-day calendar reminder routine.** When a client launches, create three Google Calendar events tied to their launch date: (1) `+11 months` → send continuous-hosting email (template in `BUILD-GUIDE.md` §19), (2) `+12 months` → check usage + renewal-decision touchpoint, (3) quarterly recurring → maintenance pass (Lighthouse + link check + domain check, per `BUILD-GUIDE.md` §17). Zero infrastructure, zero forgotten emails.
- [ ] **Get a Google Places API key** and install Python + scraper requirements so `scraper/find_leads.py` can run
- [ ] **Decide which agency site to ship live**: `index.html` (peach/blue bento) or `index-v2.html` (cream/rust editorial)

---

## Open — Claude to do (waiting on Brian)

Tasks Claude will execute when Brian gives the trigger or unblocks them.

- [ ] **Wire Stripe Payment Links into templates** once Brian has the three URLs:
  - Replace `[STRIPE_DEPOSIT_LINK]` in `templates/proposal.html` and the deposit/proposal emails in `OPERATIONS.md` Part 3
  - Replace `[STRIPE_LAUNCH_LINK]` in `templates/invoice.html` and the final-invoice email in `OPERATIONS.md` Part 3
- [ ] **Wire the Stripe Customer Portal URL** into the launch email template (`OPERATIONS.md` Part 3 §9) once Brian enables the Portal
- [ ] **Wire the Google Form intake link** into the deposit-confirmation email in `OPERATIONS.md` Part 3 §5 once Brian has the form URL
- [ ] **Update `index.html` (or `index-v2.html`)** with Brian's real phone number, email, and any other contact info once he has them

---

## Open — Claude to do (no blockers)

Things Claude can do anytime; Brian just needs to say go.

- [ ] **Build out the demo template library** — add nail salon, landscaper, HVAC, auto repair, florist, chiropractor, cleaning service (each with a distinct aesthetic per the design rules in `CLAUDE.md`). Goal: 6–8 polished templates so personalizing for a new lead is content-swap, not from-scratch.
- [ ] **Build the chat-driven personalized-demo + email workflow.** Brian says *"build demo for [Business Name]"* in chat → Claude reads the matching row from the Leads sheet → picks the closest template from the demo library → swaps in real business info (name, address, hours, services, photos pulled from Google Places) → commits to `demos/leads/[business-slug]/` so Vercel auto-deploys → returns the live URL + a draft personalized follow-up email Brian reviews and sends. Also: *"draft follow-up for [Business]"*, *"mark [Business] as proposal sent"*, *"who's due for a callback today?"*.
- [ ] **Implement lead-list deduplication and revisit logic in the scraper.** When `find_leads.py` runs, check against the Leads sheet before adding any row: skip businesses already present, flag callbacks whose Next Action Date is today or earlier, and keep a separate `do-not-call` list for `Status = dead` entries so they never re-enter the funnel.

---

## Done

(Move items here with a completed date as they're finished.)
