# 01. Project Idea

## Project Title

**TrustLens**  
**AI-Based Website Trust & Phishing Risk Analyzer**

---

## One-Line Summary

TrustLens is an AI-powered Website Trust Assessment Platform that combines Machine Learning and rule-based cybersecurity analysis to evaluate whether a website appears trustworthy or potentially malicious.

Instead of providing only a binary prediction, the system explains the reasons behind its assessment, generates a risk score, identifies suspicious URL characteristics, and offers practical security recommendations.

---

## Project Vision

Most phishing detection systems simply classify a URL as **Phishing** or **Legitimate**. While this is useful, it does not always help users understand why a website is considered risky.

TrustLens aims to make phishing detection more transparent and educational. Rather than acting only as a black-box classifier, it provides understandable information about suspicious URL characteristics and security indicators.

The project combines:

- Machine Learning
- Cybersecurity
- URL structural analysis
- Explainable results
- Risk assessment
- Security recommendations
- Practical application development

The overall goal is to create a beginner-friendly cybersecurity application that is practical, informative, and easy to understand.

---

## Target Users

TrustLens is designed for users who may receive website links through:

- Emails
- WhatsApp
- SMS
- QR Codes
- Social Media
- Online Advertisements
- Other online sources

It can be useful for:

- Students
- Business employees
- General internet users
- Individuals with limited cybersecurity knowledge

The system acts as a decision-support tool, helping users make a more informed decision before visiting a suspicious website or entering sensitive information.

---

## The Core Idea

Cybercriminals often create phishing websites that attempt to look legitimate or use deceptive URLs to convince users to interact with them.

Users may find it difficult to identify suspicious characteristics such as:

- Unusual domains
- Suspicious keywords
- Long URLs
- Multiple subdomains
- IP-address based domains
- Unusual URL paths
- Encoded characters
- Large numbers of query parameters

TrustLens addresses this problem by analyzing a submitted website URL using Machine Learning and cybersecurity-oriented rules.

The system:

1. Accepts a URL or extracts a URL from another supported input.
2. Validates the URL.
3. Extracts structural and lexical URL features.
4. Passes the features to the trained Machine Learning model.
5. Generates phishing and legitimate probabilities.
6. Converts the phishing probability into a risk score.
7. Assigns a risk level.
8. Identifies suspicious URL characteristics.
9. Provides understandable explanations.
10. Provides security recommendations.

---

## Version 1 Features

Version 1 focuses on building a complete and practical URL-based website trust and phishing risk analyzer.

### 1. URL Analysis

The user can submit a website URL for analysis.

The system predicts whether the URL appears:

- Legitimate
- Phishing

The application also provides the estimated phishing probability and risk assessment.

---

### 2. URL Feature Analysis

TrustLens analyzes structural and lexical characteristics of URLs.

The production system uses exactly **17 URL-based features**, including characteristics related to:

- URL Length
- Domain Length
- Domain IP usage
- TLD
- TLD Length
- Number of Subdomains
- URL Obfuscation
- Obfuscated Characters
- Digits in URL
- Equals Signs
- Question Marks
- HTTPS Usage
- Number of Dots
- Number of Slashes
- Suspicious Keywords
- Hyphens in Domain
- Path Depth

These features are used by the Machine Learning pipeline during prediction.

---

### 3. Machine Learning Prediction

TrustLens uses a trained Machine Learning model to classify URLs.

The final production system uses a Random Forest pipeline with preprocessing.

The model produces probabilities for:

- Phishing
- Legitimate

The prediction is then used to calculate the phishing risk score.

---

### 4. Risk Score

Instead of showing only a binary prediction, TrustLens displays a **Risk Score from 0 to 100**.

The score is derived from the model's phishing probability.

A higher score indicates a higher estimated phishing risk.

The score should not be interpreted as a guarantee that a website is malicious or safe.

---

### 5. Risk Classification

The current application uses the following classification:

| Phishing Probability | Risk Level | Final Classification |
|---|---|---|
| Below 40% | Low | Legitimate |
| 40% – 74.99% | Medium | Suspicious |
| 75% or higher | High | Phishing |

This makes the Machine Learning output easier for non-technical users to understand.

---

### 6. Rule-Based Cybersecurity Checks

TrustLens performs additional rule-based checks alongside the Machine Learning prediction.

Examples include:

- Missing HTTPS
- IP-address pattern in the domain
- Unusually long URL
- Multiple subdomains
- Suspicious keywords
- Hyphens in the domain
- Obfuscated or percent-encoded characters
- Deep URL paths
- High number of dots

These checks help provide understandable security observations alongside the Machine Learning result.

---

### 7. Explainable Results

TrustLens does not only display the final classification.

It also provides human-readable explanations describing suspicious URL characteristics detected during analysis.

For example:

- The URL uses HTTP instead of HTTPS.
- Suspicious keywords were detected.
- An IP-address pattern was detected.
- The domain contains a hyphen.
- Obfuscated URL characters were detected.
- The URL is unusually long.
- The URL contains a deep path structure.
- Multiple subdomains were detected.

These explanations are rule-based observations and are not exact feature-attribution values from the Random Forest model.

---

### 8. Security Recommendations

TrustLens provides practical security recommendations based on the detected risk.

Examples include:

- Verify the official website.
- Avoid entering passwords on suspicious websites.
- Avoid entering payment information when the URL appears unsafe.
- Do not share OTPs with suspicious websites.
- Leave the website if strong phishing indicators are detected.

The purpose is to convert technical analysis into practical security guidance.

---

### 9. QR Code Analysis

The current application supports QR-code based URL analysis.

