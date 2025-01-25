# Project Overview

This project includes setup and execution details for running machine learning experiments and CI/CD pipelines using various tools such as `make`, `MLflow`, and `DVC`. Follow the step-by-step instructions to get started.

---

## Installation Guide

### Prerequisites

Ensure you have Python 3.12.8 installed. You can download it from the official Python website:  
[https://www.python.org/downloads/release/python-3128/](https://www.python.org/downloads/release/python-3128/)

3.12.8 Windows installer [64-bit](https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe)

### Step 1: Install Chocolatey (Windows Only)
If you're using Windows, install Chocolatey package manager by following the instructions on the official website:  
[https://chocolatey.org/install](https://chocolatey.org/install)

### Step 2: Install `make` via Chocolatey
Once Chocolatey is installed, open a PowerShell terminal as Administrator and run:

```powershell
choco install make
```

Verify the installation by running:

```powershell
make --version
```

If the version is displayed, `make` is installed successfully.

---

## Project Setup

### Step 3: Install Python Dependencies

Ensure you have Python installed, then install the required dependencies using:

```bash
pip install -r requirements.txt
```

The project dependencies include:

- pandas==2.2.0
- numpy==2.0.0
- scikit-learn==1.6.1
- joblib==1.4.2
- pytest==8.3.4

---

## Running the Project

### Step 4: Default Run Command

To execute the default command specified in the `Makefile`, simply run:

```bash
make
```

This will execute the primary target defined in the `Makefile` and initiate necessary steps such as running tests or deploying the model.

---

## Child Pages

Refer to the following sub-pages for more specific details on different modules:

- [M1: MLOps Foundations](m1-assignment-readme.md): Overview of CI/CD pipeline setup and version control practices.
- [M2: Machine Learning Project](m2-assignment-readme.md): Instructions for experiment tracking with MLflow and data versioning with DVC.

---

## Additional Resources

- [Chocolatey Documentation](https://docs.chocolatey.org/)
- [Makefile Documentation](https://www.gnu.org/software/make/manual/make.html)
- [Python Package Installation](https://pip.pypa.io/en/stable/user_guide/)
