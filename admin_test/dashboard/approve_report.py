from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def approve_report(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/dashboard")
        # CLICK calendar tab
        reports_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Reports']")))
        reports_tab.click()
        print("✅ Reports tab clicked successfully.")
        print("✅ Successfully navigated to Reports tab.")
        
        # review button
        prev_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Review Report']")))
        prev_btn.click()
        print("✅ Clicking Review button successful.")
        
        # Approve report
        approve_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Approve']")))
        approve_btn.click()
        print("✅ Clicking Approve button successful.")
        print("✅ Report Approved successfully.")
        
    except TimeoutException as e:
        print(f"Error during approving report: {e}")
        raise