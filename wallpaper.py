import requests
import os
import re
import time
import random
from datetime import datetime

# Folder to save wallpapers
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Wallpapers")
os.makedirs(desktop_path, exist_ok=True)

def sanitize_filename(title):
    return re.sub(r'[\/:*?"<>|]', '_', title)

def scrap_for_wallpaper():
    url = 'https://www.reddit.com/r/wallpapers/top/.json?sort=top&t=month&limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{datetime.now()}] Failed to fetch data: {e}")
        return

    data = response.json()

    for post in data['data']['children']:
        title = sanitize_filename(post['data']['title'])
        img_url = post['data']['url']

        if img_url.endswith(('.jpg', '.png')):
            download_wallpaper(img_url, title)

            # Sleep 2–5 minutes between each download to avoid blocks
            sleep_time = random.randint(120, 300)
            print(f"[{datetime.now()}] Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)

def download_wallpaper(url, title):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"[{datetime.now()}] Failed to download {url}: {e}")
        return

    ext = os.path.splitext(url)[1]
    filename = os.path.join(desktop_path, f"{title}{ext}")

    if os.path.exists(filename):
        print(f"[{datetime.now()}] Already downloaded: {filename}")
        return

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"[{datetime.now()}] Downloaded: {filename}")

if __name__ == '__main__':
    print(f"[{datetime.now()}] Starting wallpaper scraper...")
    scrap_for_wallpaper()
    print(f"[{datetime.now()}] Scraping complete.")
