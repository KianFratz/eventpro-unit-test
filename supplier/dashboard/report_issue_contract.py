from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def report_issue_contract(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/dashboard")
        print("✅ Successfully navigated to Supplier Dashboard")
        
        
        # click offers tab
        offers_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Offers']"))
        )
        offers_tab.click()
        print("✅ Offers tab successfully clicked")
        print("✅ Offers loaded successfully")
        
        
        # click view contract
        view_contract = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='View Contract']"))
        )
        view_contract.click()
        print("✅ View Contract button clicked successfully")
        print("✅ Contract loaded successfully")
        
        
        # report button
        report_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Report']"))
        )
        report_btn.click()
        print("✅ Report button clicked successfully")
        print("✅ Report page loaded successfully")
        
        
        # check box non-payment by planner
        non_payment = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='nonPayment']"))
        )
        non_payment.click()
        print("✅ Non-payment by Planner check box clicked successfully")
        
        
        # others check box
        others = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='others']"))
        )
        others.click()
        print("✅ Others check box clicked successfully")
        
        
        # others text area
        textarea_others = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Explain what happened or describe the issue in detail...']"))
        )
        textarea_others.click()
        print("✅ Others text area clicked successfully")
        textarea_others.send_keys("test text")
        print("✅ Test text send successfully")
        
        
        # issue / remarks text area
        issue_remarks = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Describe the issue or provide additional details...']"))
        )
        issue_remarks.click()
        print("✅ Issue/remarks text area clicked successfully")
        issue_remarks.send_keys("test text")
        print("✅ Test text send successfully")
        
        
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
        
        
        # confirm issue buttom
        confirm = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Confirm']"))
        )
        confirm.click()
        print("✅ Confirm button clicked successfully")
        print("✅ Report issue in contract successful")
        
    except Exception as e:
        print(f"Error during reporting issue on contract: {e}")
        raise