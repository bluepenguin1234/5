# Frontpage Studio — Build Guide

How to deliver every part of the package and the ongoing Care Plan. For sales, scripts, emails, and process flow, see `OPERATIONS.md`. For pricing facts, see `CLAUDE.md`.

> **Package = 3 pages:** Home, Services, Contact. Extra pages $75 each.
> **Add-ons (each $75):** FAQ section · extra page · extra revision round.
> **Care Plan ($79/mo, 12-mo minimum):** hosting, security updates, website edits, backup/maintenance, support.

Start every build from the closest demo in `demos/`. Most of what's below is a brief reference, not a tutorial — the real source code for each pattern is already in the three demos.

---

# Part A — Package Deliverables

## 1. 3-Page Website

| Page | Sections |
|---|---|
| Home | Hero + CTA, services overview, reviews, photo gallery, hours + service area, email signup, contact CTA |
| Services | Each service: name, short description, starting price (optional), click-to-call |
| Contact | Phone (click-to-call), email, address, hours, service area, Google Maps embed, contact form |

Each page is a separate `.html` file (`index.html`, `services.html`, `contact.html`). Keep the nav and footer identical across all three. Footer carries phone + address + social links + privacy/terms.

**Time:** 3–5 hours per build after the first 2–3.

## 2. Mobile-Friendly Design

Required: `<meta name="viewport" content="width=device-width, initial-scale=1.0">` in every `<head>`. Use flexbox/grid for all layouts. One breakpoint at `max-width: 768px` minimum. Test in Chrome DevTools at 375px (iPhone) and 768px (iPad). Body text ≥14px. Tap targets ≥44px tall.

## 3. Contact Form + Click-to-Call

**Contact form (Formspree):**
1. formspree.io → new form per client
2. Copy endpoint URL: `https://formspree.io/f/xxxxx`
3. `<form action="..." method="POST">` with name / email / phone / message fields
4. Add `<input type="hidden" name="_next" value="https://[client-site]/thanks.html">` for the redirect
5. Test by submitting

Free tier: 50 submissions/month per form. Plenty for a local business.

**Click-to-call:** wrap the phone number in a `tel:` link (`<a href="tel:+15125550123">`). Sticky button on Services page (mobile bottom-right). Inline next to each service. Footer everywhere. Phone calls convert ~10x better than forms for local services.

## 4. Reviews / Testimonials

Get 3–6 from client (or permission to pull from their Google Business Profile). Each: 1–3 sentences, first name + last initial + city.

Use the card-grid pattern from the demos. If client has zero reviews, ask them to text 5 recent customers — 3 will reply within a day. Soft-launch without if needed; add post-launch.

For schema markup (Section 11), only include `aggregateRating` if the numbers are real from their GBP.

## 5. Photo Gallery

Get 10–20 photos from client (or pull from their Google Maps listing with permission). Resize to max 1200px wide (squoosh.app or tinypng.com). CSS grid:

```css
grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
```

Photo aspect 4/3, `object-fit: cover`, border-radius 12px. If client has no photos: pull from Google Maps, use Unsplash for the business type, or ask for 10 quick phone photos.

## 6. Business Hours + Service Area

**Hours:** display top of Contact page (large), footer (compact), and inside LocalBusiness schema. Use `<dl class="hours">` with `<dt>day</dt><dd>time</dd>`. If client is 24/7 (plumbers, locksmiths), put "OPEN 24/7" in the hero on every page — massive trust signal.

**Service area:** inline paragraph on Home + Contact ("Proudly serving Austin, Round Rock, Cedar Park"), bullet list on Services page, and `areaServed` in schema. Google uses `areaServed` to decide which "near me" searches show your client.

## 7. Google Maps Embed (Contact page)

maps.google.com → search address → Share → Embed → copy the `<iframe>`. Wrap in a `div` with `border-radius` and `overflow: hidden` to match card style.

If the business isn't on Maps yet, embed an address search instead:
```
<iframe src="https://maps.google.com/maps?q=123+Main+St+Austin+TX&output=embed" ...>
```

## 8. Email Signup Form

Easiest: a second Formspree form per client (named "[Business] Email List"). Single-field email-only — never ask for name on a homepage signup, email-only converts 3x better.

Better if client already uses Mailchimp/Brevo/ConvertKit: use their embed snippet so they get a real list with unsubscribe handling.

Placement: footer (always) + one inline on Home (after gallery or reviews).

## 9. Google Business Profile Setup & Optimization

The single highest-value local-SEO move. Walk through it WITH the client (their Google account, not yours).

1. business.google.com → sign in → Add your business
2. Claim existing or create from scratch
3. Fill **completely:** legal name, specific category (e.g. "Italian Restaurant" not "Restaurant"), 2–3 secondary categories, address (or hide if service-area-only), service area matching Section 6, phone matching the site exactly (NAP consistency matters), website URL, hours (every day including "Closed"), 750-char description with city + main service, 10+ photos.
4. Verification by postcard (5–7 days) or instant video call. Client does this step.
5. After setup: tell client to ask their next 5 customers for reviews. Reviews are everything.

## 10. Search-Ready Setup

Foundation that lets Google find and categorize the site.

