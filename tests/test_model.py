import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

# Constants
TEST_DATA_PATH = "../data/diabetes_prediction_dataset.csv"
MODEL_PATH = "models/diabetes_model.pkl"


@pytest.fixture
def load_data():
    """Fixture to load the dataset."""
    assert Path(TEST_DATA_PATH).is_file(), f"File {TEST_DATA_PATH} not found."
    data = pd.read_csv(TEST_DATA_PATH)
    return data


def test_data_loading(load_data):
    """Test if the dataset loads correctly."""
    data = load_data
    assert not data.empty, "Dataset is empty."
    assert "diabetes" in data.columns, "'diabetes' column missing dataset."


def test_model_training(load_data):
    """Test the model training process."""
    data = load_data

    # Preprocess the data
    data.dropna(inplace=True)
    X = (
        data.drop(columns=["diabetes"], axis=1)
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )
    y = data["diabetes"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    assert accuracy > 0.5, "Model accuracy is too low."
    joblib.dump(model, MODEL_PATH)

    # Ensure the model is saved
    assert Path(MODEL_PATH).is_file(), "Model file was not saved."


def test_model_prediction():
    """Test model prediction using a saved model."""
    assert Path(MODEL_PATH).is_file(), "Model file does not exist."
    model = joblib.load(MODEL_PATH)

    # Create a mock input
    mock_input = np.random.rand(1, 8)  # Assuming 8 features
    prediction = model.predict(mock_input)

    assert prediction.shape == (1,), "Prediction output shape is incorrect."
