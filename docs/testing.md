# TrustLens Testing Documentation

## 1. Overview

This document describes the testing and validation performed for the **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer**.

Testing was performed at both the Machine Learning model level and the application level. The purpose was to verify that the system correctly handles different input types, produces predictions using the final production model, and provides the expected risk assessment and explanations.

Testing also included difficult legitimate URLs to identify false positives and understand the limitations of structural URL-based analysis.

---

## 2. Testing Environment

| Component | Details |
|---|---|
| Operating System | Windows |
| Python | 3.13.14 |
| Streamlit | 1.60.0 |
| scikit-learn | 1.9.0 |
| pandas | 3.0.5 |
| Dataset | PhiUSIIL |
| Production Model | Random Forest pipeline |
| Production Features | 17 |
| Model Serialization | Joblib |

---

## 3. Functional Testing

### 3.1 URL Input Testing

| Test ID | Test Case | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T01 | Legitimate website | `https://www.google.com` | Legitimate | Legitimate | PASS |
| T02 | Legitimate website | `https://www.microsoft.com` | Legitimate | Legitimate | PASS |
| T03 | Phishing URL | `http://secure-login-example.com/verify/account` | Phishing | Phishing | PASS |
| T04 | Invalid input | `hello` | Validation error | Validation error | PASS |

The URL input mode successfully validates the submitted URL, extracts the required features, uses the saved production model, and displays the resulting classification and risk assessment.

---

## 4. QR Code Testing

TrustLens supports QR-code input by decoding a QR image and analyzing the URL contained inside it.

### 4.1 QR Code Test

| Test ID | Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T05 | QR containing phishing URL | Phishing | Phishing | PASS |

Tested QR destination:

```text
https://account-verification-update.com/login?redirect=%2Faccount%2Fverify
```

Result:

- Classification: **Phishing**
- Risk Level: **High**
- Risk Score: **100/100**

The QR code was successfully decoded and the extracted URL was passed to the same prediction pipeline used by the normal URL input mode.

---

## 5. Screenshot / OCR Testing

TrustLens supports screenshot analysis by using OCR to extract a URL from the browser/address-bar area.

The extracted URL is then validated and passed to the production prediction pipeline.

### 5.1 Screenshot Testing

| Test ID | Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T06 | Screenshot containing phishing URL | Phishing | Phishing | PASS |
| T07 | Screenshot containing legitimate URL | Legitimate | Legitimate | PASS |

The phishing screenshot test successfully extracted the URL and classified it as **Phishing / High Risk**.

A legitimate screenshot was also processed successfully.

### 5.2 OCR Limitation Observed

OCR can introduce character-level errors when the browser address bar is unclear or the screenshot quality is poor.

For example, an intended legitimate Google URL was extracted with an altered domain such as:

```text
https://ww.google.com/maps
```

The application analyzed the OCR-extracted URL rather than the original intended URL.

This demonstrates that screenshot analysis depends partly on OCR quality. Clear screenshots with readable browser address bars provide more reliable URL extraction.

---

## 6. Model Prediction Testing

### 6.1 Basic Legitimate URLs

| URL | Classification | Risk Level | Risk Score | Status |
|---|---|---|---:|---|
| `https://www.google.com` | Legitimate | Low | 0 | PASS |
| `https://www.microsoft.com` | Legitimate | Low | 0 | PASS |
| `https://www.amazon.com` | Legitimate | Low | 0 | PASS |
| `https://www.wikipedia.org` | Legitimate | Low | 0 | PASS |
| `https://github.com` | Legitimate | Low | 0 | PASS |

### 6.2 Phishing URLs


| URL | Classification | Risk Level | Risk Score | Status |
|---|---|---|---:|---|
| `http://secure-login-example.com/verify/account` | Phishing | High | 93 | PASS |
| `https://account-verification-update.com/login?redirect=%2Faccount%2Fverify` | Phishing | High | 100 | PASS |
| `http://paypal-security-check.example.com/login/verify` | Phishing | High | 97 | PASS |
| `https://secure-account-verification.example.com/update/password` | Suspicious | Medium | 44 | PASS |

The tested phishing examples were consistently detected as phishing or suspicious according to the defined risk thresholds.

These are targeted test examples and should not be interpreted as a measurement of overall real-world phishing detection accuracy.

---

## 7. Final Production Model Verification

The final production model is stored as:

```text
models/trustlens_production_pipeline.joblib
```

The saved model was successfully reloaded after serialization.

### 7.1 Reload Verification

| Test | Result |
|---|---|
| Model reload | Successful |
| Model classes | `[0 1]` |
| Class `0` | Phishing |
| Class `1` | Legitimate |

A real long legitimate URL was tested after reloading the saved model:

```text
https://www.google.com/maps/@19.1922063,72.9234965,11.82z?entry=ttu&g_ep=EgoyMDI2MDkwMi4wIKXMDSoASAFQAw%3D%3D
```

Result:

- Prediction: **Legitimate**
- Legitimate probability: **79.67%**
- Phishing probability: **20.33%**

A phishing query URL was also tested after reload and produced:

- Prediction: **Phishing**
- Legitimate probability: **0.00%**
- Phishing probability: **100.00%**

This confirms that the saved production pipeline can be loaded and used for application inference without retraining the model.

---

## 8. Model Holdout Evaluation

The final V4 production candidate was evaluated using a held-out test set.

### 8.1 Holdout Accuracy

