from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def add_favorites(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/suppliers")
        
        # click view details button
        view_details = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        view_details.click()
        print("✅ Click View Details button, successful")
        
        
        # click add favorites button
        favorite_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.p-2.rounded-full"))
        )
        favorite_btn.click()
        print("✅ Add favorites, successful")
        
    except Exception as e:
        print(f"Error during adding favorites: {e}")
        raise