# Job Market Intelligence & Career Analytics Platform

Supporting repository files for the existing Colab notebook and Power BI report.

## Included
- `run_pipeline.py`: reusable pipeline entry point
- `ingestion/adzuna_ingestion.py`: Adzuna API ingestion
- `pipeline/clean_jobs.py`: basic cleaning
- `pipeline/extract_skills.py`: keyword-based skill extraction
- `pipeline/score_jobs.py`: baseline match/fresher scoring
- `database/db_manager.py`: SQLite upsert helper
- `database/queries/analytics.sql`: sample analysis queries
- `tests/test_scoring.py`: starter test
- `.env.example`, `.gitignore`, `requirements.txt`
- `docs/PROJECT_DOCUMENTATION.md`

## Setup
1. Extract this ZIP into your repository folder.
2. Copy `.env.example` to `.env`, then enter your own Adzuna API credentials.
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python run_pipeline.py`.

These are reusable starter modules based on the project design. They may need small schema/path adjustments to match your final Colab notebook exports. Keep `.env`, real API keys, and large raw snapshots out of GitHub.