**98.34%**

This value represents performance on the held-out evaluation set. It should not be interpreted as guaranteed real-world accuracy.

### 8.2 Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Phishing | 0.9966 | 0.9648 | 0.9805 |
| Legitimate | 0.9739 | 0.9975 | 0.9856 |
| **Accuracy** | | | **0.9834** |

### 8.3 Confusion Matrix

```text
[[19771   721]
 [   67 26955]]
```

The confusion matrix shows the number of correctly and incorrectly classified examples in the held-out evaluation set.

---

## 9. Targeted False-Positive Testing

Additional testing was performed using legitimate websites with more complex URL structures.

The purpose of this testing was to identify cases that differ from the simpler legitimate URLs commonly represented in the original dataset.

Examples included:

| Test Case | Result |
|---|---|
| Google Search | Suspicious / Medium |
| Google Maps complex URL | Phishing / High |
| Amazon Search | Suspicious / Medium |
| YouTube Search | Suspicious / Medium |
| GitHub Search | Phishing / High |
| Microsoft Login | Phishing / High |
| Google Accounts | Phishing / High |
| Google Support | Phishing / High |

These results demonstrate that the model can produce false positives when legitimate websites contain complex paths, query parameters, authentication paths, or other URL structures that resemble patterns strongly associated with phishing URLs in the training data.

These targeted results are intentionally documented rather than excluded because they help show the limitations of the current URL-based approach.

---

## 10. Risk Classification Testing

TrustLens converts the model's phishing probability into a risk assessment.

| Phishing Probability | Risk Level | Final Classification |
|---|---|---|
| Below 40% | Low | Legitimate |
| 40% – 74.99% | Medium | Suspicious |
| 75% or higher | High | Phishing |

The risk score is displayed on a scale from 0 to 100.

The score is derived from the estimated phishing probability, where a higher score represents a higher estimated phishing risk.

---

## 11. Explanation Testing

The application generates human-readable reasons based on detected URL signals.

Examples include:

- HTTP instead of HTTPS
- Suspicious keywords
- IP-address pattern in the domain
- Hyphen in the domain
- Percent-encoded or obfuscated characters
- Unusually long URL
- Deep URL path structure
- Multiple subdomains
- High number of dots

These explanations are intended to help users understand the URL signals associated with the result.

They are rule-based explanations and should not be interpreted as exact feature-attribution scores from the Random Forest model.

---

## 12. PDF Report Testing

TrustLens provides a PDF report after an analysis.

The report was tested using a legitimate website analysis.

The generated report successfully contained:

- Analyzed URL
- Verdict
- Risk level
- Risk score
- Explanation / detected signals
- Technical URL features
- Security recommendations

The PDF was successfully generated and opened without an obvious formatting problem.

**Status: PASS**

---

## 13. Error and Validation Testing

The application was also tested with invalid or incomplete input.

| Test Case | Expected Behaviour | Status |
|---|---|---|
| Empty URL | Show validation message | PASS |
| Invalid text such as `hello` | Reject input | PASS |
| Missing URL in screenshot | Show warning | PASS |
| Invalid URL extracted from screenshot | Show warning | PASS |
| QR image containing a valid URL | Decode and analyze | PASS |

---

## 14. Testing Summary

The major application functions were successfully tested:

| Functionality | Status |
|---|---|
| URL analysis | PASS |
| URL validation | PASS |
| Machine Learning prediction | PASS |
| Risk classification | PASS |
| Risk explanations | PASS |
| QR code analysis | PASS |
| Screenshot/OCR analysis | PASS |
| PDF report generation | PASS |
| Saved model reload | PASS |
| Invalid input handling | PASS |

The core application workflow therefore operates successfully with the saved production model.

---

## 15. Limitations Identified During Testing

Testing also identified several important limitations.

### 15.1 Structural URL Dependence

The model primarily analyzes lexical and structural URL characteristics. It does not directly inspect the content or behaviour of the website.

### 15.2 False Positives on Complex Legitimate URLs

Some legitimate URLs containing search parameters, deep paths, map coordinates, authentication paths, or other complex structures were assigned medium or high phishing risk.

This is partly related to the distribution of the source dataset, where legitimate examples contain far fewer complex URL structures than phishing examples.

### 15.3 OCR Dependence

Screenshot analysis depends on the quality of the extracted browser-bar text. OCR errors can change characters in a URL and therefore affect the final analysis.

### 15.4 No Live Website Verification

TrustLens does not currently verify:

- Live website reputation
- Domain ownership
- Domain age
- DNS records
- SSL certificate validity
- Real-time malware status
- External threat intelligence
- Website content
- Browser behaviour

Therefore, the TrustLens risk score should not be treated as a definitive statement that a website is malicious or safe.

---

## 16. Conclusion

Testing confirms that TrustLens successfully performs URL-based website risk analysis and supports multiple input methods including direct URL input, QR-code analysis, and screenshot/OCR-based URL extraction.

The final production model was successfully saved, reloaded, and used for inference. Core legitimate and phishing test cases produced the expected results.

The held-out evaluation produced 98.34% accuracy, while targeted testing also identified false positives for some legitimate complex URLs. These targeted results demonstrate an important limitation of structural URL-based phishing detection and are documented as part of the evaluation.

TrustLens should therefore be considered an AI-assisted website trust and phishing risk analyzer, rather than a guaranteed real-time phishing detection system.