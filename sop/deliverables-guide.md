# Frontpage Studio — Deliverables Setup Guide

How to build and set up every feature in the Business Presence Package, plus the optional add-ons, plus the Ongoing Care Plan.

> **The package is 3 pages:** Home, Services, Contact. Extra pages are $75 each.
> All add-ons are **$75 each**. Features marked **(add-on)** below are not in the base $599 package.
> The Ongoing Care Plan ($79/month, mandatory 12-month minimum) covers hosting, security updates, website edits, backup/maintenance, and support.

---

# PART A — PACKAGE DELIVERABLES

These are included in every $599 Business Presence Package build.

---

## 1. 3-PAGE WEBSITE

**The standard 3 pages:**

| Page | Purpose | Key sections |
|---|---|---|
| Home | First impression, capture attention | Hero with headline + CTA, services overview, reviews/testimonials, photo gallery, business hours + service area, email signup, contact CTA |
| Services | What they offer | Each service with name, short description, starting price (if comfortable), click-to-call button |
| Contact | Get the call/form submission | Phone (click-to-call), email, address, hours, service area, embedded Google Maps, contact form |

**Setup:**
1. Use the demo sites in `demos/` as your starting template — swap content, adjust colors
2. Each page is a separate `.html` file linked from the nav (`index.html`, `services.html`, `contact.html`)
3. Keep the nav identical across all pages
4. Footer should appear on every page with phone number + address + social links

**Time estimate:** 3–5 hours for a build once you've done 2–3 of them.

---

## 2. MOBILE-FRIENDLY DESIGN

**What it means:** The site reflows and looks clean on any screen width.

**How to ensure it:**
- Use `<meta name="viewport" content="width=device-width, initial-scale=1.0">` in every `<head>` — always include this
- Use CSS flexbox or grid for all layouts
- Add breakpoints: at minimum, one for `max-width: 768px` (tablets/phones)
- Test in Chrome DevTools: press F12 → click the phone icon → check at 375px (iPhone) and 768px (iPad)
- Images: use `max-width: 100%; height: auto;` so they never overflow

**Common mistakes:**
- Fixed pixel widths on containers (use `%` or `max-width` instead)
- Text that's too small on mobile (minimum 14px body text)
- Buttons that are too small to tap (minimum 44px tall touch target)

---

## 3. CONTACT FORM + CLICK-TO-CALL

### Contact form (Formspree)

**What it does:** Visitor fills out name/email/message → email lands in your client's inbox.

