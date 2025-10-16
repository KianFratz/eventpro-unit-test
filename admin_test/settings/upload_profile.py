from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def upload_profile(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/settings")
        
        # CLICK pencil button
        edit_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.hover\\:ring-2.hover\\:ring-blue-600")))
        edit_btn.click()
        print("✅ Edit button clicked successfully.")
        
        
        # upload image
        filepond_wrapper = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".filepond--wrapper"))
        )
        
        # Find FilePond's <input type="file">
        file_input = filepond_wrapper.find_element(By.CSS_SELECTOR, "input[type='file']")
        
        
        LOCAL_IMAGE_PATH = r"C:\Users\Admin\Desktop\Unit Test EventPro\admin_test\public\images (1).jpg"
        # Upload local image
        abs_path = os.path.abspath(LOCAL_IMAGE_PATH)
        file_input.send_keys(abs_path)
        print("✅ Image sent to FilePond input")
        
        #  Wait for FilePond upload to finish
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
        print("✅ Upload Profile Picture, successful")
        
    except TimeoutException:
        print(f"Error during uploading profile picture: {e}")
        raise