import pandas as pd

def nested(value, key):
    return value.get(key, "") if isinstance(value, dict) else ""

def clean_jobs(df):
    df = df.copy()
    df["job_id"] = df.get("id", pd.Series("", index=df.index)).astype(str)
    df["job_title"] = df.get("title", pd.Series("", index=df.index)).fillna("").astype(str).str.strip()
    df["company"] = df.get("company", pd.Series(index=df.index, dtype=object)).apply(lambda x: nested(x, "display_name"))
    df["location"] = df.get("location", pd.Series(index=df.index, dtype=object)).apply(lambda x: nested(x, "display_name"))
    df["job_description"] = df.get("description", pd.Series("", index=df.index)).fillna("").astype(str)
    df["job_url"] = df.get("redirect_url", pd.Series("", index=df.index)).fillna("").astype(str)
    df["posted_day"] = pd.to_datetime(df.get("created", pd.Series("", index=df.index)), errors="coerce", utc=True).dt.date.astype("string")
    for col in ["salary_min", "salary_max"]:
        df[col] = pd.to_numeric(df.get(col, pd.Series(index=df.index, dtype=float)), errors="coerce")
    df["salary_mid"] = df[["salary_min", "salary_max"]].mean(axis=1)
    text = (df["job_title"] + " " + df["job_description"]).str.lower()
    df["is_remote"] = text.str.contains(r"\b(remote|work from home|wfh)\b", regex=True).astype(int)
    df["job_unique_key"] = df["job_title"].str.lower() + "|" + df["company"].str.lower() + "|" + df["location"].str.lower()
    df = df.drop_duplicates(subset=["job_id"], keep="last").drop_duplicates(subset=["job_unique_key"], keep="last")
    return df.reset_index(drop=True)
