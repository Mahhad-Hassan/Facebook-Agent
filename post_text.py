import requests
from config import PAGE_ID, ACCESS_TOKEN

def post_text(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"

    data = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(url, data=data)
    print(response.json())