<div align="center">

# 🌐 Intelligent News Scraper Pipeline

A robust, AI-powered pipeline that aggregates news, bypasses sophisticated anti-bot protections, and summarizes global geopolitical updates in real-time.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-Stealth-green.svg)](https://playwright.dev/)
[![Gemini API](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange.svg)](https://deepmind.google/technologies/gemini/)

</div>

---

## ✨ Why this project stands out (Features & Benefits)

This isn't just another simple web scraper. It's a highly resilient data extraction engine built to survive the modern, heavily-protected web and immediately add value through AI.

- **🛡️ Ultimate Stealth & Anti-Bot Bypass:** Leverages `playwright-stealth` with headless Chromium to effortlessly bypass Cloudflare, Datadome, and complex JavaScript rendering that block standard HTTP requests.
- **🔗 Smart Redirect Resolution:** Automatically unwraps and follows encrypted `news.google.com` redirects to extract the true, original article URLs.
- **🧠 AI Summarization:** Integrates with **Google Gemini 2.5 Flash** to read lengthy news articles and synthesize sharp, 3-5 line summaries focusing on specific topics (like Geopolitics / Middle East).
- **⚡ Fast & Concurrent:** Designed to process multiple domains in parallel reliably, fetching the latest articles (under 24 hours old).
- **📊 Clean Output:** Automatically structures the chaotic web data and exports it into polished `.csv` and `.xlsx` (Excel) formats for immediate analysis.
- **🛑 Crash-Resilient:** Aggressive error handling ensures that if one domain has impossible protections, the pipeline logs the error and continues seamlessly without breaking the whole process.

## 🛠️ Technologies Stack

- **Python 3.10+** - Core language
- **Playwright & Playwright-Stealth** - Browser automation & bot bypass
- **Google GenAI (Gemini)** - LLM Summarization
- **Pandas & OpenPyXL** - Data manipulation and Excel export
- **Feedparser & BeautifulSoup4** - RSS parsing and HTML extraction

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mhmdreda-nyx/Specific-News-Scraper.git
   cd news-scraper-pipeline
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If you don't have a requirements.txt, run: `pip install playwright playwright-stealth google-genai feedparser pandas python-dotenv beautifulsoup4 openpyxl`)*

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

5. **Configuration:**
   - Create a `.env` file in the root directory (you can copy `.env.example`).
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## 💻 Usage

Simply run the main pipeline script:

```bash
python main.py
```

**Behind the scenes during execution:**
1. The script reads the target domains list (e.g., 70 distinct sources).
2. It fetches RSS feeds for your specific target keywords.
3. It filters out articles older than 24 hours, limiting to max 3 articles per domain.
4. Headless browsers navigate to the sites, bypass protections, and extract the pure text.
5. Gemini AI summarizes the text.
6. A progress bar tracks the process, and finally, `results.csv` and `results.xlsx` are generated in your root directory!

## 🤝 Contributing
Contributions, issues, and feature requests are highly welcome! Feel free to check the issues page and submit Pull Requests.

## 📝 License
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