**Setup steps:**
1. Go to [formspree.io](https://formspree.io) and create a free account
2. Click "New Form" → give it the client's business name
3. Copy the form endpoint URL — looks like `https://formspree.io/f/xpzgkrdo`
4. In the HTML, set `<form action="https://formspree.io/f/xpzgkrdo" method="POST">`
5. Add a hidden input to redirect after submission:
   ```html
   <input type="hidden" name="_next" value="https://yourclientsite.com/thanks.html">
   ```
6. Test by submitting a test message — check it arrives in the client's inbox

**Form fields to include:**
```html
<input type="text"  name="name"    placeholder="Your name"    required>
<input type="email" name="email"   placeholder="Your email"   required>
<input type="tel"   name="phone"   placeholder="Phone number">
<textarea           name="message" placeholder="How can we help?"></textarea>
<button type="submit">Send Message</button>
```

**Free tier limits:** 50 submissions/month per form. Plenty for a local business.

### Click-to-call button

**What it does:** On mobile, tapping the phone number opens the dialer instantly.

**Markup:** Wrap the phone number in a `tel:` link — strip spaces and punctuation in the `href`, but keep formatting in the visible text.

```html
<a class="call-cta" href="tel:+15125550123">📞 Call (512) 555-0123</a>
```

**Where to put it:**
- Sticky button on the Services page (top-right or bottom-right on mobile)
- Inline next to each service description
- In the header on mobile (hamburger nav can collapse, but the call button stays visible)
- In the footer on every page

**Styling tip:** Make it visually distinct — a colored pill button. Phone calls convert ~10x better than form submissions for local services.

---

## 4. REVIEWS / TESTIMONIALS SECTION

**What it does:** Surfaces social proof on the homepage so visitors trust the business before they click "Contact".

**How to gather them (ask the client during onboarding):**
- 3–6 short reviews (1–3 sentences each)
- Customer first name + last initial (e.g. "Sarah M.")
- City or neighborhood (optional, but boosts local trust)
- If they have Google reviews already, pull the best 3–6 from their Google Business Profile

**If they have zero reviews yet:**
- Ask them to text 5 recent customers: *"Hey, mind sending me a quick sentence about working with us? Trying to update my website."* — 3 will reply within a day
- Worst case, soft-launch without testimonials and add them after week 1

**HTML structure (card grid):**
```html
<section class="reviews">
  <h2>What customers say</h2>
  <div class="review-grid">
    <article class="review-card">
      <div class="review-stars">★★★★★</div>
      <blockquote>"Showed up on time, fixed the problem, fair price. Will use again."</blockquote>
      <div class="review-by">— Sarah M., Austin TX</div>
    </article>
    <!-- repeat 3–6 times -->
  </div>
</section>
```

**Add it to the LocalBusiness schema markup** (section 11) so Google can show the stars in search results:

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.9",
  "reviewCount": "47"
}
```

Only include `aggregateRating` if the numbers are real and pulled from their Google Business Profile — don't invent.

---

## 5. PHOTO GALLERY

**What it means:** A responsive grid of the business's photos — work, location, products.

**Setup:**
- Get 10–20 photos from the client (or pull from their Google Maps listing with permission)
- Resize images to max 1200px wide before embedding (keeps load time fast) — use free tools like [Squoosh](https://squoosh.app) or [TinyPNG](https://tinypng.com)
- Build a CSS grid gallery:

```html
<div class="gallery-grid">
  <img src="photo1.jpg" alt="Description">
  <img src="photo2.jpg" alt="Description">
  <!-- etc -->
</div>
```

```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 12px;
}
.gallery-grid img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  border-radius: 12px;
}
```

**If client has no photos:** Pull from their Google Maps listing (right-click → Save image), use free Unsplash stock for the business type, or ask them to take 10 quick phone photos.

---

## 6. BUSINESS HOURS + SERVICE AREA

**What it does:** Tells visitors when the business is open and where it operates — both are major ranking factors for "near me" Google searches.

### Hours of operation

**Where to display:**
- Top of the Contact page (large, scannable)
- Footer on every page (compact)
- Inside the LocalBusiness schema markup (section 11)

**Markup:**
```html
<dl class="hours">
  <dt>Mon–Fri</dt><dd>8:00 AM – 6:00 PM</dd>
  <dt>Saturday</dt><dd>9:00 AM – 2:00 PM</dd>
  <dt>Sunday</dt><dd>Closed</dd>
