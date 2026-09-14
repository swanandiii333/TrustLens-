# 10. Risk Analysis

## 1. Introduction

Risk analysis identifies the main technical, application, development, and usage-related risks associated with **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer**.

The purpose of this analysis is to identify possible problems, explain their impact, and describe how they are managed during development and use of the system.

---

## 2. Technical Risks

### 2.1 False Positives

Some legitimate URLs may be classified as suspicious or phishing.

This is more likely for legitimate URLs with complex structures such as:

- Query parameters
- Deep URL paths
- Multiple URL components
- Authentication-related terms
- Location or map URLs

This behaviour is partly related to the distribution of the training data, where complex legitimate URL structures are less represented.

**Mitigation:**

- Perform targeted testing using legitimate complex URLs.
- Perform structural robustness testing.
- Analyze false-positive cases.
- Document model limitations.
- Avoid presenting the prediction as a guaranteed verdict.

---

### 2.2 False Negatives

A phishing URL may sometimes appear structurally similar to a legitimate URL and may not contain obvious suspicious characteristics.

As TrustLens primarily analyzes URL-level structural and lexical information, some malicious URLs may not provide enough suspicious signals for reliable classification.

**Mitigation:**

- Test the model with different phishing URL structures.
- Use both Machine Learning predictions and rule-based security indicators.
- Perform targeted phishing stress testing.
- Clearly document the limitations of URL-based detection.

---

### 2.3 Dataset Limitations

TrustLens is trained using the **PhiUSIIL phishing and legitimate URL dataset**.

A public dataset cannot represent every legitimate and phishing URL found on the current internet. In particular, the source dataset contains limited examples of some complex legitimate URL structures.

This can cause a distribution difference between the training data and real-world URLs.

**Mitigation:**

- Analyze the dataset before training.
- Examine class and feature distributions.
- Perform structural robustness experiments.
- Add controlled legitimate structural examples during experimentation.
- Test the final model using additional representative URLs.
- Avoid claiming that the model detects every phishing website.

---

### 2.4 Model Limitations

TrustLens primarily analyzes URL structure and lexical characteristics.

The system does not currently perform live analysis of the actual website or external threat intelligence.

It does not directly verify:

- Live website reputation
- Domain ownership
- Domain age
- WHOIS information
- Live DNS information
- Website content
- Real-time malware status
- Browser behaviour
- SSL certificate trust
- External threat-intelligence databases

Therefore, the model should be treated as a URL-based risk analysis component rather than a complete website security verification system.

---

## 3. Application Risks

### 3.1 Invalid Input

Users may enter incomplete, malformed, or unsupported URL values.

**Mitigation:**

- Validate URL input before analysis.
- Check for a valid HTTP or HTTPS scheme.
- Check that the URL contains a valid network location.
- Display a clear error message for invalid input.

---

### 3.2 OCR Errors

Screenshot-based URL extraction may produce incorrect characters, particularly when the browser address bar is unclear, small, distorted, or low quality.

For example, OCR may confuse similar characters or alter parts of a domain name.

**Mitigation:**

- Validate the extracted URL before prediction.
- Treat OCR output as extracted input rather than guaranteed text.
- Inform the user when the extracted value cannot be analyzed.
- Test OCR using different screenshot conditions.

---

### 3.3 QR-Code Errors

A QR code may contain:

- An invalid value
- Text instead of a URL
- An unsupported URL format
- An incorrectly decoded value
- No readable QR code

**Mitigation:**

- Decode the QR code before analysis.
- Validate the extracted content.
- Display an appropriate message when the QR code cannot be analyzed.
- Pass valid extracted URLs through the same prediction pipeline as direct URL input.

---

## 4. Risk Explanation Limitations

TrustLens provides human-readable explanations based on predefined cybersecurity rules.

Examples include:

