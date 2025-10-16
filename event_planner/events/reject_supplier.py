from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def reject_supplier(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        
        # click manage event button
        manage_event_link  = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Manage Event']"))
        )
        manage_event_link .click()
        print("✅ Manage event link clicked successfully")
        
        
        # click reject button
        reject_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reject')]"))
        )
        reject_btn.click()
        print("✅ Reject button clicked successfully")
        
        
        # textarea
        textarea = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Explain why this submission is being rejected...']"))
        )
        textarea.click()
        print("✅ Textarea click successfully")
        textarea.send_keys("Not eligible")
        print("✅ Message reason send successfully")
        
        
        # click submit  button
        btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Submit']]"))
        )
        btn.click()
        print("✅ Submit button click successfully")
        print("✅ Successfully reject Supplier.")
        
    except Exception as e:
        print(f"Error during rejecting supplier: {e}")
        raise