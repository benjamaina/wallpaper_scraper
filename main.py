import wallpaper
import telegram_bot  # Your Telegram logic
import time
import threading

# Runs wallpaper scraper every hour
def run_wallpaper_scraper():
    while True:
        wallpaper.scrap_for_wallpaper()
        time.sleep(3600)  # Scrape every 1 hour

# Runs Telegram bot or posting logic (you can schedule inside it too)
def run_telegram_bot():
    while True:
        telegram_bot.start_bot()  # You can make this send one image per run
        time.sleep(3600)  # Post once per hour (or adjust)

if __name__ == '__main__':
    wallpaper_thread = threading.Thread(target=run_wallpaper_scraper)
    telegram_thread = threading.Thread(target=run_telegram_bot)

    wallpaper_thread.start()
    telegram_thread.start()

    wallpaper_thread.join()
    telegram_thread.join()