</dl>
```

**Pro tip:** If the business is "open 24/7" (plumbers, locksmiths, towing), put **OPEN 24/7** in the hero on every page — it's a massive trust + conversion signal.

### Service area

**What it is:** The cities, neighborhoods, or zip codes the business serves. Critical for contractors, plumbers, electricians, cleaners — anyone who travels to the customer.

**Where to display:**
- Inline paragraph on Home and Contact pages: *"Proudly serving Austin, Round Rock, Cedar Park, and Pflugerville."*
- A simple bullet list on the Services page
- Inside the LocalBusiness schema markup as `areaServed`

```json
"areaServed": [
  { "@type": "City", "name": "Austin" },
  { "@type": "City", "name": "Round Rock" },
  { "@type": "City", "name": "Cedar Park" }
]
```

**Why it matters:** Google uses `areaServed` to decide which cities your client shows up for in "near me" searches.

---

## 7. GOOGLE MAPS EMBED (Contact page)

**What it does:** Shows an interactive map of the business location right on the Contact page.

**Setup steps:**
1. Go to [maps.google.com](https://maps.google.com)
2. Search for the business address
3. Click Share → Embed a map → Copy HTML
4. Paste the `<iframe>` directly into the HTML on the Contact page

**If the business isn't on Google Maps yet:**
- They need a Google Business Profile first (see section 9)
- In the meantime, embed the address as a map search:
  ```html
  <iframe
    src="https://maps.google.com/maps?q=123+Main+St+Austin+TX&output=embed"
    width="100%" height="350" style="border:0;" loading="lazy">
  </iframe>
  ```

**Styling tip:** Wrap in a `div` with `border-radius` and `overflow: hidden` to match your card style.

---

## 8. EMAIL SIGNUP FORM

**What it does:** Captures email addresses for the client's own marketing list — promos, seasonal updates, new services. Low-friction visitor → lead.

**Easiest option — Formspree (same account as the contact form):**
1. In Formspree, create a SECOND form for this client (e.g. "Acme Plumbing Email List")
2. Use the new endpoint:
   ```html
   <form action="https://formspree.io/f/YOUR_NEWSLETTER_ID" method="POST" class="signup-form">
     <label class="visually-hidden" for="signup-email">Email address</label>
     <input id="signup-email" type="email" name="email" placeholder="your@email.com" required>
     <input type="hidden" name="_subject" value="New email signup — Acme Plumbing">
     <button type="submit">Get updates</button>
   </form>
   ```
3. Tell the client: every signup gets emailed to their inbox. They can copy/paste the email into Mailchimp/Brevo later.

**Better option (if the client already has Mailchimp / Brevo / ConvertKit):** Use that provider's embed snippet instead — they get a real list with unsubscribe handling out of the box.

**Where to put it:**
- Footer (always)
- One inline placement on the Home page (after the gallery or reviews works well)
- Short, single-field — never ask for name on a homepage signup; email-only converts 3x better

**Copy guidance:**
- "Get specials + seasonal tips in your inbox." (services)
- "Be the first to know about new menu items." (restaurants)
- "Monthly tips for keeping your home running." (home services)

---

## 9. GOOGLE BUSINESS PROFILE SETUP & OPTIMIZATION

**What it means:** Their listing on Google Maps and Google Search ("the box" that appears when you search a business name). This is the single highest-value SEO thing you can do for a local business.

**Setup steps:**
1. Go to [business.google.com](https://business.google.com)
2. Sign in with a Google account (ideally the client's, or create one for them)
3. Click "Add your business" → search for the business name
4. If it exists already: claim it (they'll verify by postcard, phone, or email)
5. If it doesn't exist: create it from scratch

**Fields to fill in completely:**
- Business name (exact legal name — must match the website and any other directory listings)
- Category (be specific — "Italian Restaurant" not just "Restaurant")
- Secondary categories (add 2–3 if relevant)
- Address (or hide it if service-area business with no storefront)
- Service area (list all cities/zip codes — must match section 6 on the site)
- Phone number (must match the site exactly — Google checks for NAP consistency)
- Website URL (their new site)
- Hours of operation (every day, including "Closed")
- Business description (750 characters, include their city and main service)
- Upload 10+ photos (exterior, interior, products/services, owner, team)
- Add services with descriptions (this populates the "Services" tab on their listing)

**Verification:** Google usually verifies by postcard (5–7 days) or instant video call. Give the client a heads-up — they need to be the one to do the final verify step.

**After setup:**
- Tell the client to ask their first 5 customers to leave a Google review. Reviews are everything.
- Set a calendar reminder for them to post a Google Business Profile update once a month (new photos, specials, seasonal hours) — it keeps the listing ranked.

---

## 10. SEARCH-READY SETUP

**What it means:** The technical SEO foundation that lets Google find, read, and properly categorize the site. Bundled with every Business Presence Package build.

**Checklist for every build:**

**Title tags** — unique for every page, 50–60 characters:
```html
<title>Tucker Plumbing — Emergency Plumber in Austin, TX</title>
```

**Meta description** — every page, 120–160 characters:
```html
<meta name="description" content="Tucker Plumbing offers 24/7 emergency plumbing in Austin, TX. Licensed, insured, same-day service. Call (512) 555-0123.">
```

**Heading hierarchy:**
- One `<h1>` per page — should contain the business type + city
- Use `<h2>` for section headings, `<h3>` for sub-items
- Never skip levels (don't go `<h1>` → `<h3>`)

**Image alt text:**
```html
<img src="plumber-austin.jpg" alt="Tucker Plumbing technician fixing pipes in Austin TX">
```

**Consistent NAP** (Name, Address, Phone — must be readable text, not an image, and identical across the site, the Google Business Profile, and any directory listings):
```html
<p>Tucker Plumbing | 456 Repair Ave, Austin, TX 78701 | (512) 555-0123</p>
```

**Clean URLs:** Match the page name — `services.html`, `contact.html`, not `page2.html`.

**Keyword targeting (light version — included, deeper work as add-on):**
- Pick ONE primary keyword per page using format `[service] + [city]` (e.g. "emergency plumber Austin TX")
- Use it in the page `<title>`, the `<h1>`, the meta description, and the first paragraph

Do not promise keyword rankings — search-ready setup just means Google can find, read, and properly categorize the site. Combined with Google Business Profile (section 9) and schema markup (section 11), it's enough to start ranking for "[business type] near me" and "[business type] [city]" within a few weeks of launch.

---

## 11. LOCAL SCHEMA MARKUP (JSON-LD)

**What it means:** Hidden code that tells Google exactly what kind of business this is, their hours, phone, address, service area, and reviews — improves how they appear in search results.

**Paste this in the `<head>` of every page, filled out for the client:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "name": "Tucker Plumbing Services",
  "description": "24/7 emergency plumbing in Austin, TX",
  "url": "https://tuckerplumbing.com",
  "telephone": "+15125550123",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "456 Repair Ave",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701",
    "addressCountry": "US"
  },
  "areaServed": [
    { "@type": "City", "name": "Austin" },
    { "@type": "City", "name": "Round Rock" }
  ],
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "$$",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "47"
  }
}
</script>
```

