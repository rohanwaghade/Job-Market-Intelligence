-- Example queries for the historical_jobs SQLite table
SELECT posted_day, COUNT(*) AS jobs_posted
FROM historical_jobs GROUP BY posted_day ORDER BY posted_day DESC;

SELECT job_title, COUNT(*) AS listing_count
FROM historical_jobs GROUP BY job_title ORDER BY listing_count DESC LIMIT 15;

SELECT company, COUNT(*) AS listing_count
FROM historical_jobs GROUP BY company ORDER BY listing_count DESC LIMIT 15;
