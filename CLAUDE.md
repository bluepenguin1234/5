# Frontpage Studio — Claude Instructions

This file is the **source of truth** for the project. Anything that contradicts it in another file is wrong and should be updated to match.

## What This Project Is

Frontpage Studio is Brian's web design business targeting local businesses with no website. Cold call outreach model. Brian builds the sites, handles hosting, and does the sales calls himself.

**Working directory:** `C:\Users\Brian\Desktop\web`

---

## Business Model

- Find local businesses with no website using the scraper or Google Maps
- Cold call them, pitch a flat-rate website build
- Every client pays a one-time build fee + a mandatory 12-month Ongoing Care Plan at $79/month

**Current pricing (do not change without being asked):**
- **Business Presence Package:** $599 one-time
- **Ongoing Care Plan:** $79/month — mandatory for a minimum of 12 months ($948 minimum over the year)
- The $79/month is NOT optional. After the initial 12 months it goes month-to-month and the client can cancel with 30 days' notice
- Care Plan covers: hosting, security updates, website edits, backup/maintenance, support
- First-year total to the client: $599 + ($79 × 12) = **$1,547**

---

## Design System

All sites (agency site + client demos) use this design system. Always follow it when building or editing any site in this project.

**Fonts:** Inter (from Google Fonts) — `https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300&display=swap`

**Agency site color palette:**
```css
--peach:      #FAD4C0;
--peach-deep: #F0B49A;
--blue:       #80A1C1;
--blue-deep:  #5C83A8;
--surface:    #FFF5E6;
--bg:         #F7F0E8;
--card:       #FFFFFF;
--dark:       #111827;
--text:       #111827;
--text-2:     #6B7280;
--text-3:     #9CA3AF;
--border:     rgba(17,24,39,0.07);
--radius:     20px;
--radius-sm:  12px;
--gap:        14px;
```

**Card variants:** `.card-peach`, `.card-blue`, `.card-dark`, `.card-surface`, `.card-featured`

**Layout:** Bento grid system — CSS Grid with modular cards of varying sizes. Use `grid-template-columns`, `grid-column: span N` for layout. Sticky frosted-glass nav, generous padding, clean typography.

---

## File Map

```
web/
├── CLAUDE.md                ← Source of truth. Facts, pricing, design rules, file map.
├── OPERATIONS.md            ← The playbook. Selling, building, launching, billing. All scripts + email templates + setup appendix.
├── BUILD-GUIDE.md           ← Technical reference. How to actually build each feature (forms, schema, GBP, hosting, care-plan ops).
│
├── index.html               ← Agency website (Frontpage Studio's own site)
├── index-v2.html            ← Alternate design of the agency site (taste-skill aesthetic)
├── vercel.json              ← Vercel deployment config
├── .gitignore
│
├── demos/
│   ├── restaurant/index.html ← Maplewood Kitchen (Cormorant Garamond, dark luxury)
│   ├── barbershop/index.html ← Sharp & Co. (Bebas Neue, navy/gold, classic)
│   └── plumber/index.html    ← Tucker Plumbing (Barlow Condensed, blue/orange)
│
├── scraper/
│   ├── find_leads.py        ← Google Places API scraper (finds businesses with no website)
│   └── requirements.txt
│
├── templates/
│   ├── proposal.html        ← Client proposal (print to PDF, attach to email)
│   ├── invoice.html         ← Client invoice (print to PDF)
│   ├── msa.html             ← Master Service Agreement (print to PDF, send pre-deposit)
│   ├── welcome-packet.html  ← Welcome PDF (print + attach to deposit confirmation email)
│   ├── launch-handover.md   ← Launch handover doc (send at go-live with account info)
│   ├── refund-policy.md     ← Refund and cancellation policy (referenced by MSA, also for agency site)
│   ├── client-intake.md     ← Master intake questionnaire (paste into Google Form)
│   ├── client-privacy-policy.html ← Drop-in /privacy.html template for client sites
│   ├── client-terms-of-service.html ← Drop-in /terms.html template for client sites
│   └── sheets/              ← Import-ready CSVs for the command-center Google Sheet
│       ├── README.md        ← 5-minute setup walkthrough
│       ├── leads.csv        ← Leads tab structure
│       ├── active-builds.csv ← Active Builds tab structure
│       ├── care-plan-clients.csv ← Care Plan Clients tab structure
│       └── revenue.csv      ← Revenue tab structure
│
└── TODO.md                  ← Outstanding work and tasks (Brian and Claude)
```

---

## Rules for Building Sites

### When building the agency site (`index.html`)
- Use the bento design system above — peach/blue/cream palette, Inter font, card grid layout
- Pricing must always show the single Business Presence Package: $599 one-time + $79/month
- The $79/month Ongoing Care Plan must always be described as mandatory with a 12-month minimum, never optional

