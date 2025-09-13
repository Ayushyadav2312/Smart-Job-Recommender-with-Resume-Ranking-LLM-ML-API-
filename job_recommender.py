from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_from_listings(resume_skills, listings, top_n=10):
    # Combine resume skills with job descriptions
    docs = [" ".join(resume_skills)] + [" ".join(job['Skills'].split(',')) for job in listings]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(docs)
    sims = cosine_similarity(tfidf[0:1], tfidf[1:])[0]

    ranked = sorted(zip(listings, sims), key=lambda x: -x[1])
    top_jobs = []
    for job, score in ranked[:top_n]:
        job['score'] = score
        top_jobs.append(job)
    return top_jobs
