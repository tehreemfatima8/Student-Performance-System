def generate_recommendations(student_data, prediction_result):
    """
    Generate personalized recommendations based on
    student input and AI prediction.
    """

    academic = []
    health = []
    technology = []
    overall = []

    # =========================
    # Convert numeric values
    # =========================

    student_data["age"] = int(student_data.get("age", 0))
    student_data["study_hours_per_day"] = float(student_data.get("study_hours_per_day", 0))
    student_data["social_media_hours"] = float(student_data.get("social_media_hours", 0))
    student_data["netflix_hours"] = float(student_data.get("netflix_hours", 0))
    student_data["attendance_percentage"] = float(student_data.get("attendance_percentage", 0))
    student_data["sleep_hours"] = float(student_data.get("sleep_hours", 0))
    student_data["exercise_frequency"] = float(student_data.get("exercise_frequency", 0))
    student_data["mental_health_rating"] = float(student_data.get("mental_health_rating", 0))

    # =========================
    # Academic Habits
    # =========================

    study_hours = student_data.get("study_hours_per_day", 0)

    if study_hours < 2:
        academic.append(
            f"You study only {study_hours} hour(s) daily. "
            "Increase your study time for better academic performance."
        )

    elif study_hours < 4:
        academic.append(
            f"You study {study_hours} hours daily. "
            "Increasing study time to around 5 hours may improve your results."
        )

    attendance = student_data.get("attendance_percentage", 0)

    if attendance < 75:
        academic.append(
            f"Your attendance is {attendance}%. "
            "Try maintaining above 85% attendance."
        )

    elif attendance < 90:
        academic.append(
            f"Your attendance is {attendance}%. "
            "Improving attendance can increase consistency."
        )

    # =========================
    # Health & Lifestyle
    # =========================

    sleep = student_data.get("sleep_hours", 0)

    if sleep < 6:
        health.append(
            f"You sleep only {sleep} hours/day. "
            "Aim for 7-8 hours for better focus."
        )

    elif sleep > 9:
        health.append(
            f"You sleep {sleep} hours/day. "
            "Maintain balanced sleeping hours."
        )

    exercise = student_data.get("exercise_frequency", 0)

    if exercise < 2:
        health.append(
            "Increase physical activity to improve concentration and energy."
        )

    diet = student_data.get("diet_quality", "").lower()

    if diet == "poor":
        health.append(
            "Improve your diet by adding nutritious meals."
        )

    elif diet == "fair":
        health.append(
            "A healthier diet can improve focus and productivity."
        )

    mental = student_data.get("mental_health_rating", 10)

    if mental <= 4:
        health.append(
            "Your mental health rating is low. "
            "Consider stress management activities."
        )

    # =========================
    # Technology Usage
    # =========================

    social = student_data.get("social_media_hours", 0)

    if social > 4:
        technology.append(
            f"You spend {social} hours/day on social media. "
            "Try reducing usage."
        )

    elif social > 2:
        technology.append(
            "Reducing social media usage slightly may create more study time."
        )

    netflix = student_data.get("netflix_hours", 0)

    if netflix > 3:
        technology.append(
            "Reduce entertainment screen time to improve productivity."
        )

    # =========================
    # Extracurricular
    # =========================

    extra = student_data.get(
        "extracurricular_participation",
        "No"
    )

    if extra.lower() == "no":
        academic.append(
            "Participating in extracurricular activities improves teamwork and confidence."
        )

    # =========================
    # Prediction Result
    # =========================

    predicted_score = prediction_result.get(
        "predicted_score",
        0
    )

    if predicted_score < 50:

        risk = "High"

        overall.append(
            f"Your predicted score is {predicted_score}. "
            "Focus immediately on improving your academic habits."
        )

    elif predicted_score < 70:

        risk = "Medium"

        overall.append(
            f"Your predicted score is {predicted_score}. "
            "Some improvements can increase your performance."
        )

    elif predicted_score < 85:

        risk = "Low"

        overall.append(
            f"Your predicted score is {predicted_score}. "
            "Good performance. Maintain your routine."
        )

    else:

        risk = "Very Low"

        overall.append(
            f"Excellent performance prediction: {predicted_score}. "
            "Continue your current habits."
        )

    return {
        "risk_level": risk,
        "Academic Habits": academic,
        "Health & Lifestyle": health,
        "Technology Usage": technology,
        "Overall Advice": overall
    }