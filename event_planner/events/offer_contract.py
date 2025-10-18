from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def offer_contract(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # click manage event button
        manage_event_link  = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='Manage Event']"))
        )
        manage_event_link[0].click()
        print("✅ Manage event link clicked successfully")
        
        
        # click approve  button
        approve = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Approve')]"))
        )
        approve.click()
        print("✅ Approve button clicked successfully")
        
        
        # Wait for the SweetAlert2 "OK" button to appear.
        # confirmation button
        ok_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(@class, 'swal2-confirm')]"
        )))
        ok_btn.click()
        print("✅ Confirmation button clicked successfully")
        
        
        # choose service
        service_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Premium Plan')]"))
        )
        service_btn.click()
        print("✅ Premium Plan selected successfully.")
        
        
        # proceed to contract button
        proceed_contract_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Proceed to Contract Details']"))
        )
        proceed_contract_btn.click()
        print("✅ Proceed Contract button clicked successfully.")
        
        
        # send offer button
        send_offer = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Offer']"))
        )
        send_offer.click()
        print("✅ Send Offer button clicked successfully.")
        print("✅ Contract send successfully to Supplier")
        
    except Exception as e:
        print(f"Error during proposing contract to supplier: {e}")
        raise