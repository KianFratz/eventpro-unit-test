from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def change_email(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://unite-eventpro.netlify.app/settings")
        
        # CLICK edit button
        edit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Change']")))
        edit_btn.click()
        print("✅ Change email button clicked successfully.")
        
        
        # CLICK input box
        password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your password']")))
        password.click()
        print("✅ Input box click, successfully")
        password.clear()
        password.send_keys("123123")
        print("✅ Password send successfully")
        
        
        # verify password button
        verify_password_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Verify Password']")))
        verify_password_btn.click()
        print("✅ Verify Password button, clicked successfully.")
        
        
        # CLICK input box for new email address
        new_email = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter new email address']")))
        new_email.click()
        print("✅ Input box click, successfully")
        new_email.send_keys("maria@gmail.com")
        print("✅ New email send successfully")
        
        
        # click change email button
        change_email_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Change email']")))
        change_email_btn.click()
        print("✅ Change email button, clicked successfully.")
        time.sleep(3)
        print("✅ Changing email, successful.")
        
    except TimeoutException as e:
        print(f"Error during changing email: {e}")
        raise