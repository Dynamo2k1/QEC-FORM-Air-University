<div align="center">

# 🎓 QEC Auto-Filler — Air University

**Automatically fills all QEC evaluation forms on the Air University portal.**
No Python. No setup. Just run and done.

[![Release](https://img.shields.io/github/v/release/Dynamo2k1/QEC-FORM-Air-University?style=flat-square&color=brightgreen)](https://github.com/Dynamo2k1/QEC-FORM-Air-University/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey?style=flat-square)](#download)

</div>

---

## ⚡ Download & Run (No Install Needed)

> Go to [**Releases**](https://github.com/Dynamo2k1/QEC-FORM-Air-University/releases/latest) and download the file for your OS.

| OS | File to Download | How to Run |
|---|---|---|
| 🪟 Windows | `QEC-AutoFiller-Windows.exe` | Double-click it |
| 🐧 Linux | `QEC-AutoFiller-Linux` | `chmod +x QEC-AutoFiller-Linux && ./QEC-AutoFiller-Linux` |

**The only requirement:** Google Chrome (or Chromium) must be installed on your machine.

- Windows: [Download Chrome](https://www.google.com/chrome/)
- Linux: `sudo apt install google-chrome-stable` or `sudo apt install chromium-browser`

> **First run note:** On first launch, the tool auto-downloads the correct ChromeDriver (~6 MB) and caches it. After that it starts instantly.

---

## 🤖 What It Does

After you enter your AU Registration ID and Password, it automatically:

1. **Logs in** to the QEC portal
2. **Student Course Evaluation** — selects every course, marks all answers **A (Strongly Agree)**, fills comments, submits
3. **Teacher Evaluation** — same for all teachers
4. **Online Learning Feedback** — fills and submits

All running **headless** (no browser window pops up). Your credentials are **never saved**.

```
==========================================================
    QEC Auto-Filler  —  Air University Student Portal
==========================================================

  Enter your QEC portal credentials.
  Your password is NEVER saved — used only this session.

  AU Registration ID : 123456
  Password           :

  Opening QEC portal...
  Logged in successfully!

  Filling QEC forms...

  [1/3] Student Course Evaluation
     Entry #1 submitted.
     Entry #2 submitted.
  Done: Course Evaluation (2 entries)

  [2/3] Teacher Evaluation
     Entry #1 submitted.
  Done: Teacher Evaluation (1 entries)

  [3/3] Online Learning Feedback
     Entry #1 submitted.
  Done: Online Learning Feedback (1 entries)

==========================================================
  All QEC forms filled successfully!
==========================================================
```

---

## ✏️ Customize Comments

Before building, open `QEC-FORM.py` and find `main()` near the bottom:

```python
# Change these to whatever comments you want
process_proforma(driver, wait, "Course Evaluation",
                 "Great course overall!")

process_proforma(driver, wait, "Teacher Evaluation",
                 ["Good.", "Excellent teaching!"])

process_proforma(driver, wait, "Online Learning Feedback",
                 "Smooth online experience!")
```

---

## 🔨 Build It Yourself

Want to compile from source? All build scripts are included.

### 🪟 Windows

**Requirements:** Python 3 · Google Chrome

```bat
# 1. Clone the repo
git clone https://github.com/Dynamo2k1/QEC-FORM-Air-University.git
cd QEC-FORM-Air-University

# 2. Run the build script (installs everything automatically)
build_windows.bat

# 3. Your EXE is at:
dist\QEC-AutoFiller-Windows.exe
```

### 🐧 Linux

**Requirements:** Python 3 · Chrome or Chromium

```bash
# 1. Clone the repo
git clone https://github.com/Dynamo2k1/QEC-FORM-Air-University.git
cd QEC-FORM-Air-University

# 2. Run the build script
chmod +x build_linux.sh
./build_linux.sh

# 3. Your binary is at:
dist/QEC-AutoFiller-Linux
```

---

## 📁 Repository Structure

```
QEC-FORM-Air-University/
├── QEC-FORM.py            ← Main script (edit this to customize comments)
├── build_windows.bat      ← Auto-builds Windows EXE
├── build_linux.sh         ← Auto-builds Linux binary
├── CHANGELOG.md           ← Version history
└── README.md              ← This file
```

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `Could not start Chrome` | Install Chrome or Chromium (see above) |
| Login failed | Check Registration ID (digits only) and password |
| Forms say already submitted | Those forms are already done — nothing to fill |
| Slow internet / timeout | Edit script: change `WebDriverWait(driver, 20)` → `40` |
| Linux: Permission denied | Run `chmod +x QEC-AutoFiller-Linux` first |
| Windows Defender warning | Click "More info" → "Run anyway" (false positive for unsigned EXE) |

---

## 🔐 Security & Privacy

- Credentials are **never stored** anywhere — only held in memory during the session
- All network traffic goes only to `portals.au.edu.pk`
- Source code is fully open — audit it yourself

---

## 📄 License

MIT License — Not affiliated with Air University or QEC.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Dynamo2k1">Dynamo2k1</a>
</div>
