"""
Frontpage Studio — Lead Finder
Finds local businesses with NO website using Google Places API.
Output: CSV file with business name, phone, address, Maps link.

Setup:
  1. Get a free Google Places API key at: https://console.cloud.google.com
     (Enable "Places API (New)" — 10,000 free calls/month)
  2. pip install -r requirements.txt
  3. Run: python find_leads.py

Or set key via env var:
  Windows PowerShell: $env:GOOGLE_PLACES_API_KEY = "your-key"
  Then: python find_leads.py
"""

import requests
import csv
import time
import os
import sys
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    BOLD = Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = YELLOW = CYAN = BOLD = RESET = ""

PLACES_URL = "https://places.googleapis.com/v1/places:searchText"

FIELD_MASK = (
    "places.id,"
    "places.displayName,"
    "places.formattedAddress,"
    "places.nationalPhoneNumber,"
    "places.websiteUri,"
    "places.rating,"
    "places.userRatingCount,"
    "places.businessStatus,"
    "places.regularOpeningHours"
)

BUSINESS_TYPES = [
    "restaurant",
    "plumber",
    "hair salon",
    "barbershop",
    "electrician",
    "HVAC",
    "auto repair",
    "landscaper",
    "cleaning service",
    "dentist",
    "chiropractor",
    "florist",
    "nail salon",
    "law office",
    "accountant",
    "pest control",
    "roofing contractor",
    "painter",
    "carpet cleaning",
    "massage therapy",
]


def get_api_key():
    key = os.environ.get("GOOGLE_PLACES_API_KEY", "").strip()
    if not key:
        print(f"\n{RED}ERROR: Google Places API key not found.{RESET}")
        print("Get a free key at: https://console.cloud.google.com")
        print('Enable "Places API (New)" then create an API key under Credentials.')
        print(f"\nSet it with: {CYAN}$env:GOOGLE_PLACES_API_KEY = \"your-key-here\"{RESET}")
        print("Then re-run this script.\n")
        sys.exit(1)
    return key


def search_businesses(query: str, api_key: str, page_token: str = None) -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": FIELD_MASK,
    }
    body = {
        "textQuery": query,
        "maxResultCount": 20,
        "languageCode": "en",
    }
    if page_token:
        body["pageToken"] = page_token

    try:
        resp = requests.post(PLACES_URL, json=body, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 400:
            print(f"{RED}API Error 400: {resp.text}{RESET}")
            print("Check your API key and that 'Places API (New)' is enabled.")
        elif resp.status_code == 403:
            print(f"{RED}API Error 403: Permission denied.{RESET}")
            print("Make sure 'Places API (New)' is enabled in your Google Cloud project.")
        else:
            print(f"{RED}HTTP Error: {e}{RESET}")
        return {}
    except requests.exceptions.Timeout:
        print(f"{YELLOW}Request timed out — retrying...{RESET}")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"{RED}Request error: {e}{RESET}")
        return {}


def extract_lead(place: dict) -> dict | None:
    """Return lead dict if business has no website, else None."""
    if place.get("businessStatus") not in ("OPERATIONAL", None, ""):
        return None

    website = place.get("websiteUri", "").strip()
    if website:
        return None  # Has a website — not a lead

    name = place.get("displayName", {}).get("text", "Unknown")
    phone = place.get("nationalPhoneNumber", "")
    address = place.get("formattedAddress", "")
    rating = place.get("rating", "")
    review_count = place.get("userRatingCount", "")
    place_id = place.get("id", "")

    # Build Google Maps link from place ID
    maps_link = f"https://www.google.com/maps/place/?q=place_id:{place_id}" if place_id else ""

    # Check if they have phone (higher priority lead)
    priority = "HIGH" if phone else "LOW"

    return {
        "Priority": priority,
        "Business Name": name,
        "Phone": phone,
        "Address": address,
        "Rating": rating,
        "Review Count": review_count,
        "Google Maps": maps_link,
        "Website": "NONE",
        "Status": "New Lead",
        "Date Found": datetime.now().strftime("%Y-%m-%d"),
        "Notes": "",
    }


