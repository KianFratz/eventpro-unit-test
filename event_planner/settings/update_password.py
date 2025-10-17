from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def update_password(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/settings")
        
        # current password
        curr_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your current password']")))
        curr_password.click()
        print("✅ Input box clicked, successfully")
        curr_password.send_keys("123123")
        print("✅ Current Password send successfully")
        
        
        # new password
        new_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter new password']")))
        new_password.click()
        print("✅ Input box clicked, successfully")
        new_password.send_keys("123123123")
        print("✅ New Password send successfully")
        
        
        # confirm new password
        confirm_new_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Confirm new password']")))
        confirm_new_password.click()
        print("✅ Input box clicked, successfully")
        confirm_new_password.send_keys("123123123")
        print("✅ Confirm New Password send successfully")
        
        
        # click update password button
        update_password_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update Security Settings']")))
        update_password_btn.click()
        print("✅ Update Security Settings, clicked successfully.")
        time.sleep(3)
        print("✅ Changing password, successful.")
        
    except TimeoutException as e:
        print(f"Error during updating password: {e}")
        raise