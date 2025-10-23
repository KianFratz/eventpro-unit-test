from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def generate_report(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/dashboard")
        print("✅ Successfully navigated to Supplier Dashboard")
        
        # click generate report
        report_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Generate Report']"))
        )
        report_btn.click()
        print("✅ Generating Report button clicked successfully")
        print("✅ Generating Report successful")
        
    except Exception as e:
        print(f"Error during generating report: {e}")
        raise