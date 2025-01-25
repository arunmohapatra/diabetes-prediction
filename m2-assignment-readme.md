# Machine Learning Project

## Tasks

### 1. Experiment Tracking

- **Use MLflow to track experiments for a machine learning project.**
- **Record metrics, parameters, and results of at least three different model training runs.**

### 2. Data Versioning

- **Use DVC (Data Version Control) to version control a dataset used in your project.**
- **Show how to revert to a previous version of the dataset.**

## Deliverables

- **MLflow experiment logs with different runs and their results.**
- **A DVC repository showing different versions of the dataset.**

---

## Step-by-Step Instructions

### 1. Experiment Tracking with MLflow

1. **Install MLflow:**
   ```bash
   pip install mlflow

2. **Set up MLflow in your project:**

```bash
import mlflow
import mlflow.sklearn

mlflow.set_experiment("my_experiment")
Track your experiments:

with mlflow.start_run():
    # Your model training code here
    mlflow.log_param("param_name", param_value)
    mlflow.log_metric("metric_name", metric_value)
    mlflow.sklearn.log_model(model, "model")
```
2. **Record metrics, parameters, and results for at least three different runs:**

```
Run 1: python train.py --param1 value1 --param2 value2
Run 2: python train.py --param1 value3 --param2 value4
Run 3: python train.py --param1 value5 --param2 value6
```
3. **Data Versioning with DVC**

Install DVC:

pip install dvc
Initialize DVC in your project:

dvc init
Add your dataset to DVC:

dvc add data/dataset.csv
Commit the changes:

git add data/dataset.csv.dvc .gitignore
git commit -m "Add dataset to DVC"
Show how to revert to a previous version of the dataset:

dvc checkout <commit_hash>