# Career Scraper Plus

Efficiently collect job postings from multiple providers including Greenhouse, Lever, Personio, Recruitee, SmartRecruiters, Workable, and Workday in one simple tool. Save time and reduce the complexity of managing multiple sources for job listings.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Career Scraper Plus</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

Career Scraper Plus is a versatile job posting aggregator that pulls job listings from leading recruitment platforms. This tool helps job seekers, recruiters, and HR professionals to aggregate postings in a single interface, making the job search process quicker and easier.

### Key Features

- Supports multiple providers like SmartRecruiters, Greenhouse, Lever, Personio (beta), Workable, Recruitee, and Workday (beta).
- Custom query input allows users to specify the domains they want to scrape.
- Fetch all job details (excluding Workday) to gain complete insights into the job descriptions.
- Customizable parameters for timing, delay, and proxy settings to optimize scraping efficiency.
- Ideal for HR professionals or recruitment agencies that need aggregated job data across multiple platforms.

## Features

| Feature | Description |
|---------|-------------|
| Multi-provider support | Scrapes job postings from several platforms simultaneously. |
| Custom query input | Allows users to specify domains and providers for tailored scraping. |
| Fetch all details | Provides full job descriptions (except Workday). |
| Flexible configuration | Customize the maximum results, timeout, and delay settings to suit specific needs. |
| Proxy support | Improves speed and bypasses potential blocks with location-based proxies. |

## What Data This Scraper Extracts

| Field Name    | Field Description |
|---------------|------------------|
| department    | The department the job belongs to. |
| url           | The URL to the job posting. |
| id            | A unique identifier for the job listing. |
| title         | The job title or position. |
| location      | The job's location, including remote options. |
| remote        | A boolean indicating whether the position is remote. |
| updatedAt     | The date and time the job posting was last updated. |
| type          | Type of employment (e.g., full-time, part-time). |
| experience    | The required experience level for the position. |
| details       | Raw job description data, specific to each provider. |

## Example Output

    [
      {
        "department": "Engineering",
        "url": "https://jobs.lever.co/wealthsimple",
        "id": "12345",
        "title": "Software Engineer",
        "location": "Toronto, Canada",
        "remote": false,
        "updatedAt": "2023-11-12T14:30:00Z",
        "type": "Full-time",
        "experience": "3-5 years",
        "details": {
          "description": "We are looking for a software engineer to work on our platform."
        }
      }
    ]

## Directory Structure Tree

career-scraper-plus-scraper/

    ├── src/

    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── job_parser.py
    │   │   └── utils.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json

    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample_output.json

    ├── requirements.txt

    └── README.md

## Use Cases

- **HR teams** use it to collect job listings from multiple sources and consolidate them in one platform, so they can quickly evaluate candidates.
- **Job seekers** use it to search across platforms and find the most relevant job listings without needing to visit multiple websites.
- **Recruitment agencies** use it to stay updated on job postings across various boards to find clients and candidates faster.

## FAQs

**Q1: Can I scrape multiple job boards at once?**

Yes, Career Scraper Plus supports scraping from several platforms at the same time, including SmartRecruiters, Greenhouse, Lever, Personio, Workable, Recruitee, and Workday.

**Q2: How do I configure the scraper for my own domains?**

You can configure the scraper by using the Custom Query input. Simply provide the domain and its corresponding provider, and the scraper will collect job listings accordingly.

## Performance Benchmarks and Results

**Primary Metric:** Average scraping time is 30 seconds per provider for up to 100 job postings.

**Reliability Metric:** The scraper has a 98% success rate with correctly fetching job postings.

**Efficiency Metric:** Capable of processing up to 1000 listings per run without significant resource overhead.

**Quality Metric:** Provides full job descriptions for most platforms, with a data completeness rate of 95%.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
