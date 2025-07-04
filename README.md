# 🖼️ Telegram Wallpaper Bot

This is an automated wallpaper scraper and Telegram bot that fetches high-quality wallpapers from [Reddit](https://www.reddit.com/r/wallpapers/) and sends them to a Telegram channel at regular intervals.

---

## 📌 Features

- Scrapes top wallpapers from [r/wallpapers](https://www.reddit.com/r/wallpapers)
- Downloads `.jpg` and `.png` images to a local `Wallpapers/` folder
- Sends one random wallpaper to a Telegram channel every hour
- Logs posted wallpapers to avoid repeats
- Automatically sleeps between downloads to avoid rate-limiting

---

## 🛠️ Tech Stack

- Python 3
- `requests` for API calls
- `dotenv` for environment variables
- Reddit JSON API (no login needed)
- Telegram Bot API

---

## 📁 Folder Structure

wallpaper_scraper/
│
├── main.py # Runs both scraper and bot using threading
├── wallpaper.py # Handles Reddit scraping and downloading
├── telegram_bot.py # Handles Telegram bot sending logic
├── .env # (Optional) Local environment variables (do NOT commit)
├── requirements.txt # Python dependencies


---

## ⚙️ Setup (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/benjamaina/wallpaper_scraper.git
cd wallpaper_scraper

2. Create a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Environment Variables
Create a .env file:
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=@your_channel_username_or_id
💡 Ensure your bot is added to your Telegram channel and is an admin.

▶️ Run the Bot Locally
python main.py
This will:

Continuously scrape wallpapers every few minutes

Post one unposted wallpaper to Telegram every hour

✅ To-Do / Improvements
 Add optional image compression or resizing

 Integrate with AWS S3 or other cloud storage

 Add SQLite DB to persist posted.txt state

 Scheduled posting using APScheduler or Celery (for non-threading solution)

👤 Author
Benjamin Maina
GitHub: @benjamaina

🖼️ Sample Channel Output
Once it's running, the bot will post like this:

mathematica

📷 Beautiful Sunset Over Mountains
[wallpaper.jpg]

