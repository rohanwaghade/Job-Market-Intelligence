# Job Market Intelligence & Career Analytics Platform

### Data Analytics | Python | SQL | Power BI | Career Intelligence

An end-to-end data analytics project that explores the job market for data professionals in India. This project collects job listings through the Adzuna API, processes job data, identifies in-demand skills, applies rule-based suitability scoring, and presents insights through an interactive Power BI dashboard.

The goal is to help job seekers better understand hiring trends, identify valuable skills, and explore opportunities relevant to entry-level and early-career professionals.

---

## Project Overview

Finding relevant jobs as a fresher can be challenging. Job listings often contain different titles, technical requirements, and experience expectations, making it difficult to identify suitable opportunities and understand the skills employers demand.

The **Job Market Intelligence & Career Analytics Platform** organizes job-posting data into an analytical workflow that helps users explore:

- Job-market trends and role distributions.
- Frequently mentioned technical and analytical skills.
- Potential opportunities for freshers and entry-level candidates.
- Individual job listings for further investigation.
- Job suitability indicators based on predefined rules.

This project combines Python-based data processing with SQL and Power BI to transform job-listing data into actionable insights.

## Key Features

- **Job Data Ingestion:** Collects job listings using the Adzuna API.
- **Data Cleaning:** Prepares job records for consistent downstream analysis.
- **Skill Extraction:** Identifies skills using keyword-based matching.
- **Suitability Scoring:** Applies rule-based heuristics to help prioritize listings.
- **Database Support:** Includes SQLite utilities and analytical SQL queries.
- **Interactive Dashboard:** Presents job-market insights across four Power BI report pages.
- **Fresher Opportunity Exploration:** Helps identify listings that may be relevant to early-career candidates.

> **Important:** Suitability scores are heuristic indicators, not predictions of hiring success or guarantees that a candidate meets an employer's requirements.

---

## Power BI Dashboard

The report is organized into four analytical pages.

| Dashboard Page | Description |
|---|---|
| **Market Overview** | Summarizes the collected job market and key listing patterns. |
| **Skill Intelligence** | Explores the skills frequently mentioned in job descriptions. |
| **Fresher Opportunities** | Helps surface potentially relevant entry-level opportunities. |
| **Job Explorer** | Supports detailed exploration of individual job listings. |

### Dashboard Screenshots

#### 1. Market Overview
![Market Overview](dashboard/Dashboard%20Screenshots/market-overview.png)

#### 2. Skill Intelligence
![Skill Intelligence](dashboard/Dashboard%20Screenshots/skill-intelligence.png)

#### 3. Fresher Opportunities
![Fresher Opportunities](dashboard/Dashboard%20Screenshots/fresher-opportunities.png)

#### 4. Job Explorer
![Job Explorer](dashboard/Dashboard%20Screenshots/job-explorer.png)

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline orchestration and data processing |
| Pandas | Data cleaning and transformation |
| Requests | API communication |
| python-dotenv | Environment variable management |
| SQLite | Lightweight local data storage |
| SQL | Analytical queries |
| Power BI | Interactive dashboards and visual analytics |
| pytest | Automated testing |

---

## Project Workflow

The project follows a structured data analytics workflow:

1. **Data Collection:** Retrieve job listings from the Adzuna API.
2. **Data Preparation:** Clean job records and prepare fields for analysis.
3. **Skill Extraction:** Identify relevant skills through keyword matching.
4. **Suitability Scoring:** Apply baseline rules to assess potential relevance.
5. **Data Storage and Export:** Save raw and processed data for downstream analysis.
6. **Dashboard Development:** Explore job-market patterns through Power BI.
7. **Career Insights:** Use the dashboard to investigate role requirements and skill demand.

---

## Repository Structure

```text
Job-Market-Intelligence/
│
├── README.md
├── requirements.txt
├── run_pipeline.py
├── .env.example
├── .gitignore
│
├── ingestion/
│   └── adzuna_ingestion.py
│
├── pipeline/
│   ├── clean_jobs.py
│   ├── extract_skills.py
│   └── score_jobs.py
│
├── database/
│   ├── db_manager.py
│   └── queries/
│       └── analytics.sql
│
├── tests/
│   └── test_scoring.py
│
├── docs/
│   └── PROJECT_DOCUMENTATION.md
│
├── dashboard/
│   └── screenshots/
│
└── data/
    ├── raw/
    ├── processed/
    └── database/
```

*Note: This structure describes the intended organization of the project. Some folders may contain only placeholders until the corresponding files or generated outputs are added.*

---

## Getting Started

Follow these steps to set up the Python pipeline locally.

### 1. Clone the Repository

```bash
git clone https://github.com/rohanwaghade/Job-Market-Intelligence.git
cd Job-Market-Intelligence
```

### 2. Create a Virtual Environment

On Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure API Credentials

Copy `.env.example` to a file named `.env`.

Add your own Adzuna API credentials using the environment-variable names expected by `ingestion/adzuna_ingestion.py`.

**Security reminder:** Never commit your `.env` file, API credentials, or other secrets to GitHub.

### 5. Run the Pipeline

```bash
python run_pipeline.py
```

The current runner is designed to retrieve job listings, process the records, and write raw and processed output files under the `data/` directory.

Review the console output and generated files after execution. Depending on the API response and current implementation, additional schema or path adjustments may be necessary.

---

## Testing

Run the included tests with:

```bash
pytest -q
```

The included tests provide a starting point for checking the scoring logic. They do not independently validate the entire ingestion, processing, database, and Power BI workflow.

---

## Data Considerations

- Job listings and availability can change over time.
- The collected dataset represents the records retrieved during a particular run, not the entire Indian job market.
- Keyword-based skill extraction may miss synonyms or match ambiguous terms.
- Rule-based scoring should be treated as a prioritization aid rather than a definitive assessment.
- Always verify job requirements and application details against the original employer listing.
- Follow the API provider's terms, rate limits, and data-use requirements.

---

## Future Improvements

Potential areas for further development include:

- Improving skill extraction with normalized skill names and synonyms.
- Expanding automated tests and data-quality validation.
- Tracking job-market changes across multiple collection dates.
- Evaluating scoring rules against representative job descriptions.
- Improving reproducibility between the Python pipeline and Power BI dataset.
- Adding dashboard screenshots and a small, safe-to-share sample dataset.

---

## Skills Demonstrated

This project demonstrates practical experience with:

- Python-based data processing.
- Data cleaning and transformation.
- API integration.
- SQL and database fundamentals.
- Exploratory data analysis.
- Rule-based scoring and feature extraction.
- Power BI dashboard development.
- Data storytelling and analytical problem-solving.

---

## Author

**Rohan Waghade**

Aspiring Data Analyst | Python | SQL | Power BI

- **GitHub Profile:** https://github.com/rohanwaghade
- **Project Repository:** https://github.com/rohanwaghade/Job-Market-Intelligence

---

*This project is intended for educational and portfolio purposes. Verify job information with the original source before making application decisions.*
