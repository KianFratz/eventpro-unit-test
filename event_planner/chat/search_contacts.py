from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def search_contacts(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/chats/VT0D4psVdic3guGRle7g")
        
        # click search contacts
        input_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search contacts...']"))
        )
        input_box.click()
        print("✅ Search textbox successfully clicked")
        input_box.send_keys("mapit")
        print("✅ Message input successfully")
        print("✅ Searching contact successful")
        
    except Exception as e:
        print(f"Error during searching contacts: {e}")
        raise