- HTTP instead of HTTPS
- Suspicious keywords
- IP-address patterns
- Hyphens in the domain
- URL obfuscation
- Unusually long URLs
- Deep path structures
- Multiple subdomains
- High numbers of dots

These explanations help users understand suspicious characteristics of a URL.

However, they are **rule-based explanations and not exact Machine Learning feature-attribution results**.

**Mitigation:**

- Clearly describe the explanation system in the documentation.
- Avoid claiming that a displayed reason is necessarily the exact cause of the model's prediction.
- Use the explanations as supporting security indicators.

---

## 5. Performance Risks

Large datasets and Machine Learning experiments can require significant processing time and memory.

The structural robustness experiments can also require substantial computational resources because large numbers of URL variants may be generated and evaluated.

**Mitigation:**

- Perform model training separately from normal application execution.
- Save the final trained pipeline using Joblib.
- Load the saved model during application startup instead of retraining it.
- Avoid unnecessary retraining when the production model has already been finalized.

---

## 6. Security and Privacy Considerations

TrustLens analyzes URL information supplied by the user.

The application should not be presented as a replacement for professional security tools, browser security systems, or antivirus software.

Users should avoid entering credentials, payment information, or other sensitive information into suspicious websites even when TrustLens classifies a URL as legitimate.

A **Legitimate** classification means that the URL has a lower estimated phishing risk according to the current model and analysis rules. It does not guarantee that the website is completely safe.

---

## 7. Project Development Risks

The project is developed as an academic project with limited development time and resources.

Possible development risks include:

- Limited testing data
- Limited access to real-time threat intelligence
- Changes in phishing techniques
- Dataset distribution limitations
- Time constraints
- Dependency compatibility issues
- Machine Learning experimentation taking longer than expected
- OCR extraction errors
- Integration issues between application components

**Mitigation:**

- Maintain a modular project structure.
- Test individual components before integration.
- Keep the production model separate from experimental models.
- Use Git for version control.
- Document known limitations and unresolved issues.
- Perform final end-to-end testing before project submission.

---

## 8. Version and Dependency Risks

The application depends on Python libraries and external packages for Machine Learning, image processing, OCR, application development, and report generation.

Changes in package versions may cause compatibility issues in the future.

**Mitigation:**

- Use a Python virtual environment.
- Maintain the project dependency requirements.
- Keep the working development environment documented.
- Use version control to track application changes.

---

## 9. Risk Management Approach

TrustLens manages project and system risks through the following activities:

1. Dataset analysis
2. Data preprocessing and validation
3. Machine Learning model evaluation
4. Structural robustness testing
5. Targeted legitimate and phishing URL testing
6. False-positive analysis
7. False-negative analysis
8. Functional application testing
9. QR-code testing
10. Screenshot/OCR testing
11. Production model save/reload verification
12. Clear documentation of limitations

These activities help identify weaknesses before the system is used for demonstration or evaluation.

---

## 10. Overall Risk Assessment

The main risks associated with TrustLens are related to the limitations of URL-based phishing detection rather than the basic operation of the application.

The application can successfully process supported URL inputs and generate a Machine Learning-based risk assessment, but the prediction is dependent on the patterns learned from the training data and the structural information available in the submitted URL.

The most important limitation is that TrustLens does not inspect the live website or use real-time threat intelligence.

---

## 11. Conclusion

TrustLens is designed as an **AI-assisted URL risk analyzer and cybersecurity awareness tool**, rather than a complete cybersecurity detection system.

The main risks include:

- False positives
- False negatives
- Dataset limitations
- Model limitations
- OCR errors
- QR-code errors
- Invalid input
- Dependency and development constraints
- Lack of live website and threat-intelligence verification

These risks are managed through dataset analysis, Machine Learning evaluation, structural robustness testing, application testing, and clear documentation of limitations.

TrustLens should therefore be used as a **supporting security-awareness and decision-support tool**, not as a guaranteed determination of whether a website is malicious or safe.