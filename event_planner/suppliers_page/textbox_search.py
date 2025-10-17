from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def textbox_search(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/suppliers")
        
        # CLICK textbox
        search_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search suppliers by name or service...']"))
        )
        search_box.click()
        print("✅ Search box clicked successfully.")
        search_box.send_keys("Mary")
        print("✅ Searching for Supplier in textbox successful")
        
    except TimeoutException as e:
        print(f"Error during searching for supplier in textbox: {e}")
        raise