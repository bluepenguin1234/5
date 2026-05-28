# Frontpage Studio — Launch Guide
### Everything you need to start landing clients. Follow in order.

---

## COMPANY OVERVIEW

**Name:** Frontpage Studio  
**Tagline:** "We build websites for businesses that deserve to be found."  
**What you do:** Cold-call local businesses that have NO website. Build them one in 7 days. Charge a flat rate.  
**Domain to register:** `frontpagestudio.com` (check availability) or `frontpage.studio`  
**Company email:** `brian@frontpagestudio.com` (via Zoho — free)

---

## PHASE 1 — Brand Setup (2–3 hours)

### Step 1: Register Your Domain (~$12/yr)
1. Go to **namecheap.com** or **cloudflare.com/registrar** (Cloudflare is at-cost, cheapest option)
2. Search: `frontpagestudio.com`
3. If taken, try: `frontpage.studio` | `frontpagweb.com` | `myfrontpagestudio.com`
4. Buy it. ~$10–$15/year.

### Step 2: Set Up Free Company Email (Zoho Mail)
1. Go to **zoho.com/mail** → click "Get Started for Free" → choose "Forever Free Plan"
2. Enter your domain when prompted
3. Verify ownership by adding a TXT DNS record in Namecheap (Zoho walks you through this)
4. Create inbox: `brian@frontpagestudio.com`
5. Download Zoho Mail app on your phone
6. **Test it:** Send yourself an email from Gmail → confirm it arrives

### Step 3: GitHub Account
1. Go to **github.com** → Sign Up (free)
2. Create a new repository called `frontpagestudio`
3. Upload the contents of `C:\Users\Brian\Desktop\web\` (drag and drop files in browser)
4. ✅ Your code is now in the cloud and ready to deploy

---

## PHASE 2 — Deploy Your Agency Website (1 hour)

Your agency website is at `C:\Users\Brian\Desktop\web\index.html`

### Step 4: Deploy to Vercel (Free)
1. Go to **vercel.com** → Sign Up with GitHub
2. Click "Add New Project"
3. Import your `frontpagestudio` GitHub repo
4. Leave all settings default → click **Deploy**
5. Vercel gives you a free URL like `frontpagestudio.vercel.app` — this works immediately!
6. To add your custom domain:
   - In Vercel: Project Settings → Domains → Add `frontpagestudio.com`
   - In Namecheap: Manage DNS → Add the CNAME records Vercel gives you
   - Takes 10–30 minutes to go live

### Step 5: Set Up Your Contact Form
Your contact form is already wired to Formspree. Activate it:
1. Go to **formspree.io** → Sign Up free
2. Click "New Form" → name it "Frontpage Studio Contact"
3. Copy your form endpoint (looks like `https://formspree.io/f/XXXXXXXX`)
4. Open `C:\Users\Brian\Desktop\web\index.html` → find `action="https://formspree.io/f/YOUR_FORM_ID"` → replace `YOUR_FORM_ID` with your actual ID
5. Redeploy to Vercel (just push to GitHub again)
6. **Test it:** Fill out and submit the form — you should get an email

---

## PHASE 3 — Set Up Lead Generation (1 hour)

### Step 6: Get a Google Places API Key (Free — 10,000 calls/month free)
1. Go to **console.cloud.google.com**
2. Create a new project (name it "Frontpage Studio Leads")
3. Enable: **Places API (New)**
4. Go to Credentials → Create Credentials → API Key
5. Copy your API key

### Step 7: Run the Lead Scraper
1. Install Python if needed: **python.org/downloads**
2. Open PowerShell, navigate to the scraper folder:
   ```
   cd C:\Users\Brian\Desktop\web\scraper
   pip install -r requirements.txt
   ```
3. Set your API key:
   ```
   $env:GOOGLE_PLACES_API_KEY = "your-key-here"
   ```
4. Run the scraper:
   ```
   python find_leads.py
   ```
