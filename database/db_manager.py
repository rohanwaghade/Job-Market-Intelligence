import json, sqlite3
from pathlib import Path

def upsert_jobs(df, db_path="data/database/job_market.db"):
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS historical_jobs (
            job_id TEXT PRIMARY KEY, job_url TEXT, job_title TEXT, company TEXT,
            posted_day TEXT, payload_json TEXT)""")
        for _, row in df.iterrows():
            job_id = str(row.get("job_id", "")).strip()
            if not job_id:
                continue
            conn.execute("""INSERT INTO historical_jobs
            (job_id, job_url, job_title, company, posted_day, payload_json)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(job_id) DO UPDATE SET job_url=excluded.job_url,
            job_title=excluded.job_title, company=excluded.company,
            posted_day=excluded.posted_day, payload_json=excluded.payload_json""",
            (job_id, str(row.get("job_url","")), str(row.get("job_title","")),
             str(row.get("company","")), str(row.get("posted_day","")),
             json.dumps(row.to_dict(), default=str, ensure_ascii=False)))
