# 04. Project Scope

# Purpose

The purpose of this document is to define the boundaries of **Version 1** of **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer**.

It clearly specifies what features are included, what features are intentionally excluded, and the assumptions and constraints under which the project will be developed.

Defining the project scope ensures that the project remains focused, achievable, and realistic within a single academic semester.

---

# In Scope (Version 1)

The following features are included in Version 1 of TrustLens:

## Dataset & Machine Learning

- Collect and preprocess a public phishing URL dataset.
- Perform Exploratory Data Analysis (EDA).
- Extract lexical (URL-based) features from website URLs.
- Train and compare multiple Machine Learning models using Scikit-learn.
- Select the final model based on experimental evaluation rather than assumptions.
- Evaluate model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - ROC-AUC
  - Confusion Matrix

---

## Website Trust Analysis

The application will allow users to submit a website URL and receive:

- Website classification (Legitimate or Phishing)
- Trust Score (0–100)
- Confidence Score
- Threat Level
  - Safe
  - Low Risk
  - Medium Risk
  - High Risk
  - Critical Risk

---

## Rule-Based Cybersecurity Checks

The system will perform additional cybersecurity checks alongside Machine Learning, including:

- HTTPS availability
- IP Address usage
- URL length analysis
- Suspicious keywords
- Excessive subdomains
- Special characters
- Prefix/Suffix symbols
- Other lexical URL indicators

These checks complement the ML model and improve explainability.

---

## Explainable Results

Instead of providing only a binary prediction, the system will explain why a website appears suspicious by showing:

- Important features affecting the prediction
- Rule-based findings
- Security observations

This improves user understanding and transparency.

---

## Security Recommendations

Based on the detected risks, TrustLens will generate recommendations such as:

- Avoid Login
- Avoid Payment
- Do Not Enter OTP
- Verify the Official Website
- Leave the Website Immediately

---

## User Interface

Develop a Streamlit dashboard that allows users to:

- Enter a URL
- Analyze website trust
- View prediction
- View Trust Score
- View Confidence Score
- View Threat Level
- View rule-based findings
- View security recommendations

The dashboard will also include simple analytics such as:

- Total URLs analyzed
- Safe vs Phishing counts
- Trust Score distribution
- Basic charts

---

## Documentation & Version Control

- Maintain complete project documentation.
- Use Git for version control.
- Host the project on GitHub.
- Maintain a clean project structure with meaningful commits.

---

# Out of Scope (Version 1)

The following features are intentionally excluded from Version 1.

| Feature | Reason |
|----------|--------|
| Email Phishing Detection | Planned for Version 2. |
| Browser Extension | Requires browser integration beyond the current scope. |
| Mobile Application | Future enhancement. |
| WhatsApp Bot | Future enhancement. |
| Telegram Bot | Future enhancement. |
| OCR Image Analysis | Implement only if sufficient time remains after completing the core project. |
| PDF Trust Report Export | Optional enhancement after core functionality is complete. |
| WHOIS Lookup | Requires external services and internet-based lookups. |
| Domain Age Analysis | Depends on WHOIS data and external databases. |
| SSL Certificate Validation | Requires live website analysis and is outside the lexical feature approach. |
| VirusTotal Integration | Requires external APIs and internet connectivity. |
| Threat Intelligence APIs | Future enhancement. |
| Real-Time Website Crawling | Beyond the scope of the current project. |
| User Authentication | Not required for an academic mini project. |
| Database Integration | Future enhancement. |
| Admin Dashboard | Future enhancement. |
| Cloud Deployment | The application will run locally for development and demonstration. |

---

# Assumptions

The project is developed under the following assumptions:

- A suitable public phishing URL dataset is available.
- The application will run on a standard personal computer.
- Internet access is required only during development for downloading datasets and libraries.
- During prediction, the system relies primarily on lexical URL analysis and local model inference.
- Users will interact with the application through a locally running Streamlit application.

---

# Constraints

The project is developed under the following constraints:

- **Developer:** Single student developer.
- **Duration:** One academic semester.
- **Programming Language:** Python.
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Joblib, Streamlit.
- **Resources:** Free and open-source software only.
- **Dataset:** Publicly available phishing URL datasets.

---

# Scope Management

Every proposed feature will be evaluated against this scope document before implementation.

If a feature falls outside the defined scope, it will be documented under **Future Improvements** instead of being added immediately.

This approach helps prevent scope creep, keeps development manageable, and ensures that Version 1 is completed as a polished, reliable, and well-documented academic project.