5. Enter: business type (e.g., `plumber`), city, state
6. A CSV file opens — those are your leads (businesses with NO website)

### Step 8: Open Your Leads CSV
Open in Excel or Google Sheets. You'll see:
- Business name
- Phone number
- Address
- Google Maps link

Sort by rating (higher rated = more to lose by not having a website). Start calling.

---

## PHASE 4 — Start Calling (Day 2+)

### Step 9: Cold Call Setup
- Open `sop/cold-call-script.md` — your word-for-word script
- Set a daily goal: **20 calls = ~1–2 new clients/week** (industry average for cold outreach)
- Track calls in a spreadsheet: Business Name | Date Called | Outcome | Follow-up Date
- Best times to call: **Tuesday–Thursday, 9–11am and 2–4pm**

### Step 10: When Someone Says "Yes"
1. Book a 20-min discovery call (use **cal.com** — free scheduling link)
2. Send your proposal: open `templates/proposal.html` in browser → print to PDF → email it
3. Collect 50% deposit upfront (use **Venmo**, **PayPal**, or **Stripe**)
4. Build the site using the demo templates + `/frontend-design` skill in Claude Code
5. Send for review → revisions → launch
6. Collect remaining 50%

---

## PHASE 5 — Operations Ongoing

### Daily Routine
| Time | Task |
|------|------|
| 9:00am | Run scraper for new leads |
| 9:30–11am | Cold calls (20 calls) |
| 11am–noon | Follow-up emails |
| Afternoon | Build work for active clients |

### Weekly Review (every Friday)
- Calls made this week
- New leads acquired
- Active proposals outstanding
- Revenue collected
- Sites deployed

---

## PRICING REFERENCE (Quick View)
| Item | Price | Notes |
|------|-------|-------|
| Business Presence Package | $599 one-time | 7-day delivery |
| Ongoing Care Plan | $79/month | **Mandatory 12-month minimum** ($948/yr) |
| **First-year total per client** | **$1,547** | $599 build + $948 care plan |

**Always collect 50% of the build upfront.** No exceptions.  
**First month of the Care Plan ($79) is collected at launch alongside the final 50%.**  
The remaining 11 months of the Care Plan are billed monthly on the launch-day date.

---

## PAYMENT SETUP
Before your first client call, have ONE of these ready to accept payment:
- **Venmo** (easiest, personal) — @yourname
- **PayPal** business account — paypal.com/us/business
- **Stripe** (most professional) — stripe.com → create account → share payment link

---

## ❌ THINGS I (CLAUDE) COULD NOT DO FOR YOU

These require your accounts, payment, or authentication:

1. **Register your domain** — needs your payment at Namecheap/Cloudflare
2. **Set up Zoho Mail** — needs you to verify domain ownership
3. **Create GitHub account** — needs your login
4. **Create Vercel account** — needs your GitHub auth
5. **Get Google Places API key** — needs your Google account
6. **Activate Formspree** — needs your email
7. **Set up Stripe/PayPal/Venmo** — needs your identity verification
8. **Create a Cal.com scheduling link** — needs your signup
9. **Set up Google Business Profile** — needs your location verification by postcard
10. **Purchase Google Workspace / Microsoft 365 email** — if you prefer paid email
11. **Register an LLC** — see legalzoom.com or your state's SOS website (~$50–$150)
12. **Take actual payment from clients** — you need a live payment account

---

## QUICK LINKS REFERENCE
| Service | URL | Cost |
|---------|-----|------|
| Domain | namecheap.com | ~$12/yr |
| Email | zoho.com/mail | Free |
| Code hosting | github.com | Free |
| Web hosting | vercel.com | Free |
| Contact forms | formspree.io | Free |
| Scheduling | cal.com | Free |
| Lead scraper | Google Cloud Console | Free tier |
| Payments | stripe.com | 2.9% + $0.30/transaction |

---

*Built by Claude Code — Frontpage Studio Launch Kit*
