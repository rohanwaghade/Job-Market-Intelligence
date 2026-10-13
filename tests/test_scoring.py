import pandas as pd
from pipeline.score_jobs import add_suitability_scores

def test_match_score():
    df = pd.DataFrame({
        "extracted_skills": [["Python","SQL","Excel","Power BI","Pandas","Statistics","Data Analysis"]],
        "job_title": ["Entry-level Data Analyst"],
        "job_description": ["No experience required"]
    })
    out = add_suitability_scores(df)
    assert out.loc[0, "job_match_score"] == 100.0
    assert out.loc[0, "job_match_category"] == "Excellent Match"
    assert out.loc[0, "fresher_suitability"] == "Highly Suitable"
