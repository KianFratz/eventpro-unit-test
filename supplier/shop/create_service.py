from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def create_service(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        
        # click services tab
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='tablist']//button[@role='tab' and normalize-space(text())='Services']"))
        )
        services_tab.click()
        print("✅ Navigated to Services Tab successfully")
        
        
        create_service_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Make a Service')] or .//span[contains(text(), 'Service Limit Reached')]]"))
        )
        create_service_btn.click()
        print("✅ Make a Service button clicked.")
        
        
        try:
            # Service Plan Type
            
            # CLICK dropdown
            plan_type_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, 'select__control') or contains(@class, 'css-')][.//div[contains(., 'e.g Basic Plan')]]"
                ))
            )
            plan_type_dropdown.click()
            print("✅ Dropdown open for choosing Service Plan type.")
            
            # choose option in dropdown
            option_text="Basic Plan"
            option = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            option.click()
            print("✅ Basic Plan selected")
            
        except Exception as e:
            print(f"❌ Error during selecting service plan type: {type(e).__name__} - {e}")
            raise
        
        
        # Price
        price = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g ₱5000']"))
        )
        price.click()
        price.clear()
        price.send_keys("5000")

        print("✅ Price added successfully.")
        
        
        # Inclusions
        try:
            # 1st inclusion
            inclusion = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g One Free Tiramisu']"))
            )
            inclusion.click()
            inclusion.send_keys("Mango Float")
            
            print("✅ Mango float successfully send.")
            
            add_inclusion_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-green-600"))
            )
            add_inclusion_btn.click()
            print("✅ Mango float successfully added in inclusion.")

            
            # 2nd inclusion
            inclusion = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g One Free Tiramisu']"))
            )
            inclusion.click()
            inclusion.send_keys("Bibimbap")
            print("✅ Bibimbap successfully send.")
            
            add_inclusion_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-green-600"))
            )
            add_inclusion_btn.click()
            print("✅ Bibimbap successfully added in inclusion.")
            
        except Exception as e:
            print(f"❌ Error during adding inclusions: {type(e).__name__} - {e}")
            raise
        
        
        # Remove Inclusions
        try:
            target_inclusion = "Mango Float"
            remove = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    f"//span[contains(., '{target_inclusion}')]/button[normalize-space(text())='×']"
                ))
            )
            remove.click()
            print("✅ Mango Float remove successfully.")
            
        except Exception as e:
            print(f"❌ Error during removing inclusion: {type(e).__name__} - {e}")
            raise
        
        
        try:
            # Payment Notice
            # CLICK dropdown
            business_permit_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='e.g Pay after service..']]"
                ))
            )
            business_permit_dropdown.click()
            print("✅ Dropdown open for Payment Notice.")
            
            # choose option in dropdown
            option_text ="Down Payment required atleast 50 percent."
            option_payment_notice = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            option_payment_notice.click()
            print("✅ Down Payment required atleast 50 percent. selected")
            
            
        except Exception as e:
            print(f"❌ Error during uploading business document: {type(e).__name__} - {e}")
            raise
        

        # click create button
            create_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Create']"))
            )
            create_btn.click()
            print("✅ Service created successfully!")
        
    except Exception as e:
        print(f"Error during Creating Service: {e}")
        raise