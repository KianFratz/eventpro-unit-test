from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def delete_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # click manage event button
        delete = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'hover:bg-red-50')]"))
        )
        delete.click()
        print("✅ Delete button clicked successfully")
        
        # Wait until the confirmation button appears
        confirm_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes')]"
        )))
        confirm_btn.click()
        print("✅ Confirmation Delete button clicked successfully")
        print("✅ Successfully deleted Event.")
        
    except Exception as e:
        print(f"Error during deleting event: {e}")
        raise