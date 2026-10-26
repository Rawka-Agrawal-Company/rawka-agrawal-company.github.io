import os
import datetime
import feedparser
import google.generativeai as genai
import re

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Fetch RSS Feed
feed = feedparser.parse('https://taxguru.in/feed/')
latest_entry = feed.entries[0]

# Generate Content
prompt = f"Write a professional 2-paragraph summary of this Indian tax update for a CA firm's blog. Do not use conversational filler. Title: {latest_entry.title}. Link: {latest_entry.link}"
response = model.generate_content(prompt)

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
