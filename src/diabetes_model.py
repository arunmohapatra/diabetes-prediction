import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


import joblib

# Load the dataset
file_path = "diabetes_prediction_dataset.csv"  # Replace with the correct path to your dataset
data = pd.read_csv(file_path)

# Inspect the dataset
print(data.head())
print(data.info())
print(data.describe())

# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Handle missing values (if any)
# Option 1: Drop rows with missing values
data.dropna(inplace=True)

# Option 2: Fill missing values (e.g., with the mean of each column)
# data.fillna(data.mean(), inplace=True)

# Split features and target
X = data.drop(columns=['diabetes'], axis=1)  # 'Diabetes' is the target column
y = data['diabetes']

# Ensure all columns are numeric (convert any non-numeric columns)
X = X.apply(pd.to_numeric, errors='coerce')

# Handle missing values in X after coercion (if any)
X.fillna(X.mean(), inplace=True)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, 
    y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y,
)


# Build a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the model
joblib.dump(model, "diabetes_model.pkl")
