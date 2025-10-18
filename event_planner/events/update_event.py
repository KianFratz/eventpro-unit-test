from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def update_event(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("http://localhost:5173/events")
        print("✅ Successfully navigated to Events page.")
        
        # click manage event button
        manage_event_link  = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='Manage Event']"))
        )
        manage_event_link[1].click()
        print("✅ Manage event link clicked successfully")
        
        # event name
        event_name = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter event name']"))
        )
        event_name.click()
        print("✅ Event Name textbox clicked successfully")
        event_name.clear()
        print("✅ Event Name textbox cleared successfully")
        event_name.send_keys("Kian")
        print("✅ New Event Name successfully send")
        
        # location
        location = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g University of Cebu Lapu-Lapu and Mandaue']"))
        )
        location.click()
        print("✅ Location textbox clicked successfully")
        location.clear()
        print("✅ Location textbox cleared successfully")
        location.send_keys("Mandani Bay, Philippines")
        print("✅ New Location successfully send")
        
        # date
        date_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='event_date']"))
        )
        date_input.clear()
        print("✅ Date cleared successfully")
        date_input.send_keys("2025-10-25")
        print("✅ New Date successfully send")
        
        # start time
        start_time = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='start_time']"))
        )
        start_time.clear()
        print("✅ Start time cleared successfully")
        start_time.send_keys("15:00")
        print("✅ New Start time successfully send")
        
        # end time
        end_time = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='end_time']"))
        )
        end_time.clear()
        print("✅ End time cleared successfully")
        end_time.send_keys("16:00")
        print("✅ New End time successfully send")
        
        try:
            # event type
            # CLICK dropdown
            dropdown = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, '-control')][.//div[text()='Wedding (Planners & Services)']]"
                ))
            )       
            dropdown.click()
            print("✅ Dropdown open for Event type.")
            
            # choose option in dropdown
            option_text ="Birthday Party"
            pick_options = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
            )
            pick_options.click()
            print("✅ Birthday Party option selected successfully")
            print("✅ New Event type successfully pick")
            
        except Exception as e:
            print(f"Error during selecting event type: {e}")
            raise
        
        
        
        # budget
        budget = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='25,500']"))
        )
        budget.click()
        print("✅ Budget textbox clicked successfully")
        budget.clear()
        print("✅ Budget textbox cleared successfully")
        budget.send_keys("100000")
        print("✅ New Budget successfully send")
        
        
        # description
        description = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Describe your event...' ]"))
        )
        description.click()
        print("✅ Description textbox clicked successfully")
        description.clear()
        print("✅ Description textbox cleared successfully")
        description.send_keys("Update test")
        print("✅ New Description successfully send")
        
        
        # remove specify supplier
        supplier_name = "Photography (Photo & Video)"
        remove_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//span[contains(@class, 'inline-flex')][.//text()[normalize-space()='{supplier_name}']]//button"
            ))
        )
        remove_button.click()
        print("✅ Specified Supplier: Photography (Photo & Video) successfully removed.")
        

        # add new specified supplier
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
        option_text ="Event Stylist / Decorator"
        supplier_options = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'-option') and normalize-space(text())='{option_text}']"))
        )
        supplier_options.click()
        print("✅ Event Stylist / Decorator supplier selected successfully")
        
        # add category button
        add_supplier_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Category']"))
        )
        add_supplier_btn.click()
        print("✅ New Specify Supplier added successfully")
        
        # update button
        update_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update Event']"))
        )
        update_btn.click()
        print("✅ Update button clicked successfully")        
        print("✅ Successfully updated Event.")
        
    except Exception as e:
        print(f"Error during updating event: {e}")
        raise