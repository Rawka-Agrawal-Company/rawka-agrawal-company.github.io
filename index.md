---
layout: single
author_profile: true
---

<style>
  .home-section {
    margin-top: 10px;
  }
  
  /* Upgraded Hero Section */
  .hero-card {
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 40px;
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    margin-bottom: 40px;
    border-top: 4px solid #0056b3; 
    text-align: center;
  }
  .hero-title {
    margin: 0 0 16px 0 !important;
    font-size: 2em;
    color: #2c3e50;
  }
  .hero-text {
    font-size: 1.1em;
    color: #4a5568;
    line-height: 1.6;
    margin-bottom: 24px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }
  .btn-primary {
    display: inline-block;
    padding: 12px 24px;
    background-color: #0056b3;
    color: white !important;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 700;
    transition: background-color 0.2s;
  }
  .btn-primary:hover {
    background-color: #004494;
  }

  /* Section Headers */
  .section-heading {
    font-size: 1.6em;
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

  /* Services Mini-Grid */
  .quick-services {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 16px;
    margin-bottom: 40px;
  }
  .qs-card {
    border: 1px solid #eaeaea;
    border-radius: 6px;
    padding: 20px;
    background-color: #fff;
    text-decoration: none;
    color: inherit;
    transition: box-shadow 0.2s, transform 0.2s;
    border-left: 3px solid #0056b3;
  }
  .qs-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transform: translateY(-2px);
  }
  .qs-title {
    font-size: 1.1em;
    color: #2c3e50;
    margin: 0 0 8px 0 !important;
  }
  .qs-text {
    font-size: 0.85em;
    color: #4a5568;
    margin: 0;
    line-height: 1.5;
  }

  /* Industries Tags */
  .industries-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 40px;
  }
  .industry-tag {
    background-color: #f0f4f8;
    color: #0056b3;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: 600;
    border: 1px solid #d9e2ec;
  }

  /* Post Grid */
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
    <p class="hero-text">A Chartered Accountancy firm based in Indore, Madhya Pradesh. With over four decades of experience, we empower businesses with integrity, expertise, and actionable financial insights.</p>
    <a href="/services/" class="btn-primary">Explore Our Services</a>
  </div>

  <h2 class="section-heading">Core Expertise</h2>
  <p class="section-subtext">Delivering value-based services to enhance business growth and regulatory compliance.</p>
  
  <div class="quick-services">
    <a href="/services/" class="qs-card">
      <h3 class="qs-title">Audit & Assurance</h3>
      <p class="qs-text">Statutory, Internal, and Tax audits ensuring rigorous financial reliability.</p>
    </a>
    <a href="/services/" class="qs-card">
      <h3 class="qs-title">Direct Taxation</h3>
      <p class="qs-text">Strategic tax planning, ITR filings, and expert appellate litigation.</p>
    </a>
    <a href="/services/" class="qs-card">
      <h3 class="qs-title">GST Compliance</h3>
      <p class="qs-text">Proactive structuring, reconciliations, and departmental representation.</p>
    </a>
    <a href="/services/" class="qs-card">
      <h3 class="qs-title">Corporate Advisory</h3>
      <p class="qs-text">Entity incorporation, SOP drafting, and MCA regulatory compliance.</p>
    </a>
  </div>

  <h2 class="section-heading">Industries We Serve</h2>
  <p class="section-subtext">Providing specialized financial strategies across diverse economic sectors.</p>
  <div class="industries-grid">
    <span class="industry-tag">Telecom</span>
    <span class="industry-tag">Real Estate</span>
    <span class="industry-tag">Logistics</span>
    <span class="industry-tag">Education</span>
    <span class="industry-tag">Healthcare</span>
    <span class="industry-tag">Manufacturing</span>
    <span class="industry-tag">High-Net-Worth Individuals</span>
  </div>

  <h2 class="section-heading">Recent Updates & Tax News</h2>
  <p class="section-subtext"> Daily insights and regulatory changes:</p>
  
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
