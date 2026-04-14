import os
from pathlib import Path
from dotenv import load_dotenv

# ALWAYS correct path (no matter where you run from)
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

PAGE_ID = os.getenv("PAGE_ID")
ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")  # ← changed this line

print("DEBUG ENV PATH:", ENV_PATH)
print("DEBUG PAGE_ID:", PAGE_ID)
print("DEBUG TOKEN:", ACCESS_TOKEN[:20] if ACCESS_TOKEN else None)

if not PAGE_ID or not ACCESS_TOKEN:
    raise Exception("❌ .env NOT LOADED PROPERLY")