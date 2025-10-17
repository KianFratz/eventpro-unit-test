from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def remove_favorites(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/favorites")
        print("✅ Successfully navigate to Favorites page.")
        
        # click remove favorites button
        favorite_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.transition-all.duration-200"))
        )
        favorite_btn.click()
        print("✅ Remove favorites, successfully")
        
        
    except Exception as e:
        print(f"Error during removing favorites: {e}")
        raise