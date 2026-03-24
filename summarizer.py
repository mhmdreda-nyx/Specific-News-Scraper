import os
from google import genai
from google.genai import types
from config import GEMINI_API_KEY

import json

def summarize_batch(articles_texts: list[str]) -> list[str]:
    """
    Summarizes a batch of article texts using Gemini.
    Strictly focuses on US-Iran tensions or Middle East geopolitics.
    Requires 3-5 lines output per article in a JSON array.
    """
    if not GEMINI_API_KEY:
        return ["Error: No GEMINI_API_KEY provided."] * len(articles_texts)

    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = (
        f"You are an expert geopolitical analyst. You are given {len(articles_texts)} distinct news articles.\n"
        "For EACH article, provide a 3 to 5 line summary strictly focusing on US-Iran tensions or Middle East geopolitics.\n"
        "You MUST output ONLY a valid JSON array of strings, where each string is the summary for the corresponding article in order.\n"
        "Do NOT include markdown formatting like ```json. Just output the array like [\"summary 1\", \"summary 2\"].\n\n"
    )
    
    for i, text in enumerate(articles_texts):
        # Truncate to 5000 chars per article to stay well within token limits
        prompt += f"--- ARTICLE {i} ---\n{text[:5000]}\n\n"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Clean potential markdown and parse JSON
        raw_text = response.text.replace("```json", "").replace("```", "").strip()
        summaries = json.loads(raw_text)
        
        if len(summaries) != len(articles_texts):
            print(f"Warning: Gemini returned {len(summaries)} summaries but expected {len(articles_texts)}.")
            return ["Error: AI returned mismatched summaries structure"] * len(articles_texts)
            
        return summaries
    except Exception as e:
        print(f"Error during batch summarization: {e}")
        return [f"Error: Summarization failed - {e}"] * len(articles_texts)
