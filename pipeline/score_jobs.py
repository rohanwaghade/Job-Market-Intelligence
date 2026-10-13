TARGET_SKILLS = {"python","sql","excel","power bi","pandas","statistics","data analysis"}

def add_suitability_scores(df):
    df = df.copy()
    df["job_match_score"] = df["extracted_skills"].apply(
        lambda found: round(100 * len(TARGET_SKILLS.intersection({str(x).lower() for x in found})) / len(TARGET_SKILLS), 1)
    )
    df["job_match_category"] = df["job_match_score"].apply(
        lambda x: "Excellent Match" if x >= 70 else "Strong Match" if x >= 45 else "Potential Match" if x >= 20 else "Low Match"
    )
    text = (df["job_title"].fillna("").astype(str) + " " + df["job_description"].fillna("").astype(str)).str.lower()
    fresher = text.str.contains(r"\b(fresher|freshers|entry[- ]level|graduate trainee|no experience required|0[- ]?years?)\b", regex=True)
    exp = text.str.contains(r"\b([3-9]\+?\s+years?|[3-9]\s*-\s*[0-9]+\s+years?)\b", regex=True)
    df["fresher_suitability"] = "Potentially Suitable"
    df.loc[exp, "fresher_suitability"] = "Experience Required"
    df.loc[fresher & ~exp, "fresher_suitability"] = "Highly Suitable"
    return df
