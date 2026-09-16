# 07. Project Architecture

## 1. Purpose

This document describes the overall architecture of **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer**. It explains the major components of the system, how they interact, and how data flows during model training and prediction.

The architecture separates Machine Learning development from application-time prediction so that the trained model can be reused without retraining whenever the application starts.

---

## 2. Architectural Style

TrustLens follows a modular architecture with two distinct Machine Learning stages:

1. **Training Pipeline (Offline)**
2. **Inference Pipeline (Application-Time Prediction)**

The training pipeline is used during model development and experimentation. After the final model is selected, the complete production pipeline is saved using Joblib.

The Streamlit application loads this saved pipeline and uses it for predictions when a user submits a URL.

This separation avoids unnecessary model retraining and keeps the application faster and easier to maintain.

---

## 3. System Components

| Component | Description |
|---|---|
| **Dataset** | Contains phishing and legitimate URLs used for Machine Learning development and evaluation. |
| **Data Preprocessing** | Cleans and prepares the dataset for feature engineering and model training. |
| **Feature Extraction Module** | Extracts the 17 URL-based production features from a submitted URL. |
| **Model Training Pipeline** | Performs preprocessing and trains the final Random Forest Machine Learning model. |
| **Saved Production Model** | Stores the trained Machine Learning pipeline using Joblib. |
| **Prediction Module** | Loads the saved model, extracts URL features, and generates predictions and probabilities. |
| **Risk Explanation Module** | Generates human-readable explanations based on predefined URL security rules. |
| **Streamlit Application** | Provides the user interface for URL, QR-code, and screenshot/OCR analysis. |
| **Report Generation** | Generates a PDF report containing the analysis result, features, explanations, and recommendations. |

---

## 4. Training Pipeline

The training pipeline is executed during Machine Learning development rather than every time the application runs.

### Training Flow

```text
PhiUSIIL Dataset
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
17 Production URL Features
      ↓
Train / Test Split
      ↓
Preprocessing Pipeline
      ↓
Random Forest Classifier
      ↓
Model Evaluation
      ↓
Final Production Pipeline
      ↓
Joblib Model File
```

The final production pipeline contains the preprocessing steps and Random Forest classifier required for prediction.

The saved model is stored as:

```text
models/trustlens_production_pipeline.joblib
```

---

## 5. Production Feature Extraction

TrustLens uses the same defined set of URL-based features during application-time prediction.

The 17 production features are:

1. `URLLength`
2. `DomainLength`
3. `IsDomainIP`
4. `TLD`
5. `TLDLength`
6. `NoOfSubDomain`
7. `HasObfuscation`
8. `NoOfObfuscatedChar`
9. `NoOfDegitsInURL`
10. `NoOfEqualsInURL`
11. `NoOfQMarkInURL`
12. `IsHTTPS`
13. `NoOfDots`
14. `NoOfSlashes`
15. `SuspiciousKeywordCount`
16. `HasHyphenInDomain`
17. `PathDepth`

The feature extraction logic is implemented in the backend and is reused whenever a URL is analyzed.

This helps maintain consistency between the features expected by the trained model and the features supplied during prediction.

---

## 6. Inference Pipeline

The inference pipeline is used when a user analyzes a website.

### Inference Flow

```text
User Input
    ↓
Input Validation
    ↓
URL / QR / Screenshot Processing
    ↓
URL Extraction
    ↓
URL Feature Extraction
    ↓
Saved Production ML Pipeline
    ↓
Prediction + Probabilities
    ↓
Risk Score Calculation
    ↓
Risk Classification
    ↓
Rule-Based Explanation
    ↓
Security Recommendations
    ↓
TrustLens Results
```

- For **direct URL analysis**, the URL is sent to the prediction backend after validation.
- For **QR-code analysis**, the application first decodes the QR code and extracts the URL.
- For **screenshot analysis**, OCR is used to extract the URL from the browser address bar before the normal URL validation and prediction process.

---

## 7. Prediction Module

The main application-facing prediction function is:

