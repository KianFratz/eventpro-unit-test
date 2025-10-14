from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def withdrawal_balance(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/settings")
        
        # click balance and withdrawal tab
        withdrawal_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Balance & Withdrawal']"))
        )
        withdrawal_tab.click()
        print("✅ Successfully navigated to Balance and Withdrawal tab")
        
        
        # input withdrawal amount
        amount = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='0.00']")))
        amount.click()
        print("✅ Input box click, successfully")
        amount.send_keys("2467.5")
        print("✅ Amount send successfully")
        
        
        # payment method GCASH
        payment_name = "Gcash"
        gcash_elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, f"//span[text()='{payment_name}']"))
        )
        gcash_elements[0].click()
        print("✅ GCash clicked, successfully")
       
        
        # account holder name
        account_holder = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Account Holder Name']")))
        account_holder.click()
        print("✅ Account Holder input box click, successfully")
        account_holder.send_keys("Mary")
        print("✅ Account Holder name send successfully")
        
        
        # account number
        account_number = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Account Number']"))
        )
        account_number.click()
        print("✅ Account Number input box click, successfully")
        account_number.send_keys("09123123123")
        print("✅ Account Number send successfully")
        
        
        # request withdrawal button
        request_withdrawal = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Request Withdrawal']")))
        request_withdrawal.click()
        print("✅ Request Withdrawal, clicked successfully.")
        
        
        # withdraw button
        withdraw_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, withdraw it!']")))
        withdraw_btn.click()
        print("✅ Withdrawal button, clicked successfully.")
        time.sleep(20)
        print("✅ Balance Withdrawal, successful.")
        
    except TimeoutException as e:
        print(f"Error during balance withdrawal : {e}")
        raise