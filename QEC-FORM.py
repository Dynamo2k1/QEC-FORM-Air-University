#!/usr/bin/env python3
"""
QEC Auto-Filler for Air University
Standalone binary — no Python or driver installation needed.
On first run, automatically downloads the correct ChromeDriver (~6MB).
"""

import sys
import os
import time
import getpass
import platform

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def banner():
    print("=" * 58)
    print("    QEC Auto-Filler  —  Air University Student Portal")
    print("=" * 58)
    print()

def strip_non_bmp(text):
    return "".join(c for c in text if ord(c) <= 0xFFFF)

def prompt_credentials():
    clear()
    banner()
    print("  Enter your QEC portal credentials.")
    print("  Your password is NEVER saved — used only this session.\n")
    reg_id   = input("  AU Registration ID : ").strip()
    password = getpass.getpass("  Password           : ")
    return reg_id, password

# ── Selenium setup ────────────────────────────────────────────────────────────
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException,
    NoAlertPresentException, WebDriverException
)

def get_chrome_options():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--log-level=3")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-infobars")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    return opts

def start_driver():
    """
    Start Chrome. Selenium 4 selenium-manager auto-downloads
    the correct ChromeDriver on first run (~6MB, cached afterwards).
    """
    opts = get_chrome_options()
    try:
        return webdriver.Chrome(options=opts)
    except WebDriverException as e:
        print(f"\n  ERROR: {e}")
        print("\n  Make sure Google Chrome is installed:")
        print("  Windows : https://www.google.com/chrome/")
        print("  Linux   : sudo apt install google-chrome-stable")
        print("            OR: sudo apt install chromium-browser")
        input("\n  Press Enter to exit...")
        sys.exit(1)

# ── Login ─────────────────────────────────────────────────────────────────────
def login(driver, wait, reg_id, password):
    print("\n  Opening QEC portal...")
    driver.get("https://portals.au.edu.pk/qec/login.aspx")
    Select(wait.until(EC.presence_of_element_located(
        (By.ID, "ctl00_ContentPlaceHolder2_ddlcampus")
    ))).select_by_value("Islamabad")
    Select(driver.find_element(
        By.ID, "ctl00_ContentPlaceHolder2_ddlUserType"
    )).select_by_visible_text("Student/Alumni")
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_txt_regid").send_keys(reg_id)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_txt_password").send_keys(password)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_btnAccountlogin").click()
    time.sleep(2)
    for sel in [".error", ".alert-danger", "#lblError",
                "#ctl00_ContentPlaceHolder2_lblError"]:
        try:
            el = driver.find_element(By.CSS_SELECTOR, sel)
            msg = el.text.strip()
            if msg:
                print(f"\n  Login failed: {msg}")
                return False
        except Exception:
            pass
    print("  Logged in successfully!")
    return True

# ── Form automation ───────────────────────────────────────────────────────────
def click_all_A_radios(driver):
    for radio in driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][value='A']"):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio)
            radio.click()
        except ElementClickInterceptedException:
            driver.execute_script("window.scrollBy(0,-100);")
            radio.click()
        except Exception:
            pass

def handle_alert(driver):
    try:
        alert = WebDriverWait(driver, 4).until(EC.alert_is_present())
        print(f"     >> {alert.text.strip()}")
        alert.accept()
    except (TimeoutException, NoAlertPresentException):
        pass

def process_proforma(driver, wait, label, comment_text="No comments."):
    count = 0
    while True:
        try:
            selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))
        except TimeoutException:
            break
        target = None
        for sel in selects:
            try:
                opts = Select(sel).options
                if len(opts) > 1 and (opts[1].get_attribute("value") or "").strip():
                    target = sel
                    break
            except Exception:
                continue
        if not target:
            break
        Select(target).select_by_index(1)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio']")))
        except TimeoutException:
            break
        click_all_A_radios(driver)
        tas = driver.find_elements(By.TAG_NAME, "textarea")
        comments = [comment_text] if isinstance(comment_text, str) else comment_text
        for idx, ta in enumerate(tas):
            raw = comments[idx] if idx < len(comments) else comments[-1]
            safe = strip_non_bmp(raw)
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ta)
                ta.clear()
                ta.send_keys(safe)
            except Exception:
                pass
        try:
            submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit)
            submit.click()
        except Exception:
            break
        handle_alert(driver)
        count += 1
        print(f"     Entry #{count} submitted.")
        time.sleep(0.5)
    status = f"{count} entries" if count else "nothing to fill (already submitted?)"
    print(f"  Done: {label} ({status})")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    reg_id, password = prompt_credentials()

    print("\n  Starting browser...")
    print("  (First run may take ~10 seconds to download ChromeDriver)")
    driver = start_driver()
    wait   = WebDriverWait(driver, 20)

    try:
        if not login(driver, wait, reg_id, password):
            driver.quit()
            input("\n  Press Enter to exit...")
            sys.exit(1)

        print("\n  Filling QEC forms...\n")

        print("  [1/3] Student Course Evaluation")
        driver.get("https://portals.au.edu.pk/qec/p1.aspx")
        process_proforma(driver, wait, "Course Evaluation", "Great course overall!")

        print("\n  [2/3] Teacher Evaluation")
        driver.get("https://portals.au.edu.pk/qec/p10.aspx")
        process_proforma(driver, wait, "Teacher Evaluation",
                         ["Good.", "Excellent teaching!"])

        print("\n  [3/3] Online Learning Feedback")
        driver.get("https://portals.au.edu.pk/qec/p10a_learning_online_form.aspx")
        process_proforma(driver, wait, "Online Learning Feedback",
                         "Smooth online experience!")

        print("\n" + "=" * 58)
        print("  All QEC forms filled successfully!")
        print("=" * 58)

    except KeyboardInterrupt:
        print("\n\n  Interrupted.")
    except Exception as e:
        print(f"\n  Unexpected error: {e}")
    finally:
        driver.quit()

    input("\n  Press Enter to exit...")

if __name__ == "__main__":
    main()
