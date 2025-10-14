from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def edit_contact_number(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/settings")
        
        # CLICK edit button
        edit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Edit Contact Number']")))
        edit_btn.click()
        print("✅ Edit button clicked successfully.")
        
        # CLICK input box
        input_box = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.w-full.bg-transparent.text-lg.font-small.text-gray-800")))
        input_box.click()
        print("✅ Input box click, successful.")
        input_box.clear()
        input_box.send_keys("09270000000")
        print("✅ New Contact Number send successfully")
        
        
        # save button
        save_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save Contact Number')]")))
        save_btn.click()
        print("✅ Clicking save button, successful.")
        print("✅ Updating Contact Number successful")
        
        
    except TimeoutException as e:
        print(f"Error during editing contact number: {e}")
        raise