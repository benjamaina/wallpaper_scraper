# 🖼️ Wallpaper Scraper & Auto-Changer

A Python script that scrapes high-quality wallpapers from the web and sets them as your desktop background automatically. Built using `requests`, `BeautifulSoup`, and `ctypes` for Windows integration.

## 🌟 Features

- 🔍 Scrape and download wallpaper images from a target URL
- 🖥️ Automatically set the downloaded image as the desktop wallpaper (Windows)
- 📁 Saves wallpapers locally in a specified folder
- ⚙️ Easy to customize scraping source or image criteria

## 🧰 Tech Stack

- Python 3
- `requests`
- `BeautifulSoup`
- `os`, `ctypes`, `random` (built-in modules)

## 📁 Project Structure

wallpaper_scraper/
├── wallpaper.py # Main script
└── wallpapers/ # Folder where wallpapers are saved

bash
Copy
Edit

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/benjamaina/wallpaper_scraper.git
cd wallpaper_scraper
Install dependencies:

bash
Copy
Edit
pip install requests beautifulsoup4
Run the script:

bash
Copy
Edit
python wallpaper.py
A new wallpaper will be downloaded and set as your desktop background instantly! 🔄

🧪 How It Works
Connects to a wallpaper site (can be customized)

Scrapes image URLs using BeautifulSoup

Randomly selects and downloads a wallpaper

Uses ctypes to update your wallpaper (Windows only)

🚀 Future Ideas
Add support for multiple sources (e.g., Unsplash, Pexels)

Add auto-run on startup

Create a GUI using Tkinter or PyQt

Mac and Linux support
