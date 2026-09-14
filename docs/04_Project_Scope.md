# 04. Project Scope

## 1. Scope Overview

TrustLens focuses on analyzing website URLs and estimating their phishing risk using Machine Learning and URL-based cybersecurity indicators.

## 2. In-Scope Features

- URL validation
- URL feature extraction
- 17 production URL features
- Machine Learning prediction
- Phishing probability
- Risk score from 0–100
- Low, Medium, and High risk levels
- Rule-based security checks
- Explainable results
- Security recommendations
- QR-code URL analysis
- Screenshot/OCR URL extraction
- Streamlit web interface
- PDF report generation
- Model evaluation and testing
- Project documentation

## 3. Out-of-Scope Features

The following are not part of the current implementation:

- Live website reputation checking
- WHOIS/domain-age analysis
- Live DNS analysis
- SSL certificate verification
- Website content inspection
- Real-time malware detection
- External threat intelligence APIs
- VirusTotal integration
- Email phishing detection
- SMS phishing detection
- Browser extension
- Mobile application
- Cloud deployment
- User authentication and admin systems

These can be considered for future versions.

## 4. Technical Scope

The project uses:

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Joblib
- Streamlit
- OCR and QR-code processing
- Git and GitHub

## 5. Limitations

TrustLens mainly analyzes URL structure and lexical characteristics.

Therefore, the result does not guarantee that a website is safe or malicious.

Complex legitimate URLs may also produce false-positive risk assessments.

## 6. Conclusion

The project scope is intentionally limited to URL-based phishing risk analysis so that the current system remains manageable, testable, and suitable for an academic cybersecurity project.