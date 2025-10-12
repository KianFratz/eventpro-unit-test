from login import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from shop.edit_booking_details import edit_booking_details


PATH = "C:/Program Files (x86)/chromedriver.exe"

# ✅ Create a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# --- Execution ---
try:
    login(driver)
    edit_booking_details(driver)
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Ensure the browser closes at the end of the script
    if 'driver' in globals():
        driver.quit()