def find_leads(business_type: str, city: str, state: str, max_results: int = 80) -> list:
    api_key = get_api_key()
    leads = []
    seen_names = set()
    page_token = None
    query = f"{business_type} in {city}, {state}"

    print(f"\n{CYAN}Searching: \"{query}\"{RESET}")

    page = 0
    while len(leads) < max_results:
        page += 1
        data = search_businesses(query, api_key, page_token)

        if not data:
            break

        places = data.get("places", [])
        if not places:
            break

        for place in places:
            lead = extract_lead(place)
            if lead is None:
                continue
            name = lead["Business Name"]
            if name in seen_names:
                continue
            seen_names.add(name)
            leads.append(lead)
            phone_display = lead["Phone"] if lead["Phone"] else "no phone listed"
            print(f"  {GREEN}✓{RESET} {name} — {phone_display}")

        page_token = data.get("nextPageToken")
        if not page_token:
            break

        print(f"  {YELLOW}Loading next page...{RESET}")
        time.sleep(2)  # Respect rate limits

    return leads


def save_leads(leads: list, filename: str):
    if not leads:
        print(f"\n{YELLOW}No leads found for this search.{RESET}")
        print("Try a different city, or a broader business type.")
        return

    fieldnames = list(leads[0].keys())
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # Sort: HIGH priority (has phone) first, then by rating desc
        sorted_leads = sorted(
            leads,
            key=lambda x: (0 if x["Priority"] == "HIGH" else 1, -(float(x["Rating"]) if x["Rating"] else 0))
        )
        writer.writerows(sorted_leads)

    print(f"\n{GREEN}{BOLD}✅ Saved {len(leads)} leads → {filename}{RESET}")

    high = sum(1 for l in leads if l["Priority"] == "HIGH")
    low = len(leads) - high
    print(f"   {GREEN}High priority (has phone): {high}{RESET}")
    print(f"   {YELLOW}Low priority (no phone listed): {low}{RESET}")
    print(f"\n{CYAN}Open {filename} in Excel or Google Sheets to start calling!{RESET}")
    print(f"Tip: Sort by 'Priority' then 'Rating' — highest rated + no website = best lead.\n")


def print_banner():
    print(f"\n{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}{CYAN}   Frontpage Studio — Lead Finder{RESET}")
    print(f"{BOLD}{CYAN}   Find businesses with no website in your city{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}\n")


def prompt_business_type() -> str:
    print("Common business types:")
    for i, bt in enumerate(BUSINESS_TYPES, 1):
        print(f"  {i:2}. {bt}")
    print()
    choice = input("Enter a business type (or number from list above): ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(BUSINESS_TYPES):
            return BUSINESS_TYPES[idx]

    return choice


def main():
    print_banner()

    business_type = prompt_business_type()
    if not business_type:
        print("Business type is required.")
        sys.exit(1)

    city = input("City: ").strip()
    if not city:
        print("City is required.")
        sys.exit(1)

    state = input("State (e.g., OH, TX, FL, NY): ").strip()
    if not state:
        print("State is required.")
        sys.exit(1)

    max_results_str = input("Max leads to find (default 50): ").strip()
    max_results = int(max_results_str) if max_results_str.isdigit() else 50

    print(f"\n{YELLOW}Starting search... this may take 30–60 seconds.{RESET}")
    print("Businesses WITHOUT a website will appear as leads.\n")

    leads = find_leads(business_type, city, state, max_results)

    # Generate filename
    clean_type = business_type.replace(" ", "_").lower()
    clean_city = city.replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"leads_{clean_type}_{clean_city}_{timestamp}.csv"

    save_leads(leads, filename)


if __name__ == "__main__":
    main()
