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
driver.get("http://localhost:5173/login")


# Wait for page load (optional small delay)
time.sleep(2)

# Find text boxes and fill them in
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

# fill textbox
email.send_keys("kanefratz@gmail.com")
password.send_keys("123123")

# click button
driver.find_element(By.CSS_SELECTOR, "button.bg-blue-600").click()

print("Event Planner Account Login Successfully")

time.sleep(3)
driver.quit()