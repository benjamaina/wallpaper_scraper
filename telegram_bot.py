import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WALLPAPER_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "Wallpapers")
posted_log = os.path.join(WALLPAPER_DIR, "posted.txt")

MAX_PHOTO_SIZE = 10 * 1024 * 1024  # 10MB
MAX_DOC_SIZE = 50 * 1024 * 1024    # 50MB

def has_been_posted(filename):
    if not os.path.exists(posted_log):
        return False
    with open(posted_log, 'r') as f:
        return filename in f.read()

def mark_as_posted(filename):
    with open(posted_log, 'a') as f:
        f.write(f"{filename}\n")

def start_bot():
    wallpapers = [
        f for f in os.listdir(WALLPAPER_DIR)
        if f.endswith(('.jpg', '.png'))
    ]

    unposted = [f for f in wallpapers if not has_been_posted(f)]

    if not unposted:
        print("No unposted wallpapers left.")
        return

    wallpaper = random.choice(unposted)
    filepath = os.path.join(WALLPAPER_DIR, wallpaper)
    caption = f"📷 {os.path.splitext(wallpaper)[0]}"
    filesize = os.path.getsize(filepath)

    # Determine the right endpoint and file type
    if filesize <= MAX_PHOTO_SIZE:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        file_field = {'photo': open(filepath, 'rb')}
    elif filesize <= MAX_DOC_SIZE:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        file_field = {'document': open(filepath, 'rb')}
    else:
        print(f"❌ Skipped {wallpaper}: file too large ({filesize // (1024 * 1024)}MB)")
        return

    try:
        res = requests.post(
            url,
            data={'chat_id': CHAT_ID, 'caption': caption},
            files=file_field
        )

        if res.status_code == 200:
            print(f"✅ Wallpaper sent successfully: {wallpaper}")
            mark_as_posted(wallpaper)
        else:
            print(f"❌ Failed to send wallpaper: {res.text}")

    except Exception as e:
        print(f"⚠️ Error sending wallpaper: {e}")
    finally:
        file_field[list(file_field.keys())[0]].close()  # Ensure file is closed

if __name__ == '__main__':
    start_bot()
# This script is designed to run as a standalone Telegram bot that posts wallpapers.
# It checks for unposted wallpapers in a specified directory, sends one at random,