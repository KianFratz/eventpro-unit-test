from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login(driver):
    # Open your login page
    driver.get("http://localhost:5173/login")

    # Wait for page load (optional small delay)
    time.sleep(2)

    # Find text boxes and fill them in
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "password")

    # Add inputs
    email.send_keys("maryfaith@gmail.com")
    password.send_keys("123123")

    # click button
    driver.find_element(By.CSS_SELECTOR, "button.bg-blue-600").click()
        
    # Explicitly wait for the URL to change to the suppliers page
    wait = WebDriverWait(driver, 10)
    try:
        # Replace 'http://localhost:5173/suppliers' with the actual URL 
        # of the page you land on after a successful login.
        wait.until(EC.url_to_be("http://localhost:5173/shop")) 
    except TimeoutException:
        print("Warning: Login successful but URL change timed out.")
        # You might want to raise an error here if a successful redirect is mandatory

    print("Login Successfully")