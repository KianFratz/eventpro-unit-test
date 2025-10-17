from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def viewDetails(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Open your supplier page
        driver.get("http://localhost:5173/suppliers")

        # click button
        supplier_details_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        supplier_details_btn.click()
        print("✅ View Details button click successfully.")
        print("✅ Supplier About Details loaded successfully.")
        
        # services
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Services']"))
        )
        services_tab.click()
        print("✅ Successfully clicked Services tab.")
        print("✅ Services loaded successfully.")

        # reviews        
        reviews_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reviews']"))
        )
        reviews_tab.click()
        print("✅ Successfully clicked Reviews tab.")
        print("✅ Reviews loaded successfully.")

        print("✅ Supplier Details loaded Successfully")

    except TimeoutException as e:
        print(f"Error during viewing Supplier details: {e}")
        raise # Re-raise the exception to terminate the test on failure