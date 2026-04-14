import requests
from config import PAGE_ID, ACCESS_TOKEN


# =========================
# 🎥 VIDEO FROM URL (POST)
# =========================
def post_video(video_url, description):
    url = f"https://graph.facebook.com/{PAGE_ID}/videos"

    payload = {
        "file_url": video_url,
        "description": description,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(url, data=payload)
    print(response.json())


# =========================
# 🎥 VIDEO FROM FILE (UPLOAD)
# =========================
def upload_video(file_path, description):
    url = f"https://graph.facebook.com/{PAGE_ID}/videos"

    with open(file_path, 'rb') as video_file:
        files = {
            'source': video_file
        }

        data = {
            "description": description,
            "access_token": ACCESS_TOKEN
        }

        response = requests.post(url, files=files, data=data)
        print(response.json())


# =========================
# ⚡ SMART AUTO FUNCTION (BEST)
# =========================
def smart_post_video(input_value, description):
    """
    If input is URL → post_video
    If input is file path → upload_video
    """

    if input_value.startswith("http"):
        return post_video(input_value, description)
    else:
        return upload_video(input_value, description)