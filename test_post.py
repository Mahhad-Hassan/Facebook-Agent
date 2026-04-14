# import requests

# PAGE_ACCESS_TOKEN =  "EAAeYCZCR1884BRF8TX176oS8FgnPt3LzeUUttHfWqAo4toW61ZBFPPRV0cch9A4XYylxM6d5Ufn79hbAZAWuTaP0eBdM2XXQlunIrn69Nf9kaPvdcOfLfxAgTFui37jWqqR6UHF8yZBMsXK5NUp4oZAYWrW7CWl2zxA7JGsoLF1isQtsAZCvlV7bdmDbBmAfVLqsUGaR40E7wNiUlPmZASyzlRS6VNIcf1X3jJd8dIgn14ZD"
# PAGE_ID = "1089085580954214"


# # =========================
# # 📢 TEXT POST FUNCTION
# # =========================
# def post_text(message):
#     url = f"https://graph.facebook.com/{PAGE_ID}/feed"

#     payload = {
#         "message": message,
#         "access_token": PAGE_ACCESS_TOKEN
#     }

#     response = requests.post(url, data=payload)
#     print(response.json())


# # =========================
# # 📸 IMAGE POST FUNCTION
# # =========================
# def post_image(image_url, caption):
#     url = f"https://graph.facebook.com/{PAGE_ID}/photos"

#     payload = {
#         "url": image_url,
#         "caption": caption,
#         "access_token": PAGE_ACCESS_TOKEN
#     }

#     response = requests.post(url, data=payload)
#     print(response.json())


# # =========================
# # 🎥 VIDEO POST FUNCTION
# # =========================
# def post_video(video_url, description):
#     url = f"https://graph.facebook.com/{PAGE_ID}/videos"

#     payload = {
#         "file_url": video_url,
#         "description": description,
#         "access_token": PAGE_ACCESS_TOKEN
#     }

#     response = requests.post(url, data=payload)
#     print(response.json())


# # =========================
# # 🤖 USER INTERFACE
# # =========================
# def main():
#     print("\n🤖 Facebook AI Posting Agent")
#     print("1️⃣ Text Post")
#     print("2️⃣ Image Post")
#     print("3️⃣ Video Post")

#     choice = input("\n👉 Select option (1/2/3): ")

#     if choice == "1":
#         message = input("✍ Enter your post text: ")
#         post_text(message)

#     elif choice == "2":
#         image_url = input("🖼 Enter image URL: ")
#         caption = input("✍ Enter caption: ")
#         post_image(image_url, caption)

#     elif choice == "3":
#         video_url = input("🎥 Enter video URL: ")
#         description = input("✍ Enter description: ")
#         post_video(video_url, description)

#     else:
#         print("❌ Invalid option")


# # =========================
# # 🚀 RUN PROGRAM
# # =========================
# if __name__ == "__main__":
#     main()





from post_text import post_text
from post_image import smart_post_image
from post_video import smart_post_video


def main():
    print("\n🤖 Facebook AI Posting Agent")
    print("1️⃣ Text Post")
    print("2️⃣ Image Post (URL or File)")
    print("3️⃣ Video Post (URL or File)")
    print("4️⃣ Exit")

    choice = input("\n👉 Select option (1/2/3/4): ")

    if choice == "1":
        msg = input("✍ Enter text: ")
        post_text(msg)

    elif choice == "2":
        img = input("🖼 Enter image URL or file path: ")
        cap = input("✍ Enter caption: ")
        smart_post_image(img, cap)

    elif choice == "3":
        vid = input("🎥 Enter video URL or file path: ")
        desc = input("✍ Enter description: ")
        smart_post_video(vid, desc)

    elif choice == "4":
        print("👋 Exiting...")

    else:
        print("❌ Invalid option")


if __name__ == "__main__":
    main()