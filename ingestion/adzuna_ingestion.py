import os, time, requests

BASE_URL = "https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

def fetch_jobs():
    app_id, app_key = os.getenv("ADZUNA_APP_ID"), os.getenv("ADZUNA_APP_KEY")
    if not app_id or not app_key or "your_" in app_id or "your_" in app_key:
        raise RuntimeError("Set ADZUNA_APP_ID and ADZUNA_APP_KEY in .env.")
    country = os.getenv("ADZUNA_COUNTRY", "in")
    location = os.getenv("ADZUNA_LOCATION", "India")
    per_page = int(os.getenv("ADZUNA_RESULTS_PER_PAGE", "50"))
    max_pages = int(os.getenv("ADZUNA_MAX_PAGES", "2"))
    queries = [q.strip() for q in os.getenv(
        "ADZUNA_QUERIES", "data analyst,business analyst,BI analyst,data science"
    ).split(",") if q.strip()]
    jobs, seen = [], set()
    for query in queries:
        for page in range(1, max_pages + 1):
            response = requests.get(BASE_URL.format(country=country, page=page), params={
                "app_id": app_id, "app_key": app_key, "results_per_page": per_page,
                "what": query, "where": location, "content-type": "application/json"
            }, timeout=30)
            response.raise_for_status()
            for job in response.json().get("results", []):
                key = str(job.get("id") or (
                    str(job.get("title", "")) + "|" +
                    str((job.get("company") or {}).get("display_name", ""))
                ))
                if key not in seen:
                    seen.add(key)
                    job["_search_query"] = query
                    jobs.append(job)
            time.sleep(0.15)
    return jobs
