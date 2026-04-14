import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
SHORT_LIVED_TOKEN = os.getenv("SHORT_LIVED_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")  # Add this to your .env


# =========================
# 🔁 STEP 1: GET LONG LIVED TOKEN (60 days)
# =========================
def get_long_lived_token():
    url = "https://graph.facebook.com/v18.0/oauth/access_token"

    params = {
        "grant_type": "fb_exchange_token",
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "fb_exchange_token": SHORT_LIVED_TOKEN
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("🔁 Long-Lived Token Response:", data)

    if "access_token" in data:
        return data["access_token"]
    return None


# =========================
# ♾️ STEP 2: GET NEVER-EXPIRING PAGE TOKEN
# =========================
def get_permanent_page_token(long_lived_token):
    url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"

    params = {
        "fields": "access_token",
        "access_token": long_lived_token
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("♾️ Permanent Page Token Response:", data)

    if "access_token" in data:
        return data["access_token"]
    return None


# =========================
# 🚀 MAIN: RUN ONCE, SAVE FOREVER
# =========================
if __name__ == "__main__":
    print("⏳ Step 1: Getting long-lived token...")
    long_lived = get_long_lived_token()

    if long_lived:
        print("✅ Long-lived token obtained!")
        print("\n⏳ Step 2: Getting permanent page token...")
        permanent = get_permanent_page_token(long_lived)

        if permanent:
            print("\n✅ SUCCESS! Your permanent token:")
            print(permanent)
            print("\n💾 Save this in your .env as PAGE_ACCESS_TOKEN=...")
        else:
            print("❌ Failed to get page token.")
    else:
        print("❌ Failed to get long-lived token.")