# 03. Objectives

## Primary Objective

To develop **TrustLens**, an AI-based Website Trust & Phishing Risk Analyzer that uses Machine Learning, URL feature analysis, and rule-based cybersecurity checks to assess the trustworthiness of websites and help users make safer decisions before visiting suspicious links.

The system will classify websites as **Legitimate** or **Phishing**, generate a **Trust Score**, provide a **Confidence Score**, explain suspicious characteristics, and offer security recommendations through a simple Streamlit interface.

---

## Secondary Objectives

### 1. Data Collection & Preprocessing

Collect a suitable public phishing URL dataset and prepare it for Machine Learning by:

- Cleaning the dataset
- Handling missing values
- Removing duplicate entries
- Understanding class distribution
- Preparing data for feature extraction and model training

---

### 2. URL Feature Engineering

Extract meaningful lexical (URL-based) features such as:

- URL Length
- Number of Dots
- Number of Slashes
- Number of Digits
- Special Characters
- Presence of HTTPS
- Number of Subdomains
- Prefix/Suffix (-)
- Use of IP Address
- Suspicious Keywords

These features will help distinguish phishing websites from legitimate websites.

---

### 3. Rule-Based Cybersecurity Analysis

Implement additional cybersecurity checks alongside Machine Learning, including:

- Missing HTTPS
- IP Address Usage
- Excessive URL Length
- Suspicious Characters
- Too Many Subdomains
- Presence of Risky Keywords

This objective demonstrates how practical cybersecurity tools often combine Machine Learning with expert-defined security rules.

---

### 4. Machine Learning Model Development

Train and compare multiple Machine Learning algorithms using Scikit-learn, including:

- Logistic Regression
- Decision Tree
- Random Forest

The final model will be selected based on experimental evaluation rather than assumptions.

---

### 5. Model Evaluation

Evaluate model performance using standard Machine Learning metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

This ensures that the selected model is reliable and its performance is clearly justified.

---

### 6. Trust Score Generation

Design a Website Trust Score ranging from 0–100 to provide users with more informative results instead of only binary predictions.

Example:

- 81–100 → Safe
- 61–80 → Low Risk
- 41–60 → Medium Risk
- 21–40 → High Risk
- 0–20 → Critical Risk

This makes the system easier for non-technical users to understand.

---

### 7. Confidence Score Display

Display the model's confidence level along with predictions.

Example:

Prediction: Likely Phishing

Confidence: 94%

This helps users understand how certain the model is about its prediction.

---

### 8. Explainable AI

Provide simple explanations for predictions by showing which URL features contributed most to the decision.

Examples:

- URL too long
- Uses IP address
- Contains suspicious keywords
- Excessive subdomains

This improves transparency and user trust.

---

### 9. Security Recommendations

Generate practical cybersecurity advice based on the analysis, such as:

- Avoid entering passwords
- Avoid payments
- Verify the official website
- Do not share OTPs
- Leave the website immediately

This converts technical analysis into actionable guidance.

---

### 10. Dashboard Development

Develop a clean Streamlit dashboard displaying:

- Total URLs analyzed
- Safe websites
- Phishing websites
- Trust Score distribution
- Charts and analytics

This improves usability and provides better insights.

---

### 11. Documentation & Version Control

Maintain proper documentation throughout development and use:

- Git
- GitHub
- Organized folder structure
- Meaningful commits

to demonstrate good software engineering practices.

---

### 12. Testing & Validation

Test the system using:

- Legitimate URLs
- Phishing URLs
- Invalid URLs
- Edge cases

to ensure reliable performance.

---

## Notes on Scope

Version 1 of TrustLens focuses primarily on:

- URL Analysis
- Machine Learning
- Rule-Based Detection
- Trust Score
- Explainable Results
- Recommendations
- Dashboard

The following features are considered future enhancements:

- QR Code Analysis
- OCR-Based URL Extraction
- Email Phishing Detection
- WHOIS Lookup
- SSL Validation
- VirusTotal Integration
- Browser Extension
- Cloud Deployment

These features are intentionally excluded from Version 1 to keep the project realistic, focused, and achievable within a single academic semester.