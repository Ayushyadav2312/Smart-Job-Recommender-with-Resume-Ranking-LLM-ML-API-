import os
from resume_parser import extract_text_from_pdf
from groq import Groq

def extract_summary_and_skills(file_path: str):
    resume_text = extract_text_from_pdf(file_path)

    client = Groq(api_key="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")

    prompt = f"Extract key skills and experince from this resume:\n\n{resume_text}"

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",  # or your preferred model
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    file_path = "Ayush_Resume.pdf"
    skills_summary = get_skills_from_resume(file_path)
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
