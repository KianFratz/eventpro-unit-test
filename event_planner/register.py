from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

PATH = "C:/Program Files (x86)/chromedriver.exe"

# ✅ Create a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# Open your login page
driver.get("http://localhost:5173/Register")


# Wait for page load (optional small delay)
time.sleep(2)

# click the "Supplier" role card
driver.find_element(By.XPATH, "//button[.//h3[text()='Event Planner']]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()


# Find text boxes 
first_name = driver.find_element(By.ID, "firstName")
last_name = driver.find_element(By.ID, "lastName")
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# and fill them in
first_name.send_keys("kane")
last_name.send_keys("fratz")
email.send_keys("kanefratz@gmail.com")
password.send_keys("123123")

# click button to create account
create_account_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Create account']")
create_account_btn.click()

time.sleep(3)

print("Event Planner Account Created Successfully")

time.sleep(3)
driver.quit()