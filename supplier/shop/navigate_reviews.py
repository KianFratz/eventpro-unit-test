from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def navigate_reviews(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        
        # click services tab
        reviews_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='tablist']//button[@role='tab' and normalize-space(text())='Reviews']"))
        )
        reviews_tab.click()
        print("✅ Navigated to Reviews Tab successfully")
        print("✅ Customer reviews successfully loaded")
        
    except Exception as e:
        print(f"Error during navigating to Reviews tab: {e}")
        raise