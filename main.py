import pandas as pd
from datetime import datetime
from config import DOMAINS
from rss_fetcher import fetch_google_news_urls
from scraper import NewsScraper
from summarizer import summarize_batch
import time

def process_batch(batch_queue, results):
    if not batch_queue:
        return
        
    print(f"\n>>> Batch summarizing {len(batch_queue)} articles to save API RPD limits... <<<")
    texts = [b['text'] for b in batch_queue]
    summaries = summarize_batch(texts)
    
    for item, summary in zip(batch_queue, summaries):
        results.append({
            "Domain": item['domain'],
            "Title": item['title'],
            "Real_URL": item['real_url'],
            "AI_Summary": summary,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
    # PROGRESSIVE SAVE: Write to CSV immediately so you never lose data on a freeze
    import pandas as pd
    if results:
        pd.DataFrame(results).to_csv("results.csv", index=False)
        print("Progress saved to results.csv!")
        
    batch_queue.clear()
    time.sleep(3) # Small safety sleep

def run_pipeline():
    print("Starting News Aggregation Pipeline...")
    results = []
    batch_queue = []
    
    # Initialize the scraper browser only once
    scraper = NewsScraper()
    
    try:
        for domain in DOMAINS:
            print(f"\n--- Processing Domain: {domain} ---")
            articles = fetch_google_news_urls(domain)
            
            if not articles:
                print(f"No articles found for {domain} in the requested timeframe.")
                continue
            
            for index, article in enumerate(articles):
                print(f"[{index + 1}/{len(articles)}] Scraping: {article['title']}")
                
                final_url, text = scraper.scrape_article(article['url'])
                
                if not text or len(text.strip()) < 100:
                    results.append({
                        "Domain": domain,
                        "Title": article['title'],
                        "Real_URL": final_url if final_url else article['url'],
                        "AI_Summary": "Failed to extract meaningful text or bypass protections.",
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    print(f"Extracted {len(text)} characters. Added to batch queue.")
                    batch_queue.append({
                        "domain": domain,
                        "title": article['title'],
                        "real_url": final_url,
                        "text": text
                    })
                    
                if len(batch_queue) >= 15:
                    process_batch(batch_queue, results)
                    
        # Process any remaining articles in the queue
        process_batch(batch_queue, results)

    finally:
        print("\nClosing Scraper instance...")
        scraper.close()

    # Export to Excel/CSV
    if results:
        df = pd.DataFrame(results)
        
        # Save as CSV
        csv_filename = "results.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        print(f"\nSaved {len(results)} records to {csv_filename}")
        
        # Save as Excel
        excel_filename = "results.xlsx"
        df.to_excel(excel_filename, index=False)
        print(f"Saved {len(results)} records to {excel_filename}")
    else:
        print("No results to export.")

if __name__ == "__main__":
    run_pipeline()
