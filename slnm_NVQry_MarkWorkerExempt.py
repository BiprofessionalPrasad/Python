# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 13:20:01 2025

@author: 9387758
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date, timedelta
import os
import pyautogui, time
import pandas

def initialize():
    # Initialize Chrome driver instance
    #driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    # Navigate 
    #chrome_options = Options()
    #chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get('https://genco.nextviewcloud.com/Pages/P.aspx?tpl=Dashboard')
    time.sleep(3)
    driver.maximize_window() 
    return(driver)
    
def login():
    driver=initialize()
    #---------------------------
    # Login
    #---------------------------
    username=driver.find_element(By.ID,"txtUsername")
    password=driver.find_element(By.ID,"txtPassword")
    username.send_keys("pgaitond")
    password.send_keys("Export-hit-file-recent1!1")
    driver.find_element(By.NAME, "btnLogin").click()
    return(driver)
    time.sleep(3)
    
def mark_exempt():
    driver=login()
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(3)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Worker')
    time.sleep(3)
    Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[2]/select")).select_by_visible_text('_test_') 
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[2]/div/button").click()

    
    
        
def main():
    
    
if __name__ == '__main__':
    main()    