import os


class Config:
    """
    Central configuration file for the AI Student Performance System.
    All project paths and application settings are managed here.
    """

    # -----------------------------
    # Flask Settings
    # -----------------------------
    SECRET_KEY = "student-performance-ai"

    # -----------------------------
    # Base Directory
    # -----------------------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # -----------------------------
    # Dataset Path
    # -----------------------------
    DATASET_PATH = os.path.join(
        BASE_DIR,
        "dataset",
        "student_dataset.csv"
    )

    # -----------------------------
    # Model Paths
    # -----------------------------
    CLASSIFIER_MODEL = os.path.join(
        BASE_DIR,
        "models",
        "classifier_model.pkl"
    )

    REGRESSION_MODEL = os.path.join(
        BASE_DIR,
        "models",
        "regression_model.pkl"
    )

    LABEL_ENCODERS = os.path.join(
        BASE_DIR,
        "models",
        "label_encoders.pkl"
    )