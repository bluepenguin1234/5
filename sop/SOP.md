# Frontpage Studio — Standard Operating Procedure

**Last Updated:** 2026-05-27  
**Version:** 1.1

---

## BUSINESS MODEL OVERVIEW

You find small businesses with no website, call them cold, and offer to build a professional website for a flat build fee plus mandatory $79/month hosting and care. The key insight: **there are hundreds of thousands of businesses in any metro area without a website.** They're not hard to find — they just haven't been asked yet.

**Pricing model:**
- Starter: $599 one-time build + $79/month hosting & care
- Professional: $999 one-time build + $79/month hosting & care
- The $79/month is required with every plan — it covers hosting, updates, and support
- 10 clients on hosting = $790/month recurring before you close a single new deal

**Target customers:**
- Restaurants, diners, cafés
- Plumbers, electricians, HVAC, general contractors
- Hair salons, barbershops, nail salons
- Auto repair shops
- Landscapers, lawn care
- Cleaning services
- Florists, gift shops
- Local law offices, accountants
- Chiropractors, massage therapists

**Avoid (for now):**
- Large chains (have corporate web teams)
- Businesses with websites but "bad" ones (different pitch, different product)
- Startups (different needs)

---

## PROCESS MAP

```
LEAD GENERATION → COLD CALL → DISCOVERY CALL → PROPOSAL → DEPOSIT → BUILD → REVIEW → LAUNCH → PAYMENT
```

---

## 1. LEAD GENERATION

**Tool:** `scraper/find_leads.py`  
**Output:** CSV with business name, phone, address, Google Maps link

**SOP:**
1. Run scraper every morning with 2–3 business types + your target city
2. Open the CSV in Excel/Sheets
3. Sort by rating (desc) — higher-rated businesses lose the most without a web presence
4. Remove duplicates from previous days
5. Add new leads to your master tracking sheet

**Master Tracking Sheet columns:**
| Business Name | Phone | Address | Type | Date Added | Called? | Outcome | Follow-up |

**Goal:** 20+ new leads per day. You'll need ~100 calls to close 1–2 clients per week.

---

## 2. COLD CALLING

**Script:** See `cold-call-script.md`  
**Target:** 20 calls/day minimum  
**Best hours:** Tue–Thu, 9–11am and 2–4pm

**Call outcomes to track:**
- `VM` — Left voicemail (follow up in 2 days)
- `NA` — No answer (try again next day, different time)
- `NI` — Not interested (mark closed, do not call again)
- `CB` — Callback requested (note date/time)
- `INT` — Interested, discovery call booked
- `CLOSED` — Agreed to proceed

**Voicemail script:**
> "Hi, this is Brian from Frontpage Studio — I'm a web designer and I noticed [Business Name] doesn't have a website yet. I'd love to show you what one could look like for your business — takes about 10 minutes. My number is [your number]. Feel free to call or text — thanks!"

---

## 3. DISCOVERY CALL

**Duration:** 15–20 minutes  
**Goal:** Qualify the prospect, understand their needs, set up for proposal

**Questions to ask:**
1. "How do most of your customers currently find you?" (Google, word-of-mouth, Yelp, etc.)
2. "Have you ever looked into getting a website before? What stopped you?"
3. "What services/products do you most want people to know about?"
4. "Do you have a logo already? Any brand colors?"
5. "Any competitor websites you like the look of?"
6. "Are you looking to take bookings/reservations online, or just information?"
7. "What's the best way for customers to contact you — phone, email, or form?"

**Qualify on:**
- Do they have budget? ($599 or $999 build + $79/month ongoing)
- Are they the decision maker?
- Is there urgency? (If yes, move fast)

**End the call:**
> "Great — based on what you've told me, I think a [Starter/Professional] package would work well for you. I'll send you a proposal by end of day. It'll include a mockup idea and exact pricing. Sound good?"

---

## 4. PROPOSAL

**File:** `templates/proposal.html` (print to PDF and email)  
**Send within:** 24 hours of discovery call  
**Follow up:** If no response in 48 hours, call back

**Proposal includes:**
- Recommended package + why
- What's included (specific pages, features)
- Timeline (7 days from deposit)
- Price + payment terms (50% upfront, 50% on launch)
- Simple call-to-action: "Reply YES to proceed and I'll send you an invoice"

---

## 5. AGREEMENT & DEPOSIT

**Tools needed:** PayPal, Venmo, or Stripe (your choice)

