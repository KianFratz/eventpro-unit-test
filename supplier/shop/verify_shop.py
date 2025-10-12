from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def verify_shop(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/verify")
        print("✅ Navigated to Supplier Verification page.")
        
        additional_info = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Any extra details...']"))
        )
        additional_info.click()
        additional_info.send_keys("Please verify me! please.")
        print("✅ Added additional information successfully.")
        
        
        try:
            # Upload valid id
            
            
            # CLICK dropdown
            id_type_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Select ID type']]"
                ))
            )
            id_type_dropdown.click()
            print("✅ Dropdown open for upload valid id.")
            
            # choose option in dropdown
            option_text="National ID"
            option = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            option.click()
            print("✅ National ID selected")
            
            # wait for FilePond input to appear
            file_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file' and contains(@class, 'filepond--browser')]"))
            )
            # Define file paths (absolute paths are required)
            file1 = os.path.abspath(r"C:\Users\Admin\Desktop\Unit Test EventPro\supplier\public\images.jpg")
            file2 = os.path.abspath(r"C:\Users\Admin\Desktop\Unit Test EventPro\supplier\public\breed_abyssinian_cat.jpg")
            
            # Send both file paths (space-separated) to upload both at once
            file_input.send_keys(f"{file1}\n{file2}")
            print("✅ Driver's License images uploaded successfully.")
        except Exception as e:
            print(f"❌ Error during uploading valid ID: {type(e).__name__} - {e}")
            raise
        
        
        try:
            # Upload business document
            # CLICK dropdown
            business_permit_dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Select document type']]"
                ))
            )
            business_permit_dropdown.click()
            print("✅ Dropdown open for business document.")
            
            # choose option in dropdown
            option_business_document_text ="Business Permit"
            option_business_document = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_business_document_text}']"))
            )
            option_business_document.click()
            print("✅ Business Permit selected")
            
            # wait for FilePond input to appear
            file_input_business_document = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file' and contains(@class, 'filepond--browser')]"))
            )
            # Define file paths (absolute paths are required)
            file3 = os.path.abspath(r"C:\Users\Admin\Desktop\Unit Test EventPro\supplier\public\image-79322-800.jpg")
            
            # Send file
            file_input_business_document.send_keys(f"{file3}")
            print("✅ Business Permit image uploaded successfully.")
        except Exception as e:
            print(f"❌ Error during uploading business document: {type(e).__name__} - {e}")
            raise
        
        
        # checkbox
        checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
        )
        checkbox.click()
        print("✅ Confirm that all information provided is accurate and authentic, clicked successfully.")
        
                
        # button submit
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Submit')]"))
        )
        submit_button.click()
        print("✅ Supplier Verification submitted successfully!")
        
        
    except Exception as e:
        print(f"Error during Supplier Verification: {e}")
        raise