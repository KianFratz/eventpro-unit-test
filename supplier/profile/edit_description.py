from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def edit_description(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/profile")
        
        # click edit
        edit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Edit']"))
        )
        edit_btn.click()
        print("✅ Edit button successfully clicked")
        
        
        # description
        text_area = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='e.g Kian is an event planner for almost a decade.']"))
        )
        text_area.click()
        text_area.clear()
        text_area.send_keys("Update description")
        print("✅ New Description successfully send")
        
        
        # save edit
        save_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Save']"))
        )
        save_btn.click()
        print("✅ Save button successfully clicked")
        print("✅ Description Updated successfully")
        
    except Exception as e:
        print(f"Error during editing profile description: {e}")
        raise