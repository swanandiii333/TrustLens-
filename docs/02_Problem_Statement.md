# 02. Problem Statement

## Current Situation

Phishing attacks continue to be one of the most common cybersecurity threats, targeting individuals and organizations worldwide. Attackers create fake websites that closely resemble legitimate ones in order to steal sensitive information such as usernames, passwords, banking credentials, credit card details, and personal data.

Users commonly encounter suspicious website links through:

- Emails
- WhatsApp messages
- SMS (Smishing)
- Social media platforms
- QR codes
- Online advertisements

To determine whether a website is safe, most users rely on two primary approaches:

1. **Manual judgment** — inspecting the URL for spelling mistakes, unusual domain names, suspicious characters, or other visible warning signs.
2. **Existing browser security mechanisms** — web browsers and security services use blacklists, reputation systems, and known threat databases to warn users about many malicious websites.

While these approaches provide valuable protection, they cannot identify every phishing website, particularly newly created or previously unseen attacks.

---

## The Gap

Modern phishing websites have become increasingly sophisticated. Attackers carefully design URLs that closely imitate legitimate websites by using misleading words, additional subdomains, slight spelling variations, shortened links, or deceptive domain names.

At the same time, users often browse the internet quickly and make decisions under time pressure. Many people click links without carefully examining the URL, especially when the website appears convincing or is received from a seemingly trusted source.

Existing security tools generally provide a simple warning or a binary classification without explaining *why* a website appears suspicious. As a result, users may still struggle to understand the actual risks and make informed security decisions.

---

## Who Is Affected

Although phishing can target anyone, some groups are particularly vulnerable:

- Business employees handling work-related links and documents.
- Students accessing educational portals and online resources.
- General internet users performing online banking, shopping, or social networking.
- Individuals with limited cybersecurity awareness.

Since phishing attacks primarily exploit human trust rather than technical vulnerabilities, even experienced users can occasionally be deceived.

---

## Why Existing Solutions Are Not Always Enough

Current phishing detection systems provide an important first layer of defense, but they also have several limitations.

- Many tools rely heavily on known blacklists and reputation databases, making it difficult to detect newly emerging phishing websites.
- Most systems simply label a website as "Safe" or "Phishing" without explaining the reasoning behind the decision.
- Users often receive little guidance about which characteristics of the URL appear suspicious.
- Many existing tools assume users already possess basic cybersecurity knowledge, making them less useful for non-technical users.

Consequently, users are often forced to make security decisions without understanding the factors that contribute to website risk.

---

## Problem Statement

**Internet users frequently struggle to determine whether a website is trustworthy, particularly when phishing websites closely imitate legitimate ones. Existing tools often provide only binary predictions or limited explanations, making it difficult for users to understand the actual level of risk. Therefore, there is a need for an intelligent and explainable system that not only predicts whether a website is legitimate or phishing but also evaluates its overall trustworthiness, identifies suspicious characteristics, and provides practical security recommendations that help users make informed decisions.**

---

## Project's Role

TrustLens is designed as an **AI-Based Website Trust & Phishing Risk Analyzer** rather than a simple phishing classifier.

The system combines Machine Learning with rule-based cybersecurity analysis to examine multiple characteristics of a website URL.

For every analyzed website, TrustLens provides:

- A prediction (Legitimate or Phishing)
- A Website Trust Score (0–100)
- A Threat Level
- Model Confidence
- Rule-Based Security Findings
- Explainable analysis of suspicious URL characteristics
- Practical security recommendations

Rather than replacing browser security mechanisms or antivirus software, TrustLens serves as a **decision-support tool** that helps users better understand website risks before interacting with potentially malicious websites.