from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PATH = "C:/Program Files (x86)/chromedriver.exe"

# ✅ Create a Service object
service = Service(PATH)
driver = webdriver.Chrome(service=service)
    
def login():
    # Open your login page
    driver.get("http://localhost:5173/login")

    # Wait for page load (optional small delay)
    time.sleep(2)

    # Find text boxes and fill them in
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "password")

    # Add inputs
    email.send_keys("test@gmail.com")
    password.send_keys("123123")

    # click button
    driver.find_element(By.CSS_SELECTOR, "button.bg-blue-600").click()
    
    # Explicitly wait for the URL to change to the suppliers page
    wait = WebDriverWait(driver, 5)
    try:
        # Replace 'http://localhost:5173/suppliers' with the actual URL 
        # of the page you land on after a successful login.
        wait.until(EC.url_to_be("http://localhost:5173/suppliers")) 
    except TimeoutException:
        print("Warning: Login successful but URL change timed out.")
        # You might want to raise an error here if a successful redirect is mandatory


    print("Login Successfully")
    
    
def register():
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

def viewDetails():
    wait = WebDriverWait(driver, 10)
    
    try:
        # Open your supplier page
        driver.get("http://localhost:5173/suppliers")

        # Wait for page load (optional small delay)
        time.sleep(2)

        # click button
        supplier_details_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        
        # Click the button
        supplier_details_btn.click()
        
        # Wait for and click the element that contains the text 'Services'
        services_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Services']"))
        )
        services_tab.click()
        print("Services loaded Successfully")
        
        reviews_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reviews']"))
        )
        reviews_tab.click()
        print("Reviews loaded Successfully")

        time.sleep(2)
        print("Supplier Details loaded Successfully")

        time.sleep(3)
    except TimeoutException:
        print("Error: 'View Details' button did not become clickable within 10 seconds.")
        # If the wait fails, the exception will be caught by the main try/except block
        raise # Re-raise the exception to terminate the test on failure


# --- Execution ---
try:
    login()
    viewDetails()
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Ensure the browser closes at the end of the script
    if 'driver' in globals():
        driver.quit()
