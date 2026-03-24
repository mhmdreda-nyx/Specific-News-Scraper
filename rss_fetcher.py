import feedparser
import urllib.parse
import time
from googlenewsdecoder import new_decoderv1
from config import SEARCH_QUERY, WHEN_PARAM, MAX_ARTICLES_PER_DOMAIN

def fetch_google_news_urls(domain: str) -> list[str]:
    """
    Fetches the latest Google News URLs for a specific domain matching the query.
    Note: These are usually Google News redirect URLs, which must be resolved.
    """
    query = f"{SEARCH_QUERY} site:{domain} when:{WHEN_PARAM}"
    encoded_query = urllib.parse.quote(query)
    
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"
    
    try:
        feed = feedparser.parse(rss_url)
        urls = []
        for entry in feed.entries[:MAX_ARTICLES_PER_DOMAIN]:
            raw_url = entry.link
            try:
                # Instantly resolve the Google News JS redirect using the decoder
                decoded = new_decoderv1(raw_url)
                if decoded.get('status'):
                    real_url = decoded.get('decoded_url')
                else:
                    real_url = raw_url
            except Exception:
                real_url = raw_url
                
            urls.append({
                "title": entry.title,
                "url": real_url
            })
            time.sleep(1) # Small delay to avoid decoder rate limits
        return urls
    except Exception as e:
        print(f"Error fetching RSS for {domain}: {e}")
        return []

if __name__ == "__main__":
    # Test
    print(fetch_google_news_urls("reuters.com"))
