<style>
  .team-section {
    margin-top: 30px;
  }
  .team-card-horizontal {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 24px;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 24px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    margin-bottom: 24px;
    transition: box-shadow 0.2s ease;
  }
  .team-card-horizontal:hover {
    box-shadow: 0 6px 12px rgba(0,0,0,0.08);
  }
  .team-photo {
    width: 140px;
    height: 140px;
    border-radius: 8px;
    object-fit: cover;
    background-color: #f8f9fa;
    border: 1px solid #eaeaea;
    flex-shrink: 0;
  }
  .team-info {
    display: flex;
    flex-direction: column;
  }
  .team-name {
    margin: 0 0 4px 0 !important;
    font-size: 1.35em;
    color: #2c3e50;
  }
  .team-title {
    font-size: 0.85em;
    font-weight: 700;
    color: #0056b3;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
    display: block;
  }
  .team-bio {
    font-size: 0.95em;
    line-height: 1.6;
    color: #4a5568;
    margin: 0 !important;
  }
  .support-staff-box {
    background-color: #f8f9fa;
    border-left: 4px solid #0056b3;
    padding: 20px;
    border-radius: 4px;
    margin-top: 10px;
    font-size: 0.95em;
    line-height: 1.6;
    color: #4a5568;
  }
  
  /* Stacks the photo on top of the text on small screens */
  @media (max-width: 650px) {
    .team-card-horizontal {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
  }
</style>

<div class="team-section">
  <h2>Partners</h2>
  
  <div class="team-card-horizontal">
    <!-- Replace src with actual image path once uploaded, e.g., /assets/images/kailash.jpg -->
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Kailash Agrawal" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Kailash Agrawal</h3>
      <span class="team-title">Senior Partner</span>
      <p class="team-bio">With over five decades of distinguished professional practice, CA Kailash Agrawal provides foundational leadership and high-level strategic oversight to the firm. He leverages his extensive experience to monitor practice quality and advise the leadership team on complex tax litigations and corporate planning.</p>
    </div>
  </div>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Sandeep Garg" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Sandeep Garg</h3>
      <span class="team-title">Senior Partner</span>
      <p class="team-bio">With nearly three decades of professional experience, CA Sandeep Garg serves as the principal managing partner overseeing the firm’s entire spectrum of services. He actively leads all client communications, statutory audits, tax assessments, return filings, and comprehensive management consultancy engagements.</p>
    </div>
  </div>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Vikas Bansal" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Vikas Bansal</h3>
      <span class="team-title">Partner</span>
      <p class="team-bio">CA Vikas Bansal brings valuable strategic oversight and advisory support to the firm's leadership team. He contributes to the firm's overarching compliance strategies and provides high-level guidance on complex regulatory frameworks.</p>
    </div>
  </div>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Shubham Goyal" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Shubham Goyal</h3>
      <span class="team-title">Partner</span>
      <p class="team-bio">CA Shubham Goyal is a key member of the firm's audit and assurance practice, specializing in the seamless execution of statutory audits. His meticulous approach to financial reconciliation and compliance reporting ensures high-quality deliverables. </p>
    </div>
  </div>

  <h2>Core Team & Administration</h2>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Ankit Neema" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Ankit Neema</h3>
      <span class="team-title">Associate</span>
      <p class="team-bio">CA Ankit Neema drives critical statutory and internal audit engagements for the firm's corporate clientele. He brings specialized proficiency in risk assessment and financial compliance, ensuring rigorous adherence to auditing standards.</p>
    </div>
  </div>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="CA Piyush Garg" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">CA Piyush Garg</h3>
      <span class="team-title">Associate</span>
      <p class="team-bio">CA Piyush Garg provides dedicated financial management and customized compliance solutions for key strategic accounts. His highly focused approach ensures that complex client portfolios receive continuous, specialized attention and robust operational support.</p>
    </div>
  </div>

  <div class="team-card-horizontal">
    <img src="https://via.placeholder.com/140/f0f0f0/cccccc?text=Photo" alt="Adv. Soumya Garg" class="team-photo">
    <div class="team-info">
      <h3 class="team-name">Adv. Soumya Garg</h3>
      <span class="team-title">Head of Operations & Tax Compliance</span>
      <p class="team-bio">Adv. Soumya Garg oversees the firm's internal operations, management workflows, and individual tax compliance mandates, including comprehensive ITR filings. Leveraging her legal background, she ensures seamless administrative functioning and efficient service delivery.</p>
    </div>
  </div>

  <h2>Professional Support Staff</h2>
  <div class="support-staff-box">
    The core leadership is backed by a dynamic team of accountants, compliance executives, and article assistants. This dedicated support staff ensures the timely and accurate execution of daily financial workflows, return filings, and client service mandates.
  </div>
</div>
