import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json

def fetch_jobs_from_api(offset=0):
    url = "https://linkedin-job-search-api.p.rapidapi.com/active-jb-7d"

    querystring = {"offset":"0","location_filter":"India"}

    headers = {
	    "x-rapidapi-key": os.environ.get("Job_Api"),
	"x-rapidapi-host": "linkedin-job-search-api.p.rapidapi.com"
    }


    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        raw_data = response.json()
        jobs = []
        for item in raw_data:
            job = {
                "id": item.get("id"),
                "title": item.get("title", "N/A"),
                "organization": item.get("organization", "N/A"),
                "location": item.get("locations_derived", ["N/A"])[0],
                "employment_type": item.get("employment_type", ["N/A"])[0],
                "url": item.get("url", ""),
                "description": item.get("linkedin_org_description", ""),
                "industry": item.get("linkedin_org_industry", "N/A"),
            }
            jobs.append(job)
            return jobs

    except Exception as e:
        print(f"[ERROR] Failed to fetch jobs: {e}")
        return []


# if __name__ == "__main__":
#     job_results = fetch_jobs_from_api()
#     for i, job in enumerate(job_results[:5]):  # Show only first 5 for brevity
#         print(f"\nJob {i+1}:")
#         print(f"Title        : {job['title']}")
#         print(f"Company      : {job['organization']}")
#         print(f"Location     : {job['location']}")
#         print(f"Type         : {job['employment_type']}")
#         print(f"Job Link     : {job['url']}")