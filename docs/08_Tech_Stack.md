# 08. Tech Stack

## 1. Purpose

This document describes the technologies, frameworks, libraries, and development tools used to build **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer**.

The selected technologies support the complete project workflow, including data processing, Machine Learning, model persistence, backend prediction, Streamlit application development, QR-code analysis, OCR-based URL extraction, testing, and version control.

---

## 2. Programming Language

| Technology | Purpose | Justification |
|---|---|---|
| **Python 3.13.14** | Main programming language | Python provides a large ecosystem for Machine Learning, data processing, cybersecurity development, automation, and application development. |

Python is used throughout the project for data preparation, feature extraction, Machine Learning, backend prediction, QR/OCR processing, PDF generation, and the Streamlit application.

---

## 3. Machine Learning

| Technology | Purpose | Justification |
|---|---|---|
| **Scikit-learn** | Machine Learning pipeline, preprocessing, model training, evaluation, and prediction | Provides the required tools for building and evaluating the phishing classification system. |
| **Random Forest Classifier** | Final production classification model | Suitable for classification using structured URL features and can provide class probabilities for risk analysis. |
| **Joblib** | Model persistence | Allows the trained production pipeline to be saved and loaded without retraining the model every time the application starts. |

The final TrustLens production model is a Random Forest-based Scikit-learn pipeline.

The saved production model is:

```text
models/trustlens_production_pipeline.joblib
```

---

## 4. Data Processing and Analysis

| Technology | Purpose | Justification |
|---|---|---|
| **Pandas** | Dataset loading, cleaning, transformation, and analysis | Provides efficient tabular data processing for the phishing URL dataset. |
| **NumPy** | Numerical operations and data manipulation | Supports numerical processing used during Machine Learning preparation and analysis. |
| **Matplotlib** | Data visualization and exploratory analysis | Used to visualize dataset characteristics and Machine Learning-related analysis during development. |

These tools were mainly used during the dataset preparation, exploratory analysis, feature engineering, and model development stages.

---

## 5. Web Application

| Technology | Purpose | Justification |
|---|---|---|
| **Streamlit** | User interface and local application execution | Allows the Machine Learning backend to be connected to an interactive web interface using Python without requiring a separate frontend framework. |

The Streamlit application provides the main TrustLens interface for submitting URLs and viewing the resulting analysis.

---

## 6. URL Feature Extraction

TrustLens uses a custom Python feature extraction module for converting a submitted URL into the 17 production features expected by the Machine Learning pipeline.

The production features include:

- URL length
- Domain length
- IP-address detection
- TLD
- TLD length
- Number of subdomains
- URL obfuscation
- Obfuscated character count
- Number of digits
- Number of equals signs
- Number of question marks
- HTTPS usage
- Number of dots
- Number of slashes
- Suspicious keyword count
- Hyphen detection in the domain
- Path depth

The same feature definitions are used by the application during prediction to maintain consistency with the trained production model.

---

## 7. QR-Code and OCR Processing

| Technology | Purpose | Justification |
|---|---|---|
| **OpenCV** | Image processing and QR-code related processing | Supports image preprocessing and QR-code analysis workflows. |
| **OCR Processing** | Extracting URLs from screenshots | Allows TrustLens to analyze a URL shown in a browser screenshot or similar image. |

The application supports two additional input methods besides direct URL entry:

- QR-code URL extraction
- Screenshot-based URL extraction using OCR

After the URL is extracted, it is passed through the same validation, feature extraction, and prediction pipeline used for direct URL analysis.

---

## 8. PDF Report Generation

TrustLens can generate a PDF report containing the results of a URL analysis.

The report can include:

- Analyzed URL
- Prediction
- Risk level
- Risk score
- Security explanations
- Technical URL features
- Security recommendations

This provides a downloadable record of the analysis for demonstration and academic use.

---

## 9. Development Tools

| Technology | Purpose |
|---|---|
| **Jupyter Notebook** | Dataset analysis, feature engineering, Machine Learning experiments, evaluation, and final model development |
| **Visual Studio Code** | Application and backend development |
| **Python Virtual Environment** | Isolates project dependencies from the system Python environment |

The Machine Learning development workflow is primarily documented in the project notebooks, while the final application is organized into Python source files.

---

## 10. Version Control and Project Management

| Technology | Purpose |
|---|---|
| **Git** | Source-code version control and change tracking |
| **GitHub** | Remote repository and project collaboration/version history |
| **Git LFS** | Storage and versioning of the production Machine Learning model |

Git LFS is used because the trained production model is larger than a typical source-code file and is better managed using large-file version control.

---

## 11. Dataset

TrustLens uses the **PhiUSIIL phishing and legitimate URL dataset** for Machine Learning development.

The dataset contains both phishing and legitimate website URLs and provides the foundation for:

- Data cleaning
- Exploratory data analysis
- Feature engineering
- Model training
- Model evaluation
- Structural robustness experiments

The final production model uses a selected set of 17 URL-based features rather than relying on all original dataset columns.

---

## 12. Project Architecture Support

The technology stack supports a clear separation between Machine Learning development and application-time prediction.

The overall workflow is:

```text
Dataset
   ↓
Pandas / NumPy
   ↓
Feature Engineering
   ↓
Scikit-learn
   ↓
Random Forest Model
   ↓
Joblib
   ↓
Saved Production Pipeline
   ↓
Streamlit Application
   ↓
URL / QR / Screenshot Input
   ↓
Feature Extraction
   ↓
Prediction + Risk Analysis
```

This structure allows the trained model to be reused by the application without performing training during normal user interaction.

---

## 13. Technology Selection Summary

The TrustLens technology stack was selected primarily because it is:

- Suitable for Machine Learning development
- Mostly open-source and freely available
- Compatible with Python-based development
- Practical for an academic cybersecurity project
- Suitable for local development and demonstration
- Flexible enough to support future improvements

The combination of Python, Scikit-learn, Pandas, NumPy, Random Forest, Joblib, Streamlit, OpenCV, Git, and GitHub provides the required foundation for the current TrustLens implementation.

---

## 14. Conclusion

The selected technology stack is suitable for developing and maintaining TrustLens as an academic cybersecurity project.

Python and its Machine Learning ecosystem support the data and model development process, while Streamlit provides the application interface. Joblib enables the trained production model to be reused efficiently, and Git/GitHub with Git LFS provide version control for the project and its model artifact.

The additional QR-code, OCR, and PDF capabilities extend the application beyond direct URL input while still using the same core URL analysis pipeline.