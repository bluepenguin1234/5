# Frontpage Studio — Claude Instructions

## What This Project Is

Frontpage Studio is Brian's web design business targeting local businesses with no website. Cold call outreach model. Brian builds the sites, handles hosting, and does the sales calls himself.

**Working directory:** `C:\Users\Brian\Desktop\web`

---

## Business Model

- Find local businesses with no website using the scraper or Google Maps
- Cold call them, pitch a flat-rate website build
- Every client pays a one-time build fee + mandatory $79/month hosting & care plan

**Current pricing (do not change without being asked):**
- Starter: $599 one-time + $79/month
- Professional: $999 one-time + $79/month
- $79/month is NOT optional — it is required with every plan
- It covers: hosting on Vercel, 1 hr/month content updates, domain reminders, priority support

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
├── index.html                  ← Agency website (Frontpage Studio's own site)
├── CLAUDE.md                   ← This file
├── LAUNCH-GUIDE.md             ← Step-by-step launch checklist for Brian
├── vercel.json                 ← Vercel deployment config (static HTML)
├── .gitignore
│
├── demos/
│   ├── restaurant/index.html   ← Maplewood Kitchen (Cormorant Garamond, dark luxury)
│   ├── barbershop/index.html   ← Sharp & Co. (Bebas Neue, navy/gold, classic)
│   └── plumber/index.html      ← Tucker Plumbing (Barlow Condensed, blue/orange)
│
├── scraper/
│   ├── find_leads.py           ← Google Places API scraper (finds businesses with no website)
│   └── requirements.txt
│
├── sop/
│   ├── SOP.md                  ← Master business operating procedure
│   ├── packages.md             ← Package breakdown (what each plan includes)
│   ├── pricing.md              ← Pricing strategy, objection handling, revenue projections
│   ├── deliverables-guide.md   ← How to set up every feature (SEO, forms, GMB, etc.)
│   ├── cold-call-script.md     ← Word-for-word call scripts + objection handling
│   └── email-templates.md      ← All email templates (outreach through launch)
│
└── templates/
    ├── proposal.html           ← Client proposal (print to PDF)
    └── invoice.html            ← Client invoice (print to PDF)
```

---

## Rules for Building Sites

### When building the agency site (`index.html`)
- Use the bento design system above — peach/blue/cream palette, Inter font, card grid layout
- Pricing must always show $599 + $79/mo and $999 + $79/mo
- $79/month must always be described as included/required, never optional

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

## Key SOPs to Know

- **Revisions:** Starter = 1 round, Professional = 2 rounds. A "round" = one email with all feedback consolidated. Extra revisions = $75/hr.
- **Payment:** 50% deposit before build starts, 50% at launch + first month of $79 hosting.
- **Delivery:** 7 business days from deposit + content received.
- **Hosting:** Vercel free tier. Push to GitHub, connect repo to Vercel, add custom domain. SSL is automatic.
- **Contact forms:** Formspree (formspree.io) — free up to 50 submissions/month per form.
- **Basic SEO (Starter):** Title tags, meta descriptions, heading hierarchy, alt text, NAP in text.
- **Full SEO (Professional):** Above + keyword-targeted titles/h1s, Google Business Profile setup, LocalBusiness JSON-LD schema.

---

## What Brian Still Needs to Do (One-Time Setup)

These require Brian to act — Claude cannot do them:
1. Buy domain (frontpagestudio.com or frontpage.studio)
2. Set up Zoho Mail for brian@frontpagestudio.com (free)
3. Create GitHub account + push this repo
4. Connect repo to Vercel (vercel.com) and add custom domain
5. Sign up for Formspree and replace `YOUR_FORM_ID` in index.html
6. Get Google Places API key and add to `.env` for the scraper
7. Set up Stripe or PayPal for client billing

Full instructions in `LAUNCH-GUIDE.md`.
