from dotenv import load_dotenv
import os
from resume_parser import extract_text_from_pdf
from groq import Groq
import json

load_dotenv()

def extract_summary_and_skills(file_path: str):
    resume_text = extract_text_from_pdf(file_path)
    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = f"Extract key skills and experince from this resume:\n\n{resume_text}"

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",  # or your preferred model
    )

    return response.choices[0].message.content




with open("jobs_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def extract_skills_from_Jobs(description: str):
    desc = description
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = "Extract key skills & experince required from the following job descriptions:\n\n{desc}"
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",  # or your preferred model
        )
    return response.choices[0].message.content



for job in data:
    title = job.get("title", "N/A")
    location = job.get("locations_raw")[0].get("address", "N/A").get("addressCountry", "N/A")
    emp_type = job.get("employment_type", "N/A")
    skills_required = extract_skills_from_Jobs(job.get("description_text", "N/A"))

if __name__ == "__main__":
    file_path = "Ayush_Resume.pdf"
    skills_summary = extract_summary_and_skills(file_path)
    print(skills_summary)



# ------------------------------------------------------------



# pseudo‑client import; adapt to actual Claude or Gemini SDK
# from anthropic import Client  # if using Claude

# client = Client(api_key=os.getenv("CLAUDE_API_KEY"))

# def extract_summary_and_skills(resume_text: str):
    
#     prompt = f"Extract skills and summary from this resume:\n\n{resume_text}"
#     resp = client.complete(prompt=prompt, model="claude‑2", max_tokens=500)
#     summary = resp['completion']
#     skills = parse_skills_from_summary(summary)
#     return {"summary": summary}, skills

# def ask_resume_bot(summary, skills, user_question: str):
#     system = "You are a career coach. Use resume info to answer."
#     prompt = f"Summary: {summary}\nSkills: {skills}\nUser: {user_question}"
#     resp = client.complete(prompt=prompt, model="claude‑2", max_tokens=300)
#     return resp['completion']

# def parse_skills_from_summary(summary):
#     # Example placeholder logic
#     return [line.strip() for line in summary.splitlines() if '-' in line and 'skill' in line.lower()]
