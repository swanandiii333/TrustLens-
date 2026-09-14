# 09. Project Timeline

## 1. Overview

The TrustLens project was planned as an academic project covering problem identification, dataset preparation, Machine Learning development, backend implementation, application development, testing, documentation, and final project preparation.

The development plan was organized across **16 weeks**. Some activities were completed iteratively rather than strictly week-by-week, particularly Machine Learning experiments, robustness testing, application testing, and documentation updates.

---

## 2. 16-Week Development Timeline

| Week | Phase | Main Activities |
|------|-------|-----------------|
| **Week 1** | Project Planning | Define project idea, identify the phishing detection problem, and establish the initial project vision. |
| **Week 2** | Project Planning | Define objectives, scope, requirements, target users, and initial system architecture. |
| **Week 3** | Environment Setup | Set up Python, virtual environment, required libraries, Jupyter Notebook, development tools, Git, and GitHub repository. |
| **Week 4** | Dataset Exploration | Select the PhiUSIIL dataset, inspect the available fields, understand the labels, and perform initial exploratory analysis. |
| **Week 5** | Dataset Exploration | Analyze URL characteristics, phishing/legitimate distributions, duplicates, suspicious patterns, and dataset limitations. |
| **Week 6** | Data Preprocessing | Clean the dataset, remove duplicate URLs, prepare labels, and create the data required for Machine Learning. |
| **Week 7** | Feature Engineering | Identify useful URL-based structural and lexical features and implement the initial feature extraction workflow. |
| **Week 8** | Feature Engineering | Refine the URL features, perform feature analysis, and finalize the 17 production features used by TrustLens. |
| **Week 9** | Machine Learning | Prepare training and testing data and train candidate Machine Learning models. |
| **Week 10** | Machine Learning | Evaluate candidate models and perform additional experiments to improve structural robustness. |
| **Week 11** | Machine Learning | Perform targeted testing, analyze false positives and false negatives, select the final production pipeline, and verify its predictions. |
| **Week 12** | Model Finalization | Save the final production pipeline using Joblib and verify that the saved model can be reloaded successfully. |
| **Week 13** | Backend and Application | Connect the saved production model to the backend and implement URL prediction, probabilities, risk scoring, and classification. |
| **Week 14** | Streamlit Application | Develop the TrustLens interface and integrate URL, QR-code, screenshot/OCR, explanations, recommendations, and PDF reporting. |
| **Week 15** | Testing | Perform functional testing, legitimate/phishing URL testing, invalid-input testing, QR/OCR testing, risk explanation testing, and false-positive analysis. |
| **Week 16** | Documentation and Finalization | Complete documentation, review the application, prepare screenshots and presentation material, organize the GitHub repository, and prepare for demonstration and viva. |

---

## 3. Phase 1 – Project Planning

### Weeks 1–2

The initial phase focused on understanding the problem and defining the direction of the project.

Main activities included:

- Defining the TrustLens project idea
- Identifying phishing website detection as the core problem
- Defining project objectives
- Identifying target users
- Defining Version 1 scope
- Preparing the initial requirements
- Preparing the initial architecture
- Establishing the project documentation structure

### Deliverables

- Project idea
- Problem statement
- Objectives
- Project scope
- Initial requirements
- Initial architecture

---

## 4. Phase 2 – Development Environment Setup

### Week 3

The development environment was prepared for Machine Learning and application development.

Activities included:

- Installing Python
- Creating the Python virtual environment
- Installing required libraries
- Setting up Jupyter Notebook
- Setting up the development environment
- Creating the Git repository
- Connecting the project to GitHub
- Organizing the project directory structure

### Deliverables

- Working Python environment
- Project repository
- Initial project structure
- Development workflow

---

## 5. Phase 3 – Dataset and Data Analysis

### Weeks 4–5

The PhiUSIIL phishing and legitimate URL dataset was selected for Machine Learning development.

Activities included:

- Loading the dataset
- Inspecting dataset columns
- Understanding the target labels
- Checking the number of legitimate and phishing URLs
- Identifying duplicate URLs
- Studying URL-length patterns
- Studying domain and subdomain characteristics
- Analyzing URL paths and query parameters
- Studying suspicious keywords
- Identifying limitations in the source dataset

### Deliverables

- Dataset analysis
- Data quality observations
- Understanding of phishing and legitimate URL patterns
- Identified dataset limitations

---

## 6. Phase 4 – Data Preprocessing

### Week 6

The dataset was prepared for Machine Learning.

Main activities included:

- Removing duplicate URLs
- Cleaning and preparing URL records
- Preparing the target labels
- Checking feature values
- Preparing training and testing data
- Ensuring the data could be used consistently by the Machine Learning pipeline

### Deliverables

- Cleaned dataset
- Prepared Machine Learning data
- Preprocessing workflow

---

## 7. Phase 5 – Feature Engineering

### Weeks 7–8

The feature engineering phase focused on identifying URL characteristics that could help distinguish phishing URLs from legitimate URLs.

The final production feature set contains 17 URL-based features:

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

The feature extraction logic was implemented so that the same feature definitions could be used during application-time prediction.

### Deliverables

- Feature analysis
- URL feature extractor
- Final 17-feature production schema

---

## 8. Phase 6 – Machine Learning Development

### Weeks 9–11

The Machine Learning phase involved training, evaluating, and testing classification models.

