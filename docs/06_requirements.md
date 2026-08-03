# 06. Requirements

## Purpose

This document defines the functional and non-functional requirements for Version 1 of the **AI-Powered Phishing URL Detection System**. It specifies what the system must do and the quality standards it must satisfy throughout development.

---

# Intended Users

The primary users of this system are business employees who want to verify whether a website URL is legitimate or potentially phishing before visiting it. The application is designed to provide a quick and easy-to-understand prediction without requiring cybersecurity expertise.

---

# Functional Requirements (FR)

Functional requirements describe the specific functions the system must perform.

| ID | Requirement |
|----|-------------|
| **FR-1** | The system shall accept a website URL as text input from the user through the Streamlit interface. |
| **FR-2** | The system shall validate that the submitted input is a properly formatted URL before attempting prediction. If the input is empty or invalid, an appropriate error message shall be displayed. |
| **FR-3** | The system shall extract predefined lexical (URL-based) features from the submitted URL, such as URL length, number of dots, hyphens, digits, subdomains, presence of an IP address, and other structural characteristics required by the Machine Learning model. |
| **FR-4** | The system shall use a trained Machine Learning model to classify the submitted URL as either **Phishing** or **Legitimate**. |
| **FR-5** | The system shall display the predicted classification label to the user. |
| **FR-6** | The system shall display the confidence score associated with the prediction. |
| **FR-7** | The system shall allow users to classify multiple URLs without restarting the application. |
| **FR-8** | The system shall train and evaluate the Machine Learning model using a publicly available phishing URL dataset and record evaluation metrics including Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. |
| **FR-9** | The system shall save the trained Machine Learning model using Joblib and load it for future predictions without retraining each time the application starts. |

---

# Non-Functional Requirements (NFR)

Non-functional requirements describe the quality attributes and constraints of the system.

| ID | Category | Requirement |
|----|----------|-------------|
| **NFR-1** | Performance | The system shall return a prediction within a few seconds after the user submits a valid URL on a standard personal computer. |
| **NFR-2** | Usability | The user interface shall be simple, intuitive, and easy to navigate, allowing users to perform URL classification with minimal effort. |
| **NFR-3** | Reliability | The system shall handle invalid or malformed input gracefully without crashing or producing unexpected behavior. |
| **NFR-4** | Maintainability | The source code shall be organized into modular components (such as data preprocessing, feature extraction, model training, model prediction, and user interface) to simplify maintenance and future enhancements. |
| **NFR-5** | Portability | The application shall run on any standard computer with Python and the required libraries installed, without requiring specialized hardware or paid software. |
| **NFR-6** | Model Quality | The Machine Learning model shall be evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. Performance shall be reported transparently based on experimental results rather than a predetermined accuracy target. |
| **NFR-7** | Security | The application shall process user-provided URLs locally and shall not permanently store or transmit submitted URLs during prediction. |
| **NFR-8** | Compatibility | The application shall be compatible with Windows operating systems and Python 3.x. |

---

# Requirement Summary

The system is expected to provide a reliable and user-friendly solution for detecting phishing URLs using Machine Learning. The requirements defined in this document will guide the implementation, testing, and evaluation of Version 1 of the project while ensuring the scope remains focused and achievable within the project timeline.