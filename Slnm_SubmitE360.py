# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:38:34 2025
submit E360
-run query
-open website
-submit
@author: 9387758

DOES NOT WORK.
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
    password.send_keys("Enjoy-week-father-this2{1")
    driver.find_element(By.NAME, "btnLogin").click()
    return(driver)
    time.sleep(3)

def clean_downloads():
    # Clean Downloads folder
   os.chdir("C:/Users/9387758/Downloads")
   for f in os.listdir("."):
       if not f.endswith(".csv"):
           continue
       else:
           os.remove(os.path.join("", f))
           
def run_lastweek_labsum(formatted_lastsunday,formatted_lastsaturday):
    driver=login()
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(3)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select"))
    dropdown_select.select_by_visible_text('Labor Summary')
    time.sleep(3)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select"))
    dropdown_select.select_by_visible_text('Prasad E360 Weekly Labor Data Submission Form')
    time.sleep(3)
    to=driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[4]/div[5]/input")
    to.clear()
    to.send_keys(formatted_lastsunday)    
    from1=driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[5]/div[5]/input")
    from1.clear()
    from1.send_keys(formatted_lastsaturday)
    execute_link=driver.find_element(By.XPATH, '//button[text()="Execute"]')
    execute_link.click()
    time.sleep(120)
    # Export to Excel
    exportcsv_link=driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel")
    exportcsv_link.click()
    time.sleep(5)

def init_E360():
    # Initialize Chrome driver instance
    #driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    # Navigate 
    #chrome_options = Options()
    #chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=E8hFuebc-EGEV1oSwv4Vv_jA5ZdTvZlIqngh3TaodEJUQVRUWEpXMjFKOENBTDA2UVQ5VFJZSjkwNy4u')
    time.sleep(3)
    driver.maximize_window() 
    return(driver)
    time.sleep(3)

def login_E360():
    driver=init_E360()
    signin=driver.find_element(By.XPATH,"/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
    signin.send_keys('prasad.gaitonde@fedex.com')
    execute_link=driver.find_element(By.XPATH,"/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")
    execute_link.click()
    time.sleep(10)
    uname=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input")
    uname.send_keys('9387758')
    pwd=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input")
    pwd.send_keys('Enjoy-week-father-this2{')
    execute_link=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input")
    execute_link.click()
    return(driver)
    time.sleep(3)
        
def submit_E360(formatted_lastsaturday,earned_hrs,actual_hrs,Direct_hrs,PaidDirect_hrs):
    driver=login_E360()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div[1]/div[2]/div/div[3]/button/div").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/input").send_keys(formatted_lastsaturday)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[3]/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[4]/div/label/span[1]/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/span[1]").click()
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[14]/span[2]/span").click()
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[3]/div/button[2]").click()
    
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/span/input").send_keys(earned_hrs)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input").send_keys(actual_hrs)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/span/input").send_keys(Direct_hrs)
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/span/input").send_keys(PaidDirect_hrs)
    
    driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[3]/span[1]/input").click()
    #--- SUBMIT BUTTON
    #driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[4]/div/button[2]").click()
    
    
def main():
    #---- dates 
    yesterday = date.today() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%m/%d/%Y")
    monday = date.today() - timedelta(date.today().weekday()) # monday
    lastsaturday = monday - timedelta(days=2)
    formatted_lastsaturday=lastsaturday.strftime("%m/%d/%Y")
    lastsunday = monday - timedelta(days=8)
    formatted_lastsunday = lastsunday.strftime("%m/%d/%Y")
    #---- delete csvs
    clean_downloads()
    #---- run LMS query, export
    run_lastweek_labsum(formatted_lastsunday,formatted_lastsaturday)
    file=r"C:/Users/9387758/Downloads/excel.csv"
    #----- import csv
    df = pandas.read_csv(file,skipfooter=1,thousands=",",engine='python')
    #---- calc column values
    df['Earned Time']=df['Earned Time'].astype(float)
    df['E360 On-Std Direct']=df['E360 On-Std Direct'].astype(float)
    df['E360 Non-Std Direct']=df['E360 Non-Std Direct'].astype(float)
    df['E360 NPT (Unplanned)']=df['E360 NPT (Unplanned)'].astype(float)
    df['E360 NPT (Planned)']=df['E360 NPT (Planned)'].astype(float)
    
    earned_hrs=df['Earned Time'][0]/60.0
    actual_hrs=df['E360 On-Std Direct'][0]/60.0
    Direct_hrs=(df['E360 On-Std Direct'][0]+df['E360 Non-Std Direct'][0])/60.0
    PaidDirect_hrs=(df['E360 NPT (Unplanned)'][0]+df['E360 NPT (Planned)'][0]+df['E360 On-Std Direct'][0]+df['E360 Non-Std Direct'][0])/60.0
    
    #----- Submit E360
    submit_E360(formatted_lastsaturday,earned_hrs,actual_hrs,Direct_hrs,PaidDirect_hrs)