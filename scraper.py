from playwright.sync_api import sync_playwright
from playwright_stealth.stealth import Stealth
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        # Headless mode can be detected, but stealth tries to hide it. 
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        self.stealth = Stealth()

    def scrape_article(self, url: str) -> tuple[str, str]:
        page = self.context.new_page()
        self.stealth.apply_stealth_sync(page)
        final_url = url
        text = ""
        try:
            # Force a strict 15-second timeout on ALL Playwright operations so it guarantees no infinite hangs
            page.set_default_timeout(15000)
            
            print(f"Navigating to {url}")
            page.goto(url, wait_until="commit")
            print("Successfully reached the website, waiting for Cloudflare to finish...")
            
            # Wait a few seconds for anti-bot JS challenges to resolve globally
            page.wait_for_timeout(5000)
            
            print("Extracting HTML content...")
            
            print("Page Title:", page.title())
            final_url = page.url
            html = page.content()
            
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript", "svg"]):
                tag.extract()
                
            raw_text = soup.get_text(separator="\n")
            lines = (line.strip() for line in raw_text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
        except Exception as e:
            print(f"Error scraping article {url}: {e}")
        finally:
            page.close()
            
        return final_url, text

    def close(self):
        self.browser.close()
        self.playwright.stop()

if __name__ == "__main__":
    # Test
    scraper = NewsScraper()
    test_url = "https://news.google.com/rss/articles/CBMiwAFBVV95cUxOUzI3a1F2dVQ3ZlFYRzhWZ2ZySjVHS2l3UGp5emZrTXRHaHhiT0pnVFcyWU9kTWlwZEQ1bmRrZS1oY1loZkZRM0kybVVmOEVmQV83VVdRcjhtYUZYWXJLbzVibFVFck1jWkc1UkNubDFNUDc0Nm5mc0MxTzc3T1NEWVdyRmEzdmdEcVNkY1ZIQkZHWFh0dkpmNURQNWRtS3FoWEpoTnNRckZtcnNkTFVzdWRIaXVNbExrTTJ0Y24tSTc?oc=5"
    f_url, content = scraper.scrape_article(test_url)
    print("Final URL:", f_url)
    print("Content length:", len(content))
    print("Content preview:", repr(content[:500]))
    scraper.close()
