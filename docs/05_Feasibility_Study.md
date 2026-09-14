# 05. Feasibility Study

## 1. Purpose

This document evaluates the feasibility of **TrustLens – AI-Based Website Trust & Phishing Risk Analyzer** from technical, economic, and operational perspectives.

The purpose of the feasibility study is to determine whether the project can be developed and demonstrated successfully within the available academic time, resources, and technical environment.

---

## 2. Technical Feasibility

TrustLens is technically feasible because the project can be developed using Python and commonly available open-source libraries.

### 2.1 Programming Environment

The project is developed using:

- Python 3.13.14
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib
- Streamlit
- OpenCV
- OCR-related tools
- Git and GitHub
- Jupyter Notebook

These technologies are suitable for Machine Learning, data processing, application development, and project documentation.

### 2.2 Machine Learning Feasibility

TrustLens uses the publicly available **PhiUSIIL phishing and legitimate URL dataset** for Machine Learning development.

The dataset can be processed using Pandas and NumPy, while Scikit-learn provides the required tools for:

- Data preprocessing
- Feature processing
- Model training
- Model evaluation
- Prediction
- Probability estimation

The final TrustLens production pipeline uses a **Random Forest Classifier** with a predefined set of **17 URL-based features**.

The trained pipeline is saved using Joblib and loaded by the application during prediction. This means the application does not need to retrain the model every time it starts.

### 2.3 Feature Extraction Feasibility

The required URL features can be extracted directly from the submitted URL without visiting the website.

The production feature set includes characteristics such as:

- URL length
- Domain length
- IP-address usage
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
- Hyphen usage in the domain
- Path depth

The same feature extraction logic is used by the backend during prediction, helping maintain consistency between the trained model and the application.

### 2.4 Application Feasibility

The application is implemented using Streamlit, allowing the Machine Learning model and backend logic to be connected to an interactive user interface without requiring a separate frontend framework.

The implemented application supports:

- Direct URL analysis
- QR-code URL analysis
- Screenshot-based URL extraction using OCR
- Risk classification
- Risk score calculation
- Explainable security findings
- Security recommendations
- PDF report generation

Therefore, the planned application functionality can be implemented using the selected technology stack.

---

## 3. Economic Feasibility

TrustLens is economically feasible for an academic project.

The main technologies used are open-source and do not require paid software licenses.

### 3.1 Software Costs

The project uses free or open-source tools such as:

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Streamlit
- OpenCV
- Joblib
- Jupyter Notebook
- Git
- GitHub

No commercial Machine Learning platform or paid development framework is required for the current version.

### 3.2 Hardware Requirements

The project does not require specialized hardware.

Development, model training, testing, and application execution can be performed on a standard personal computer with sufficient storage and memory for the dataset and Machine Learning workflow.

GPU hardware is not required for the final Random Forest-based implementation.

### 3.3 Development Resources

The project is developed as an academic project by a single student developer.

The use of Python-based open-source tools reduces development and infrastructure costs while still providing the functionality required for the project.

---

## 4. Operational Feasibility

TrustLens is operationally feasible because the application is designed to be simple to use and can run locally.

Users can provide a website URL and receive:

- Prediction
- Phishing probability
- Legitimate probability
- Risk score
- Risk level
- Explanation of suspicious URL characteristics
- Security recommendations

The system does not require users to have advanced Machine Learning or cybersecurity knowledge to understand the basic result.

The Streamlit interface provides a straightforward way to interact with the system.

---

## 5. Usability Feasibility

The project is designed as a decision-support tool rather than a replacement for browser security systems or antivirus software.

The application presents the result in an understandable form using:

- Legitimate / Suspicious / Phishing classification
- Low / Medium / High risk level
- Risk score from 0–100
- Human-readable security reasons
- Practical recommendations

This makes the system suitable for demonstration and educational use.

---

## 6. Project Constraints

The project is developed under the following constraints:

- **Developer:** Single student developer
- **Duration:** One academic semester
- **Programming Language:** Python
- **Dataset:** Publicly available phishing URL dataset
- **Application:** Local Streamlit application
- **Resources:** Primarily free and open-source tools
- **Analysis:** URL-based structural and lexical analysis

The system does not currently depend on live threat-intelligence services or external reputation databases for prediction.

---

## 7. Limitations Affecting Feasibility

Although the project is feasible, the current implementation has some limitations.

TrustLens primarily analyzes URL structure and lexical characteristics. It does not currently perform:

- Live website reputation checks
- WHOIS or domain-age verification
- Live DNS analysis
- Website content analysis
- Real-time threat-intelligence lookups
- Browser behavior analysis
- Malware analysis
- Complete SSL certificate validation

The model can also produce false positives for some legitimate URLs with complex structures, query parameters, deep paths, or authentication-related terms.

Therefore, TrustLens should be treated as an **AI-assisted phishing risk analysis and decision-support system**, not as a guaranteed determination of whether a website is malicious.

---

## 8. Feasibility Conclusion

Based on the technical, economic, operational, and usability evaluation, **TrustLens is feasible as an academic cybersecurity project**.

The required software tools are available, the Machine Learning workflow can be executed on standard hardware, and the application can be developed and operated locally without expensive infrastructure.

The completed implementation demonstrates that the selected approach is practical for URL-based phishing risk analysis while also recognizing the limitations of relying primarily on URL-level features.