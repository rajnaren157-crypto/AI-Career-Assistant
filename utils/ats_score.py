import re

def calculate_ats_score(text, skills, job_skills):

    text = text.lower()

    scores = {}

    # =========================
    # SKILLS SCORE
    # =========================

    matched_skills = []

    for skill in job_skills:

        if skill in skills:
            matched_skills.append(skill)

    if len(job_skills) > 0:

        skills_score = (
            len(matched_skills) / len(job_skills)
        ) * 40

    else:
        skills_score = 0

    scores["Skills"] = round(skills_score)

    # =========================
    # PROJECT SCORE
    # =========================

    project_keywords = [
        "project",
        "developed",
        "built",
        "application",
        "system",
        "website",
        "model"
    ]

    project_count = 0

    for word in project_keywords:

        if word in text:
            project_count += 1

    project_score = min(project_count * 4, 20)

    scores["Projects"] = round(project_score)

    # =========================
    # CERTIFICATION SCORE
    # =========================

    certification_keywords = [
        "certification",
        "certified",
        "course",
        "udemy",
        "coursera",
        "nptel"
    ]

    certification_count = 0

    for word in certification_keywords:

        if word in text:
            certification_count += 1

    certification_score = min(
        certification_count * 2,
        10
    )

    scores["Certifications"] = round(
        certification_score
    )

    # =========================
    # EDUCATION SCORE
    # =========================

    education_keywords = [
        "b.tech",
        "b.e",
        "cgpa",
        "college",
        "university"
    ]

    education_score = 0

    for word in education_keywords:

        if word in text:
            education_score = 10
            break

    scores["Education"] = education_score

    # =========================
    # EXPERIENCE SCORE
    # =========================

    experience_keywords = [
        "internship",
        "experience",
        "worked",
        "company"
    ]

    experience_count = 0

    for word in experience_keywords:

        if word in text:
            experience_count += 1

    experience_score = min(
        experience_count * 2,
        10
    )

    scores["Experience"] = round(
        experience_score
    )

    # =========================
    # FINAL SCORE
    # =========================

    total_score = sum(scores.values())

    if total_score > 100:
        total_score = 100

    scores["Total"] = total_score

    return scores