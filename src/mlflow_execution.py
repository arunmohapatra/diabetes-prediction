import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

# Load the dataset
data = pd.read_csv("../data/diabetes_prediction_dataset.csv")

# Display dataset info
print(data.info())

# Separate features and target variable
X = data.drop(columns=["diabetes"], axis=1)

# Ensure all columns are numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Target variable
Y = data["diabetes"].copy()

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Set the MLflow experiment
mlflow.set_experiment("Random Forest Experiment")

# Define experiment parameters
experiments = [
    {"n_estimators": 75, "random_state": 19},
    {"n_estimators": 100, "random_state": 29},
    {"n_estimators": 125, "random_state": 57},
]

# Run experiments
for exp in experiments:
    with mlflow.start_run():
        # Retrieve parameters
        n_estimators = exp["n_estimators"]
        random_state = exp["random_state"]

        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("random_state", random_state)

        print(f"Running with n_estimators={n_estimators}, "
        f"random_state={random_state}")


        # Initialize and train the Random Forest model
        rf = RandomForestClassifier(
         n_estimators=n_estimators,
         random_state=random_state
        )

        rf.fit(X_train, Y_train)

        # Predict on the test set
        Y_pred = rf.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(Y_test, Y_pred)
        r2 = r2_score(Y_test, Y_pred)

        print(f"Mean Squared Error: {mse}")
        print(f"R2 Score: {r2}")

        # Log metrics to MLflow
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)

        # Log the model to MLflow
        mlflow.sklearn.log_model(rf, "rf-default")
        print(f"Model saved in run {mlflow.active_run().info.run_uuid}")

        # Pause between experiments to avoid any conflicts
        time.sleep(5)
