# Frontpage Studio — Deliverables Setup Guide

How to build and set up every feature in the Business Presence Package, plus the optional add-ons.

> **The package is 3 pages:** Home, Services, Contact. Anything beyond that is an add-on ($75/page). Features marked **(add-on)** below are not in the base $599 package.

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
2. Each page is a separate `.html` file linked from the nav
3. Keep the nav identical across all pages
4. Footer should appear on every page with phone number + address + social links

**Time estimate:** 3–5 hours for a build once you've done 2–3 of them.

---

## 2. MOBILE RESPONSIVE

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

## 3. CONTACT FORM (Formspree)

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

---

## 4. GOOGLE MAPS EMBED

**What it does:** Shows an interactive map of the business location right on the page.

**Setup steps:**
1. Go to [maps.google.com](https://maps.google.com)
2. Search for the business address
3. Click Share → Embed a map → Copy HTML
4. Paste the `<iframe>` directly into the HTML

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

## 5. SOCIAL MEDIA LINKS

**What it means:** Icons (or text links) in the nav or footer linking to their profiles.

**Setup:**
1. Ask the client for their handles during onboarding
2. Common platforms for local businesses: Facebook, Instagram, Yelp, Google Maps (their listing)
3. Use SVG icons or a free icon library like [Heroicons](https://heroicons.com) or simple emoji (✓ for quick builds)
4. Place in the footer: `<a href="https://facebook.com/businessname" target="_blank" rel="noopener">`
5. Always use `target="_blank"` so it opens in a new tab, and always pair with `rel="noopener"` for security

**If they don't have social media:** Skip the icons. Don't put dead links.

---

## 6. SEARCH-READY SETUP

**What it means:** The technical foundation that lets Google find and understand the site. Bundled with every Business Presence Package build.

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

**NAP in text** (Name, Address, Phone — must be readable text, not an image):
```html
<p>Tucker Plumbing | 456 Repair Ave, Austin, TX 78701 | (512) 555-0123</p>
```

**Clean URLs:** Name your files logically — `about.html`, `services.html`, not `page2.html`

Do not promise keyword rankings — search-ready setup just means Google can find, read, and properly categorize the site. Combined with Google Business Profile (section 9) and schema markup (section 11), it's enough to start ranking for "[business type] near me" and "[business type] [city]" within a few weeks of launch.

---

## 7. ONLINE BOOKING LINK (add-on — $99)

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

**Other options:**
- Square Appointments (if they use Square for payments) — $99 add-on to integrate
- Acuity Scheduling — $99 add-on
- Just a phone number CTA if they prefer calls: "Call to Book: (512) 555-0123"

---

## 8. PHOTO GALLERY

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

## 9. GOOGLE BUSINESS PROFILE SETUP

**What it means:** Their listing on Google Maps and Google Search ("the box" that appears when you search a business name). This is the single highest-value SEO thing you can do for a local business.

**Setup steps:**
1. Go to [business.google.com](https://business.google.com)
2. Sign in with a Google account (ideally the client's, or create one for them)
3. Click "Add your business" → search for the business name
4. If it exists already: claim it (they'll verify by postcard, phone, or email)
5. If it doesn't exist: create it from scratch

**Fields to fill in completely:**
- Business name (exact legal name)
- Category (be specific — "Italian Restaurant" not just "Restaurant")
- Address
- Phone number
- Website URL (their new site)
- Hours of operation (every day, including "Closed")
- Business description (250 characters, include their city and main service)
- Upload 5–10 photos (exterior, interior, products/services, owner)

**Verification:** Google usually verifies by postcard (5–7 days) or instant video call. Give the client a heads-up — they need to be the one to do the final verify step.

**After setup:** Tell the client to ask their first 5 customers to leave a Google review. Reviews are everything.

---

## 10. KEYWORD-TARGETED SEO (light version included)

> The base package handles the search-ready foundation (section 6). The deeper keyword work below is what makes a site actually rank — do it for every build, but don't promise specific rankings.

**What it means:** Every page targets a specific phrase people search for in Google.

**How to find the right keyword:**
- Format: `[service] + [city]` — e.g. "emergency plumber Austin TX", "Italian restaurant Denver"
- Use [Google's free keyword planner](https://ads.google.com/home/tools/keyword-planner/) or just look at Google autocomplete
- Pick ONE primary keyword per page — don't stuff multiple

**Where to use the keyword:**
- Page `<title>` tag
- `<h1>` heading (exact or close match)
- Meta description
- First paragraph of body text
- One image alt tag
- URL slug if possible (e.g. `emergency-plumber-austin.html`)

**Example for a plumber:**
```html
<title>Emergency Plumber in Austin TX — Tucker Plumbing | 24/7 Service</title>
<h1>Austin's Trusted Emergency Plumber</h1>
<meta name="description" content="Need an emergency plumber in Austin TX? Tucker Plumbing offers same-day service, 24/7. Licensed and insured. Call (512) 555-0123.">
```

Do this for every page — each page targets a different keyword.

---

## 11. SCHEMA MARKUP / JSON-LD

**What it means:** Hidden code that tells Google exactly what kind of business this is, their hours, phone, address — improves how they appear in search results.

**Paste this in the `<head>` of every page, filled out for the client:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
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
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "$$"
}
</script>
```

**`@type` options for common businesses:**
- Plumber, Electrician, HVACBusiness → `"@type": "Plumber"` etc.
- Restaurant → `"@type": "Restaurant"`
- Hair salon → `"@type": "HairSalon"`
- General → `"@type": "LocalBusiness"`

Takes 5 minutes per site. Validate at [schema.org/validator](https://validator.schema.org) after.

---

## 12. FAQ SECTION (add-on — $99)

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

---

## 13. HOSTING ON VERCEL (Care Plan)

**What it means:** The site lives on Vercel's servers — fast global CDN, free SSL, zero cost to you.

**Setup steps (one-time per client site):**
1. Push the site files to a GitHub repo (one repo per client)
2. Go to [vercel.com](https://vercel.com) → New Project → Import from GitHub
3. Select the repo → Deploy (no config needed for plain HTML)
4. Vercel gives a free URL: `yoursite.vercel.app`
5. Add the client's custom domain: Settings → Domains → Add → follow DNS instructions
6. SSL is automatic — done

**Ongoing:** Any time you update files and push to GitHub, Vercel auto-deploys in ~30 seconds.

**Cost to you:** $0 (Vercel Hobby tier is free for unlimited static sites)

---

## 14. WEBSITE EDITS (Care Plan — included)

Every Care Plan client gets ongoing edits. Budget **~1 hour per month per client** for planning purposes; the package isn't marketed with an explicit hourly cap, but watch for clients who consistently exceed an hour.

**What counts as a normal edit:**
- Changing hours of operation
- Updating a phone number or address / service area
- Swapping in a new photo
- Adding or editing a service description
- Updating a menu item or price
- Adding a seasonal promotion banner
- Fixing a typo

**What does NOT count (quote separately):**
- Adding a new page (+$75)
- Redesigning a section
- New features (booking, e-commerce, etc.)
- Anything taking more than ~2 hours of work

**Process:**
- Give every Care Plan client your email and tell them to send update requests there
- Batch updates — do them once a week, not same-day (unless urgent)
- Log time in a simple spreadsheet so you can tell clients what you did at month 11

**If a client routinely burns through 1 hr/month:** At their 12-month renewal conversation, offer to upgrade them to a 2 hr/month plan at $129/month, or charge overage at $75/hr going forward.

---

## 15. CARE PLAN — 12-MONTH MINIMUM TERM

Every Care Plan signs the client up for a **mandatory 12-month minimum**. After that it goes month-to-month.

**Track for every client:**
- Launch date (= billing day each month)
- Month-12 anniversary date (= renewal-decision touchpoint)
- Total monthly hours used (for the upgrade conversation at month 11)

**Month 11 email (template):**
> "Hi [Name] — your initial Care Plan term wraps up next month. There's nothing you need to do: it'll keep running month-to-month at the same $79/month. Lots of clients stay because the edits + hosting + support add up faster than they expect. If you'd ever want to cancel after that, just give me 30 days' heads-up and I'll hand over your files. Otherwise, here's to year two!"

**If they ask to cancel during months 1–12:**
> "I totally get it. The 12-month term is fixed — that's what lets me keep the build at $599. The remaining [X] months are still due. Once the year is up, you're free to cancel or move hosting elsewhere with a 30-day heads-up. Want me to send you a summary of what you've used so far?"
