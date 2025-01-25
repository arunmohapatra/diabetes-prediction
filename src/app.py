from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from sklearn.preprocessing import StandardScaler


# Initialize Flask application
app = Flask(__name__)


# Load the trained model and scaler
print("Current Working Directory:", os.getcwd())
model = joblib.load("diabetes_model.pkl")
scaler = StandardScaler()


@app.route("/")
def home():
    return "Diabetes Prediction API is running!"


# API endpoint for prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse input JSON
        input_data = request.get_json()

        # Convert input JSON to DataFrame
        data = pd.DataFrame([input_data])

        # Ensure all columns are numeric
        data = data.apply(pd.to_numeric, errors="coerce")

        # Standardize the input features
        data_scaled = scaler.fit_transform(data)

        # Make predictions
        prediction = model.predict(data_scaled)

        # Return the prediction as JSON
        result = {"prediction": int(prediction[0])}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
