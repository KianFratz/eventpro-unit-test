from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def reject_report(driver):
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
        
        # Reject report
        reject_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reject']")))
        reject_btn.click()
        print("✅ Clicking Reject button successful.")
        
        # reject reason
        reason = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Enter rejection reason...']"))
        )
        reason.click()
        print("✅ Clicking textarea successful.")
        reason.send_keys("No evidence")
        print("✅ Reason send successfully.")
        
        # Confirm reject button
        confirm_reject = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm Reject']"))
        )
        confirm_reject.click()
        print("✅ Clicking Confirm Reject button successful.")
        print("✅ Report Rejected successfully.")
        
    except TimeoutException as e:
        print(f"Error during rejecting report: {e}")
        raise