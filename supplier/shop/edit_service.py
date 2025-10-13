from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def edit_service(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        
        # click services tab
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='tablist']//button[@role='tab' and normalize-space(text())='Services']"))
        )
        services_tab.click()
        print("✅ Navigated to Services Tab successfully")
        
        
        edit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Edit Services']"))
        )
        edit_btn.click()
        print("✅ Edit Service button clicked.")
        
        
        try:
            # Service Plan Type
            
            # CLICK dropdown
            plan_type_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, 'select__control') or contains(@class, 'css-')][.//div[contains(., 'Premium Plan')]]"
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
            print("✅ Basic Plan selected successfully.")
            print("✅ New Service Plan selected successfully.")
            
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
        print("✅ 5000 send successfully.")
        print("✅ New Price added successfully.")
        
        
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
            print("✅ New Inclusion added successfully.")

        except Exception as e:
            print(f"❌ Error during adding inclusions: {type(e).__name__} - {e}")
            raise
        
        
        # Remove Inclusions
        try:
            target_inclusion = "Bibimbap"
            remove = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    f"//span[contains(., '{target_inclusion}')]/button[normalize-space(text())='×']"
                ))
            )
            remove.click()
            print("✅ Bibimbap remove successfully.")
            
        except Exception as e:
            print(f"❌ Error during removing inclusion: {type(e).__name__} - {e}")
            raise
        
        
        try:
            # Payment Notice
            # CLICK dropdown
            business_permit_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Pay after service delivered']]"
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
            print("✅ Pay after service delivered, successfully selected.")
            print("✅ New Payment Notice successfully selected")
            
        except Exception as e:
            print(f"❌ Error during editing payment notice: {type(e).__name__} - {e}")
            raise
        

        # click save button
        create_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Save']"))
        )
        create_btn.click()
        print("✅ Service updated successfully!")
        
    except Exception as e:
        print(f"Error during Creating Service: {e}")
        raise