**Verbal agreement is enough to start.** For your first few clients, a simple email reply of "yes, let's do it" is sufficient. Once you're doing $5k+/month, add a simple contract (see `templates/contract.md`).

**Payment terms:** 50% deposit before you start. 50% before launch (before you give them the domain password).

**Never start building without a deposit.** Even with nice people. One ghost will teach you this lesson.

---

## 6. BUILD PROCESS

**Timeline:** 5–7 business days from deposit

**Day 1–2: Content gathering**
- Send the client a simple Google Form asking for:
  - Business description (1–2 paragraphs)
  - Services list with brief descriptions
  - Hours of operation
  - Address and phone number
  - 3–5 photos (or tell them you'll use free stock photos)
  - Any existing logo files
  - Social media handles (Instagram, Facebook, Yelp, etc.)

**Day 3–5: Build**
- Use Claude Code with `/frontend-design` skill
- Start from the appropriate demo template (restaurant, barbershop, plumber, etc.)
- Customize: name, colors, content, photos
- Build responsive (test on mobile)
- Add contact form (Formspree)
- Add Google Maps embed

**Day 6: Internal review**
- Test all links
- Test contact form (submit it yourself)
- Test on mobile (iPhone and Android layouts)
- Check spelling and grammar on every page
- Run through Google PageSpeed Insights (aim for 85+)

**Day 7: Client review**
- Send staging link (Vercel preview URL)
- Message: "Your website is ready for your review! Here's the link: [url]. Please take a look and let me know any changes by [date+2 days]."

---

## 7. REVISIONS

**Policy per package:**
- Starter: 1 round of revisions
- Professional: 2 rounds

**A "round" = one email with a list of changes.** Not ongoing back-and-forth.

**How to handle revision requests:**
> "Got your notes — I'll have those updates done within 24 hours."

**Out-of-scope requests (charge extra):**
- Additional pages beyond package
- New features not discussed (e-commerce, booking system, etc.)
- Major redesign after approval

**Out-of-scope rate:** $75/hour or flat-fee by project

---

## 8. LAUNCH

**Checklist before launch:**
- [ ] Client approved final version
- [ ] Remaining 50% payment received
- [ ] Domain purchased or transferred (client pays for domain)
- [ ] Vercel project connected to custom domain
- [ ] SSL certificate active (Vercel does this automatically)
- [ ] Contact form working
- [ ] Google Analytics / Search Console submitted (if included in package)
- [ ] Sitemap submitted to Google Search Console

**Handoff message:**
> "Congratulations — your site is live at [domain]! 🎉 I've sent you an email with your login info and a quick guide on how to contact me if you ever need changes. Thank you so much for trusting me with your business's online presence."

---

## 9. BILLING & BOOKKEEPING

**Track every transaction in a simple spreadsheet:**
| Client | Invoice # | Amount | Deposit Paid | Balance Paid | Date |

**Invoice numbering:** FS-001, FS-002, FS-003...

**Save all receipts.** You'll need these for taxes. Web design income is self-employment income — set aside 25–30% for taxes.

**Free accounting tools:**
- Wave (wave.com) — free invoicing + expense tracking
- Or just a simple Excel spreadsheet for now

---

## 10. HOSTING + CARE PLAN ($79/month — required with every plan)

Every client pays $79/month starting at launch. This is not optional — it's part of every package.

**What's included:**
- Hosting on Vercel (costs you $0)
- Content updates up to 1 hour/month (text changes, new photos, updated hours, etc.)
- Domain renewal reminders (30 days before expiry)
- Priority email support (same-day response)

**How to handle it:**
- Collect the first month's $79 with the final build payment at launch
- Set up a recurring charge via Stripe, PayPal, or Venmo on the same day each month
- Log all active hosting clients in your tracking spreadsheet

**Billing:**
- Invoice monthly on the same day as their launch date
- If a client wants to cancel: give them their files, point their domain wherever they want, done
- Never hold the site hostage — just make cancelling painless and they'll rarely do it

**Revenue math:** 10 clients = $790/month. 20 clients = $1,580/month. Pure profit after your first year.

---

## KEY METRICS TO TRACK WEEKLY

| Metric | Target |
|--------|--------|
| Leads generated | 100+/week |
| Calls made | 20/day |
| Discovery calls booked | 3–5/week |
| Proposals sent | 3–5/week |
| Clients closed | 1–2/week |
| Revenue collected | $599–$2,000+/week |
| Active hosting clients | Growing monthly |
| Recurring hosting revenue | $79 × active clients |

---

*Frontpage Studio SOP v1.0 — Keep this updated as your process improves.*
