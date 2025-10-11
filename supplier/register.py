from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def register(driver):
    # Open your login page
    driver.get("http://localhost:5173/Register")

    # Wait for page load (optional small delay)
    time.sleep(2)

    # click the "Supplier" role card
    driver.find_element(By.XPATH, "//button[.//h3[text()='Supplier']]").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()

    # Find text boxes 
    first_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    # and fill them in
    first_name.send_keys("mary")
    last_name.send_keys("faith")
    email.send_keys("maryfaith@gmail.com")
    password.send_keys("123123")

    # click button to create account
    create_account_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Create account']")
    create_account_btn.click()

    time.sleep(2)

    print("Supplier Account Created Successfully")