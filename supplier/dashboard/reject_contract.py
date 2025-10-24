from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def reject_contract(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/dashboard")
        print("✅ Successfully navigated to Supplier Dashboard")
        
        
        # click offers tab
        offers_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Offers']"))
        )
        offers_tab.click()
        print("✅ Offers tab successfully clicked")
        print("✅ Offers loaded successfully")
        
        
        # click view contract
        view_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='View Contract']"))
        )
        view_contract.click()
        print("✅ View Contract button clicked successfully")
        print("✅ Contract loaded successfully")
        
        
        # click reject contract
        reject_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Reject']"))
        )
        reject_contract.click()
        print("✅ Reject Contract button clicked successfully")
        print("✅ Reject Submission modal loaded successfully")
        
        
        # reject reason text area
        reason = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Explain why this submission is being rejected...']"))
        )
        reason.click()
        print("✅ Reject reason text area clicked successfully")
        reason.send_keys("test text")
        print("✅ Reject reason test send successfully")
        
        
        # submit button
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[normalize-space(text())='Submit']]"))
        )
        submit.click()
        print("✅ Submit button clicked successfully")
        print("✅ Rejecting contract successful")
        
    except Exception as e:
        print(f"Error during rejecting contract: {e}")
        raise