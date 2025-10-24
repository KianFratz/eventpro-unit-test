from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def submit_delivery(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/dashboard")
        print("✅ Successfully navigated to Supplier Dashboard")
        
        
        # click contract tab
        offers_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Contracts']"))
        )
        offers_tab.click()
        print("✅ Contract tab successfully clicked")
        print("✅ Contracts loaded successfully")
        
        
        # click view contract
        view_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='View Contract']"))
        )
        view_contract.click()
        print("✅ View Contract button clicked successfully")
        print("✅ Contract loaded successfully")
        
        
        # click submit delivery button
        submit_delivery_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Submit Delivery']"))
        )
        submit_delivery_btn.click()
        print("✅ Submit Delivery button clicked successfully")
        print("✅ Delivery Submission modal loaded successfully")
        
        
        # Additional Information text area
        additional_info = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Enter any additional notes...']"))
        )
        additional_info.click()
        print("✅ Additional Information text area clicked successfully")
        additional_info.send_keys("test text")
        print("✅ Additional Information test text send successfully")
        
        
        # proof image
        # upload image
        filepond_wrapper = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".filepond--wrapper"))
        )
        
        # Find FilePond's <input type="file">
        file_input = filepond_wrapper.find_element(By.CSS_SELECTOR, "input[type='file']")
        
        
        LOCAL_IMAGE_PATH = r"C:\Users\Admin\Desktop\Unit Test EventPro\supplier\public\images (1).jpg"
        # Upload local image
        abs_path = os.path.abspath(LOCAL_IMAGE_PATH)
        file_input.send_keys(abs_path)
        print("✅ Image sent to FilePond input successful")
        
        #  Wait for FilePond upload to finish
        # FilePond adds a .filepond--item[data-filepond-item-state="processing-complete"]
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".filepond--item[data-filepond-item-state='processing-complete']")
            )
        )
        print("✅ Image successfully uploaded")
        
        
        # submit button
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Submit']"))
        )
        submit.click()
        print("✅ Submit button clicked successfully")
        print("✅ Submit proof of delivery successful")
        
    except Exception as e:
        print(f"Error during submitting proof of delivery: {e}")
        raise