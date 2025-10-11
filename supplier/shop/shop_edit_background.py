from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def shop_edit_background(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/shop")
        # 1) Click the Edit button to open modal
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]"))
        )
        edit_button.click()
        
        # 2) Wait for FilePond to appear
        filepond_wrapper = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".filepond--wrapper"))
        )

        # 3) Find FilePond's <input type="file">
        file_input = filepond_wrapper.find_element(By.CSS_SELECTOR, "input[type='file']")
        
        LOCAL_IMAGE_PATH = r"C:\Users\Admin\Desktop\Unit Test EventPro\supplier\public\cat.jpg"

        # 4) Upload local image
        abs_path = os.path.abspath(LOCAL_IMAGE_PATH)
        file_input.send_keys(abs_path)
        print("✅ Image sent to FilePond input")
        
        # 5) Wait for FilePond upload to finish
        # FilePond adds a .filepond--item[data-filepond-item-state="processing-complete"]
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".filepond--item[data-filepond-item-state='processing-complete']")
            )
        )
        print("✅ FilePond upload completed")
        
        # 6) Click the Submit button
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
        )
        submit_button.click()
        print("✅ Submit clicked")

        # Optional: Wait for modal to close or success toast
        time.sleep(2)
        
    except Exception as e:
        print(f"An error occurred during uploading background image: {e}")
        raise # Stop the script on failure
