# TrustLens

## AI-Based Website Trust & Phishing Risk Analyzer

TrustLens is an AI-assisted cybersecurity application that analyzes URLs and estimates their phishing risk using machine learning and URL-based security indicators.

The system is designed to help users understand why a URL may be risky instead of only showing a simple phishing/legitimate result.

---

## Overview

TrustLens analyzes the structure and characteristics of a URL and uses a trained Machine Learning model to classify it as:

- Legitimate
- Suspicious
- Phishing

The application also calculates a **Risk Score from 0 to 100**, where a higher score represents a higher phishing probability.

TrustLens can analyze URLs entered directly by the user as well as URLs obtained from QR codes and screenshots.

---

## Features

### URL Analysis

- Accepts HTTP and HTTPS URLs
- Validates user input
- Extracts URL-based security features
- Predicts phishing risk

### Machine Learning Prediction

The production system uses a Random Forest-based Machine Learning pipeline trained on the PhiUSIIL URL dataset.

The final production model uses **17 URL features**.

### Risk Score

The phishing probability is converted into a Risk Score from 0 to 100.

| Phishing Probability | Risk Level | Classification |
|---|---|---|
| Below 40% | Low | Legitimate |
| 40%–74.99% | Medium | Suspicious |
| 75% or above | High | Phishing |

### Explainable Results

TrustLens provides simple reasons that may contribute to a higher risk assessment, such as:

- Suspicious keywords
- Long URLs
- Multiple subdomains
- IP-address patterns
- URL obfuscation
- Hyphens in the domain
- Deep URL paths
- High number of dots
- Missing HTTPS

These indicators are explanations based on URL characteristics and should not be interpreted as proof that a website is malicious.

### QR Code Analysis

Users can upload a QR-code image.

TrustLens:

1. Decodes the QR code
2. Extracts the URL
3. Validates the URL
4. Sends it through the same prediction pipeline
5. Displays the risk result

### Screenshot / OCR Analysis

Users can upload a screenshot containing a browser URL.

The application uses OCR to extract the URL and then analyzes it using the same backend prediction system.

OCR accuracy may depend on screenshot quality and text clarity.

### PDF Reports

TrustLens can generate a PDF report containing:

- Analyzed URL
- Prediction
- Risk level
- Risk score
- Explanation
- Technical URL features
- Security recommendations

---

## Machine Learning

### Dataset

TrustLens uses the **PhiUSIIL** phishing and legitimate URL dataset.

The dataset was cleaned and processed before model training.

### Production Features

The final production pipeline uses the following 17 features:

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

### Model

The production model uses:

- Random Forest Classifier
- 300 estimators
- Balanced class weights
- Scikit-learn Pipeline
- Target encoding for the TLD feature
- Joblib for model saving and loading

---

## Model Evaluation

The production candidate achieved approximately:

**98.34% accuracy on the evaluated holdout dataset.**

The holdout evaluation produced:

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Phishing | 99.66% | 96.48% | 98.05% |
| Legitimate | 97.39% | 99.75% | 98.56% |

These results represent performance on the evaluated dataset and should **not** be interpreted as guaranteed real-world phishing detection accuracy.

Additional targeted testing was performed using difficult legitimate and phishing URL structures. Some complex legitimate URLs produced elevated phishing probabilities, which is an important limitation of the current URL-structure-based approach.

---

## How TrustLens Works

```text
User Input
    |
    +---- URL
    |
    +---- QR Code
    |
    +---- Screenshot
              |
              v
       URL Extraction
              |
              v
       URL Validation
              |
              v
     Feature Extraction
              |
              v
   Production ML Pipeline
              |
              v
 Prediction + Probabilities
              |
              v
     Risk Classification
              |
              v
 Explanation + Recommendations
              |
              v
        TrustLens UI


## Technologies

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib
- OpenCV
- OCR
- QR-code processing
- Git
- GitHub
- Git LFS
- Jupyter Notebook

---

## Project Structure

```text
TrustLens/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── ...
│
├── docs/
│   ├── 01_Project_Idea.md
│   ├── 02_Problem_Statement.md
│   ├── 03_Objectives.md
│   ├── 04_Project_Scope.md
│   ├── 05_Feasibility_Study.md
│   ├── 06_requirements.md
│   ├── 07_Project_Architecture.md
│   ├── 08_Tech_Stack.md
│   ├── 09_Project_Timeline.md
│   ├── 10_Risk Analysis.md
│   ├── 11_Future_Improvements.md
│   └── testing.md
│
├── models/
│   └── trustlens_production_pipeline.joblib
│
├── notebooks/
│   └── ...
│
├── src/
│   └── src/
│       ├── feature_extractor.py
│       ├── predictor.py
│       └── risk_explainer.py
│
├── screenshots/
│   └── ...
│
└── Project Planning/
    └── ...
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/swanandiii333/TrustLens-.git
cd TrustLens-
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## Example Use Cases

TrustLens can be used to analyze:

- A URL copied from an email
- A suspicious link received through a message
- A URL shared on social media
- A QR code containing a website link
- A browser screenshot containing a URL

---

## Testing

Testing was performed for:

- Legitimate URLs
- Phishing URLs
- Invalid inputs
- Complex URL structures
- QR-code analysis
- Screenshot/OCR extraction
- Risk classification
- Risk explanations
- Model save and reload
- PDF report generation

Testing also included false-positive analysis using complex legitimate URLs.

---

## Limitations

TrustLens is primarily a **URL-based phishing risk analyzer**.

It does not currently perform:

- Live website reputation checks
- WHOIS/domain-age verification
- DNS analysis
- Website content inspection
- SSL certificate verification
- Real-time malware detection
- Browser behavior analysis
- Real-time external threat-intelligence checks

A legitimate classification does not guarantee that a website is completely safe.

Similarly, a high-risk classification should be treated as a warning based on the analyzed URL characteristics.

---

## Future Improvements

Possible future improvements include:

- Live threat-intelligence integration
- Domain and DNS analysis
- Website content analysis
- Browser extension
- Mobile application
- Larger and newer training datasets
- Improved OCR
- Advanced model explainability
- Continuous model monitoring
- Email and message URL analysis

---

## Disclaimer

TrustLens is an academic and educational cybersecurity project.

The Risk Score and classification are based primarily on URL characteristics and machine-learning predictions. They are not a guarantee of the actual security or maliciousness of a website.

Users should avoid entering sensitive information into suspicious websites even when a URL receives a low-risk result.

---

## Author

**Swanandi Balapurkar**