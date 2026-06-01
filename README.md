# 🛡️ Advanced Phishing Email Detection & Security Analysis System

A comprehensive cybersecurity tool developed using Python and Flask for detecting phishing emails through content analysis, email authentication verification, sender spoofing detection, attachment inspection, and automated report generation.

---

# 📌 Project Overview

Phishing attacks are among the most common cybersecurity threats used to steal credentials, financial information, and sensitive data. This project helps identify phishing emails by analyzing:

- Email Content
- Email Headers
- Sender Authentication
- URL Safety
- Domain Reputation
- Attachments
- Grammar & Spelling Indicators

The application classifies emails into:

- 🟢 Safe
- 🟡 Suspicious
- 🔴 Phishing

and generates a detailed investigation report.

---

# 🎯 Objectives

- Detect phishing indicators in email content.
- Analyze SPF, DKIM, and DMARC authentication results.
- Identify sender spoofing attempts.
- Detect suspicious URLs and fake domains.
- Analyze potentially dangerous attachments.
- Identify grammar and spelling anomalies commonly found in phishing emails.
- Generate detailed security reports.
- Provide risk scoring and recommendations.

---

# ✨ Features

## 📧 Email Content Analysis

### ✔ Urgency Keyword Detection

Examples:

- Urgent
- Immediate Action Required
- Act Now
- Emergency

### ✔ Generic Greeting Detection

Examples:

- Dear User
- Dear Customer
- Hello Friend

### ✔ Grammar & Spelling Analysis

Detects:

- Common phishing spelling mistakes
- Excessive capitalization
- Repeated punctuation
- Sentence capitalization issues

---

## 🌐 URL & Domain Analysis

### ✔ Suspicious Link Detection

Detects:

- HTTP links
- Unknown domains
- Potential phishing URLs

### ✔ Fake Domain Detection

Examples:

- paypal-secure-login.com
- amazon-security-check.com

### ✔ Blacklisted Domain Detection

Checks URLs against a blacklist database.

---

## 📨 Email Header Analysis

### ✔ SPF Verification

Checks whether the sender is authorized to send emails from the domain.

### ✔ DKIM Verification

Verifies message authenticity and integrity.

### ✔ DMARC Verification

Determines whether authentication policies are properly enforced.

---

## 🎭 Sender Spoofing Detection

Detects:

- From vs Return-Path mismatches
- Failed SPF records
- Failed DKIM signatures
- Failed DMARC validation

---

## 📎 Attachment Analysis

Detects potentially dangerous attachments such as:

- `.exe`
- `.bat`
- `.cmd`
- `.js`
- `.jar`
- `.zip`
- `.rar`
- `.docm`
- `.xlsm`
- `.pptm`

---

## 📄 Report Generation

Automatically generates:

### Phishing Analysis Report

Contains:

- Executive Summary
- Risk Score
- Indicators
- Detailed Findings
- Recommendations
- Email Content
- Technical Notes

---

# 🏗️ System Architecture

```text
Email Input
      │
      ▼
Content Analysis
 ├─ Urgency Detection
 ├─ Generic Greetings
 └─ Grammar Analysis
      │
      ▼
URL Analysis
 ├─ Suspicious URLs
 ├─ Fake Domains
 └─ Blacklist Check
      │
      ▼
Header Analysis
 ├─ SPF Verification
 ├─ DKIM Verification
 ├─ DMARC Verification
 └─ Spoofing Detection
      │
      ▼
Attachment Analysis
      │
      ▼
Risk Classification Engine
      │
      ▼
Report Generator
      │
      ▼
Safe / Suspicious / Phishing
```

---

# 📊 Risk Scoring Model

| Indicator | Score |
|------------|---------|
| Urgency Keywords | +1 |
| Suspicious URL | +2 |
| Generic Greeting | +1 |
| Fake Domain | +2 |
| Blacklisted Domain | +3 |
| Header Authentication Issues | +2 |
| Sender Spoofing | +3 |
| Grammar Issues | +1 |
| Suspicious Attachment | +2 |

## Risk Classification

| Score | Classification |
|---------|---------------|
| 0 – 3 | Safe |
| 4 – 7 | Suspicious |
| 8+ | Phishing |

---

# 📂 Project Structure

```text
phishing-email-security-analyzer/
│
├── app.py
├── phishing_detector.py
│
├── text_analyzer.py
├── link_checker.py
├── email_header_analyzer.py
├── attachment_analyzer.py
├── risk_classifier.py
├── report_generator.py
│
├── blacklist.txt
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 💻 Technologies Used

## Backend

- Python 3
- Flask

## Security Techniques

- SPF Analysis
- DKIM Analysis
- DMARC Analysis
- Sender Spoofing Detection
- URL Inspection
- Domain Validation

## Frontend

- HTML5
- CSS3
- JavaScript

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/phishing-email-security-analyzer.git

cd phishing-email-security-analyzer
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

## Open Browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Sample Analysis

## Input Email

```text
From: support@paypal.com
Return-Path: account-security@paypal-security.com

Subject: Urgent Account Verification

Dear Customer,

Your account has been temporary blocked.

Please verifiy immediately:

http://paypal.secure-login.verify-account.com/login
```

## Output

```text
Risk Level: PHISHING

Indicators:
✔ SPF Fail
✔ DKIM Fail
✔ DMARC Fail
✔ Sender Spoofing
✔ Fake Domain
✔ Suspicious URL
✔ Grammar Error
✔ Urgency Language

Risk Score: 11
```

---

# 📸 Screenshots

Create a screenshots folder:

```text
screenshots/
│
├── home_page.png
├── safe_email.png
├── suspicious_email.png
├── phishing_email.png
├── report_generation.png
└── github_repository.png
```

Example:

```markdown
![Home Page](screenshots/home_page.png)

![Phishing Detection](screenshots/phishing_email.png)

![Generated Report](screenshots/report_generation.png)
```

---

# 🔐 Security Benefits

- Detects common phishing techniques.
- Provides email authentication verification.
- Highlights spoofed sender information.
- Improves phishing awareness.
- Generates investigation-ready reports.

---

# 🚀 Future Enhancements

- Machine Learning-Based Detection
- VirusTotal Integration
- URL Reputation Services
- Gmail Plugin
- Outlook Add-in
- QR Code Phishing Detection
- Threat Intelligence Feeds
- Email Reputation Scoring

---

# 🎓 Academic Relevance

This project demonstrates:

- Cybersecurity Concepts
- Email Security
- Secure Software Development
- Python Programming
- Flask Web Development
- Risk Assessment Techniques
- Digital Forensics Principles

---

# 👨‍💻 Author

**Nidhish Kumaran M.A**

B.Sc Computer Science with Cyber Security  
Dr. N.G.P Arts and Science College

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Project Highlights

✅ SPF, DKIM & DMARC Authentication Analysis

✅ Sender Spoofing Detection

✅ Grammar & Spelling Inspection

✅ Attachment Risk Analysis

✅ URL & Domain Reputation Checks

✅ Automated Security Reports

✅ Risk Scoring Engine

✅ Flask-Based Web Interface

✅ Cybersecurity-Oriented Mini Project

---

**Made with ❤️ for Cybersecurity Awareness and Email Protection**
