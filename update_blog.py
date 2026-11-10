import os
import datetime
import feedparser
import re
import time
from google import genai
from openai import OpenAI

# Fetch RSS Feed
feed = feedparser.parse('https://taxguru.in/feed/')
latest_entry = feed.entries[0]
prompt = f"Write a professional 2-paragraph summary of this Indian tax update for a CA firm's blog. Do not use conversational filler. Title: {latest_entry.title}. Link: {latest_entry.link}"

blog_content = ""
gemini_success = False
max_retries = 3

# Try Gemini First (with Retry Logic for 503 Errors)
for attempt in range(max_retries):
    try:
        gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        response = gemini_client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        blog_content = response.text
        gemini_success = True
        break  # Exit loop if successful
        
    except Exception as e:
        error_msg = str(e)
        if "503" in error_msg and attempt < max_retries - 1:
            print(f"Gemini overloaded (Attempt {attempt + 1} of {max_retries}). Waiting 30 seconds...")
            time.sleep(30)
        else:
            print(f"Gemini failed ({error_msg}).")
            break # Break out of loop if it's not a 503 or if retries are exhausted

# Fallback to ChatGPT if Gemini failed all attempts
if not gemini_success:
    print("Switching to ChatGPT...")
    try:
        openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        blog_content = response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI fallback also failed: {e}")
        # Exit script with error code so GitHub Actions registers the failure
        exit(1)

# Format for Jekyll Website
date_str = datetime.datetime.now().strftime('%Y-%m-%d')
safe_title = re.sub(r'[^a-z0-9]+', '-', latest_entry.title.lower())[:50]
filename = f"_posts/{date_str}-{safe_title}.md"

os.makedirs("_posts", exist_ok=True)

content = f"""---
title: "{latest_entry.title.replace('"', '')}"
date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
layout: single
---

{blog_content}

[Read full official update on TaxGuru]({latest_entry.link})
"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
