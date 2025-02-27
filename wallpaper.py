import requests
import os
import re
import glob
import datetime
import time
import random
import ctypes

def sanitize_filename(title):
    return re.sub(r'[\/:*?"<>|]', '_', title)


def scrap_for_wallpaper():
    url = 'https://www.reddit.com/r/wallpapers/top/.json?sort=top&t=month&limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return

    data = response.json()

    for post in data['data']['children']:
        title = sanitize_filename(post['data']['title'])  
        url = post['data']['url']
        if url.endswith(('.jpg', '.png')):  
            download_wallpaper(url, title)


def download_wallpaper(url, title):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:

        filename = title + os.path.splitext(url)[1]
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Downloaded: {filename}')
    else:
        print(f'Failed to download {url}')

def set_wallpaper(wallpaper_path):
    # Change wallpaper on Windows 10 using ctypes and SystemParametersInfoW
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    print(f"Wallpaper set to {wallpaper_path}")

def auto_change_desktop_wallpaper():
    while True:
        wallpapers = glob.glob("*.png")

        if not wallpapers:
            print('No new wallpapers found')
            time.sleep(10)
            continue

        wallpaper = random.choice(wallpapers)
        wallpaper_path = os.path.join(os.getcwd(), wallpaper)

        try:
            set_wallpaper(wallpaper_path)
            print(f'Changed desktop wallpaper to {wallpaper}')

        except Exception as e:
            print(f'Failed to change desktop wallpaper: {str(e)}')

        time.sleep(5)

def auto_delete_wallpaper():
    wallpapers = glob.glob('*.png')
    cutoff_time = (datetime.datetime.now() - datetime.timedelta(days=10)).timestamp()
    for wallpaper in wallpapers:
        if os.path.getctime(wallpaper) < cutoff_time:
            os.remove(wallpaper)
            print(f'Deleted: {wallpaper}')
    
if __name__ == '__main__':
    scrap_for_wallpaper()  
    auto_delete_wallpaper()  
    auto_change_desktop_wallpaper()