Activities included:

- Preparing training and testing datasets
- Training candidate models
- Comparing model behaviour
- Evaluating classification performance
- Studying prediction probabilities
- Performing structural robustness experiments
- Testing legitimate URLs with different URL structures
- Testing phishing URL patterns
- Investigating false positives
- Investigating false negatives
- Selecting the final production approach

The final production implementation uses a **Random Forest Classifier** inside a Scikit-learn pipeline.

### Deliverables

- Trained Machine Learning pipeline
- Model evaluation results
- Structural robustness analysis
- False-positive analysis
- Final production model candidate

---

## 9. Phase 7 – Production Model Finalization

### Week 12

The selected production pipeline was finalized and saved for application use.

Activities included:

- Finalizing the production pipeline
- Saving the trained pipeline using Joblib
- Loading the saved model again
- Verifying model classes
- Testing legitimate URLs
- Testing phishing URLs
- Confirming that the application can reuse the saved model without retraining

The production model is stored as:

`models/trustlens_production_pipeline.joblib`

### Deliverables

- Final production Machine Learning pipeline
- Verified saved model
- Model reload verification

---

## 10. Phase 8 – Backend Development

### Week 13

The backend was developed to connect the saved Machine Learning pipeline with the application.

Main activities included:

- Implementing URL feature extraction
- Loading the saved production model
- Implementing the `predict_url()` function
- Generating prediction probabilities
- Calculating the risk score
- Assigning Low, Medium, or High risk levels
- Assigning Legitimate, Suspicious, or Phishing classifications
- Implementing rule-based risk explanations
- Generating security recommendations

### Deliverables

- Working prediction backend
- Risk classification system
- Explanation system
- Recommendation system

---

## 11. Phase 9 – Streamlit Application Development

### Week 14

The Streamlit interface was developed and connected to the backend.

Implemented functionality includes:

- Direct URL analysis
- URL validation
- QR-code URL extraction
- Screenshot/OCR URL extraction
- Machine Learning prediction
- Risk score display
- Risk level display
- Security explanations
- Security recommendations
- Technical feature display
- PDF report generation

All supported input methods eventually use the same core URL analysis and prediction pipeline.

### Deliverables

- Working TrustLens Streamlit application
- Integrated backend
- URL, QR, and screenshot/OCR analysis
- PDF reporting

---

## 12. Phase 10 – Testing and Validation

### Week 15

Testing focused on verifying both individual features and the complete application workflow.

Testing activities included:

- Legitimate URL testing
- Phishing URL testing
- Invalid input testing
- QR-code testing
- Screenshot/OCR testing
- Prediction probability testing
- Risk classification testing
- Risk explanation testing
- PDF report testing
- Production model reload testing
- False-positive analysis
- Structural robustness testing

Testing also helped identify the limitations of URL-only structural analysis, particularly for complex legitimate URLs.

### Deliverables

- Functional test results
- Model behaviour analysis
- Application validation
- Identified limitations

---

## 13. Phase 11 – Documentation and Finalization

### Week 16

The final phase focused on preparing the project for submission and demonstration.

Activities included:

- Reviewing project documentation
- Updating technical documentation to match the implemented system
- Updating the README
- Reviewing the project structure
- Preparing screenshots
- Reviewing the final Streamlit application
- Verifying the production model
- Organizing Git and GitHub history
- Preparing presentation material
- Preparing for project demonstration and viva

### Deliverables

- Updated documentation
- README
- Final project repository
- Screenshots
- Presentation material
- Viva preparation

---

## 14. Major Project Milestones

The major milestones of the project were:

### Milestone 1 – Project Definition

The problem, objectives, scope, and initial architecture were defined.

### Milestone 2 – Dataset Preparation

The PhiUSIIL dataset was analyzed, cleaned, and prepared for Machine Learning.

### Milestone 3 – Feature Engineering

The final 17 production URL features and shared feature extraction logic were established.

### Milestone 4 – Machine Learning Development

The Machine Learning pipeline was trained, evaluated, and tested for structural robustness.

### Milestone 5 – Production Model

The final Random Forest production pipeline was saved and successfully reloaded using Joblib.

### Milestone 6 – Backend Integration

The prediction backend was connected to the production model and risk analysis logic.

### Milestone 7 – Application Development

The Streamlit application was integrated with URL, QR-code, and screenshot/OCR analysis.

### Milestone 8 – Testing

The complete application was tested using legitimate URLs, phishing URLs, invalid inputs, QR codes, screenshots, and PDF reports.

### Milestone 9 – Final Documentation

The project documentation, README, screenshots, GitHub repository, and presentation material were prepared for final submission.

---

## 15. Timeline Summary

The TrustLens development timeline progresses from **planning → dataset preparation → feature engineering → Machine Learning → production model → backend → Streamlit application → testing → documentation and finalization**.

The timeline also allowed iterative Machine Learning experimentation and testing rather than treating model development as a single fixed step.

This approach helped identify limitations in the source dataset and evaluate how the model behaves on URL structures that differ from the original training distribution.

---

## 16. Conclusion

The project timeline provides a structured development path for TrustLens from initial problem definition to final application and documentation.

The completed workflow combines Machine Learning development with practical application development, testing, and cybersecurity-focused analysis. The final project is organized so that the trained production model can be reused by the application while future improvements can be added without changing the complete architecture.