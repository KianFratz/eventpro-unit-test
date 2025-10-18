from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def create_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # click create new event button
        create_event_btn  = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create New Event']"))
        )
        create_event_btn.click()
        print("✅ Create new event clicked successfully")
        
        # event name
        event_name = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter event name']"))
        )
        event_name.click()
        print("✅ Event Name textbox clicked successfully")
        event_name.send_keys("Tani's College Graduation Party")
        print("✅ Event Name successfully send")
        
        # location
        location = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g University of Cebu Lapu-Lapu and Mandaue']"))
        )
        location.click()
        print("✅ Location textbox clicked successfully")
        location.send_keys("Mandani Bay, Philippines")
        print("✅ Location successfully send")
        
        # date
        date_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='event_date']"))
        )
        date_input.send_keys("2025-10-25")
        print("✅ Date successfully send")
        
        # start time
        start_time = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='start_time']"))
        )
        start_time.send_keys("15:00")
        print("✅ Start time successfully send")
        
        # end time
        end_time = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='end_time']"))
        )
        end_time.send_keys("16:00")
        print("✅ End time successfully send")
        
        try:
            # event type
            # CLICK dropdown
            dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Select event type']]"
                ))
            )       
            dropdown.click()
            print("✅ Dropdown open for Event type.")
            
            # choose option in dropdown
            option_text ="Venue Provider"
            pick_options = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            pick_options.click()
            print("✅ Venue Provider option selected successfully")
            print("✅ Event type successfully pick")
            
        except Exception as e:
            print(f"Error during selecting event type: {e}")
            raise
        
        
        
        # budget
        budget = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='25,500']"))
        )
        budget.click()
        print("✅ Budget textbox clicked successfully")
        budget.send_keys("100000")
        print("✅ Budget successfully send")
        
        
        # description
        description = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Describe your event...' ]"))
        )
        description.click()
        print("✅ Description textbox clicked successfully")
        description.send_keys("After two decades, Tani finally accomplished her education. In May 25, 2026, let's celebrate Tani's Graduation in College")
        print("✅ Description successfully send")
        
        
        # add specified supplier
        # CLICK dropdown
        dropdown_supplier = wait.until(
            EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Select supplier category']]"
            ))
        )
        dropdown_supplier.click()
        print("✅ Dropdown open for Specify the supplier you are looking for.")
        
        # choose option in dropdown
        option_text ="Lighting & Sound System"
        supplier_options = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
        )
        supplier_options.click()
        print("✅ Lightning & Sound System supplier selected successfully")
        
        # add category button
        add_supplier_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Category']"))
        )
        add_supplier_btn.click()
        print("✅ Specify Supplier added successfully")
        
        # update button
        create = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Event']"))
        )
        create.click()
        print("✅ Create Event button clicked successfully")        
        print("✅ Successfully created Event.")
        
    except Exception as e:
        print(f"Error during creating event: {e}")
        raise