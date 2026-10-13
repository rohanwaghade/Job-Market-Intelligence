# Project Documentation

## Objective
Analyze job listings, identify requested skills, and explore entry-level suitability for data analytics and related roles.

## Workflow
1. Collect listings from the Adzuna API.
2. Clean job titles, company/location fields, posting dates, salary values, URLs, and duplicates.
3. Extract skills using a configurable keyword dictionary.
4. Calculate a transparent baseline skill-overlap score and fresher suitability label.
5. Store historical records in SQLite.
6. Export CSV datasets for the Power BI report.

## Power BI report pages
- Market Overview
- Skill Intelligence
- Fresher Opportunities
- Job Explorer

## Limitations
API results depend on the search terms, location, and API coverage. Skill extraction and fresher suitability are heuristic and require manual validation. A match score is not a guarantee of shortlisting. Salary data may be missing or inconsistent.

## Security
Store API keys in `.env`, never commit credentials, and avoid publishing full raw snapshots or private application data.
