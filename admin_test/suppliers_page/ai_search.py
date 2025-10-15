from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def ai_search(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/suppliers")
        
        # CLICK ai search button
        search_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='AI Search']]"))
        )
        search_button.click()
        print("✅ AI Search button click successfully.")
        
        
        # search for supplier
        search_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=\"Example: 'Event suppliers with at least 5 star rating'\"]"))
        )
        search_input.click()
        print("✅ AI Search input click successfully.")
        search_input.send_keys("Looking for a Floral supplier")
        print("✅ Input send successfully.")
        
        
        # click button
        ai_search = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Search with AI']"))
        )
        ai_search.click()
        print("✅ Search with AI button clicked successfully.")
        print("✅ Search with AI, successful.")
        
    except TimeoutException:
        print(f"Error during AI searching: {e}")
        raise