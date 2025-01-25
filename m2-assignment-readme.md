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
## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### Sample Output

```plaintext
Collecting dvc==3.58.0 (from -r requirements.txt (line 6))
    Downloading dvc-3.58.0-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\work\py312\lib\site-packages (from pandas==2.2.0->-r requirements.txt (line 1)) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in c:\work\py312\lib\site-packages (from pandas==2.2.0->-r requirements.txt (line 1)) (2024.2)
Requirement already satisfied: tzdata>=2022.7 in c:\work\py312\lib\site-packages (from pandas==2.2.0->-r requirements.txt (line 1)) (2025.1)
Requirement already satisfied: scipy>=1.6.0 in c:\work\py312\lib\site-packages (from scikit-learn==1.6.1->-r requirements.txt (line 3)) (1.15.1)
Requirement already satisfied: threadpoolctl>=3.1.0 in c:\work\py312\lib\site-packages (from scikit-learn==1.6.1->-r requirements.txt (line 3)) (3.5.0)
Requirement already satisfied: colorama in c:\work\py312\lib\site-packages (from pytest==8.3.4->-r requirements.txt (line 5)) (0.4.6)
Requirement already satisfied: iniconfig in c:\work\py312\lib\site-packages (from pytest==8.3.4->-r requirements.txt (line 5)) (2.0.0)
Requirement already satisfied: packaging in c:\work\py312\lib\site-packages (from pytest==8.3.4->-r requirements.txt (line 5)) (24.2)
Requirement already satisfied: pluggy<2,>=1.5 in c:\work\py312\lib\site-packages (from pytest==8.3.4->-r requirements.txt (line 5)) (1.5.0)
Collecting attrs>=22.2.0 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading attrs-25.1.0-py3-none-any.whl.metadata (10 kB)
Collecting celery (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading celery-5.4.0-py3-none-any.whl.metadata (21 kB)
Collecting configobj>=5.0.9 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading configobj-5.0.9-py2.py3-none-any.whl.metadata (3.2 kB)
Collecting distro>=1.3 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting dpath<3,>=2.1.0 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dpath-2.2.0-py3-none-any.whl.metadata (15 kB)
Collecting dulwich (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dulwich-0.22.7-cp312-cp312-win_amd64.whl.metadata (4.5 kB)
Collecting dvc-data<3.17,>=3.16.2 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_data-3.16.8-py3-none-any.whl.metadata (5.0 kB)
Collecting dvc-http>=2.29.0 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_http-2.32.0-py3-none-any.whl.metadata (1.3 kB)
Collecting dvc-objects (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_objects-5.1.0-py3-none-any.whl.metadata (3.7 kB)
Collecting dvc-render<2,>=1.0.1 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_render-1.0.2-py3-none-any.whl.metadata (5.4 kB)
Collecting dvc-studio-client<1,>=0.21 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_studio_client-0.21.0-py3-none-any.whl.metadata (4.3 kB)
Collecting dvc-task<1,>=0.3.0 (from dvc==3.58.0->-r requirements.txt (line 6))
    Downloading dvc_task-0.40.2-py3-none-any.whl.metadata (10.0 kB)
Collecting flatten_dict<1,>=0.4.1 (from dvc==3.58.0->-r requirements.txt (line 6))
```

### Initialize DVC in your project

To initialize DVC in your project, run the following command:

```bash
dvc init
```

Sample Output:

```plaintext
(py312) C:\Users\sagar\OneDrive\Documents\My Docs\Education\BITS - MTECH\SME 3\MLOps\Assignment-1\diabetes-prediction>dvc init 
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/iterative/dvc>
```

## Adding DVC Files to GitHub

After initializing DVC and adding your dataset, you need to add the DVC files to your Git repository. Run the following command:

```bash
git status
git add .dvc
```

Sample Output:

```plaintext
(py312) C:\Users\sagar\OneDrive\Documents\My Docs\Education\BITS - MTECH\SME 3\MLOps\Assignment-1\diabetes-prediction>git status
On branch feature/code-cleanup
Your branch is up to date with 'origin/feature/code-cleanup'.

Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
                new file:   .dvc/.gitignore
                new file:   .dvc/config
                new file:   .dvcignore
                new file:   .gitignore

Changes not staged for commit:
    (use "git add/rm <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
                modified:   README.md
                modified:   m2-assignment-readme.md
                deleted:    model/diabetes_model.pkl
                modified:   requirements.txt
                modified:   src/diabetes_model.py

Untracked files:
    (use "git add <file>..." to include in what will be committed)
                models/
```

To commit the changes, run:

```bash
git add .
git commit -m "Add DVC files and dataset"
git push origin feature/code-cleanup
```

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