import requests
from config import PAGE_ID, ACCESS_TOKEN


# =========================
# 🌐 IMAGE FROM URL
# =========================
def post_image(image_url, caption):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(url, data=payload)
    print(response.json())


# =========================
# 📁 IMAGE FROM LOCAL FILE
# =========================
def upload_image(file_path, caption):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    with open(file_path, 'rb') as image_file:
        files = {
            'source': image_file
        }

        data = {
            "caption": caption,
            "access_token": ACCESS_TOKEN
        }

        response = requests.post(url, files=files, data=data)
        print(response.json())


# =========================
# ⚡ SMART AUTO IMAGE FUNCTION
# =========================
def smart_post_image(input_value, caption):
    """
    Auto detects:
    - URL → post_image
    - File path → upload_image
    """

    if input_value.startswith("http"):
        return post_image(input_value, caption)
    else:
        return upload_image(input_value, caption)