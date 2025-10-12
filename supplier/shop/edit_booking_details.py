from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def edit_booking_details(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Start at the registration page
        driver.get("http://localhost:5173/shop")
        
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit Booking')]"))
        )
        edit_button.click()
        print("✅ Edit button clicked")
        
        
        # Availability days
        DAYS_TO_SELECT = ['Mon', 'Sat']
        for day in DAYS_TO_SELECT:
            click_day_button(driver, day)
        print("✅ New availability days sent successfully.")
        
        
        # Start time 
        set_time_input(driver, "Start Time", "10:00")
        set_time_input(driver, "End Time", "18:00")
        print("✅ New Start time and End time sent successfully.")
        
        try:
            dropdown = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='-control']"))
            )
            dropdown.click()
            print("✅ Dropdown open")

            option_text="Within 1 Hour"
            # Choose one of the options — e.g., "Within 4 Hour"
            option = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            option.click()
            print("✅ Within 1 Hour selected")
            print("✅ New Response Time sent successfully.")
            
        except Exception as e:
            print(f"❌ Error during editing response time: {type(e).__name__} - {e}")
            raise
        
        
        save_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-green-500"))
        )
        save_button.click()
        print("✅ Booking Details updated successfully!")
        
    except Exception as e:
        print(f"Error during editing Booking Details: {e}")
        raise
    

# helper functions
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