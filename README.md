# 🛡️ Phishing Detection Tool

A comprehensive, professional-grade phishing detection system that analyzes emails for suspicious indicators and provides risk assessment with detailed security recommendations.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Risk Scoring System](#risk-scoring-system)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

The **Phishing Detection Tool** is a security application designed to help users identify and protect themselves from phishing emails. It uses rule-based analysis and pattern matching to detect common phishing indicators, providing users with:

- **Risk Assessment**: Immediate classification of email threats
- **Detailed Analysis**: Specific indicators that triggered the detection
- **Security Tips**: Actionable advice based on the risk level
- **Professional Interface**: Easy-to-use web application

### 🚀 4-Stage Development Approach

This project was built progressively through 4 stages:

1. **Stage 1: Foundation** - Rule-based CLI tool with basic detection
2. **Stage 2: Structured Analysis** - Modular design with scoring system
3. **Stage 3: User Interface** - Professional web app with Flask
4. **Stage 4: Advanced Features** - Blacklist system and enhanced detection

---

## ✨ Features

### Core Detection Features
- ✅ **Urgency Keywords Detection** - Identifies pressure-inducing language
- ✅ **Suspicious Links Analysis** - Detects HTTP (unencrypted) and unusual URLs
- ✅ **Generic Greeting Detection** - Finds impersonal email openings
- ✅ **Fake Domain Detection** - Identifies non-legitimate domain names
- ✅ **Blacklist System** - Checks against known phishing domains
- ✅ **Risk Scoring** - Comprehensive scoring system (0-9 scale)

### User Interface
- 🎨 **Interactive Web Interface** - Beautiful gradient background with smooth animations
- 📱 **Responsive Design** - Works on desktop and tablet devices
- 🎭 **Animated Elevations** - Smooth transitions and hover effects
- 💡 **Real-time Analysis** - Instant results with detailed breakdown
- 🎯 **Color-Coded Results** - Green (Safe), Yellow (Suspicious), Red (Phishing)

### Additional Features
- 📊 **Detailed Indicators** - Shows which indicators were triggered
- 💾 **History Preservation** - Email text remains in textarea for review
- 🔒 **Local Processing** - All analysis done locally (no data sent externally)
- ⚡ **Fast Performance** - Instant analysis results

---

## 📁 Project Structure

```
phishing-tool-analyzer/
│
├── app.py                          # Flask web application
├── phishing_detector.py             # CLI version of the detector
│
├── text_analyzer.py                # Analyzes email text for urgency & greetings
├── link_checker.py                 # Checks URLs and blacklisted domains
├── risk_classifier.py              # Calculates risk level and scoring
│
├── blacklist.txt                   # Database of known phishing domains
│
├── templates/
│   └── index.html                  # Web interface (HTML + CSS + animations)
│
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install Flask:

```bash
pip install flask
```

### Step 3: Run the Application

**Option A: Web Interface (Recommended)**
```bash
python app.py
```
Then open your browser and go to: `http://127.0.0.1:5000`

**Option B: Command Line Interface**
```bash
python phishing_detector.py
```

---

## 📖 Usage

### Web Interface

1. **Open the Tool**
   - Run `python app.py`
   - Navigate to `http://127.0.0.1:5000` in your browser

2. **Analyze an Email**
   - Copy the suspicious email text
   - Paste it into the textarea
   - Click "🔍 Analyze Email"

3. **Review Results**
   - Check the Risk Level
   - Review Indicators Found
   - Read the Details section
   - Follow the Safety Tips

### CLI Interface

1. **Run the Tool**
   ```bash
   python phishing_detector.py
   ```

2. **Paste Email Text**
   - Paste your email content
   - Press Enter twice to finish

3. **View Results**
   - Risk Level (Safe/Suspicious/Phishing)
   - Risk Score (0-9+)
   - Indicators Found
   - Detailed Reasons

---

## 🧠 How It Works

### Detection Flow

```
Email Input
    ↓
Text Analysis (Urgency Keywords & Greetings)
    ↓
Link Analysis (Suspicious URLs & Domains)
    ↓
Blacklist Check (Known Phishing Domains)
    ↓
Risk Classification (Scoring Algorithm)
    ↓
Results Display (Risk Level + Details + Tips)
```

### Detection Indicators

| Indicator | Points | Example |
|-----------|--------|---------|
| Urgency Keywords | +1 | "urgent", "immediate", "act now" |
| Suspicious Links | +2 | http://, weird domains |
| Generic Greeting | +1 | "Dear user", "Hello customer" |
| Fake Domain | +2 | Domain not in whitelist |
| Blacklisted Domain | +3 | Domain in blacklist.txt |

---

## 📊 Risk Scoring System

### Scoring Breakdown

**Maximum Score: 9 points**

### Risk Levels

| Level | Score Range | Classification | Color | Recommendation |
|-------|------------|-----------------|-------|----------------|
| 🟢 **Safe** | 0-2 | Legitimate Email | Green | ✓ Safe to open |
| 🟡 **Suspicious** | 3-6 | Potential Threat | Yellow | ⚠️ Be cautious |
| 🔴 **Phishing** | 7-9+ | High Risk Threat | Red | ✗ Do not interact |

### Examples

**Score 0-2 (SAFE)**
```
Email with no suspicious indicators
→ Safe to read and interact with
```

**Score 4 (SUSPICIOUS)**
```
Suspicious URL (+2) + Fake Domain (+2) = 4
→ Be cautious, verify sender identity
```

**Score 9 (PHISHING)**
```
Urgency (+1) + Suspicious URL (+2) + Generic Greeting (+1) + 
Fake Domain (+2) + Blacklisted Domain (+3) = 9
→ Do not click links, delete immediately
```

---

## 📸 Screenshots

### 1. Home Interface
```
[Screenshot showing the main interface with:
- Title: "🛡️ Phishing Detection Tool"
- Email textarea with placeholder text
- "🔍 Analyze Email" button
- Purple-blue gradient background]
```

### 2. Safe Email Result
```
[Screenshot showing:
- Green result card
- Risk Level: Safe
- Risk Score: 1
- Indicators: All showing ❌ No
- Safety Tips displayed]
```

### 3. Suspicious Email Result
```
[Screenshot showing:
- Yellow result card with pulse animation
- Risk Level: Suspicious
- Risk Score: 4
- Details: Suspicious links and fake domains
- Safety Tips: Be cautious with links
- Hover effects on list items]
```

### 4. Phishing Email Result
```
[Screenshot showing:
- Red result card with pulse animation
- Risk Level: Phishing
- Risk Score: 9
- All indicators showing ✅ Yes
- Details: All phishing indicators found
- Safety Tips: Do not click links
- Strong visual warning]
```

### 5. Animated Transitions
```
[Screenshots showing:
- Container floating animation
- Button hover elevation with shimmer
- Result card slide-in animation
- Text fields focus states with glow effects]
```

---

## 💻 Technologies Used

### Backend
- **Python 3.8+** - Core programming language
- **Flask** - Web framework for UI
- **Regular Expressions (Regex)** - Pattern matching for URLs and text

### Frontend
- **HTML5** - Structure and markup
- **CSS3** - Styling with gradients and animations
- **JavaScript** - Embedded in HTML for interactivity

### Architecture
- **Modular Design** - Separated concerns for maintainability
  - `text_analyzer.py` - Text analysis module
  - `link_checker.py` - URL and domain verification
  - `risk_classifier.py` - Risk calculation engine

---

## 🚀 Future Enhancements

### Phase 1: Data & Analytics
- [ ] Add email header analysis
- [ ] SPF/DKIM/DMARC verification
- [ ] Attachment scanning

### Phase 2: Machine Learning
- [ ] Train on public phishing datasets
- [ ] Implement Naive Bayes classifier
- [ ] Add logistic regression model
- [ ] Improve accuracy with ML models

### Phase 3: Integration
- [ ] Email client plugin (Gmail, Outlook)
- [ ] API endpoint for integration
- [ ] Batch email scanning
- [ ] Export reports

### Phase 4: Advanced Features
- [ ] Sender reputation scoring
- [ ] Image-based phishing detection
- [ ] Homograph attack detection
- [ ] Browser extension version

---

## 📝 File Descriptions

### Core Files

**app.py**
- Flask web application entry point
- Handles HTTP requests and responses
- Integrates all detection modules

**phishing_detector.py**
- CLI version of the detector
- Standalone usage without web interface
- Good for batch processing

**text_analyzer.py**
- Detects urgency keywords
- Identifies generic greetings
- Returns boolean and list results

**link_checker.py**
- Extracts URLs from email
- Checks against whitelist
- Verifies domain legitimacy
- Blacklist comparison

**risk_classifier.py**
- Calculates risk scores
- Determines risk level
- Generates indicator dictionary
- Returns comprehensive results

**blacklist.txt**
- Line-separated list of malicious domains
- Easily updatable
- Currently includes common phishing domains

**templates/index.html**
- Professional web interface
- Responsive design
- Smooth CSS animations
- Color-coded results display

---

## 🔐 Security Notes

- ✅ **No Data Transmission** - All analysis happens locally
- ✅ **No Logs** - Emails are not stored or logged
- ✅ **Open Source** - Code is transparent and auditable
- ⚠️ **Rule-Based** - May have false positives/negatives
- 💡 **Use as Aid** - Complement with email provider tools

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Improvement Ideas
- Add more phishing keywords
- Expand domain whitelist
- Improve regex patterns
- Add unit tests
- Optimize performance

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [your-profile](https://linkedin.com/in/yourprofile)

---

## 📞 Support

### Issues or Questions?

1. Check existing issues on GitHub
2. Create a new issue with detailed information
3. Include screenshots if applicable
4. Describe steps to reproduce bugs

### Getting Help

- 📖 Read the documentation above
- 🔍 Check the code comments
- 💬 Open a GitHub discussion
- 📧 Contact the author

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Python backend development
- ✅ Web framework usage (Flask)
- ✅ Regular expressions for pattern matching
- ✅ Risk assessment algorithms
- ✅ Responsive UI design
- ✅ CSS animations and transitions
- ✅ Modular code architecture
- ✅ Security best practices

---

## 📊 Project Stats

- **Lines of Code**: ~500+
- **Modules**: 5
- **Indicators Detected**: 5 different types
- **Risk Levels**: 3 (Safe, Suspicious, Phishing)
- **Animations**: 10+
- **Development Time**: Staged approach (4 phases)

---

## 🙏 Acknowledgments

- Flask documentation and community
- OWASP for phishing indicators reference
- CSS animation inspiration from modern web practices

---

## 📅 Version History

### v1.0.0 (Current)
- Initial release with all 4 stages complete
- Web interface with animations
- CLI version available
- Blacklist system implemented
- Risk scoring system (0-9)
- 5 detection indicators

---

## 🎯 Quick Start Commands

```bash
# Clone the repository
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer

# Install dependencies
pip install flask

# Run the web app
python app.py

# Open browser
# Navigate to http://127.0.0.1:5000

# Or run CLI version
python phishing_detector.py
```

---

**Made with ❤️ for a safer internet**

Last Updated: April 29, 2026