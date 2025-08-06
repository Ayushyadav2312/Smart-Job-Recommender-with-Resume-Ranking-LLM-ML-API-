from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define sample job role descriptions
job_roles = {
    "Data Analyst": "sql excel tableau python statistics",
    "Machine Learning Engineer": "python pandas scikit-learn tensorflow",
    "Frontend Developer": "html css javascript react",
    "Backend Developer": "python django flask rest api sql",
}

def recommend_jobs(skills, top_n=3):
    docs = [" ".join(skills)] + list(job_roles.values())
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(docs)
    sims = cosine_similarity(tfidf[0:1], tfidf[1:])[0]
    ranked = sorted(zip(job_roles.keys(), sims), key=lambda x: -x[1])
    return [f"{role} ({score:.2f})" for role, score in ranked[:top_n]]
