import joblib
import pandas as pd
import os


# ==========================================================
# Load Trained Models
# ==========================================================

MODEL_DIR = "models"

classifier = joblib.load(
    os.path.join(MODEL_DIR, "classifier_model.pkl")
)

regressor = joblib.load(
    os.path.join(MODEL_DIR, "regression_model.pkl")
)

label_encoders = joblib.load(
    os.path.join(MODEL_DIR, "label_encoders.pkl")
)


# ==========================================================
# Prediction Function
# ==========================================================

def predict_student(student_data):
    """
    Predict student's exam score and pass/fail status.

    Parameters:
        student_data (dict): Dictionary containing student information.

    Returns:
        dict: Prediction results.
    """

    # Convert dictionary into DataFrame
    df = pd.DataFrame([student_data])

    # Categorical columns used during training
    categorical_columns = [
        "gender",
        "part_time_job",
        "diet_quality",
        "parental_education_level",
        "internet_quality",
        "extracurricular_participation"
    ]

    # Encode categorical values
    for column in categorical_columns:

        if column in label_encoders:

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
                .str.lower()
            )

            try:
                df[column] = label_encoders[column].transform(df[column])

            except ValueError:

                valid_values = ", ".join(label_encoders[column].classes_)

                raise ValueError(
                    f"Invalid value '{df[column].iloc[0]}' "
                    f"for '{column}'. "
                    f"Allowed values are: {valid_values}"
                )

    # ==========================================================
    # AI Predictions
    # ==========================================================

    # Predict exam score
    predicted_score = float(regressor.predict(df)[0])

    # Predict pass/fail using classifier
    predicted_class = int(classifier.predict(df)[0])

    # Prediction confidence
    confidence = float(
        classifier.predict_proba(df).max() * 100
    )

    # ==========================================================
    # Expert Rules (Business Rules)
    # ==========================================================

    # Rule 1:
    # Student studies 0 hours and attendance is below 50%
    # Force prediction to Fail.

    if (
        student_data["study_hours_per_day"] == 0
        and student_data["attendance_percentage"] < 65
    ):
        predicted_class = 0
       # confidence = 100.0

    # ==========================================================
    # Final Result
    # ==========================================================

    result = {

        "predicted_score": round(predicted_score, 2),

        "prediction": "Pass" if predicted_class == 1 else "Fail",

        "confidence": round(confidence, 2)

    }

    return result