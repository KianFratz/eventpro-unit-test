from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def delete_service(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        
        # click services tab
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='tablist']//button[@role='tab' and normalize-space(text())='Services']"))
        )
        services_tab.click()
        print("✅ Navigated to Services Tab successfully")
        
        # delete button
        delete_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-gray-500"))
        )
        delete_btn.click()
        
        print("✅ Service deleted successfully!")
        
    except Exception as e:
        print(f"Error during deleting Service: {e}")
        raise