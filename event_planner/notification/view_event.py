from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def view_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/notification")
        
        
        # click notification bell
        bell_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'relative') and contains(@class, 'transition-all')]"))
        )
        bell_btn.click()
        print("✅ Successfully clicked Notification bell.")
        
        
        # click notification content
        content = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'flex-1') and contains(@class,'min-w-0')]"))
        )
        content.click()
        print("✅ Successfully clicked Content Notification.")
        print("✅ Notification loaded successfully.")
        
        
        # click view event  button
        view_event_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='View Event']"))
        )
        view_event_btn.click()
        print("✅ View Event button click successfully")
        print("✅ Successfully View Event notification.")
        
    except Exception as e:
        print(f"Error during viewing event notification: {e}")
        raise