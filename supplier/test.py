from login import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from shop.edit_about_profile import edit_about_profile


PATH = "C:/Program Files (x86)/chromedriver.exe"

# ✅ Create a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# --- Execution ---
try:
    login(driver)
    edit_about_profile(driver)
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Ensure the browser closes at the end of the script
    if 'driver' in globals():
        driver.quit()

