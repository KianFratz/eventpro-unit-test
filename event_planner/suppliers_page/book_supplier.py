from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def book_supplier(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Open your supplier page
        driver.get("http://localhost:5173/suppliers")

        # view details button
        supplier_details_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        supplier_details_btn.click()
        print("✅ View Details button click successfully.")
        
        # book supplier button
        book_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Book Supplier']"))
        )
        book_btn.click()
        print("✅ Successfully clicked Book Supplier button.")

        # select event to book        
        event_radio = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio']"))
        )
        event_radio.click()
        print("✅ Successfully Select Event to Book.")
        
        # click book now button        
        book_now = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Book Now']"))
        )
        book_now.click()
        print("✅ Successfully clicked Book Now button.")

        # supplier services
        driver.get("http://localhost:5173/events/pLRmo575DetOVOwNeeq2/contract/TU5GfgCD6jUv2b98jpZmafNMOi63")
        print("✅ Successfully navigated to Supplier Services.")

        # choose service
        service_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Basic Plan')]"))
        )
        service_btn.click()
        print("✅ Basic Plan selected successfully.")
        
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
        print("✅ Booking Supplier successful")

    except TimeoutException as e:
        print(f"Error during booking Supplier: {e}")
        raise 