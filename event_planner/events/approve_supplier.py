from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def approve_supplier(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # click manage event button
        manage_event_link  = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='Manage Event']"))
        )
        manage_event_link[1].click()
        print("✅ Manage event link clicked successfully")
        
        # click approve  button
        approve = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reject')]"))
        )
        approve.click()
        print("✅ Approve button clicked successfully")
        print("✅ Successfully approve Supplier application.")
        
    except Exception as e:
        print(f"Error during approving supplier application: {e}")
        raise