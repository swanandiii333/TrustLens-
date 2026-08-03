# 08. Tech Stack

## Purpose

This document lists the technologies selected for Version 1 of the **AI-Powered Phishing URL Detection System**. It also explains why each technology was chosen and how it contributes to the overall project.

The selected technologies are open-source, widely adopted in industry, beginner-friendly, and appropriate for building a Machine Learning–based cybersecurity application.

---

# Programming Language

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Python** | Core programming language | Python is the industry standard for Machine Learning, Data Science, and rapid application development. It provides a rich ecosystem of libraries that support data preprocessing, model training, visualization, and web application development within a single language. |

---

# Machine Learning

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Scikit-learn** | Machine Learning framework | Used for feature preprocessing, model training, prediction, and evaluation. It provides reliable implementations of many classical Machine Learning algorithms. |
| **Candidate Algorithms** | Model experimentation | Multiple Scikit-learn classification algorithms (Logistic Regression, Decision Tree, and Random Forest) will be trained and evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. Random Forest is expected to be the primary model due to its strong performance on phishing URL classification tasks, but the final model will be selected based on experimental results rather than assumptions. |

---

# Data Handling & Visualization

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Pandas** | Data manipulation | Used to load, clean, preprocess, and manipulate the phishing URL dataset efficiently. |
| **NumPy** | Numerical computing | Provides efficient numerical operations and supports feature extraction and Machine Learning workflows. |
| **Matplotlib** | Data visualization | Used to visualize dataset characteristics and evaluation results such as confusion matrices and class distributions. |

---

# Model Persistence

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Joblib** | Save and load trained models | Used to serialize the trained Machine Learning model after training and reload it during prediction without retraining the model each time the application starts. |

---

# User Interface

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Streamlit** | Web application framework | Used to build a lightweight, interactive web interface entirely in Python. It enables rapid development of Machine Learning applications without requiring frontend frameworks like React or Angular. |

---

# Development Tools

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Visual Studio Code** | Code editor | Used for writing, debugging, and managing the project source code with built-in terminal and Git integration. |
| **Git** | Version control | Tracks source code changes through meaningful commits and supports collaborative software development practices. |
| **GitHub** | Remote repository hosting | Hosts the project online, provides version backup, enables portfolio showcasing, and maintains complete project history. |

---

# Project Structure & Documentation

| Technology | Purpose | Justification |
|------------|---------|---------------|
| **Markdown (.md)** | Documentation | Used for writing project planning documents, technical documentation, and the project README in a clean, readable, and GitHub-friendly format. |

---

# Technology Selection Summary

The chosen technology stack emphasizes:

- Open-source tools
- Cross-platform compatibility
- Beginner-friendly development
- Industry-standard Machine Learning libraries
- Easy maintenance and future scalability

This combination provides everything required to build, evaluate, document, and demonstrate the AI-Powered Phishing URL Detection System while keeping the project practical for a single-developer academic environment.