- **Title tags** — unique per page, 50–60 chars: `<title>Tucker Plumbing — Emergency Plumber in Austin, TX</title>`
- **Meta description** — every page, 120–160 chars
- **Heading hierarchy** — one `<h1>` per page (contains business type + city), `<h2>` for sections, never skip levels
- **Image alt text** — descriptive, not "image1.jpg"
- **Consistent NAP** — Name, Address, Phone identical across the site, GBP, and any directory listings. Google checks. Inconsistency hurts ranking.
- **Clean URLs** — `services.html` not `page2.html`
- **One keyword per page** in title, h1, meta description, first paragraph. Format: `[service] + [city]` (e.g. "emergency plumber Austin TX").

Don't promise rankings. Promise that Google can find and read the site.

## 11. Local Schema Markup (JSON-LD)

Paste in every page's `<head>`, filled out for the client:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "name": "Tucker Plumbing",
  "telephone": "+15125550123",
  "url": "https://tuckerplumbing.com",
  "address": { "@type": "PostalAddress", "streetAddress": "...", "addressLocality": "Austin", "addressRegion": "TX", "postalCode": "78701" },
  "areaServed": [{ "@type": "City", "name": "Austin" }],
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "$$"
}
</script>
```

`@type` for common businesses: `Plumber` / `Electrician` / `HVACBusiness` / `Restaurant` / `HairSalon` / generic `LocalBusiness`. Validate at validator.schema.org.

**Only include `aggregateRating`** if you have real numbers from the client's GBP. Faking them gets the listing flagged.

## 12. Social Media Links (Footer)

Icons in the footer linking to client's Facebook / Instagram / Yelp / Google Business listing. Use SVG icons or heroicons.com. Always `target="_blank" rel="noopener"`. If client has no social, skip — don't ship dead links.

---

# Part B — Add-ons ($75 each)

## 13. FAQ Section

Accordion-style, 6–8 questions. Ask client for their most common, or use defaults by business type. Add FAQPage schema markup so Google can show the questions in search results.

## 14. Extra Page

Standard structure inheriting nav, footer, and design system. Quote $75 per additional page on top of the base 3.

---

# Part C — Care Plan Delivery

$79/month, mandatory 12-month minimum.

## 15. Hosting (Vercel)

Push site to a GitHub repo per client → vercel.com → Import from GitHub → Deploy (no config for plain HTML) → add custom domain in Settings → SSL automatic. Vercel auto-deploys on every push. Cost to you: $0.

## 16. Security Updates

**Monthly security check (1st of every month):**
1. Each client site in incognito → confirm green padlock
2. Vercel dashboard → no failed deploys
3. Formspree submissions for a spot-check on spam patterns
4. GitHub Dependabot alerts (if any repos use packages)

If something breaks, same-day fix.

**Keep 2FA on Vercel, GitHub, and Stripe.** You're the gatekeeper for every client site.

## 17. Website Edits

Budget ~1 hr/month per client. Email is the channel.

**Normal edits:** hours, phone/address, photo swaps, service descriptions, prices, seasonal banners, typos, new testimonials.

**Out of scope (quote separately):** new pages (+$75), redesigns, new features, anything taking 2+ hours.

Batch updates weekly, not same-day (unless urgent). Log time in your Care Plan Clients sheet tab.

If a client routinely exceeds 1 hr/month: email a usage summary, offer overage at $75/hr or 2-hr plan at $129/month.

## 18. Backup / Maintenance

**Backups (automatic):** each client site lives in its own GitHub repo. Every change is a commit. To roll back: `git revert <commit>` or one-click rollback in Vercel. GitHub IS the backup.

**Quarterly maintenance (every 3 months per client):**
1. Lighthouse audit — keep all four scores ≥85
2. Verify external links (Maps embed, social, anything embedded)
3. Test contact form delivers (send yourself a submission)
4. Domain expiry check — if within 6 months, schedule renewal reminder for client

**Domain renewals:** add every client's expiry date to your calendar. Email at 60 days and 30 days before. Losing a domain is catastrophic — the client will blame you regardless of whose name is on the registrar.

## 19. Support

Email at the address you give clients at launch. Same-day weekday response before 4pm local. Next-day for evenings/weekends. Phone/text within 2 hours for actual site-down emergencies (rare).

**Boundaries up front:**
- Email/text only, no scheduled calls unless the site is actually down
- No blog/social/copy writing — that's marketing, not maintenance
- No paid ads, no reviews management — separate engagements, not something Frontpage Studio offers

## 20. Care Plan — 12-Month Minimum Term

**Track per client:** launch date, month-12 anniversary, monthly hours used, last edit date, domain renewal date.

**Month-11 email (continuous hosting confirmation):**
> "Hi [Name] — quick heads-up: your initial 12-month Care Plan wraps up next month, and hosting continues uninterrupted at the same $79/month going forward. Nothing you need to do. After this point you can cancel any time with 30 days' notice. Thanks for being a great client this year."

**If they ask to cancel during months 1–12:**
> "I get it. The 12-month term is fixed — that's what lets me keep the build at $599. The remaining [X] months are still due. After year one you can cancel anytime with 30 days' notice."

**At month 12 if they cancel:** hand over the GitHub repo + a zip of the latest files within 24 hours. Disable auto-billing. They often come back within 6 months.
