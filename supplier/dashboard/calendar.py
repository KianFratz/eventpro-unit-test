from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
def calendar_test(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://localhost:5173/dashboard")
        # CLICK calendar tab
        calendar_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Calendar']")))
        calendar_tab.click()
        print("✅ Calendar tab clicked successfully.")
        print("✅ Successfully navigated to Calendar tab.")
        # prev button
        prev_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-prev-button")))
        prev_btn.click()
        print("✅ Clicking prev button to navigate to the previous month, successful.")
        # next button
        next_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-next-button")))
        next_btn.click()
        print("✅ Clicking next button to navigate to the next month, successful.")
        print("✅ Calendar testing successful")
    except TimeoutException:
        print(f"Error during testing calendar: {e}")
        raise