```python
predict_url()
```

The prediction module performs the following steps:

1. Receives the URL.
2. Extracts the 17 production features.
3. Passes the features to the saved production pipeline.
4. Obtains the model prediction.
5. Obtains phishing and legitimate probabilities.
6. Calculates the risk score.
7. Determines the risk level and final classification.
8. Generates rule-based explanations.
9. Returns the complete analysis result to the Streamlit application.

The production model uses:

- Random Forest Classifier
- Scikit-learn Pipeline
- Target Encoding for the `TLD` feature
- Joblib for model storage

---

## 8. Risk Classification

TrustLens converts the model's phishing probability into an easier-to-understand risk result.

| Phishing Probability | Risk Level | Final Classification |
|---|---|---|
| Below 40% | Low | Legitimate |
| 40% – 74.99% | Medium | Suspicious |
| 75% or above | High | Phishing |

The Risk Score is calculated from the phishing probability and displayed on a scale of **0–100**.

A higher risk score indicates a higher estimated phishing risk.

---

## 9. Explainability Layer

The prediction result is supplemented with rule-based security observations.

Examples include:

- HTTP instead of HTTPS
- Suspicious keywords
- Hyphens in the domain
- IP-address patterns
- Percent-encoded or obfuscated characters
- Unusually long URLs
- Deep URL paths
- Multiple subdomains
- High numbers of dots

These explanations are generated using predefined cybersecurity rules.

They are intended to help users understand suspicious characteristics of the URL and should not be interpreted as exact Machine Learning feature-attribution results.

---

## 10. Streamlit Application

The Streamlit application acts as the main user interface.

The application provides:

- URL analysis
- QR-code analysis
- Screenshot/OCR URL extraction
- Prediction results
- Risk score
- Risk level
- Security explanations
- Security recommendations
- PDF report generation

The Streamlit layer does not retrain the Machine Learning model. It loads and uses the saved production pipeline through the backend prediction module.

---

## 11. Overall Architecture

```text
                    ┌──────────────────────────┐
                    │       User Input          │
                    │ URL / QR / Screenshot     │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │   Streamlit Interface     │
                    │          app.py           │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │ Input Processing &        │
                    │ URL Validation             │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │   Feature Extraction      │
                    │     17 URL Features       │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │   Saved Production ML     │
                    │        Pipeline           │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │ Prediction + Probabilities│
                    └────────────┬─────────────┘
                                 ↓
              ┌──────────────────┴──────────────────┐
              ↓                                      ↓
    ┌────────────────────────┐          ┌────────────────────────┐
    │ Risk Classification    │          │ Rule-Based Analysis    │
    │ & Risk Score            │          │ & Explanations          │
    └────────────┬───────────┘          └────────────┬───────────┘
                 └──────────────────┬─────────────────┘
                                    ↓
                    ┌──────────────────────────┐
                    │ Results & Security         │
                    │ Recommendations            │
                    └────────────┬─────────────┘
                                 ↓
                    ┌──────────────────────────┐
                    │    Optional PDF Report    │
                    └──────────────────────────┘
```

---

## 12. Architectural Benefits

The modular architecture provides several benefits:

- The Machine Learning model is trained separately from the application.
- The saved model can be reused without retraining.
- URL feature extraction is centralized in one backend module.
- Prediction logic is separated from the Streamlit interface.
- Rule-based explanations are separated from model prediction.
- QR-code and OCR processing can feed into the same URL analysis pipeline.
- The architecture can be extended later without changing the complete system structure.

---

## 13. Architecture Summary

TrustLens uses a modular architecture that separates data preparation, Machine Learning training, model storage, URL feature extraction, prediction, risk analysis, explanation, and user interaction.

The final application follows a simple flow from user input to URL processing, feature extraction, saved model prediction, risk classification, explanation, and security recommendations.

This structure keeps the current Version 1 implementation focused while leaving room for future improvements such as live threat intelligence, domain analysis, website content analysis, and other cybersecurity capabilities.