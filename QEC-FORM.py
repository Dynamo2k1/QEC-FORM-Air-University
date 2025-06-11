#!/usr/bin/env python3
import time
import getpass
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)

def prompt_credentials():
    campus   = "Islamabad"
    u_type   = "Student/Alumni"
    reg_id   = input("AU Registration ID: ").strip()
    password = getpass.getpass("Password: ")
    return campus, u_type, reg_id, password

def strip_non_bmp(text: str) -> str:
    # remove any character outside the Basic Multilingual Plane (> U+FFFF)
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

def login(driver, wait, campus, u_type, reg_id, password):
    driver.get("https://portals.au.edu.pk/qec/login.aspx")
    Select(wait.until(EC.presence_of_element_located(
        (By.ID, "ctl00_ContentPlaceHolder2_ddlcampus")))) \
      .select_by_value(campus)
    Select(driver.find_element(
        By.ID, "ctl00_ContentPlaceHolder2_ddlUserType")) \
      .select_by_visible_text(u_type)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_txt_regid") \
          .send_keys(reg_id)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_txt_password") \
          .send_keys(password)
    driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_btnAccountlogin") \
          .click()
    time.sleep(2)  # wait for dashboard load

def click_all_A_radios(driver):
    for radio in driver.find_elements(
        By.CSS_SELECTOR, "input[type='radio'][value='A']"):
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", radio)
            radio.click()
        except ElementClickInterceptedException:
            driver.execute_script("window.scrollBy(0, -100);")
            radio.click()

def handle_alert(wait):
    try:
        alert = wait.until(EC.alert_is_present())
        print(f"🔔 Alert: {alert.text}")
        alert.accept()
    except TimeoutException:
        pass

def process_proforma(driver, wait, comment_text="No comments"):
    """
    Generic proforma handler:
      • Find first <select> with >1 real options → select index 1  
      • Wait for any radios → click all [value="A"]  
      • Fill all <textarea> with comment_text (str or list)  
      • Find & click the first input[type='submit']  
      • Handle alert, then loop until no more real options
    """
    while True:
        selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))
        target = None
        for sel in selects:
            opts = Select(sel).options
            if len(opts) > 1 and opts[1].get_attribute("value").strip():
                target = sel
                break
        if not target:
            break

        Select(target).select_by_index(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio']")))

        click_all_A_radios(driver)

        # fill textareas
        tas = driver.find_elements(By.TAG_NAME, "textarea")
        if isinstance(comment_text, list):
            for idx, ta in enumerate(tas):
                raw = comment_text[idx] if idx < len(comment_text) else comment_text[-1]
                safe = strip_non_bmp(raw)
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ta)
                ta.clear()
                ta.send_keys(safe)
        else:
            safe = strip_non_bmp(comment_text)
            for ta in tas:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ta)
                ta.clear()
                ta.send_keys(safe)

        submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit)
        submit.click()

        handle_alert(wait)
        time.sleep(0.5)

def main():
    campus, u_type, reg_id, password = prompt_credentials()

    driver = webdriver.Chrome()
    wait   = WebDriverWait(driver, 20)

    login(driver, wait, campus, u_type, reg_id, password)

    # 1️⃣ Student Course Evaluation
    driver.get("https://portals.au.edu.pk/qec/p1.aspx")
    process_proforma(driver, wait, comment_text="Great course!")
    print("✅ Course evaluations done 🎉")

    # 2️⃣ Teacher Evaluation
    driver.get("https://portals.au.edu.pk/qec/p10.aspx")
    process_proforma(driver, wait, comment_text=[
        "Good.",
        "Excellent teaching!"
    ])
    print("✅ Teacher evaluations done 🎉")

    # 3️⃣ Online Learning Feedback
    driver.get("https://portals.au.edu.pk/qec/p10a_learning_online_form.aspx")
    process_proforma(driver, wait, comment_text="Smooth online experience!")
    print("✅ Online learning feedback done 🎉")

    driver.quit()

if __name__ == "__main__":
    main()
