from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def shop_registration(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Start at the registration page
        driver.get("http://localhost:5173/shop")
        
        # supplier name
        # Wait up to 10 seconds for the element to appear
        supplier_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "SupplierName"))
        )
        # Type in the supplier name
        supplier_name_field.send_keys("Mary's flower shop")
        
        
        # location
        location_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.py-3.rounded-md.ring-1.ring-black"))
        )
        location_input.send_keys("Shangrila's Main Gate, Lapu-Lapu, Philippines")
        
        
        # --- Supplier Type (Floral) ---
        select_supplier_type(driver, "Floral (Flowers & Arrangements)")

        
        # description
        description_field = wait.until(
            EC.presence_of_element_located((By.NAME, "description"))
        )
        description_field.send_keys("We offer premium floral arrangements and event coordination services.")
        
        
        # area of expertise (Floral)
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'px-4') and contains(@class, 'rounded-lg')]"))
        )
        # Click specific expertise options by text
        expertise_options = ["Floral", "Bouquets"]
        for option in expertise_options:
            button = driver.find_element(
                By.XPATH,
                f"//button[normalize-space()='{option}']"
            )
            button.click()


        # specialization
        specialization_field = wait.until(
            EC.presence_of_element_located((By.NAME, "specializations"))
        )
        specialization_field.send_keys("We specialize in arranging flowers.")
        
        
        # email address
        email_address = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_address.send_keys("Illya@gmial.com")
        
        
        # phone number
        phone_number = wait.until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        phone_number.send_keys("09235451232") 
        
        
        # --- Response Time (Within 4 Hour) ---
        HOUR_TO_SELECT = 'Within 4 Hour'
        label_xpath = "//label[contains(normalize-space(), 'Typical Response Time')]"
        
        # Find the input control
        select_response_time = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"{label_xpath}/following-sibling::div[1]//input"))
        )
        select_response_time.click()
        
        # Click the option
        option_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[normalize-space()='{HOUR_TO_SELECT}']"))
        )
        option_element.click() 
        
        
        # pricing
        PRICE_VALUE = "5000"
        price_input = wait.until(
            EC.presence_of_element_located((By.NAME, "minimumOrders"))
        )
        price_input.clear()
        price_input.send_keys(PRICE_VALUE)
        
        
        # pick days
        DAYS_TO_SELECT = ['Mon', 'Fri']
        for day in DAYS_TO_SELECT:
            click_day_button(driver, day)

            
        # time 
        set_time_input(driver, "Start Time", "09:00")
        set_time_input(driver, "End Time", "17:00")
        
        # Submit Button
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
        )
        submit_button.click()
        
        print("Supplier Shop Registration created successfully.")
        

    except Exception as e:
        print(f"An error occurred during supplier registration: {e}")
        raise # Stop the script on failure


def select_supplier_type(driver, option_text):
    wait = WebDriverWait(driver, 10)

    # Step 1️⃣ — Click the dropdown to open options
    dropdown = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-13cymwt-control, .Select__control"))
    )
    dropdown.click()

    # Step 2️⃣ — Wait for the dropdown menu to appear and select your option
    option = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'option') and contains(text(), '{option_text}')]"))
    )
    option.click()
    
def click_day_button(driver, day_name):
    """Waits for and clicks the button corresponding to the given day name."""
    wait = WebDriverWait(driver, 10)
    print(f"Attempting to click day: '{day_name}'...")
    try:
        day_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{day_name}']"))
        )
        day_button.click()
        print(f"Successfully clicked day: '{day_name}'")
    except TimeoutException:
        print(f"Error: Button '{day_name}' did not become clickable.")
        raise
    
def set_time_input(driver,label_text, time_value):
    """Locates the time input field based on its preceding label text and sets the time value."""
    wait = WebDriverWait(driver, 10)
    print(f"Attempting to set '{label_text}' to {time_value}...")
    
    # Robust XPath: Find the label's parent, then the input
    input_xpath = (
        f"//label[normalize-space()='{label_text}']/following-sibling::input" 
    )
    
    try:
        time_input = wait.until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        time_input.clear()
        time_input.send_keys(time_value)
        print(f"Successfully set '{label_text}' to {time_value}")
        
    except Exception as e:
        print(f"Error setting '{label_text}': Could not find the input field. Details: {e}")
        raise
