# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:46:20 2024

@author: 9387758
"""

import time
import configparser
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, timedelta
import os
import pandas as pd

def clear_and_fill(driver, element_id, text):
    try:
        # Wait for element to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        
        # Click on the element to ensure it's focused
        element.click()
        # time.sleep(0.5)
        
        # Clear the field using Ctrl+A and Delete
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        # time.sleep(0.3)
        
        # Clear using JavaScript as fallback (for Vue.js/React components)
        driver.execute_script(f"document.getElementById('{element_id}').value = '';")
        # time.sleep(0.3)
        
        # Now fill in the text
        element.send_keys(text)
        # time.sleep(0.5)
        
        # Trigger change event for framework detection
        driver.execute_script(f"""
            var element = document.getElementById('{element_id}');
            element.dispatchEvent(new Event('input', {{ bubbles: true }}));
            element.dispatchEvent(new Event('change', {{ bubbles: true }}));
        """)
        # time.sleep(0.5)
        
        # Verify the text was entered
        actual_value = driver.execute_script(f"return document.getElementById('{element_id}').value;")
        if actual_value != text:
            print(f"Warning: Expected '{text}' but got '{actual_value}' in field {element_id}")
    except Exception as e:
        print(f"Error filling element {element_id}: {str(e)}")
        raise

def load_config():
    config = configparser.ConfigParser()
    config.read('config.txt')
    return config['DEFAULT']

# Load configuration
config = load_config()

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get("https://www.txdpsscheduler.com/")

# Wait for the English button to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".v-btn__content"))
)
# Click on the English button
driver.find_element(By.CSS_SELECTOR, ".v-btn__content").click()
time.sleep(2)

# Fill first name
clear_and_fill(driver, "input-55", config.get('first_name', ''))

# Fill last name
clear_and_fill(driver, "input-58", config.get('last_name', ''))

clear_and_fill(driver, "dob", config.get('date_of_birth', ''))

clear_and_fill(driver, "last4Ssn", config.get('last_4_ssn', ''))

clear_and_fill(driver,"cellPhone", config.get('cell_phone', ''))

# Wait a moment for all fields to be processed
time.sleep(2)

# Click Log On button - wait for it to become enabled first
try:
    # Wait for the button to be clickable (no longer disabled)
    logon_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log On')]"))
    )
    logon_button.click()
    print("Log On button clicked successfully")
except Exception as e:
    print(f"Button still disabled or not clickable: {str(e)}")
    # Try JavaScript click as fallback
    try:
        logon_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log On')]")
        driver.execute_script("arguments[0].click();", logon_button)
        print("Log On button clicked using JavaScript")
    except Exception as e2:
        print(f"Failed to click Log On button: {str(e2)}")

# Click continue or next button
# Find the button, e.g., by text or ID
# driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()

# Add more steps here: select service type, location, date, etc.
# For example:
# Select service
# select = Select(driver.find_element(By.ID, "service-select"))
# select.select_by_visible_text("Driver License")

# Select location
# select = Select(driver.find_element(By.ID, "location-select"))
# select.select_by_visible_text("Dallas")

# Select date/time
# ... add code for date picker

# Finally submit
# driver.find_element(By.ID, "submit-button").click()

# Wait or handle confirmation
time.sleep(5)  # Adjust as needed

# driver.quit()  # Uncomment when done