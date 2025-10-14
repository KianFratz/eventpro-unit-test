from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def category_search(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/suppliers")
        
        # CLICK dropdown
        category_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, '-control')][.//div[text()='Category']]"))
        )
        category_dropdown.click()
        print("✅ Dropdown open for Category Searching.")
        
        
        # choose option in dropdown
        option_text ="Floral (Flowers & Arrangements)"
        option_search = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
        )
        option_search.click()
        print("✅ Floral (Flowers & Arrangements). selected")
        print("✅ Searching in Category successful")
        
    except TimeoutException:
        print(f"Error during searching in category button: {e}")
        raise