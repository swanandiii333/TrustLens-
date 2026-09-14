# 06. Requirements

## 1. Purpose

This document defines the functional and non-functional requirements for Version 1 of TrustLens.

## 2. Intended Users

TrustLens is intended for students, employees, and general users who want a quick second opinion about a suspicious website URL.

## 3. Functional Requirements

| ID | Requirement |
|---|---|
| FR-1 | The system shall accept a website URL as input. |
| FR-2 | The system shall validate the submitted URL. |
| FR-3 | The system shall extract the predefined 17 URL features. |
| FR-4 | The system shall use the saved Machine Learning pipeline for prediction. |
| FR-5 | The system shall calculate phishing and legitimate probabilities. |
| FR-6 | The system shall display a 0–100 risk score. |
| FR-7 | The system shall classify results as Legitimate, Suspicious, or Phishing. |
| FR-8 | The system shall display understandable reasons for the result. |
| FR-9 | The system shall provide security recommendations. |
| FR-10 | The system shall support QR-code URL analysis. |
| FR-11 | The system shall support screenshot-based URL extraction using OCR. |
| FR-12 | The system shall allow users to generate a PDF report. |
| FR-13 | The system shall load the saved model without retraining during application startup. |

## 4. Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-1 | Performance | The system should return results within a few seconds on a standard computer. |
| NFR-2 | Usability | The interface should be simple and easy to understand. |
| NFR-3 | Reliability | Invalid inputs should be handled without crashing the application. |
| NFR-4 | Maintainability | Feature extraction, prediction, and risk explanation should remain separated into backend modules. |
| NFR-5 | Security | The application should analyze the submitted URL without directly visiting the website. |
| NFR-6 | Portability | The project should run in a Python virtual environment using the documented dependencies. |

## 5. Constraints

- Python-based implementation
- Publicly available phishing URL dataset
- Local Streamlit application
- Open-source libraries and tools
- URL-based analysis only

## 6. Conclusion

These requirements define the current Version 1 implementation of TrustLens while keeping the project focused on URL-based phishing risk analysis.