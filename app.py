import streamlit as st
import random
import pandas as pd

from utils.ats_score import calculate_ats_score
from utils.pdf_reader import extract_text
from utils.skills import extract_skills
from utils.interview_questions import questions
from utils.interview_evaluator import evaluate_answer

# PAGE SETTINGS

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# SIDEBAR

st.sidebar.title("AI Career Assistant")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Resume Analyzer",
        "Interview Assistant"
    ]
)

# =========================
# RESUME ANALYZER
# =========================

if menu == "Resume Analyzer":

    st.title("Resume Analyzer")

    st.markdown(
        """
        ## AI-Powered Resume Analysis Platform
        
        Upload your resume and compare it with job descriptions.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste Job Description"
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        skills = extract_skills(text)

        # ATS SCORE

        job_skills = extract_skills(job_description)

        scores = calculate_ats_score(
            text,
            skills,
            job_skills
            )

        score = scores["Total"]

        st.subheader("ATS Score Breakdown")

        chart_data = pd.DataFrame({

    "Category": [
        "Skills",
        "Projects",
        "Certifications",
        "Education",
        "Experience"
    ],

    "Score": [
        scores["Skills"],
        scores["Projects"],
        scores["Certifications"],
        scores["Education"],
        scores["Experience"]
    ]
})

        st.bar_chart(
            chart_data.set_index("Category")
        )

        # COLUMNS

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Detected Skills")

            st.write(skills)

        with col2:

            st.subheader("ATS Score")

            st.progress(score)

            st.write(score, "/ 100")

        # JOB MATCHING

        if job_description:

            job_skills = extract_skills(job_description)

            matched_skills = []

            missing_skills = []

            for skill in job_skills:

                if skill in skills:
                    matched_skills.append(skill)

                else:
                    missing_skills.append(skill)

            if len(job_skills) > 0:

                match_percent = int(
                    (len(matched_skills) / len(job_skills)) * 100
                )

            else:
                match_percent = 0

            st.subheader("Job Match Percentage")

            st.progress(match_percent)

            st.write(match_percent, "% Match")

            st.subheader("Matched Skills")

            st.write(matched_skills)

            st.subheader("Missing Skills")

            st.write(missing_skills)

# =========================
# INTERVIEW ASSISTANT
# =========================

if menu == "Interview Assistant":

    st.title("AI Interview Assistant")

    st.markdown(
        """
        ## AI Mock Interview System
        
        Practice interview questions and receive instant feedback.
        """
    )

    question = random.choice(questions)

    st.subheader("Interview Question")

    st.write(question)

    answer = st.text_area(
        "Enter Your Answer"
    )

    if answer:
        score, feedback = evaluate_answer(
        question,
        answer
)

        st.subheader("Interview Score")

        st.progress(score)

        st.write(score, "/ 100")

        st.subheader("Feedback")

        for item in feedback:
            st.write("-", item)

        if score >= 80:
            st.success(
        "Excellent answer"
        )

        elif score >= 50:
            st.warning(
        "Good answer, but can improve"
    )

        else:
            st.error(
        "Answer needs improvement"
    )

        

# FOOTER

st.markdown("---")

st.caption(
    "Developed by Naren Raj using Python, Streamlit and NLP"
)