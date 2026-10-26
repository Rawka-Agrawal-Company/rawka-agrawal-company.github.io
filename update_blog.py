import os
import datetime
import feedparser
import re
from google import genai
from openai import OpenAI

# Fetch RSS Feed
feed = feedparser.parse('https://taxguru.in/feed/')
latest_entry = feed.entries[0]
prompt = f"Write a professional 2-paragraph summary of this Indian tax update for a CA firm's blog. Do not use conversational filler. Title: {latest_entry.title}. Link: {latest_entry.link}"

blog_content = ""

# Try Gemini First
try:
    gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = gemini_client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    blog_content = response.text
except Exception as e:
    print(f"Gemini failed ({e}). Switching to ChatGPT...")
    # Fallback to ChatGPT
    openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    blog_content = response.choices[0].message.content

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
