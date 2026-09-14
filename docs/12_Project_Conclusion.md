# 12. Project Conclusion

## 1. Conclusion

TrustLens is an AI-assisted website trust and phishing risk analyzer developed to help users understand the potential risk of a URL before visiting it.

The system combines machine-learning-based URL classification with structural URL analysis, risk scoring, explanations, and security recommendations.

## 2. Project Outcome

The completed system can:

- Accept and validate URLs
- Extract 17 URL-based features
- Classify URLs as Legitimate or Phishing
- Identify Suspicious URLs using the defined risk thresholds
- Calculate a phishing-based Risk Score from 0 to 100
- Provide understandable reasons behind the result
- Provide basic security recommendations
- Analyze URLs obtained from QR codes
- Extract URLs from screenshots using OCR
- Generate PDF analysis reports
- Load and use the saved production machine-learning model

## 3. Machine Learning Outcome

The final production model was evaluated on a holdout dataset and achieved an accuracy of approximately **98.34%**.

Additional targeted testing was also performed to examine difficult legitimate and phishing URL structures.

The testing showed that the model performs well on the evaluated dataset and phishing stress cases, while some complex legitimate URLs can receive higher phishing probabilities.

## 4. Limitations

TrustLens is not a complete website security or real-time threat-intelligence system.

It primarily analyzes URL structure and lexical characteristics and does not currently verify:

- Live website reputation
- Domain ownership
- Domain age
- DNS records
- Website content
- SSL trust
- Real-time malware status
- Browser behavior
- External threat-intelligence databases

Therefore, the generated risk result should be treated as an indication rather than a guaranteed security verdict.

## 5. Future Scope

The project can be extended with live threat intelligence, domain and DNS analysis, website content analysis, browser extensions, mobile applications, improved OCR, larger datasets, and more advanced machine-learning approaches.

## 6. Final Statement

TrustLens demonstrates how machine learning and cybersecurity techniques can be combined to create a practical and explainable phishing-risk analysis tool.

The project also highlights an important challenge in phishing detection: URL patterns alone are useful signals, but they are not sufficient to determine the complete security status of a website.

Overall, TrustLens provides a working foundation for URL-based phishing risk analysis while keeping its limitations and future improvements clearly defined.