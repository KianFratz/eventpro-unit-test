from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def approve_contract(driver):
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
        
        
        # click approve contract
        approve_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Approve Offer']"))
        )
        approve_contract.click()
        print("✅ Approve Contract button clicked successfully")
        print("✅ Approve Confirmation loaded successfully")
        
        
        # confirmation button
        confirmation = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Yes, approve it']"))
        )
        confirmation.click()
        print("✅ Confirmation button clicked successfully")
        print("✅ Approving contract successful")
        
    except Exception as e:
        print(f"Error during approving contract: {e}")
        raise