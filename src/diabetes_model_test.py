import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Step 1: Load the trained model
model = joblib.load("diabetes_model.pkl")  # Replace with the correct path if needed

# Step 2: Prepare the new data for prediction
# Example: New data for prediction
new_data = pd.DataFrame({
    'gender': ['Male'],  # Categorical - Convert to numeric (e.g., Male=1, Female=0)
    'age': [75],
    'hypertension': [1],  # 1 = Yes, 0 = No
    'heart_disease': [0],  # 1 = Yes, 0 = No
    'smoking_history': ['current'],  # Categorical (Convert to numeric, e.g., Never=0, Former=1, Current=2)
    'bmi': [32],
    'HbA1c_level': [6.5],
    'blood_glucose_level': [150]

})

# Step 3: Preprocess the data (convert categorical variables to numeric)
# Convert 'gender' (e.g., Male=1, Female=0)
new_data['gender'] = new_data['gender'].map({'Male': 1, 'Female': 0})

# Convert 'smoking_history' (e.g., Never=0, Former=1, Current=2)
new_data['smoking_history'] = new_data['smoking_history'].map({'Never': 0, 'Former': 1, 'Current': 2})

# Ensure all columns are numeric and handle any missing values (if any)
new_data = new_data.apply(pd.to_numeric, errors='coerce')
new_data.fillna(new_data.mean(), inplace=True)

# Step 4: Standardize the new data using the same scaler used during training
scaler = StandardScaler()

# If you saved the scaler during training, you should load it:
# scaler = joblib.load('scaler.pkl')  # Uncomment if you saved the scaler separately

new_data_scaled = scaler.fit_transform(new_data)  # Standardize the new data (or use the previously fitted scaler)

# Step 5: Predict using the loaded model
prediction = model.predict(new_data_scaled)

# Step 6: Display the prediction result
# 1 = Diabetic, 0 = Non-Diabetic
if prediction[0] == 1:
    print("The person is predicted to be Diabetic.")
else:
    print("The person is predicted to be Non-Diabetic.")
