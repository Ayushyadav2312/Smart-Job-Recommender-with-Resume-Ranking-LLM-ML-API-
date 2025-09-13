import json
from llm_helpers import extract_skills_from_jobs

with open("Jobs_data.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

preprocessed = []

for job in jobs:
    # Extract skills once and store
    skills = extract_skills_from_jobs(job.get("JD", ""))
    job['skills_extracted'] = skills
    preprocessed.append(job)

with open("preprocessed_jobs.json", "w", encoding="utf-8") as f:
    json.dump(preprocessed, f, indent=4)