A user can provide a QR-code image containing a website URL.

TrustLens:

1. Detects and decodes the QR code.
2. Extracts the embedded URL.
3. Validates the extracted URL.
4. Passes it through the same URL feature extraction process.
5. Analyzes it using the production Machine Learning model.
6. Displays the resulting risk assessment.

This allows QR-based website links to be analyzed without manually typing the URL.

---

### 10. Screenshot / OCR URL Extraction

TrustLens also supports screenshot-based URL analysis.

A screenshot containing a browser address bar can be provided to the application.

The system uses OCR to:

1. Read the visible URL from the screenshot.
2. Extract the URL text.
3. Validate the extracted URL.
4. Pass it through the normal TrustLens prediction pipeline.
5. Display the resulting classification and risk assessment.

OCR accuracy depends on the clarity and quality of the screenshot.

---

### 11. Dashboard Development

TrustLens provides a Streamlit-based interface for interacting with the system.

The application allows users to:

- Enter a URL.
- Analyze a URL.
- Upload a QR-code image.
- Analyze a screenshot.
- View the prediction.
- View the risk level.
- View the risk score.
- View suspicious indicators.
- View technical URL features.
- View security recommendations.
- Generate a PDF report.

---

### 12. PDF Report Generation

TrustLens can generate a PDF report containing the result of a website analysis.

The report can include:

- Analyzed URL
- Prediction
- Risk level
- Risk score
- Explanation
- Technical URL features
- Security recommendations

This provides a documented version of the analysis result.

---

### 13. Documentation and Version Control

The project uses documentation and version control throughout development.

Technologies and practices include:

- Git
- GitHub
- Markdown documentation
- Organized project structure
- Meaningful commits
- Model versioning through the project workflow

The project documentation covers the development process, architecture, Machine Learning work, testing, limitations, and future improvements.

---

### 14. Testing and Validation

TrustLens is tested using different types of inputs, including:

- Legitimate URLs
- Phishing URLs
- Invalid URLs
- Complex legitimate URLs
- QR-code inputs
- Screenshot/OCR inputs
- Edge cases

Testing is used to verify both application functionality and Machine Learning behaviour.

False positives identified during testing are documented rather than hidden, especially for complex legitimate URLs.

---

## Current Project Scope

The current implementation focuses on **URL-based website trust and phishing risk analysis**.

The implemented system includes:

- URL analysis
- Machine Learning prediction
- URL feature extraction
- Risk score
- Risk classification
- Rule-based cybersecurity checks
- Explainable results
- Security recommendations
- QR-code analysis
- Screenshot/OCR URL extraction
- PDF report generation
- Streamlit interface

The project intentionally does not attempt to provide complete real-time website security verification.

---

## What TrustLens Is

TrustLens is:

- An academic cybersecurity project.
- A Machine Learning based URL risk analyzer.
- A URL structural and lexical analysis system.
- An AI-assisted phishing risk assessment tool.
- An explainable cybersecurity application.
- A Streamlit-based application.
- A demonstration of Machine Learning applied to a practical cybersecurity problem.

---

## What TrustLens Is Not

TrustLens is **not a guaranteed phishing detector**.

The current system does not automatically verify:

- Live website reputation
- Domain ownership
- Domain age
- Live DNS reputation
- SSL certificate trust
- Website content
- Browser behaviour
- Real-time malware status
- External threat intelligence
- Newly registered malicious domains

Therefore, a low-risk result does not guarantee that a website is completely safe.

Similarly, a high-risk result is an estimated risk assessment and should not by itself be treated as definitive proof that a website is malicious.

TrustLens should be considered an educational and decision-support security tool.

---

## Future Scope

The following features can be considered for future versions:

- Email phishing detection
- Browser extension
- Mobile application
- WHOIS lookup
- Domain age analysis
- SSL certificate validation
- DNS analysis
- VirusTotal integration
- Threat intelligence APIs
- Real-time website reputation checking
- Website content analysis
- SMS phishing detection
- Prediction history
- Database integration
- User authentication
- Admin dashboard
- REST API
- Cloud deployment
- Advanced Explainable AI techniques
- Model comparison dashboard

These features are kept outside the current core implementation to maintain a focused and manageable project scope.

---

## Project Vision

The long-term vision of TrustLens is to develop a practical cybersecurity analysis platform that combines:

- Machine Learning
- Cybersecurity analysis
- URL structural analysis
- Explainability
- Risk assessment
- Security recommendations
- Multiple forms of user input

The project can later be extended toward additional phishing channels and real-time cybersecurity intelligence.

For the current version, the focus remains on building and documenting a reliable URL-based phishing risk analysis system.

---

## Disclaimer

TrustLens is an academic and educational cybersecurity project.

Its predictions are based primarily on URL-level structural and lexical characteristics learned from the training data.

The risk score represents an estimated phishing risk and should not be treated as a definitive security verdict.

Users should verify suspicious websites through trusted sources and avoid entering passwords, OTPs, payment information, or other sensitive information when a website appears unsafe.

---

## Conclusion

TrustLens aims to make website phishing-risk analysis more understandable by combining Machine Learning with cybersecurity-oriented URL analysis and rule-based explanations.

The project goes beyond a simple **Phishing/Legitimate** prediction by providing a risk score, risk level, suspicious indicators, explanations, and security recommendations.

The current implementation also extends URL analysis to QR-code inputs and screenshot-based OCR extraction while keeping the same underlying prediction pipeline.

Overall, TrustLens demonstrates how Machine Learning and cybersecurity concepts can be combined into a practical, educational, and user-friendly website trust and phishing risk analysis application.