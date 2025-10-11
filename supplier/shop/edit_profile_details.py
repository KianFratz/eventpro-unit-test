from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import traceback

def edit_profile_details(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit Details')]"))
        )
        edit_button.click()
        print("Clicked 'Edit Details' button successful")
        
        # Wait for modal to appear
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'filepond--wrapper')]"))
            )
            print("✅ Modal form appeared")
        except Exception as e:
            print("Error")
            traceback.print_exc()
        
        # supplier name
        shop_name_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g Rivera Shop']"))
        )
        shop_name_input.clear()
        # Type in the supplier name
        shop_name_input.send_keys("Faiths's flower shop")
        print("✅ Shop name entered")

        
        # location
        location_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Location')]/following::input[1]"))
        )
        location_input.clear()
        location_input.send_keys("Mactan Newtown, Lapu-Lapu, Philippines")
        print("✅ New location entered")

        # --- Supplier Type ---
        select_supplier_type(driver, "Wedding (Planners & Services)")
        print("✅ New supplier type sent successfully")

        update_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
        )
        update_button.click()
        print("✅ Clicked Update button")

        wait.until(EC.invisibility_of_element_located((By.XPATH, "//form")))
        print("🎉 Update completed successfully")

        # Optional: Wait for modal to close or success toast
        time.sleep(2)
        
    except Exception as e:
        print(f"An error occurred during editing profile details: {e}")
        raise # Stop the script on failure

def select_supplier_type(driver, option_text):
    try:
        wait = WebDriverWait(driver, 10)

        # Step 1️⃣ — Click the dropdown to open options
        dropdown = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-13cymwt-control, .Select__control"))
        )
        dropdown.click()
        print("✅ Clicked supplier type dropdown")

        # Step 2️⃣ — Wait for the dropdown menu to appear and select your option
        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{option_text}')]"))
        )
        option.click()
        print("✅ Selected supplier type")
    except Exception as e:
        print("❌ Error selecting supplier type:")
        traceback.print_exc()
   