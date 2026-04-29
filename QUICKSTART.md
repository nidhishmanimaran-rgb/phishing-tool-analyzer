# 🚀 Quick Start Guide

## Installation (30 seconds)

```bash
# 1. Download/Clone
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer

# 2. Install
pip install -r requirements.txt

# 3. Run
python app.py
```

## Open in Browser

Navigate to: **http://127.0.0.1:5000**

---

## How to Use

### Step 1: Paste Email
Copy a suspicious email and paste it into the text box.

### Step 2: Click Analyze
Click the "🔍 Analyze Email" button.

### Step 3: Review Results
- Check the **Risk Level** (Safe/Suspicious/Phishing)
- Review **Indicators** that were triggered
- Read **Details** for specifics
- Follow **Safety Tips**

---

## What the Scores Mean

| Score | Risk Level | What to Do |
|-------|-----------|-----------|
| 0-2 | 🟢 Safe | ✅ Safe to open |
| 3-6 | 🟡 Suspicious | ⚠️ Be careful |
| 7-9+ | 🔴 Phishing | ❌ Delete it |

---

## Example

**Phishing Email Input:**
```
Dear user,

Your account has been compromised. Urgent action required. 
Click here: http://fakebank.com/login

Act now!
```

**Result:**
```
Risk Level: Phishing (Score 9)

Indicators:
✅ Urgency: Yes
✅ Suspicious URL: Yes  
✅ Generic Greeting: Yes
✅ Fake Domain: Yes
✅ Blacklisted Domain: Yes

Details:
- Urgency keywords: urgent, act now
- Suspicious links: http://fakebank.com/login
- Generic greetings: dear user
- Fake domains: fakebank.com
- Blacklisted domains: fakebank.com

Tips:
✓ Do not click any links or provide personal information
✓ Verify the sender's email address
✓ Contact the organization directly through official channels
```

---

## CLI Version (Alternative)

```bash
python phishing_detector.py
```

Then paste your email text and press Enter twice.

---

## Troubleshooting

**Port already in use?**
```bash
# Use a different port
python -c "from app import app; app.run(port=5001)"
```

**Module not found?**
```bash
pip install -r requirements.txt
```

**Need more help?**
Check `README.md` for detailed documentation.

---

**Happy phishing detecting! 🛡️**