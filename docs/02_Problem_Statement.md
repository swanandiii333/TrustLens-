# 02. Problem Statement

## Current Situation

Phishing attacks remain one of the most common cybersecurity threats, targeting individuals and organizations worldwide. One of the primary methods used by attackers is the creation of fake websites that closely resemble legitimate ones to steal sensitive information such as usernames, passwords, banking details, and personal data.

Most users rely on two main approaches to determine whether a website is safe:

1. **Manual judgment** — inspecting the website URL, looking for spelling mistakes, suspicious domain names, or unusual website behavior before visiting the page.
2. **Browser security mechanisms** — modern web browsers and security services warn users about many known malicious websites using blacklists, reputation systems, and other security techniques.

While these measures provide valuable protection, they cannot identify every phishing website, especially newly created or previously unseen ones.

---

## The Gap

Modern phishing websites are becoming increasingly sophisticated. Attackers carefully design URLs that closely resemble legitimate websites by using misleading words, similar domain names, additional characters, or slight spelling variations. As a result, many phishing URLs appear trustworthy at first glance.

At the same time, users often browse the internet quickly and may not carefully examine every website address before clicking a link. This combination of convincing phishing URLs and limited user attention increases the risk of visiting malicious websites.

---

## Who Is Affected

Although anyone using the internet can become a victim of phishing attacks, the following groups are particularly vulnerable:

- Business employees who frequently receive links related to work.
- Students accessing online learning platforms.
- General internet users performing activities such as online shopping, banking, or social media browsing.

Because phishing attacks rely heavily on human judgment, even experienced users can occasionally mistake a malicious website for a legitimate one.

---

## Why Existing Solutions Are Not Always Enough

Existing browser security features and website reputation services provide an important first layer of defense. However, they may not always detect newly created phishing websites or sophisticated attacks that closely imitate legitimate websites.

In addition, these security mechanisms usually provide only a warning or allow access without explaining why a URL appears suspicious. As a result, users often have to rely on their own judgment when deciding whether a website can be trusted.

---

## Problem Statement

**Internet users often find it difficult to distinguish between legitimate and phishing websites, especially when attackers create URLs that closely resemble genuine websites. This increases the risk of users unknowingly visiting malicious websites and exposing sensitive information. Therefore, there is a need for an intelligent system that can analyze website URLs and assist users in identifying potential phishing websites before they proceed.**

---

## Project's Role

This project is not intended to replace existing browser security features or antivirus solutions. Instead, it aims to function as a **decision-support tool** by using Machine Learning to analyze website URLs and predict whether they are phishing or legitimate.

The system provides users with a prediction along with a confidence score, helping them make more informed decisions before visiting potentially suspicious websites.