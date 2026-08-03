# 03. Objectives

## Primary Objective

To develop a Machine Learning–based system that classifies website URLs as **Phishing** or **Legitimate** using lexical (URL-based) features, and present the prediction through a simple and user-friendly Streamlit web application.

---

## Secondary Objectives

### 1. Data Collection & Preprocessing

Collect a reliable public phishing URL dataset and prepare it for Machine Learning by cleaning the data, handling missing values (if any), removing inconsistencies, and organizing it into a suitable format for model training.

---

### 2. Feature Engineering

Extract meaningful lexical (URL-based) features such as URL length, number of dots, hyphens, digits, special characters, subdomains, presence of an IP address, and other structural characteristics that help distinguish phishing URLs from legitimate ones.

---

### 3. Model Training & Evaluation

Train one or more Machine Learning classification models using Scikit-learn and evaluate their performance using appropriate metrics such as:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

to determine the effectiveness of the model.

---

### 4. Interface Development

Develop a simple and interactive Streamlit web application that enables users to:

- Enter a website URL.
- Predict whether the URL is **Phishing** or **Legitimate**.
- Display the prediction along with the model's confidence score.

---

### 5. Documentation & Version Control

Maintain comprehensive project documentation throughout the development process, organize the project using a clean folder structure, and use Git and GitHub with meaningful commit messages to demonstrate good software engineering and version control practices.

---

### 6. Testing & Validation

Test the application using a variety of legitimate, phishing, invalid, and edge-case URLs to verify that the system produces consistent and reliable predictions under different scenarios.

---

## Notes on Scope

This version of the project focuses exclusively on **lexical (URL-based) feature extraction**, meaning all predictions are made using information contained within the URL itself.

To keep the project realistic, self-contained, and suitable for a college mini project, the system does **not** rely on external services such as:

- WHOIS lookup
- Domain age analysis
- SSL certificate validation
- DNS reputation checks
- Threat Intelligence APIs

These advanced capabilities are considered future enhancements and may be incorporated in later versions of the project.