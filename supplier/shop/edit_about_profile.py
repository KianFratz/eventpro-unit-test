from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def edit_about_profile(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        # Start at the registration page
        driver.get("http://localhost:5173/shop")
        
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h3[contains(., 'About Our Business')]/ancestor::div[contains(@class, 'flex')][1]//button[contains(., 'Edit')]"))
        )
        time.sleep(3)  # let animation finish
        edit_button.click()
        print("Clicked 'Edit About Profile' button successful")
        
        # Wait for dialog to appear
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Edit About Profile')]"))
            )
            print("✅ Dialog appeared")
        except Exception as e:
            print("Error")
            traceback.print_exc()
        
        # 3️⃣ Edit "About our Business" textarea
        about_textarea = wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Tell us briefly about your business...']"))
        )
        about_textarea.clear()
        about_textarea.send_keys("We provide premium floral and event planning services across the city.")
        print("✅ New about our business sentence added")
        
        
        
        # 4️⃣ Remove existing expertise (clicking the ones with ‘–’)
        remove_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-blue-500')]"))
        )
        # Scroll into view for visibility
        driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
        time.sleep(0.3)

        # Use JS click to avoid overlays intercepting the click
        driver.execute_script("arguments[0].click();", remove_button)
        print("✅ Removed one expertise successfully.")
        
        
        # 5️⃣ Add new expertise (click the ones in the "Available Expertise" section)
        add_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'border') and contains(., '+')]"))
        )
        
        # Scroll into view for visibility
        driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        time.sleep(0.3)
        
        # Use JS click to avoid overlays intercepting the click
        driver.execute_script("arguments[0].click();", add_button)
        print("✅ Add new expertise")
        
        
        # Wait for Update button to become enabled (not disabled)
        update_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "button.bg-green-600"
            ))
        )
        # Click using JS (bypasses “element click intercepted”)
        driver.execute_script("arguments[0].click();", update_button)

        print("✅ About Our Business successfully updated!")
    except Exception as e:
        print(f"Error during editing about profile: {e}")
        raise