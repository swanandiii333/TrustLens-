# 10. Risk Analysis

## Purpose

This document identifies potential risks that may affect the successful development of the **AI-Powered Phishing URL Detection System**. Each identified risk is evaluated based on its likelihood and potential impact, along with a mitigation strategy to minimize its effect on the project.

Risk management helps ensure that potential problems are anticipated early rather than addressed only after they occur.

---

# Risk Register

| ID | Risk | Likelihood | Impact | Mitigation Strategy |
|----|------|------------|--------|---------------------|
| **R-1** | Dataset quality issues (imbalanced classes, missing values, noisy or inconsistent data) | Medium | Medium | Validate the dataset during the Data Collection phase and perform preprocessing such as cleaning, duplicate removal, and handling class imbalance before model training. |
| **R-2** | Machine Learning learning curve may take longer than expected | Medium | Medium | Follow the **Learn While Building** approach, learning each concept immediately before implementing it. Maintain a flexible schedule with a buffer week. |
| **R-3** | Model underperformance resulting in poor prediction accuracy | Medium | High | Train and compare multiple Machine Learning algorithms (Logistic Regression, Decision Tree, and Random Forest) using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix before selecting the final model. |
| **R-4** | Time conflicts due to college assignments, examinations, or other academic commitments | High | Medium | Follow the planned semester timeline and use the reserved buffer period to accommodate unavoidable delays. |
| **R-5** | Inconsistent feature extraction between training and prediction pipelines | Low | High | Develop a single reusable Feature Extraction module that is shared by both the Training Pipeline and the Inference Pipeline. |
| **R-6** | Dependency or library compatibility issues | Medium | Medium | Use a dedicated Python virtual environment and maintain all required library versions in the `requirements.txt` file. |
| **R-7** | Accidental data loss or project file corruption | Low | High | Maintain regular Git commits and push the project to GitHub frequently to create reliable backups. |
| **R-8** | Temporary internet connectivity issues during development | Low | Low | Download datasets, libraries, and documentation early so development can continue offline whenever possible. |
| **R-9** | Scope creep caused by adding unnecessary features during development | Medium | Medium | Strictly follow the Project Scope document. Additional ideas such as Email Detection, WHOIS Lookup, Browser Extension, QR Detection, or Threat Intelligence APIs will be postponed to future versions. |

---

# Risk Priority Matrix

| Impact \\ Likelihood | Low | Medium | High |
|----------------------|-----|--------|------|
| **High Impact** | R-5, R-7 | R-3 | — |
| **Medium Impact** | — | R-1, R-2, R-6, R-9 | R-4 |
| **Low Impact** | R-8 | — | — |

---

# Highest Priority Risks

The following risks require the greatest attention throughout development:

### 1. Model Underperformance (R-3)

If the Machine Learning model performs poorly, the application's predictions will not be reliable. This risk will be minimized by comparing multiple classification algorithms and selecting the best-performing model based on evaluation metrics rather than assumptions.

### 2. Time Constraints (R-4)

Since the project is developed alongside regular BCA coursework, examinations and assignments may reduce development time. A structured timeline and a dedicated buffer week help reduce this risk.

### 3. Feature Extraction Inconsistency (R-5)

Using different feature extraction logic during training and prediction can lead to incorrect predictions. This risk is minimized by implementing one shared feature extraction module that is used throughout the project.

### 4. Data Loss (R-7)

Accidental deletion or hardware failure could result in significant loss of work. Regular Git commits and GitHub backups will ensure project progress is preserved.

---

# Risk Monitoring Plan

Risk management will continue throughout the project lifecycle. At the completion of each development phase, the identified risks will be reviewed, and any newly discovered risks will be added to this document together with their corresponding mitigation strategies.

---

# Risk Analysis Summary

The overall project is considered **Low to Medium Risk**. Most identified risks are manageable through proper planning, version control, modular software architecture, regular testing, and adherence to the defined project scope. By identifying these risks early, the project is better prepared to handle technical and scheduling challenges while maintaining steady progress toward successful completion.