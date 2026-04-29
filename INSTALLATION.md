# 📦 Installation Guide

Complete step-by-step installation instructions for the Phishing Detection Tool.

---

## Prerequisites

Before installing, make sure you have:
- **Python 3.8** or higher
- **pip** (comes with Python)
- **Git** (for cloning the repository)
- ~50 MB disk space

### Check Python Version

```bash
python --version
```

Should show: `Python 3.8.0` or higher

### Check pip Installation

```bash
pip --version
```

Should show: `pip X.X.X`

---

## Windows Installation

### Step 1: Download Python (if needed)

1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.10 or higher
3. Run the installer
4. ✅ **Important**: Check "Add Python to PATH"
5. Click "Install Now"

### Step 2: Clone/Download Repository

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer
```

**Option B: Download ZIP**
1. Go to GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open command prompt in the extracted folder

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.3
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Navigate to: **http://localhost:5000** or **http://127.0.0.1:5000**

---

## macOS Installation

### Step 1: Install Python (if needed)

Using Homebrew:
```bash
brew install python3
```

Or download from [python.org](https://www.python.org/downloads/)

### Step 2: Clone Repository

```bash
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer
```

### Step 3: Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python3 app.py
```

### Step 6: Open Browser

Navigate to: **http://localhost:5000**

---

## Linux Installation

### Step 1: Install Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

### Step 2: Clone Repository

```bash
git clone https://github.com/yourusername/phishing-tool-analyzer.git
cd phishing-tool-analyzer
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python3 app.py
```

### Step 6: Access Application

Open browser to: **http://localhost:5000**

---

## Virtual Environment Setup (Recommended)

### Why Use Virtual Environments?

Virtual environments keep project dependencies isolated and prevent conflicts.

### Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies in Virtual Environment

```bash
pip install -r requirements.txt
```

### Deactivate Virtual Environment

```bash
deactivate
```

---

## Troubleshooting

### Problem: "python command not found"

**Solution:**
- Python may not be in PATH
- Try `python3` instead of `python`
- Reinstall Python and check "Add to PATH"

### Problem: "pip command not found"

**Solution:**
```bash
python -m pip install -r requirements.txt
```

### Problem: "No module named flask"

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: "Port 5000 already in use"

**Solution:**
```bash
python -c "from app import app; app.run(port=5001)"
```

Then access: **http://localhost:5001**

### Problem: "Permission denied" on macOS/Linux

**Solution:**
```bash
sudo chmod +x app.py
python3 app.py
```

### Problem: Module import errors

**Solution:**
```bash
# Reinstall all requirements
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## Verify Installation

### Test 1: Check Python

```bash
python --version
```

### Test 2: Check Flask

```bash
python -c "import flask; print(flask.__version__)"
```

Should show: `3.0.3` or similar

### Test 3: Run Application

```bash
python app.py
```

Should show:
```
 * Running on http://127.0.0.1:5000
```

### Test 4: Test in Browser

1. Open **http://127.0.0.1:5000**
2. You should see the Phishing Detection Tool interface
3. Try pasting test email text
4. Click "Analyze Email"

---

## Using CLI Version

If you prefer command-line interface:

```bash
python phishing_detector.py
```

Then paste email text and press Enter twice.

---

## Advanced Setup

### Using Different Port

```bash
# Windows
set FLASK_ENV=development & python app.py

# macOS/Linux
export FLASK_ENV=development && python3 app.py
```

### Run on Network

To access from other machines on network:

```python
# Edit app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Then access from: **http://your-machine-ip:5000**

---

## Next Steps

1. ✅ **Installation complete!**
2. 📖 Read [README.md](README.md) for full documentation
3. 🚀 Check [QUICKSTART.md](QUICKSTART.md) for usage guide
4. 🧪 Test with sample emails
5. 🌐 Upload to GitHub
6. 💡 Consider contributions/improvements

---

## Still Having Issues?

1. Check Python version: `python --version`
2. Check pip version: `pip --version`
3. Verify file locations: `ls -la` (or `dir` on Windows)
4. Check Flask: `pip show flask`
5. Read error message carefully
6. Open GitHub issue with full error message

---

**Troubleshooting Checklist:**
- [ ] Python 3.8+ installed
- [ ] pip working correctly
- [ ] All files downloaded
- [ ] requirements.txt installed
- [ ] No port conflicts
- [ ] Browser can access localhost

---

**Installation Complete! 🎉**

Now proceed to usage in [QUICKSTART.md](QUICKSTART.md)