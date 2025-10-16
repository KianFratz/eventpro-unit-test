from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def apply_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/favorites")
        print("✅ Successfully navigated to Events page.")
        
        # click remove favorites button
        apply_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
        )
        apply_btn.click()
        print("✅ Apply button click, successfully")
        print("✅ Applying Event, successful")
        
        
    except Exception as e:
        print(f"Error during applying event: {e}")
        raise