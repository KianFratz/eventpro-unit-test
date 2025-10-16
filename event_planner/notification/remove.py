from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def remove(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/notification")
        print("✅ Successfully navigated to Notification page.")
        
        
        # click remove  button
        remove_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'hover:text-red-600') and contains(@class,'hover:bg-red-50') and contains(@class,'rounded-lg')]"))
        )
        remove_btn.click()
        print("✅ Remove button click successfully")
        print("✅ Successfully remove notification.")
        
    except Exception as e:
        print(f"Error during removing notification: {e}")
        raise