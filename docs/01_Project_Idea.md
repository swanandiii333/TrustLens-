# 01. Project Idea

## Project Title

**TrustLens**  
**AI-Based Website Trust & Phishing Risk Analyzer**

---

## One-Line Summary

TrustLens is an AI-powered Website Trust Assessment Platform that combines Machine Learning and rule-based cybersecurity analysis to evaluate whether a website appears trustworthy or potentially malicious. Instead of providing only a binary prediction, the system explains the reasons behind its assessment, generates a Website Trust Score, identifies suspicious URL characteristics, and offers practical security recommendations.

---

## Project Vision

Most phishing detection tools simply classify a URL as **Phishing** or **Legitimate**. While this is useful, it often does not help users understand *why* a website is considered risky.

TrustLens aims to bridge this gap by making phishing detection more transparent and educational. Rather than acting as a black-box classifier, it explains the reasoning behind each prediction through cybersecurity checks, feature analysis, and a Trust Score.

The goal is to combine:

- Machine Learning
- Cybersecurity
- Explainable AI
- Product Thinking

into a single beginner-friendly application that is practical, informative, and easy to understand.

---

## Target Users

TrustLens is designed for users who frequently receive website links through:

- Emails
- WhatsApp
- SMS
- QR Codes
- Social Media
- Online Advertisements

It is especially useful for:

- Business employees
- Students
- General internet users
- Individuals with limited cybersecurity knowledge

The system acts as a decision-support tool, helping users make informed choices before visiting a suspicious website or entering sensitive information.

---

## The Core Idea

Cybercriminals increasingly create phishing websites that closely resemble legitimate websites in appearance and structure. Many users struggle to distinguish between genuine and malicious websites, especially when browsing under time pressure.

TrustLens addresses this problem by analyzing a submitted website URL using both Machine Learning and cybersecurity rules.

The system examines multiple URL characteristics, predicts whether the website is legitimate or phishing, calculates an overall Trust Score, identifies suspicious indicators, and provides clear security recommendations that users can easily understand.

---

## Version 1 Features

Version 1 focuses on building a complete, polished, and well-documented foundation.

The system will include:

### URL Analysis

The user submits a website URL.

The system predicts whether the URL is:

- Legitimate
- Phishing

---

### URL Feature Analysis

The application analyzes important lexical features such as:

- URL Length
- HTTPS Usage
- Number of Dots
- Number of Slashes
- Number of Subdomains
- IP Address Usage
- Prefix/Suffix (-)
- Suspicious Keywords
- Special Characters

These features are used by the Machine Learning model and are also explained to the user.

---

### Rule-Based Cybersecurity Checks

TrustLens performs additional cybersecurity checks such as:

- Missing HTTPS
- IP Address instead of Domain Name
- Excessively Long URL
- Excessive Subdomains
- Suspicious Keywords
- Unusual URL Structure

These checks complement the Machine Learning prediction and improve the interpretability of the result.

---

### Website Trust Score

Instead of showing only a prediction, TrustLens generates an overall **Website Trust Score (0–100)**.

The Trust Score helps users quickly understand the overall risk associated with a website.

Threat Levels include:

- Safe
- Low Risk
- Medium Risk
- High Risk
- Critical Risk

---

### Confidence Score

The application displays the confidence level of the Machine Learning model, indicating how certain the model is about its prediction.

Example:

- Prediction: Likely Phishing
- Confidence: 96%

---

### Explainable Results

Rather than acting like a "black box," TrustLens explains the factors influencing the prediction.

Users can understand:

- Which URL characteristics appear suspicious
- Why the website received its Trust Score
- Why the model classified it as phishing or legitimate

---

### Security Recommendations

Based on the analysis, the application provides practical guidance such as:

- Avoid entering passwords.
- Do not submit payment information.
- Do not share OTPs.
- Verify the official website.
- Leave the website immediately if necessary.

These recommendations help users make safer online decisions.

---

### Dashboard

The Streamlit dashboard presents useful statistics including:

- Total URLs Analyzed
- Safe URLs
- Phishing URLs
- Trust Score Distribution
- Summary Charts

The interface is intentionally simple and suitable for a college mini project.

---

## Expected Output

For every analyzed URL, TrustLens will display:

- Prediction (Legitimate / Phishing)
- Website Trust Score (0–100)
- Threat Level
- Confidence Score
- Suspicious URL Indicators
- Rule-Based Security Findings
- Security Recommendations

---

## Why This Project

This project was chosen because:

- Phishing remains one of the most common cybersecurity attacks.
- Many users cannot confidently judge whether a website is trustworthy.
- Existing tools often provide only binary predictions without explanation.
- Combining Machine Learning with rule-based cybersecurity techniques produces more informative and transparent results.
- It provides practical experience in Machine Learning, cybersecurity, software engineering, explainability, and product design within a single academic project.

---

## Why Machine Learning?

Traditional rule-based systems rely on manually defined conditions and may struggle with unseen phishing patterns.

Machine Learning can identify hidden relationships within URL characteristics by learning from historical data, making it capable of detecting patterns that are difficult to express using fixed rules alone.

By combining Machine Learning with rule-based cybersecurity checks, TrustLens provides both predictive capability and human-readable explanations.

---

## What TrustLens Is NOT (Version 1)

To keep the project realistic for a single-semester mini project, Version 1 deliberately excludes:

- Browser Extensions
- Email Phishing Detection
- SMS Phishing Detection
- QR Code Analysis
- OCR-based URL Extraction
- WHOIS Lookup
- Domain Age Analysis
- SSL Certificate Validation
- VirusTotal Integration
- Threat Intelligence APIs
- User Authentication
- Database Integration
- Cloud Deployment
- Admin Dashboard

These enhancements are reserved for future versions after the core platform is fully implemented and evaluated.

---

## Long-Term Vision

TrustLens is designed with future expansion in mind.

Future versions may evolve into a comprehensive Website Trust Assessment Platform capable of analyzing URLs from multiple sources, integrating real-time threat intelligence, generating detailed security reports, supporting browser extensions and mobile applications, and providing explainable cybersecurity assistance to a wider range of users.

Version 1 establishes the strong foundation required for those future enhancements while remaining achievable within the scope of a college semester project.