# 04. Project Scope

## Purpose

The purpose of this document is to define the boundaries of Version 1 of the **AI-Powered Phishing URL Detection System**. It clearly specifies what features are included, what features are intentionally excluded, and the assumptions and constraints under which the project will be developed.

Defining the project scope helps keep the project focused, manageable, and achievable within the duration of a college mini project.

---

# In Scope (Version 1)

The following features and activities are included in Version 1 of the project:

- Collect and preprocess a public phishing URL dataset.
- Extract lexical (URL-based) features from website URLs.
- Train and evaluate Machine Learning classification models using Scikit-learn.
- Evaluate model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- Develop a Streamlit web application that allows users to:
  - Enter a website URL.
  - Predict whether the URL is **Phishing** or **Legitimate**.
  - Display the prediction confidence score.
- Maintain complete project documentation throughout development.
- Use Git and GitHub for version control and project management.

---

# Out of Scope (Version 1)

The following features are intentionally excluded from the first version of the project.

| Feature | Reason |
|----------|--------|
| Email phishing detection | Planned as a future enhancement to keep Version 1 focused on URL detection. |
| Browser extension | Beyond the scope of a single-semester mini project. |
| Real-time website scanning | Requires additional infrastructure and browser integration. |
| Website content or HTML analysis | The project focuses only on lexical URL analysis. |
| WHOIS lookup | Requires external services and internet-based lookups. |
| Domain age analysis | Depends on WHOIS information and external databases. |
| SSL certificate validation | Not required for the lexical feature-based approach. |
| DNS reputation checking | Requires external threat intelligence services. |
| Threat Intelligence API integration | Planned for future versions. |
| QR code phishing detection | Different problem domain. |
| SMS phishing detection | Different problem domain. |
| User authentication and database | Not required for a single-user academic application. |
| Cloud deployment | The application will run locally during development and demonstration. |

---

# Assumptions

The project is developed under the following assumptions:

- A suitable public phishing URL dataset is available for educational use.
- The application will run on a local machine.
- Internet access is not required during prediction because the model analyzes only the URL itself.
- Users will interact with the application through a locally running Streamlit interface.

---

# Constraints

The project is developed with the following constraints:

- **Developer:** Single student developer.
- **Duration:** One academic semester.
- **Programming Language:** Python.
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Joblib, and Streamlit.
- **Dataset:** Publicly available phishing URL datasets.
- **Resources:** Development will use free and open-source tools only.

---

# Scope Management

Any new feature proposed during development will first be evaluated against this scope document.

If a feature is outside the defined scope, it will be considered for a future version instead of being added to Version 1. This helps prevent unnecessary complexity and keeps the project focused on its primary objective.