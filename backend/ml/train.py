import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)

from preprocess import preprocess_data


# -----------------------------
# Load and preprocess dataset
# -----------------------------
df, label_encoders = preprocess_data(
    "data/processed/cleaned_data.csv"
)

# -----------------------------
# Create target variable
# -----------------------------
df["pass_fail"] = (df["exam_score"] >= 50).astype(int)

# -----------------------------
# Features & Targets
# -----------------------------
X = df.drop(columns=["exam_score", "pass_fail"])

y_score = df["exam_score"]

y_class = df["pass_fail"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train_score, y_test_score, y_train_class, y_test_class = train_test_split(
    X,
    y_score,
    y_class,
    test_size=0.20,
    random_state=42
)

# -----------------------------
# Classification Model
# -----------------------------
classifier = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

classifier.fit(X_train, y_train_class)

class_predictions = classifier.predict(X_test)

# -----------------------------
# Classification Metrics
# -----------------------------
accuracy = accuracy_score(y_test_class, class_predictions)

precision = precision_score(y_test_class, class_predictions)

recall = recall_score(y_test_class, class_predictions)

f1 = f1_score(y_test_class, class_predictions)

# -----------------------------
# Regression Model
# -----------------------------
regressor = LinearRegression()

regressor.fit(X_train, y_train_score)

score_predictions = regressor.predict(X_test)

# -----------------------------
# Regression Metrics
# -----------------------------
r2 = r2_score(y_test_score, score_predictions)

mae = mean_absolute_error(
    y_test_score,
    score_predictions
)

rmse = root_mean_squared_error(
    y_test_score,
    score_predictions
)

# -----------------------------
# Print Results
# -----------------------------
print("\n========== Classification ==========")

print(f"Accuracy : {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall   : {recall:.4f}")

print(f"F1 Score : {f1:.4f}")

print("\n========== Regression ==========")

print(f"R² Score : {r2:.4f}")

print(f"MAE      : {mae:.4f}")

print(f"RMSE     : {rmse:.4f}")

# -----------------------------
# Save Models
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(
    classifier,
    "models/classifier_model.pkl"
)

joblib.dump(
    regressor,
    "models/regression_model.pkl"
)

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

print("\nModels saved successfully.")