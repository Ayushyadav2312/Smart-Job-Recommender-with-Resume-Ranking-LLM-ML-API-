import streamlit as st
from llm_helpers import extract_summary_and_skills, ask_resume_bot
from job_recommender import recommend_from_listings
import json

st.set_page_config(page_title="Smart Job Recommender", layout="wide")

# Load job JSON
with open("Jobs_data.json", "r", encoding="utf-8") as f:
    job_listings = json.load(f)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🚀 Smart Job Recommender with Chatbot")

# Resume Upload
uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded:
    resume_skills = extract_summary_and_skills(uploaded)
    st.subheader("📝 Extracted Skills & Experience")
    st.write(", ".join(resume_skills))

    # Show top jobs
    if st.button("Show Top Jobs"):
        recommendations = recommend_from_listings(resume_skills, job_listings, top_n=10)
        st.subheader("💼 Top Job Matches")

        # Display jobs in 2 columns
        for i in range(0, len(recommendations), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(recommendations):
                    job = recommendations[i + j]
                    with col:
                        st.markdown(f"### {job['Job Name']} at {job['Company Name']}")
                        st.markdown(f"📍 **Location:** {job['Location']}  |  🕒 **YOE:** {job['YOE']}  |  🎓 **Qualification:** {job['Qualification:']}")
                        st.markdown(f"💡 **Skills Required:** {job['Skills']}")
                        st.progress(int(job['score']*100))  # Skill match bar
                        if job.get("Website"):
                            st.markdown(f"[🔗 Apply Here]({job['Website']})")
                        st.markdown("---")

    # Chatbot Section
    st.divider()
    st.subheader("💬 Ask the Careers Chatbot")
    user_q = st.chat_input("Ask about resume tips, ATS score, formatting, career advice…")
    if user_q:
        st.session_state.chat_history.append({"role": "user", "content": user_q})
        response = ask_resume_bot(resume_skills, user_q)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
