def evaluate_answer(question, answer):

    question = question.lower()
    answer = answer.lower()

    score = 0

    feedback = []

    # =========================
    # QUESTION CATEGORIES
    # =========================

    categories = {

        "strengths": {

            "keywords": [
                "hardworking",
                "teamwork",
                "leadership",
                "adaptable",
                "problem solving",
                "communication"
            ],

            "action_words": [
                "improved",
                "solved",
                "managed",
                "organized"
            ]
        },

        "project": {

            "keywords": [
                "developed",
                "system",
                "application",
                "frontend",
                "backend",
                "database",
                "api",
                "streamlit",
                "python"
            ],

            "action_words": [
                "implemented",
                "created",
                "designed",
                "built"
            ]
        },

        "machine learning": {

            "keywords": [
                "model",
                "training",
                "algorithm",
                "prediction",
                "dataset",
                "classification",
                "accuracy"
            ],

            "action_words": [
                "trained",
                "implemented",
                "optimized"
            ]
        },

        "programming": {

            "keywords": [
                "python",
                "java",
                "c++",
                "sql",
                "javascript",
                "coding"
            ],

            "action_words": [
                "developed",
                "coded",
                "built"
            ]
        }
    }

    # =========================
    # DETECT CATEGORY
    # =========================

    selected_category = None
    question_type = "descriptive"

    list_questions = [

    "what programming languages",
    "what skills",
    "which technologies",
    "list",
    "tools"
]

    for item in list_questions:

        if item in question:

            question_type = "list"
            break

    for category in categories:

        if category in question:

            selected_category = categories[category]
            break

    # DEFAULT CATEGORY

    if selected_category is None:

        selected_category = {

            "keywords": [],
            "action_words": []
        }

    # =========================
    # RELEVANCE SCORE
    # =========================

    relevance_score = 0      

    for word in selected_category["keywords"]:

        if word in answer:

            relevance_score += 5

    relevance_score = min(relevance_score, 50)

    score += relevance_score

    # =========================
    # ACTION WORD SCORE
    # =========================

    action_score = 0

    for word in selected_category["action_words"]:

        if word in answer:

            action_score += 5

    action_score = min(action_score, 20)

    score += action_score

    # =========================
    # COMMUNICATION SCORE
    # =========================

    communication_score = 0

    word_count = len(answer.split())

# LIST TYPE QUESTIONS

    if question_type == "list":
        if word_count >= 2:
            communication_score = 20

# DESCRIPTIVE QUESTIONS

    else:
        if word_count > 25:
            communication_score += 10

        if "." in answer:
            communication_score += 10

    score += communication_score

    # =========================
    # PENALTY FOR VERY SHORT ANSWERS
    # =========================

    if question_type != "list":

        if word_count < 10:

            score -= 20

            feedback.append(
            "Answer is too short."
        )


    # =========================
    # FEEDBACK
    # =========================

    if relevance_score < 15:

        feedback.append(
            "Try adding more relevant points."
        )

    if action_score < 5:

        feedback.append(
            "Use stronger action words."
        )

    if communication_score < 10:

        feedback.append(
            "Improve explanation clarity."
        )

    # =========================
    # FINAL SCORE
    # =========================

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score, feedback