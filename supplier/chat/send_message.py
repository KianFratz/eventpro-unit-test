from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def send_message(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/chats/tzTeoMKm1L4pf1cqg4ZU")
        
        # click input box for chat
        input_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your message...']"))
        )
        input_box.click()
        input_box.send_keys("Testing")
        print("✅ Message input successfully")
        
        # send button
        send_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-700"))
        )
        send_btn.click()
        print("✅ Message send successfully")
        
        
    except Exception as e:
        print(f"Error during sending message: {e}")
        raise