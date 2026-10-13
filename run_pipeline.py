from pathlib import Path
import json
import pandas as pd
from dotenv import load_dotenv
from ingestion.adzuna_ingestion import fetch_jobs
from pipeline.clean_jobs import clean_jobs
from pipeline.extract_skills import add_extracted_skills
from pipeline.score_jobs import add_suitability_scores

ROOT = Path(__file__).resolve().parent

def main():
    load_dotenv(ROOT / ".env")
    raw_dir = ROOT / "data" / "raw"
    processed_dir = ROOT / "data" / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    jobs = fetch_jobs()
    if not jobs:
        raise SystemExit("No jobs returned. Check credentials, quota, and network.")
    (raw_dir / "adzuna_jobs_raw.json").write_text(
        json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    df = clean_jobs(pd.DataFrame(jobs))
    df = add_extracted_skills(df)
    df = add_suitability_scores(df)
    output = processed_dir / "jobs_with_match_scores.csv"
    df.to_csv(output, index=False, encoding="utf-8-sig")
    print(f"Fetched {len(jobs)} records. Output: {output}")

if __name__ == "__main__":
    main()
