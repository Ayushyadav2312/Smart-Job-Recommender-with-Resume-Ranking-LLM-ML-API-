import streamlit as st
# from dotenv import load_dotenv
import os
from groq import Groq

# load_dotenv()
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_summary_and_skills(file_path):
    from resume_parser import extract_text_from_pdf
    resume_text = extract_text_from_pdf(file_path)
    prompt = f"Extract key skills and experience from this resume:\n\n{resume_text}"
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content.split("\n")  # Returns list of skills/experience

def extract_skills_from_jobs(description: str):
    prompt = f"Extract key skills, qualifications, and experience required from this job description:\n\n{description}"
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content.split("\n")

def ask_resume_bot(summary_skills, user_question):
    if any(word in user_question.lower() for word in ["ats", "resume", "format", "font", "cv", "interview"]):
        prompt = f"You are a career expert. Provide detailed guidance to improve resume, ATS score, formatting, and career tips. Question: {user_question}"
    else:
        prompt = f"You are a career coach. Candidate info:\n{summary_skills}\n\nQuestion: {user_question}"

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content
