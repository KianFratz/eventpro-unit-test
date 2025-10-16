from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def search_events(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://unite-eventpro.netlify.app/events")
        
        # click search box
        search = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search events by name, location, or category...']"))
        )
        search.click()
        print("✅ Search input successfully clicked")
        search.send_keys("Pagobo")
        print("✅ Search input successfully send")
        print("✅ Search events, successful")
        
    except Exception as e:
        print(f"Error during searching events: {e}")
        raise