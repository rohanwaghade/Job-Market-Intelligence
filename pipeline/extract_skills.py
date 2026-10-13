SKILLS = ["Python","SQL","Excel","Power BI","Tableau","Looker","Power Query","DAX","Pandas","NumPy","Machine Learning","Deep Learning","NLP","TensorFlow","PyTorch","Scikit-learn","AWS","Azure","GCP","Git","Docker","ETL","Data Visualization","Statistics","Data Analysis","Reporting","JIRA","SAP","Alteryx"]

def extract_skills(text):
    text = str(text or "").lower()
    return [skill for skill in SKILLS if skill.lower() in text]

def add_extracted_skills(df):
    df = df.copy()
    combined = df["job_title"].fillna("").astype(str) + " " + df["job_description"].fillna("").astype(str)
    df["extracted_skills"] = combined.apply(extract_skills)
    df["skills_count"] = df["extracted_skills"].apply(len)
    return df
