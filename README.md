# 📝 QEC Auto-Filler Script for Air University

A powerful and simple automation script to fill out **QEC Proformas** (Student Course Evaluation, Teacher Evaluation, and Online Learning Feedback) at [Air University’s QEC portal](https://portals.au.edu.pk/qec/login.aspx) using **Python** and **Selenium**.

✅ Auto-fills all radio buttons
🧠 Smart form detection
💬 Adds custom comments automatically
🔐 Safe login via CLI (your password isn’t stored)
✨ With fun emoji feedback for each stage

---

## 🔧 Requirements

* Python **3.7+**
* Google Chrome browser (or Firefox)
* ChromeDriver (compatible with your Chrome version)
* pip packages:

  * `selenium`

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/QEC-FORM-Air-University.git
   cd QEC-FORM-Air-University
   ```

2. **Install dependencies**

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**

   * Visit: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   * Extract and place it in your system PATH or the project folder.

---

## 🚀 Usage

Run the script using:

```bash
python QEC-FORM.py
```

You'll be prompted to enter:

* 🎓 Campus name (e.g. `Islamabad`)
* 👤 Login type (`Student/Alumni` or `Teacher`)
* 🆔 AU Registration ID (only the digits, e.g. `231309`)
* 🔒 Password (typed securely)

---

## 🤖 What It Does

Once logged in, the script will automatically:

1. Go to **Student Course Evaluation**
2. Select each course
3. Mark all answers as **A** (Strongly Agree)
4. Fill in course comments (`Great course! 👍`)
5. Submit and move to the next

Then it does the same for:

* 👩‍🏫 **Teacher Evaluation** (comment: `Excellent teaching! 👩‍🏫`)
* 💻 **Online Learning Feedback** (comment: `Smooth online experience! 💻`)

Each step is confirmed with emoji output like:

```
🔔 Alert: CS325 has been saved successfully.
✅ Course evaluations done 🎉
```

---

## 🛠️ Troubleshooting

* Make sure your ChromeDriver matches your installed version of Chrome.
* If you're using Firefox, change:

  ```python
  driver = webdriver.Chrome()
  ```

  to:

  ```python
  driver = webdriver.Firefox()
  ```
* Slow internet? Increase `WebDriverWait` timeouts (default is 20 seconds).
* Script not clicking? It's designed to scroll and retry—let it run and don’t move your mouse over the browser.

---

## 🔐 Security Note

Your credentials are **not saved** anywhere. Everything is processed in real-time within the script.

---

## 📄 License

This project is licensed under the MIT License.
Not affiliated with Air University or QEC.

---

## 🙌 Credits

Developed with ❤️ by Dynamo2k1

Tested at [https://portals.au.edu.pk/qec](https://portals.au.edu.pk/qec)