> **Important:** Only include the `aggregateRating` block if the numbers come from the client's real Google Business Profile. If they have no reviews yet, delete the whole block — fake numbers will get the listing flagged.

**`@type` options for common businesses:**
- Plumber, Electrician, HVACBusiness → `"@type": "Plumber"` etc.
- Restaurant → `"@type": "Restaurant"`
- Hair salon → `"@type": "HairSalon"`
- General → `"@type": "LocalBusiness"`

Takes 5 minutes per site. Validate at [validator.schema.org](https://validator.schema.org) after.

---

## 12. SOCIAL MEDIA LINKS (footer)

**What it means:** Icons (or text links) in the footer linking to the client's social profiles.

**Setup:**
1. Ask the client for their handles during onboarding
2. Common platforms for local businesses: Facebook, Instagram, Yelp, Google Business Profile (their listing)
3. Use SVG icons or a free icon library like [Heroicons](https://heroicons.com)
4. Place in the footer: `<a href="https://facebook.com/businessname" target="_blank" rel="noopener">`
5. Always use `target="_blank"` so it opens in a new tab, and always pair with `rel="noopener"` for security

**If they don't have social media:** Skip the icons. Don't put dead links.

---

# PART B — ADD-ONS

Quote these separately. Not included in the base $599 package.

---

## 13. ONLINE BOOKING LINK (add-on — $75)

**What it means:** A link or embedded widget that lets customers schedule an appointment.

**Easiest option — Calendly (free tier):**
1. Go to [calendly.com](https://calendly.com) and create a free account for the client
2. Set up an event type (e.g. "Free Consultation — 30 minutes")
3. Set their availability (or have them do it)
4. Get the booking link: `https://calendly.com/businessname`
5. Embed or link prominently — at minimum, a CTA button: `<a href="https://calendly.com/businessname">Book an Appointment</a>`

**Embed option (inline widget):**
```html
<div class="calendly-inline-widget" data-url="https://calendly.com/businessname" style="min-width:320px;height:630px;"></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

**Other options (also $75 add-on each):**
- Square Appointments (if they use Square for payments)
- Acuity Scheduling
- Just a phone number CTA if they prefer calls: "Call to Book: (512) 555-0123" (free — just put it on the Services page)

---

## 14. FAQ SECTION (add-on — $75)

**What it means:** Accordion-style Q&A section. Helps with SEO (Google sometimes pulls FAQ answers into search results) and reduces "dumb questions" in the client's inbox.

**Ask the client for their 6–8 most common questions.** If they don't know, use these defaults based on business type:
- *Plumber:* Do you offer emergency service? Are you licensed? What areas do you serve? Do you give free estimates?
- *Restaurant:* Do you take reservations? Is parking available? Do you have vegetarian options? Do you cater events?
- *Salon:* Do I need an appointment? How far in advance should I book? Do you accept walk-ins?

**HTML structure:**
```html
<div class="faq-item">
  <button class="faq-q">Do you offer emergency service?</button>
  <div class="faq-a">Yes — we're available 24/7 for emergencies. Call (512) 555-0123 any time.</div>
</div>
```

**JS to make it toggle:**
```javascript
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.nextElementSibling.classList.toggle('open');
  });
});
```

**Bonus:** Add FAQPage schema markup so Google can show the questions in search results — increases the listing's real estate on the results page.

---

# PART C — ONGOING CARE PLAN

$79/month, mandatory 12-month minimum. Covers everything below.

---

## 15. HOSTING (Care Plan)

**What it means:** The site lives on Vercel's servers — fast global CDN, free SSL, zero cost to you.

**Setup steps (one-time per client site):**
1. Push the site files to a GitHub repo (one repo per client)
2. Go to [vercel.com](https://vercel.com) → New Project → Import from GitHub
3. Select the repo → Deploy (no config needed for plain HTML)
4. Vercel gives a free URL: `yoursite.vercel.app`
5. Add the client's custom domain: Settings → Domains → Add → follow DNS instructions
6. SSL is automatic — done

**Ongoing:** Any time you update files and push to GitHub, Vercel auto-deploys in ~30 seconds.

**Cost to you:** $0 (Vercel Hobby tier is free for unlimited static sites).

---

## 16. SECURITY UPDATES (Care Plan)

**What's covered:**
- **SSL/TLS certificate** — Vercel rotates it automatically every 90 days; you verify monthly that it's valid (green padlock in the browser)
- **Dependency patches** — if you ever use any JS library (Calendly widget, Formspree script, analytics), check for advisories quarterly and bump versions
- **Form spam control** — if Formspree starts forwarding obvious junk to the client, turn on Formspree's honeypot or reCAPTCHA (free)
- **Domain registrar lock** — confirm the client's domain has "registrar lock" enabled at Namecheap/Cloudflare so it can't be stolen via transfer
- **DNS / Vercel account 2FA** — keep 2FA on your Vercel and GitHub accounts; you're the gatekeeper for every client site

**Monthly security check (do this on the 1st):**
1. Visit each client site in an incognito window → confirm the padlock is green
2. Open Vercel dashboard → check no deployments have failed
3. Glance at Formspree submissions for any one client → spot-check for spam patterns
4. Skim GitHub Dependabot alerts (if any repos use packages)

If something breaks, fix it that same day — clients don't see "security update" line items, they just see whether their site is up.

---

## 17. WEBSITE EDITS (Care Plan)

Every Care Plan client gets ongoing edits. Budget **~1 hour per month per client** for planning purposes; the package isn't marketed with an explicit hourly cap, but watch for clients who consistently exceed an hour.

**What counts as a normal edit:**
- Changing hours of operation
- Updating a phone number or address / service area
- Swapping in a new photo
- Adding or editing a service description
- Updating a menu item or price
- Adding a seasonal promotion banner
- Fixing a typo
- Adding new testimonials as they come in

**What does NOT count (quote separately):**
- Adding a new page (+$75)
- Redesigning a section
- New features (booking, FAQ, e-commerce, etc.)
- Anything taking more than ~2 hours of work

**Process:**
- Give every Care Plan client your email and tell them to send update requests there
- Batch updates — do them once a week, not same-day (unless urgent)
- Log time in a simple spreadsheet so you can tell clients what you did at month 11

**If a client routinely burns through 1 hr/month:** Email them a usage summary at any point and offer to either bill overage at $75/hr or upgrade to a 2 hr/month plan at $129/month going forward.

---

## 18. BACKUP / MAINTENANCE (Care Plan)

**Backups (automatic):**
- Every site lives in its own GitHub repo
- Every change is a Git commit — full history is preserved forever
- To restore to any prior version: `git revert <commit>` or roll back the Vercel deployment in one click
- No third-party backup service needed; GitHub IS the backup

**Quarterly maintenance pass (do this every 3 months for every client):**
1. Lighthouse audit in Chrome DevTools — keep Performance, Accessibility, Best Practices, SEO all ≥ 85
2. Verify all external links still work (Google Maps embed, social links, Calendly link if any)
3. Confirm contact form still delivers (send a test submission yourself)
4. Confirm the domain isn't expiring in the next 6 months (renew or remind the client to renew)

**Domain renewal:**
- Add every client's domain expiry date to your calendar
- Email the client 60 days before, then again at 30 days
- If they ignore both reminders, call them — losing a domain is catastrophic and they will blame you regardless of whose name is on the registrar

---

## 19. SUPPORT (Care Plan)

**What clients get:**
- Email support at the address you give them at launch
- Same-day response on weekdays for any request received before 4 PM local time
- Next-day response for evening / weekend emails
- Emergency phone/text response within 2 hours for sites that are fully down (rare)

**Process:**
- Triage every incoming request into one of: edit (do this week), question (reply today), bug/down (fix today), out-of-scope (quote separately)
- Use a single email inbox or a free help-desk tool (e.g. Front, Plain free tier) once you pass ~15 clients
- Keep a "common requests" snippet file — most edits repeat across clients (seasonal banners, holiday hours, photo swaps)

**Boundaries to set up front:**
- You don't take calls — email/text only — unless the site is actually down
- You don't write blog posts, social posts, or copy for them (that's marketing, not maintenance)
- You don't run paid ads or manage their reviews — that's a separate engagement and not something Frontpage Studio offers

---

## 20. CARE PLAN — 12-MONTH MINIMUM TERM

Every Care Plan signs the client up for a **mandatory 12-month minimum**. After that it goes month-to-month.

**Track for every client:**
- Launch date (= billing day each month)
- Month-12 anniversary date (= renewal-decision touchpoint)
- Total monthly hours used (for the upgrade conversation at month 11)

**Month 11 email (template) — continuous hosting confirmation:**
> "Hi [Name] — quick heads-up: your initial 12-month Care Plan wraps up next month, and your hosting will continue uninterrupted at the same $79/month going forward. Nothing you need to do. After this point you can cancel any time with 30 days' notice. Thanks for being a great client this year!"

**If they ask to cancel during months 1–12:**
> "I totally get it. The 12-month term is fixed — that's what lets me keep the build at $599. The remaining [X] months are still due. Once the year is up, you're free to cancel or move hosting elsewhere with a 30-day heads-up. Want me to send you a summary of what you've used so far?"

**At month 12, if they cancel:** hand over the GitHub repo + a zip of the latest files within 24 hours. Disable auto-billing. Wish them well. They often come back within 6 months.
