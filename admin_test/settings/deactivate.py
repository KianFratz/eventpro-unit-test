from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def deactivate(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/settings")
        
        # CLICK deactivate button
        deactivate_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.flex.items-center.text-slate-700")))
        deactivate_btn.click()
        print("✅ Deactivate button clicked successfully.")
        
        
        # choose reason for deactivating
        option_text="Too many emails"
        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//label[.//span[normalize-space(text())='{option_text}']]"))
        )
        option.click()
        print("✅ Too many emails reason selected successfully")
        
        # re enter password
        re_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your password']")))
        re_password.click()
        print("✅ Re-enter password input clicked successfully.")
        re_password.send_keys("123123")
        print("✅ Re-enter password input send successfully.")
        
        
        # click terms and conditions
        check_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
        )
        check_box.click()
        print("✅ Terms and Conditions clicked successfully.")
        
        
        # deactivate button
        deactivate_account = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Deactivate Account']"))
        )
        deactivate_account.click()
        print("✅ Deactivate Account button clicked successfully.")
        print("✅ Deactivating Account, successful")
        
    except TimeoutException:
        print(f"Error during deactivating account: {e}")
        raise