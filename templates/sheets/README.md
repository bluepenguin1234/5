# Command-Center Google Sheet — Setup

This folder contains the import-ready CSVs for the four tabs of the Frontpage Studio command-center Google Sheet. Total setup time: about 5 minutes.

Claude can't create the Google Sheet directly in your Drive (needs your account auth). What's here is the structure — you import each CSV as a tab and you're done.

---

## One-time setup (5 minutes)

### 1. Create the sheet
1. Go to **sheets.google.com** → click the blank `+` to create a new sheet
2. Name it **`Frontpage Studio — Command Center`**
3. Bookmark the URL. This is what you open every morning.

### 2. Create the four tabs by importing each CSV

For each of the four CSV files in this folder, repeat this:

1. Add a new sheet tab at the bottom (`+` icon) and rename it (or rename the default `Sheet1` for the first one)
2. **File → Import → Upload** → drop the CSV file
3. **Import location: "Replace current sheet"**
4. **Separator type: "Detect automatically"**
5. Click **Import data**

Tab names (in order):

| Tab name | Import this CSV |
|---|---|
| **Leads** | `leads.csv` |
| **Active Builds** | `active-builds.csv` |
| **Care Plan Clients** | `care-plan-clients.csv` |
| **Revenue** | `revenue.csv` |

Each CSV ships with one example row so the columns are obvious. Delete the example row once you've replaced it with real data.

### 3. Add dropdowns for status columns

This is what makes the sheet useful. Pick a column → **Data → Data validation** → **Add rule** → **Criteria: Dropdown** → enter the values below.

**Leads tab, "Status" column:**
- `new`
- `called`
- `VM`
- `emailed`
- `interested`
- `proposal sent`
- `closed`
- `dead`

**Active Builds tab, "Content Received" column:**
- `Y`
- `N`

**Care Plan Clients tab, "Care Plan Status" column:**
- `Active`
- `Cancelled — Notice Given`
- `Cancelled — Month-to-Month Ended`

### 4. Add useful formulas

**Care Plan Clients tab** — auto-fill the reminder and renewal dates from the launch date.

In the **Month 11 Reminder** column (column C), paste this formula in row 2 and copy down:
```
=IF(B2="","",EDATE(B2,11))
```

In the **Month 12 Renewal** column (column D):
```
=IF(B2="","",EDATE(B2,12))
```

In the **Domain Renewal Date** column (column G):
```
=IF(B2="","",EDATE(B2,12))
```

Now whenever you add a new client's launch date in column B, the three downstream dates auto-calculate.

**Revenue tab** — auto-calculate Total and Net.

In the **Total Collected** column (column F), paste in row 2 and copy down:
```
=B2+C2+D2+E2
```

In the **Net** column (column H):
```
=F2-G2
```

### 5. Set up conditional formatting (optional but recommended)

**Leads tab, "Next Action Date" column** — highlight rows where the next action is today or overdue.

- Select column H (Next Action Date)
- **Format → Conditional formatting**
- **Custom formula:** `=AND($H2<>"",$H2<=TODAY())`
- Background color: red

That makes your morning workflow trivial: open the sheet, see what's red, do those things first.

---

## What each tab is for

**Leads** — your call list and follow-up tracker. The scraper writes new rows here (after you wire that up). You update the Status as you work each lead.

**Active Builds** — clients between paid deposit and live launch. One row per active build. Drop the row when the site goes live (it graduates to Care Plan Clients).

**Care Plan Clients** — every client whose site is live and on the Care Plan. This is where the recurring revenue tracking lives.

**Revenue** — monthly totals for visibility and taxes. One row per month.

---

## When the scraper exists

Currently the scraper (`scraper/find_leads.py`) writes to a local CSV. Once Brian sets up the Google Sheet, Claude can extend the scraper to either:

- Append directly to the **Leads** tab via the Google Sheets API (cleaner, requires OAuth setup)
- Or keep writing to a local CSV that Brian copy-pastes into the **Leads** tab (simpler, takes 10 seconds per run)

Start with the manual copy-paste approach. If it gets annoying after a week, wire up the API.
