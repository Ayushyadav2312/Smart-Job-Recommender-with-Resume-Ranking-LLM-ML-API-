import streamlit as st
from resume_parser import extract_text_from_pdf
from llm_helpers import extract_summary_and_skills, ask_resume_bot
from job_api import fetch_jobs_via_api
from job_recommender import recommend_from_listings

st.set_page_config(page_title="Job Recommender", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🔍 Smart Job Recommender with Chatbot")

uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf","DOCX"])
if uploaded:
    resume_text = extract_text_from_pdf(uploaded)
    st.subheader("Extracted Resume Text")
    st.write(resume_text[:1000] + "...")

    if st.button("Analyze Resume"):
        summary, skills = extract_summary_and_skills(resume_text)
        st.subheader("Resume Summary")
        st.json(summary)

        listings = fetch_jobs_via_api(keywords=", ".join(skills), location="India")
        recommendations = recommend_from_listings(resume_text, listings, top_n=5)

        st.subheader("💼 Top Job Matches")
        for job in recommendations:
            st.markdown(f"**{job['title']}** at *{job['company']}* — {job['location']} — Match: {job['score']:.2%}")
            if job.get("url"):
                st.markdown(f"[View Job]({job['url']})")

    st.divider()
    st.subheader("💬 Ask the Careers Chatbot")
    user_q = st.chat_input("Ask: What job suits me or resume tips…")
    if user_q:
        st.session_state.chat_history.append({"role": "user", "content": user_q})
        response = ask_resume_bot(summary, skills, user_q)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
