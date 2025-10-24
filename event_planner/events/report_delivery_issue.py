from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def report_delivery_issue(driver):
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
        
        # click view contract button
        view_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View Contract')]"))
        )
        view_contract.click()
        print("✅ View Contract button clicked successfully")
        print("✅ Contract loaded successfully.")
        
        
        # click issue button
        issue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Issue')]"))
        )
        issue_button.click()
        print("✅ Issue button clicked successfully")
        print("✅ Report Delivery Issues modal loaded successfully")
        
        
        # check box late delivery
        late_delivery = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='lateDelivery']"))
        )
        late_delivery.click()
        print("✅ Late Delivery check box clicked successfully")
        
        
        # check box service non-conformity
        non_conformity = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='serviceNonConformity']"))
        )
        non_conformity.click()
        print("✅ Service Non-Conformity check box clicked successfully")
        
        
        # radio button badly damaged
        badly_damaged = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='bad']"))
        )
        badly_damaged.click()
        print("✅ Badly damage radio button clicked successfully")
        
        
        # Review / Reason for Issuing
        reason = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Describe the issue or reason for applying penalties...']"))
        )
        reason.click()
        print("✅ Reason for issuing text area clicked successfully")
        reason.send_keys("test text")
        print("✅ Reason for issuing test send successfully")
        
        
        # click confirm button
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]"))
        )
        confirm_button.click()
        print("✅ Confirm button clicked successfully")
        
        
        print("✅ Reporting Delivery Issue successful.")
        
    except Exception as e:
        print(f"Error during reporting delivery issue: {e}")
        raise