# Frontpage Studio — Operations

Everything to sell, deliver, and run the business. For technical "how to build" details, see `BUILD-GUIDE.md`. For pricing facts and design rules, see `CLAUDE.md`.

---

## Contents

**Part 1 — The Offer:** [Business Model](#business-model) · [Package](#business-presence-package) · [Care Plan](#ongoing-care-plan) · [Add-ons](#add-ons) · [Objections](#handling-objections)

**Part 2 — Client Journey:** [Lead Gen](#1-lead-generation) · [Cold Call](#2-cold-calling) · [Discovery](#3-discovery-call) · [Proposal](#4-proposal) · [Deposit](#5-deposit--agreement) · [Build](#6-build-days-17) · [Revisions](#7-revisions) · [Launch](#8-launch) · [Care Plan Ongoing](#9-care-plan-ongoing)

**Part 3 — Email Templates** ([5 essential](#email-templates))

**Appendix** — [One-Time Setup](#appendix--one-time-setup)

---

# Part 1 — The Offer

## Business Model

Cold-call local businesses with no website. Build them one for $599 + a mandatory $79/month Care Plan (12-month minimum). Hundreds of thousands of these businesses exist in any metro. They're not hard to find — they just haven't been asked.

**Target customers:** restaurants, plumbers, electricians, HVAC, contractors, hair salons, barbershops, nail salons, auto repair, landscapers, cleaners, florists, law offices, accountants, chiropractors, massage therapists.

**Avoid:** large chains, businesses with existing sites (different pitch), startups.

## Business Presence Package

**$599 one-time.** 3-page website (Home, Services, Contact), mobile-friendly, contact form + click-to-call, reviews section, photo gallery, business hours + service area, Google Maps embed, email signup, Google Business Profile setup, search-ready setup (titles + meta + NAP + LocalBusiness schema), 1 revision round, 7-day delivery from completed intake.

**Cost to deliver:** ~3–5 hours to build once you've done a few. ~30–60 min/month ongoing per client.

## Ongoing Care Plan

**$79/month. Mandatory 12-month minimum.** Required with every build. After month 12 converts to month-to-month, cancellable with 30 days' notice.

Covers: hosting (Vercel), security updates + SSL maintenance, website edits (~1 hr/month budget), backup and maintenance, email support (same-day weekday).

**First-year client commitment:** $948.

## First-Year Numbers Per Client

| Stage | Amount | When |
|---|---|---|
| Deposit | $299.50 | At signing |
| Launch payment | $378.50 | At launch (balance + first Care Plan month) |
| Domain pass-through | ~$12–$15 | At launch, only if registering for client. Re-billed annually at cost. |
| Months 2–12 | $79/month | Auto-charged on launch-day anniversary |
| **Total Y1 (excl. domain)** | **$1,547** | |

## Add-ons

| Add-on | Price | When |
|---|---|---|
| Extra page | $75/page | More than the included 3 |
| FAQ section | $75 | Repeat questions worth surfacing |
| Extra revision round | $75 | Past the included round |
| Custom logo | $149 | No logo or a bad one |
| E-commerce (up to 20 products) | $399 | Selling online |
| Rush delivery (48 hrs) | +$200 | Fast turnaround |

**Domain is not an add-on.** Always purchased through Namecheap on the client's behalf, billed back at registrar cost (~$12–$15) on the launch invoice. No markup. Re-billed at cost each annual renewal.

## Handling Objections

**"That's too expensive."**
> "I understand. A local agency would charge $2,500–$10,000 for the same scope, with monthly retainers of $500+. You get build, hosting, security, edits, backups and maintenance, and support — for a year — at well under that."

**"I have a Facebook page."**
> "That's a great start, and a lot of customers will find you there. The difference is Google. When someone types '[your trade] near me,' they see websites first. Facebook pages rank much lower. That's the gap a website fills."

**"My nephew can do it."**
> "Awesome — use him. If it doesn't work out or takes too long, keep my number. One-week turnarounds."

**"Why is the $79/month required for 12 months?"**
> "Two reasons. One, it's how I can offer the build at $599 instead of $1,500 like the agencies charge. Two, it covers hosting, security, edits, backups and maintenance, and support — the things that keep your site working long after launch. After year one it's month-to-month and you can cancel anytime."

**"Can I just pay for the website and host it myself?"**
> "We don't unbundle the build from the Care Plan. That's how the upfront price stays low and how I can guarantee the site stays current. After 12 months you can move hosting elsewhere — your files are yours."

**"What if I want to cancel during the 12 months?"**
> "The 12-month term is fixed, like a phone contract. Cancelling early means the remaining months are due. After month 12 you can cancel anytime with 30 days' notice."

---

# Part 2 — Client Journey

```
LEAD GEN → COLD CALL → DISCOVERY → PROPOSAL → DEPOSIT → BUILD → LAUNCH → CARE PLAN
```

## 1. Lead Generation

`scraper/find_leads.py` outputs a CSV with business name, phone, address, Maps link.

1. Run scraper morning of, 2–3 business types + target city
2. Sort by rating descending (higher-rated businesses lose the most without a web presence)
3. Add new leads to the **Leads** tab of your command-center Sheet
4. Skip anyone already in the sheet (manual until dedup logic ships — see TODO Phase 2)

**Goal:** 20+ new leads/day. ~80 calls to close 1 client.

## 2. Cold Calling

**Target:** 20 calls/day minimum. **Best hours:** Tue–Thu, 9–11am and 2–4pm. **Goal of the call:** book a discovery call. Don't pitch yet.

**Outcome codes (update Status in the Leads sheet):**
- `VM` — voicemail (follow up in 2 days)
- `NA` — no answer (try next day, different time)
- `NI` — not interested (close, don't call again)
- `CB` — callback requested (note date/time in Next Action Date)
- `INT` — discovery call booked
- `CLOSED` — agreed to proceed

### Opening (10 seconds matters most)

> "Hi, is this [Name]? Hey [Name], this is Brian from Frontpage Studio. I'm a local web designer and I was looking up [business type] in [city] — noticed your business doesn't have a website yet. Is that right?"

### If they confirm

> "Totally, lot of great businesses haven't gotten around to it. I build websites specifically for [business type] — about a week, flat rate, no surprises. Would you be open to a quick 10-minute call so I can understand your business and show you what one could look like? No obligation."

### Booking

> "Perfect. Just a quick 15-min phone call. What works better — tomorrow morning around 10, or Thursday afternoon around 2?"

Lock the specific time. Confirm by text right after.

### Voicemail (under 20 sec)

> "Hey [Name], this is Brian with Frontpage Studio. Noticed [Business] doesn't have a website yet — I'd love to show you what one could look like. Quick call, free, no pressure. Call or text me back at [number]. Thanks!"

### When in doubt, refer to the objection handlers above (Part 1 §Handling Objections).

## 3. Discovery Call

15–20 min. Goal: qualify and set up the proposal.

**Open:** "Hi [Name], thanks for making the time. I'll keep this short — a few questions so I can put together the right proposal."

**Ask:**
1. "Tell me a little about [Business] — how long have you been open?"
2. "How do customers find you now — word of mouth, Yelp, Google?"
3. "What do you want a website to do — be a presence, or actively bring new customers from Google?"
4. "Do you have a logo and brand colors, or need help there?"
5. "Any sites you've seen for similar businesses you like?"

**Qualify on:** budget ($1,547 first year), decision-maker, urgency.

**Close:** "Based on what you've told me, the Business Presence Package is a great fit. I'll send a proposal tonight. Does [tomorrow morning] work to follow up?"

## 4. Proposal

`templates/proposal.html` → print to PDF → attach to the "Sending the Proposal" email below.

Includes recommended package, what's included, 7-day timeline, payment terms, CTA: "Reply 'I accept' + click the Stripe deposit link to proceed."

Follow up if no response in 48 hours.

## 5. Deposit & Agreement

**For your first ~10 clients:** "Yes, let's do it!" + Stripe deposit payment = legally sufficient acceptance.

**Past first few clients:** introduce `templates/msa.html` (print to PDF, both parties sign before deposit).

**Payment terms:**
- $299.50 deposit before build starts
- $378.50 at launch (balance + first Care Plan month)
- Plus domain pass-through (~$12–$15) at launch if registering for client
- Then $79/month auto-charged for 11 more months

**Never start without a deposit.** One ghost teaches this lesson.

## 6. Build (Days 1–7)

**Day 1–2 — Content gathering.** Send the intake form (Google Form built from `templates/client-intake.md`). Get business info, hours, services, photos, logo, reviews, style preferences, domain choice.

**Day 3–5 — Build.** Start from the closest demo in `demos/`. Customize: name, colors, content, photos. Build responsive. Wire Formspree. Embed Google Maps. Add LocalBusiness schema. Set up Google Business Profile. See `BUILD-GUIDE.md` for per-deliverable specifics.

**Day 6 — Internal review.** Test links. Submit the contact form yourself. Test on iPhone and Android viewports. Spelling pass. Lighthouse ≥85 across the four scores.

**Day 7 — Client review.** Send the staging link. Client has 48 hours to respond with one consolidated revision list.

## 7. Revisions

**1 round included.** A "round" = one consolidated email of changes. Provider turns them around within 24 hours.

**Out-of-scope (charge separately):** new pages ($75), new features (e-commerce, FAQ section, etc.), redesign after approval.

**Out-of-scope rate:** $75/hour or flat-fee.

## 8. Launch

**Pre-launch checklist:**
- [ ] Client approved final
- [ ] Launch payment received (Stripe launch link)
- [ ] Domain purchased through Namecheap (your account, billed back at cost)
- [ ] Vercel connected to the custom domain
- [ ] SSL active (Vercel automatic)
- [ ] Contact form delivers end-to-end
- [ ] `/privacy.html` deployed (from `templates/client-privacy-policy.html`)
- [ ] `/terms.html` deployed (from `templates/client-terms-of-service.html`)
- [ ] Footer links to /privacy and /terms on every page
- [ ] Sitemap submitted to Google Search Console

**Handoff:** send the launch confirmation email + personalized `templates/launch-handover.md` (fill placeholders → PDF or shared Google Doc). Handover is the client's single reference post-launch.

## 9. Care Plan Ongoing

Every client on $79/month for 12 months minimum (mandatory). Stripe subscription auto-charges monthly.

**Add to your Sheet's Care Plan Clients tab.** Track launch date, month-11 reminder date, month-12 anniversary, hours used, last edit date, domain renewal date.

**Monthly:** security check across all client sites (incognito visit, Vercel dashboard for failed deploys, Formspree spam patterns). See `BUILD-GUIDE.md` for the checklist.

**Weekly:** batch website edits. Budget ~1 hour/month per client.

**Quarterly:** Lighthouse audit + external-link check + domain expiry check per client. See `BUILD-GUIDE.md`.

**Month 11 email:** courtesy heads-up that the initial term wraps next month, plan continues at $79/month month-to-month. No action needed.

**Cancellations:**
- Months 1–12: remaining months due in full
- After month 12: hand over files within 24 hours, point domain wherever

**If a client exceeds 1 hr/month routinely:** email a usage summary anytime, offer overage at $75/hr or upgrade to 2-hr plan at $129/month.

---

# Part 3 — Email Templates

Customize `[brackets]` per client. Five templates cover the full lifecycle.

## 1. Initial Outreach (cold email when phone fails)

**Subject:** Your business deserves a website — quick question

> Hi [Name],
>
> I run Frontpage Studio, a web design company working with local [business type] in [city]. Came across [Business Name] and noticed you don't have a website yet. I build mobile-friendly sites for businesses like yours — flat rate, 7-day turnaround.
>
> Demo for a similar business: [demo link]
>
> Open to a quick 10-min call this week?
>
> — Brian
> Frontpage Studio · [phone] · brian@frontpagestudio.com

## 2. Voicemail Follow-up

**Subject:** Following up — web design for [Business Name]

> Hi [Name],
>
> Left you a voicemail earlier — wanted to follow up. I build websites for local [business type] in [city] for $599 plus a $79/month plan (required for the first 12 months, then month-to-month) covering hosting, security, edits, backups and maintenance, and support. No tech headaches.
>
> Demo: [demo link]
>
> If you're curious, reply with a couple of times that work and we'll lock something in.
>
> — Brian · Frontpage Studio · [phone]

## 3. Sending the Proposal

**Subject:** [Business Name] — Your Website Proposal

> Hi [Name],
>
> Custom proposal attached. Key details:
>
> **Business Presence Package** — $599 one-time + $79/month (12-month minimum)
> **Includes:** 3-page site (Home, Services, Contact), mobile, contact form + click-to-call, reviews, gallery, hours + service area, Maps embed, email signup, Google Business Profile setup, search-ready setup
> **Timeline:** 7 days from your completed intake form
> **Payment:** $299.50 deposit now, $378.50 at launch (balance + first Care Plan month), then $79/month for 11 more months. Plus domain pass-through at cost (~$12–$15).
> **First-year total:** $1,547
>
> To move forward:
> 1. Reply with "I accept"
> 2. Pay the deposit: [STRIPE_DEPOSIT_LINK]
>
> As soon as both are in, I kick off the build and send the content form.
>
> — Brian
> Frontpage Studio

## 4. Deposit Confirmation + Intake Form

**Subject:** Deposit received — let's build your site

> Hi [Name],
>
> Deposit received, thank you. Build is officially kicking off.
>
> Before I dive in, fill out this 10-min form: [GOOGLE_FORM_LINK]
>
> Asks for: business description, services, hours, address, 10–20 photos, logo, a few customer reviews, style preferences, top 3 domain choices if you don't already own one.
>
> The 7-day clock starts when this form is in. Targeting [launch date].
>
> — Brian

## 5. Launch Confirmation

**Subject:** You're live — [Business Name] is now on the web

> Hi [Name],
>
> [businessname.com] is live.
>
> Your website: [URL]
>
> A few things to know:
> - Contact form active — you'll get an email every time someone submits
> - I've submitted your site to Google — usually 1–2 weeks to show in search
> - Your $79/month Care Plan covers hosting, security, edits, backups and maintenance, and support. Email me whenever you need anything. Plan runs through [launch + 12 months], then continues month-to-month.
> - Manage your subscription anytime: [STRIPE_CUSTOMER_PORTAL_URL]
>
> Full handover doc with account details and billing schedule attached.
>
> Thanks for trusting me with your front page. If you're happy with the work, a Google review would mean a lot.
>
> — Brian
> Frontpage Studio · brian@frontpagestudio.com · [phone]

---

# Appendix — One-Time Setup

Do this once before your first client call.

## 1. Domain + Email
- Buy domain at namecheap.com or cloudflare.com (~$12/yr)
- Set up Zoho Mail (zoho.com/mail, free), create `brian@frontpagestudio.com`, verify via TXT DNS record

## 2. GitHub + Vercel
- github.com → new repo `frontpagestudio` → push the local web/ folder
- vercel.com → sign in with GitHub → import the repo → deploy. Free `*.vercel.app` URL works immediately.
- Add custom domain in Vercel project settings, follow CNAME instructions at registrar

## 3. Formspree (contact form)
- formspree.io → new form named "Frontpage Studio Contact"
- Copy form endpoint, replace `YOUR_FORM_ID` in `index.html`
- Push to GitHub, Vercel auto-redeploys, test

## 4. Stripe (payments)
- stripe.com → start application (sole prop fine to start)
- Connect bank account, wait for verification (~1–2 days)
- Products → create **Business Presence Package** (one-time, $599) + **Ongoing Care Plan** (recurring, $79/mo)
- Payment Links → generate three reusable URLs:
  - **Deposit:** $299.50 one-time
  - **Launch:** $378.50 one-time
  - **Subscription:** $79/month recurring
- Save the three URLs (notes app or password manager)
- Replace `[STRIPE_DEPOSIT_LINK]` in `templates/proposal.html` and `templates/invoice.html`
- **Settings → Customer Portal:** enable + configure. Save the portal URL into the launch email template.

**Fees:** 2.9% + $0.30 per card transaction (~$48/client/year on $1,547). ACH 1.5% capped at $5 — offer for the build payment.

**12-month minimum isn't auto-enforced by Stripe.** If a client cancels early, manually invoice the remaining months. Rare.

## 5. Google Form (intake)
- forms.google.com → blank → name "Frontpage Studio — New Client Intake"
- Copy each question from `templates/client-intake.md` into the form, match question types
- For Logo + Photos sections, use File upload (image + PDF, 10MB cap, multiple files allowed)
- Settings → Responses → enable Collect Emails + Link to Sheet
- Save the form URL into the deposit-confirmation email template

## 6. Command-Center Sheet
- sheets.google.com → new sheet → name "Frontpage Studio — Command Center"
- Import the four CSVs in `templates/sheets/` as tabs per `templates/sheets/README.md` (5–8 minutes including formulas + dropdowns)
- Bookmark the URL. Open every morning.

## 7. Google Places API (for the scraper)
- console.cloud.google.com → new project "Frontpage Studio Leads" → enable Places API (New)
- Credentials → create API key
- On your laptop: `pip install -r scraper/requirements.txt`
- Set env var: `$env:GOOGLE_PLACES_API_KEY = "your-key"` (PowerShell)
- Run: `python scraper/find_leads.py`

## Things Claude cannot do

- Register your domain / verify Zoho mail / sign you up for any third-party service
- Get your Google Places API key
- Take payment (needs your Stripe account)
- Form an LLC (legalzoom or your state's SOS website, ~$50–$150)
