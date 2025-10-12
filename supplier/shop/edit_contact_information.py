from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def edit_contact_information(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Start at the registration page
        driver.get("http://localhost:5173/shop")
        
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Edit Contact')]]"))
        )
        edit_button.click()
        
        # wait for the input to appear
        phone_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='e.g 0961234567']"))
        )
        phone_input.clear()
        phone_input.send_keys("09210000001")
        print("✅ New phone number send")
        
        save_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-green-500"))
        )
        save_button.click()
        print("✅ Contact Information updated successfully")
        
    except Exception as e:
        print(f"Error during editing contact: {e}")
        raise