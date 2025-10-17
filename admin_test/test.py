from login import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dashboard.reject_report import reject_report

PATH = "C:/Program Files (x86)/chromedriver.exe"

# ✅ Create a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# --- Execution ---
try:
    login(driver)
    reject_report(driver)
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Ensure the browser closes at the end of the script
    if 'driver' in globals():
        driver.quit()

