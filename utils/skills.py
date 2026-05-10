import re

# ---------------- CLEAN TEXT ---------------- #

def clean_text(text):

    # convert to lowercase
    text = text.lower()

    # remove special characters except +
    text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text


# ---------------- SKILLS DATABASE ---------------- #

skills_db = [

    # Programming Languages
    "python",
    "c",
    "c++",
    "java",
    "javascript",

    # Web Development
    "html",
    "css",
    "react",
    "nodejs",

    # Database
    "sql",
    "mysql",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",

    # Tools
    "git",
    "github",
    "streamlit",
    "flask",

    # CS Fundamentals
    "data structures",
    "oop",
    "operating system",
    "dbms",

    # Soft Skills
    "problem solving",
    "communication",
    "teamwork"
]


# ---------------- SKILL EXTRACTION FUNCTION ---------------- #

def extract_skills(text):

    # clean text
    text = clean_text(text)

    detected_skills = set()

    for skill in skills_db:

        # special handling for c++
        if skill == "c++":

            if "c++" in text:
                detected_skills.add(skill)

        # special handling for c
        elif skill == "c":

            pattern = r'(?<!\w)c(?!\w)'

            if re.search(pattern, text):
                detected_skills.add(skill)

        else:

            pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

            if re.search(pattern, text):
                detected_skills.add(skill)

    return sorted(list(detected_skills))


# ---------------- MATCHING FUNCTION ---------------- #

def match_skills(resume_text, job_description):

    # extract skills
    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    # matched skills
    matched_skills = sorted(
        list(set(resume_skills) & set(job_skills))
    )

    # missing skills
    missing_skills = sorted(
        list(set(job_skills) - set(resume_skills))
    )

    # match percentage
    if len(job_skills) > 0:

        match_percentage = int(
            (
                len(matched_skills)
                / len(job_skills)
            ) * 100
        )

    else:
        match_percentage = 0

    return {

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "match_percentage": match_percentage
    }


# ---------------- EXAMPLE ---------------- #

resume_text = """
Python Basics
C++ Programming
AI Career Assistant project using Streamlit
Problem Solving and Teamwork
"""

job_description = """
Looking for Python developer with SQL,
Machine Learning, Git, HTML, CSS and JavaScript.
"""

result = match_skills(
    resume_text,
    job_description
)

print(result)