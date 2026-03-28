# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:40:18 2024

@author: Prasad Gaitonde
@Objective: WebpageAutomation runs error report, exports to excel
 Then for each worker, it runs recompute on activity unit
@NextStep: check the export
"""

#pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date, timedelta
import os
import pandas as pd

def main():
    # Initialize Chrome driver instance
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    # Navigate 
    driver.get('https://genco.nextviewcloud.com/Pages/P.aspx?tpl=Dashboard')
    #time.sleep(10)
    #driver.maximize_window() 
    time.sleep(10)
    #yesterday = date.today() - timedelta(days=1)
    #formatted_yesterday = yesterday.strftime("%m/%d/%Y")    
    Activity='AWRE- CHECKOUT'
    # Clean Downloads folder
    os.chdir("C:/Users/9387758/Downloads")
    for f in os.listdir("."):
        if not f.endswith(".csv"):
            continue
        else:
            os.remove(os.path.join("", f))
            
    #--- dates logic
    dates=[]
    end_date = (date.today() - timedelta(days=1)).strftime("%m/%d/%y")
    start_date = (date.today() - timedelta(days=30)).strftime("%m/%d/%y")
    date_list = pd.date_range(start_date, end_date).tolist()
    dates=[]
    for date1 in date_list:
        dates.append(date1.strftime("%m/%d/%Y"))
    #---------------------------
    # Login
    #---------------------------
    username=driver.find_element(By.ID,"txtUsername")
    password=driver.find_element(By.ID,"txtPassword")
    username.send_keys("pgaitond")
    password.send_keys("Flood-kinder-halloween1!")
    driver.find_element(By.NAME, "btnLogin").click()
    time.sleep(10)
   #-------------------------------
    # Run Activity Unit
    #-------------------------------
    search_tab=driver.find_element(By.LINK_TEXT,"Search")
    search_tab.click()
    time.sleep(10)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select"))
    dropdown_select.select_by_visible_text('Activity Unit')
    time.sleep(10)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select"))
    dropdown_select.select_by_visible_text('PG extract daily checkout')
    time.sleep(10)
    Act_Name=driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[4]/div[2]/div[3]/div[5]/input")
    Act_Name.clear()
    Act_Name.send_keys(Activity)        
    for date1 in dates:
        datepicker_link=driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date")
        datepicker_link.clear()
        datepicker_link.send_keys(date1)
        execute_link=driver.find_element(By.XPATH, '//button[text()="Execute"]')
        execute_link.click()
        time.sleep(20)
        # Export to Excel
        exportcsv_link=driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel")
        exportcsv_link.click()
        time.sleep(10)
    
    # Close the driver when done
    driver.quit()
    
    os.startfile('C:/Users/9387758/Downloads')

    #Clear all Variables
    for name in list(globals()):
        if not name.startswith('__'):
            del globals()[name]

if __name__ == '__main__':
    main()