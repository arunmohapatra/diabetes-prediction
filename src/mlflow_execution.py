from time import sleep
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

data = pd.read_csv("../data/diabetes_prediction_dataset.csv")
print(data.info())
X = data.drop(columns=["diabetes"], axis=1)
# Ensure all columns are numeric (convert any non-numeric columns)
X = X.apply(pd.to_numeric, errors="coerce")

Y = data.diabetes.copy() #["diabetes"].copy()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

mlflow.set_experiment("Random Forest Experiment")

experiments = [
    {"n_estimators": 75, "random_state": 19},
    {"n_estimators": 100, "random_state": 29},
    {"n_estimators": 125, "random_state": 57},
]

for exp in experiments:
    with mlflow.start_run(): 
        n_estimators = exp["n_estimators"]
        random_state = exp["random_state"]
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("random_state", random_state)
        print(f"Running with n_estimators={n_estimators} and random_state={random_state}")
        rf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        rf.fit(X_train, Y_train)
        Y_pred = rf.predict(X_test)

        mse = mean_squared_error(Y_test, Y_pred)
        r2 = r2_score(Y_test, Y_pred)
        
        print(f"Mean Squared Error: {mse}")
        print(f"R2 Score: {r2}")
        
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        mlflow.sklearn.log_model(rf, "rf-default")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
        sleep(5)