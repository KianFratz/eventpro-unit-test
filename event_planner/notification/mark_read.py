from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def mark_read(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/notification")
        print("✅ Successfully navigated to Notification page.")
        
        
        # click mark read  button
        mark_read_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Mark All As Read')]"))
        )
        mark_read_btn.click()
        print("✅ Mark read button click successfully")
        print("✅ Successfully mark all notification as read.")
        
    except Exception as e:
        print(f"Error during applying event: {e}")
        raise