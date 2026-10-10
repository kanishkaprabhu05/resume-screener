import streamlit as st
import re

st.set_page_config(page_title="AI Resume Screener", page_icon="📄")

st.title("📄 AI Resume Screener")
st.write("HR Tool - Paste Resume & Job Description to get Match Score!")

st.subheader("1. Job Description")
job_desc = st.text_area("Paste Job Description here", placeholder="Eg: Need Python, Machine Learning, SQL...")

st.subheader("2. Candidate Resume")
resume = st.text_area("Paste Resume Text here", height=250, placeholder="Paste full resume text here...")

if st.button("🔍 Screen Resume"):
    if not job_desc or not resume:
        st.warning("Dei macha! Job Description and Resume rendu paste pannu da!")
    else:
        job_words = set(re.findall(r'\w+', job_desc.lower()))
        resume_words = set(re.findall(r'\w+', resume.lower()))
        tech_skills = ['python', 'java', 'sql', 'machine learning', 'ai', 'excel', 'power bi', 'react', 'javascript', 'streamlit', 'html', 'css']
        matched = []
        for skill in tech_skills:
            if skill in job_desc.lower() and skill in resume.lower():
                matched.append(skill)
        score = len(matched) * 20
        if score > 100:
            score = 95
        if len(job_words.intersection(resume_words)) > 10:
            score += 10
        if score > 100:
            score = 98
        st.divider()
        st.subheader(f"Result: {score}% Match")
        if score >= 80:
            st.success(f"🔥 SUPER MATCH DA! {score}% - Shortlist this candidate!")
        elif score >= 50:
            st.info(f"👍 Good Match - {score}% - Can consider")
        else:
            st.error(f"👎 Low Match - {score}% - Not suitable")
        st.write("✅ Matched Skills:", ", ".join(matched) if matched else "No direct tech skills matched")