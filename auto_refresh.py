# from token_manager import get_long_lived_token
# from pathlib import Path

# ENV_PATH = Path(".env")

# def refresh_and_update():
#     new_token = get_long_lived_token()

#     if not new_token:
#         print("❌ Failed to refresh token")
#         return

#     print("✅ New Long-Lived Token Generated")

#     # Read existing .env
#     if ENV_PATH.exists():
#         lines = ENV_PATH.read_text().splitlines()
#     else:
#         lines = []

#     # Rewrite without old ACCESS_TOKEN
#     new_lines = []
#     for line in lines:
#         if not line.startswith("ACCESS_TOKEN="):
#             new_lines.append(line)

#     # Add new token
#     new_lines.append(f"ACCESS_TOKEN={new_token}")

#     # Save clean .env
#     ENV_PATH.write_text("\n".join(new_lines))

#     print("💾 Token updated successfully in .env")


# if __name__ == "__main__":
#     refresh_and_update()



from token_manager import get_long_lived_token
from pathlib import Path
import schedule
import time

ENV_PATH = Path(".env")


def refresh_and_update():
    new_token = get_long_lived_token()

    if not new_token:
        print("❌ Failed to refresh token")
        return

    print("✅ New Long-Lived Token Generated")

    # Read existing .env
    if ENV_PATH.exists():
        lines = ENV_PATH.read_text().splitlines()
    else:
        lines = []

    # Remove old ACCESS_TOKEN
    new_lines = []
    for line in lines:
        if not line.startswith("ACCESS_TOKEN="):
            new_lines.append(line)

    # Add new token
    new_lines.append(f"ACCESS_TOKEN={new_token}")

    # Save updated .env
    ENV_PATH.write_text("\n".join(new_lines))

    print("💾 Token updated successfully in .env")


# 🔥 Scheduler function
def job():
    print("🔄 Running scheduled token refresh...")
    refresh_and_update()


# ⏰ Schedule: every 1 hour (you can change it)
schedule.every(20).seconds.do(job)


if __name__ == "__main__":
    print("🚀 Token Scheduler Started...")

    # run once immediately (optional but recommended)
    refresh_and_update()

    # keep running forever
    while True:
        schedule.run_pending()
        time.sleep(1)