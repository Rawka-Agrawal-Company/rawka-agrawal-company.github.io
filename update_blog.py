import os
import datetime
import feedparser
from google import genai
import re

# Configure Gemini using the new SDK
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Fetch RSS Feed
feed = feedparser.parse('https://taxguru.in/feed/')
latest_entry = feed.entries[0]

# Generate Content
prompt = f"Write a professional 2-paragraph summary of this Indian tax update for a CA firm's blog. Do not use conversational filler. Title: {latest_entry.title}. Link: {latest_entry.link}"

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

# Format for Jekyll Website
date_str = datetime.datetime.now().strftime('%Y-%m-%d')
safe_title = re.sub(r'[^a-z0-9]+', '-', latest_entry.title.lower())[:50]
filename = f"_posts/{date_str}-{safe_title}.md"

# Ensure _posts directory exists
os.makedirs("_posts", exist_ok=True)

content = f"""---
title: "{latest_entry.title.replace('"', '')}"
date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
layout: single
---

{response.text}

[Read full official update on TaxGuru]({latest_entry.link})
"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
