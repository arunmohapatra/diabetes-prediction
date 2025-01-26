# M1: MLOps Foundations

**Objective**: Understand the basics of MLOps and implement a simple CI/CD pipeline for the project 'diabetes-prediction'

## Tasks

### 1. Set Up a CI/CD Pipeline
- **Use a CI/CD tool like GitHub Actions or GitLab CI to set up a pipeline for a sample machine learning project.**
  - Create a new repository on GitHub or GitLab.
  - Add a `.github/workflows` directory for GitHub Actions or a `.gitlab-ci.yml` file for GitLab CI.
  - Define the pipeline stages: linting, testing, and deploying a simple machine learning model.

- **Include stages for linting, testing, and deploying a simple machine learning model.**
  - **Linting:** Use a linter like `flake8` to check the code quality.
  - **Testing:** Use a testing framework like `pytest` to run unit tests.
  - **Deploying:** Deploy the model to a cloud service or a local server.

### 2. Version Control
- **Implement version control for your project using Git.**
  - Initialize a Git repository in your project directory.
  - Add and commit your project files.

- **Demonstrate branching, merging, and pull requests.**
  - Create a new branch for a feature or bug fix.
  - Make changes and commit them to the new branch.
  - Open a pull request to merge the changes into the main branch.
  - Review and merge the pull request.

## Deliverables
- **A report detailing the CI/CD pipeline stages.**
  - Describe each stage of the pipeline and its purpose.
  - Include configuration files and scripts used in the pipeline.

- **Screenshots or logs showing successful runs of the pipeline.**
  - Provide evidence of successful linting, testing, and deployment stages.

- **A Git repository link with branches and merge history.**
  - Share the link to your Git repository.
  - Ensure the repository includes branches and a history of merges.

## Example CI/CD Pipeline Configuration

### GitHub Actions
```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8
      - name: Lint code
        run: flake8 .

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest
      - name: Run tests
        run: pytest

  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy model
        run: echo "Deploying model..."
GitLab CI
stages:
  - lint
  - test
  - deploy

lint:
  stage: lint
  script:
    - pip install flake8
    - flake8 .

test:
  stage: test
  script:
    - pip install pytest
    - pytest

deploy:
  stage: deploy
  script:
    - echo "Deploying model..."
Example Git Commands
Initialize Git Repository
git init
git add .
git commit -m "Initial commit"
Create and Merge Branch
git checkout -b feature-branch
# Make changes and commit them
git add .
git commit -m "Add new feature"
git checkout main
git merge feature-branch
Open Pull Request
Push the branch to the remote repository.
Open a pull request on GitHub or GitLab.
Review and merge the pull request.
```
