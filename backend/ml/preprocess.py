import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(file_path):
    """
    Load and preprocess the dataset.
    Returns:
        df: processed dataframe
        label_encoders: dictionary of fitted label encoders
    """

    # Load dataset
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna(df[column].mode()[0])
        else:
            df[column] = df[column].fillna(df[column].median())

    # Encode categorical columns
    label_encoders = {}

    categorical_columns = [
        "gender",
        "part_time_job",
        "diet_quality",
        "parental_education_level",
        "internet_quality",
        "extracurricular_participation"
    ]

    for column in categorical_columns:
        if column in df.columns:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
            label_encoders[column] = encoder

    return df, label_encoders