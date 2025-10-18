from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def search_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # search event
        input_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search events by name, location, or category...']"))
        )
        input_box.send_keys("Kian")
        print("✅ Search input send successfully")
        print("✅ Search Event successful")
        
    except Exception as e:
        print(f"Error during searching event: {e}")
        raise