### When building a new client demo or client site
- Always invoke the `/frontend-design` skill first
- Each demo should have its own distinct aesthetic — do NOT reuse the same fonts/colors across demos
- Every demo must include a banner at the top linking back to `../../index.html` (for demos) or the client's live agency referral
- Reference the existing demos for tone: restaurant = luxury dark, barbershop = classic bold, plumber = professional utility

### Demo aesthetics used (don't reuse these combos for new demos)
- Restaurant: Cormorant Garamond + Jost, `#0E0A06` bg, `#C8944A` gold
- Barbershop: Bebas Neue + Barlow, `#0B1527` navy, `#C9A84C` gold
- Plumber: Barlow Condensed + Source Sans 3, `#0D3B6E` blue, `#F97316` orange

### Good demo business types to build next
- Nail salon, landscaper, HVAC, auto repair, florist, chiropractor, cleaning service

---

## Key facts (the canonical list)

- **Package:** Business Presence Package, $599 one-time, 3 pages (Home, Services, Contact), 7-day delivery
- **Care Plan:** $79/month, **mandatory 12-month minimum**, then month-to-month with 30 days' notice
- **Care Plan covers:** hosting, security updates, website edits, backup/maintenance, support
- **First-year total per client:** $1,547 ($599 build + $948 care plan)
- **Payment schedule:** $299.50 deposit at signing → $378.50 at launch (balance + first month care) → $79/month for 11 more months. Plus domain cost (~$12 to $15) as a separate pass-through line item on the launch invoice if Brian is registering one for them.
- **Revisions:** 1 round included. Extras $75 each.
- **Hosting:** Vercel free tier (Brian's cost: $0)
- **Contact forms:** Formspree
- **Payments:** Stripe (Payment Links + Subscription)
- **Search-ready setup (included):** titles, meta, heading hierarchy, alt text, consistent NAP, LocalBusiness JSON-LD, Google Business Profile setup
- **Add-ons (flat $75 each):** extra page, FAQ section, extra revision round
- **Add-ons (other):** custom logo $149, e-commerce $399, rush delivery +$200
- **Domain:** Brian always purchases the domain through Namecheap. Cost passes through to the client at the registrar's actual price (~$12 to $15 for `.com`) as a separate line item on the launch invoice. No markup, no setup fee. Each annual renewal is re-billed at the same actual cost.

For detailed scripts, email templates, build process, and launch setup: see `OPERATIONS.md`.
For how to technically build each feature: see `BUILD-GUIDE.md`.

---

## Cross-file audit rule (MANDATORY before completing any business-rule change)

When **any** of the following change, run a full audit across the entire repo before marking the task complete:

- Prices (build fee, Care Plan, add-ons, domain pass-through)
- Term length (Care Plan months, revision rounds)
- Feature lists (what's in the package, what's in the Care Plan, what's an add-on)
- Package contents (number of pages, included items)
- Care Plan deliverables
- Domain handling policy
- Discovery / sales process (cold-call script, email templates)
- Anything else listed under "Key facts" above

### The audit procedure

1. **List every file that could reference the changing fact** (use `grep -rn` on the old value across the whole repo, not just files you remember editing). At minimum check:
   - `CLAUDE.md` (this file)
   - `OPERATIONS.md`
   - `BUILD-GUIDE.md`
   - `TODO.md`
   - `index.html`, `index-v2.html`
   - `templates/proposal.html`, `templates/invoice.html`, `templates/client-intake.md`
   - `demos/*/index.html` (any demo that hardcoded a price or policy)
   - **Any new files added since this rule was last updated** — re-grep the whole repo, do not rely on this list being exhaustive

2. **Update every match in one pass.** Do not split into multiple commits where some files have the new rule and others have the old one.

3. **Verify with a second grep on the OLD value.** If anything still matches, you missed a file. Repeat step 2.

4. **Verify with a grep on the NEW value** to confirm consistency of wording across the whole repo (a list of 5 features should read the same in every place, not "4 features" in one file and "5 features" in another).

5. **Only after steps 1–4 succeed**, write the commit and push. Do not declare the task done before the audit passes.

Marketing copy drifts. Numbers drift. Feature lists drift. The cure is not memory — it is `grep`. Run it every time.

---

## What Brian still needs to do (one-time setup)

These require Brian to act — Claude cannot do them. Full instructions in `OPERATIONS.md` Appendix A.

1. Buy domain (frontpagestudio.com or frontpage.studio)
2. Set up Zoho Mail for brian@frontpagestudio.com (free)
3. Create GitHub account + push this repo
4. Connect repo to Vercel and add custom domain
5. Sign up for Formspree and replace `YOUR_FORM_ID` in index.html
6. Activate Stripe + create the three Payment Links (deposit, launch, $79/mo subscription)
7. Build the Google Form intake from `templates/client-intake.md`
8. Get a Google Places API key for the scraper
