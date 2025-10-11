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

        # Wait for page load (optional small delay)
        time.sleep(2)

        # click button
        supplier_details_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        
        # Click the button
        supplier_details_btn.click()
        
        # Wait for and click the element that contains the text 'Services'
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Services']"))
        )
        services_tab.click()
        print("Services loaded Successfully")
        
        reviews_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reviews']"))
        )
        reviews_tab.click()
        print("Reviews loaded Successfully")

        time.sleep(2)
        print("Supplier Details loaded Successfully")

        time.sleep(3)
    except TimeoutException:
        print("Error: 'View Details' button did not become clickable within 10 seconds.")
        # If the wait fails, the exception will be caught by the main try/except block
        raise # Re-raise the exception to terminate the test on failure