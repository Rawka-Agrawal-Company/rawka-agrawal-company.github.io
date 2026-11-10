---
layout: single
author_profile: true
---

<style>
  .home-section {
    margin-top: 10px;
  }
  .hero-card {
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 32px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    margin-bottom: 40px;
    border-top: 4px solid #0056b3; 
  }
  .hero-title {
    margin: 0 0 16px 0 !important;
    font-size: 1.8em;
    color: #2c3e50;
  }
  .hero-text {
    font-size: 1.1em;
    color: #4a5568;
    line-height: 1.6;
    margin-bottom: 16px;
  }
  .hero-text:last-child {
    margin-bottom: 0;
  }
  .section-heading {
    font-size: 1.5em;
    color: #2c3e50;
    margin: 0 0 8px 0;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 12px;
  }
  .section-subtext {
    color: #4a5568;
    font-size: 0.95em;
    margin-bottom: 24px;
  }
  .post-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .post-card {
    display: block;
    text-decoration: none;
    color: inherit;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 24px;
    background-color: #ffffff;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
  }
  .post-card:hover {
    box-shadow: 0 6px 12px rgba(0,0,0,0.08);
    transform: translateY(-2px);
  }
  .post-date {
    font-size: 0.85em;
    font-weight: 700;
    color: #0056b3;
    margin-bottom: 8px;
    display: block;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .post-title {
    font-size: 1.25em;
    color: #2c3e50;
    margin: 0 0 12px 0 !important;
  }
  .read-more {
    font-size: 0.9em;
    font-weight: 700;
    color: #0056b3;
  }
</style>

<div class="home-section">
  
  <div class="hero-card">
    <h1 class="hero-title">Welcome to Rawka Agrawal & Company</h1>
    <p class="hero-text">We are a premier Chartered Accountancy group based in Indore, Madhya Pradesh. With over four decades of experience, we empower businesses with integrity, expertise, and actionable financial insights.</p>
    <p class="hero-text">Our specialized teams support listed entities, private companies, LLPs, and high-net-worth individuals across audit, taxation, regulatory compliance, and management consultancy.</p>
  </div>

  <h2 class="section-heading">Recent Updates & Tax News</h2>
  <p class="section-subtext">Below are our latest daily insights:</p>
  
  <div class="post-grid">
    {% for post in site.posts limit:5 %}
    <a href="{{ post.url | relative_url }}" class="post-card">
      <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
      <h3 class="post-title">{{ post.title }}</h3>
      <span class="read-more">Read Insight &rarr;</span>
    </a>
    {% endfor %}
  </div>

</div>
