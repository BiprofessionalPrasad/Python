# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:40:18 2024

@author: Prasad Gaitonde
@Objective: WebpageAutomation Run Activity Unit query for yesterday, and recompute errors.
@NextStep: Rerun for day before
"""

#pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
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
    
def login(formatted_yesterday):
    driver=initialize()
    #---------------------------
    # Login
    #---------------------------
    username=driver.find_element(By.ID,"txtUsername")
    password=driver.find_element(By.ID,"txtPassword")
    username.send_keys("pgaitond")
    password.send_keys("Export-hit-file-recent1!")
    driver.find_element(By.NAME, "btnLogin").click()
    return(driver)
    time.sleep(3)
    
    
def run_error_report(formatted_yesterday):
    driver=login(formatted_yesterday)
    driver.find_element(By.XPATH,"/html/body/div[2]/ul/li[4]/a/span").click() # Analytics Tab
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[5]/div/div[3]/div/table/tbody/tr[2]/td/span[1]/a").click() # Reports
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[5]/div/div[4]/div/table/tbody/tr[1]/td[2]/ul/li[5]/span[2]/a").click() #error summary report
    time.sleep(3)
    report_date=driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[3]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/input")
    report_date.clear()
    report_date.send_keys(formatted_yesterday)
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[5]/button[1]").click() # run report
    time.sleep(60)
    driver.find_element(By.XPATH,"/html/body/form/div[5]/div[4]/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr/td/div/img").click() #export
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div").click() #File Format
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/span").click() #excel format
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/nobr/a").click() #final export
    time.sleep(3)
    #os.startfile('C:/Users/9387758/Downloads/CrystalReportViewer.xls')
    
def recompute_day(formatted_yesterday):
    driver=login(formatted_yesterday)
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(5)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select"))
    dropdown_select.select_by_visible_text('Activity Unit')
    time.sleep(5)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select"))
    dropdown_select.select_by_visible_text('Prasad Errors in Activity')
    time.sleep(5)
    datepicker_link=driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date")
    datepicker_link.clear()
    datepicker_link.send_keys(formatted_yesterday)
    time.sleep(3)
    execute_link=driver.find_element(By.XPATH, '//button[text()="Execute"]')
    execute_link.click()
    time.sleep(50)
    # Export to Excel
    exportcsv_link=driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel")
    exportcsv_link.click()
    time.sleep(5)
    # Recompute
    recompute_element=driver.find_element(By.XPATH,"/html/body/div[4]/div/ul/li[21]/a")
    recompute_element.click()   
    time.sleep(5)
    button_ok=driver.find_element(By.CLASS_NAME,"ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")
    button_ok.click()
    time.sleep(5)

def recompute_allactivities_day(formatted_yesterday):
    driver=login(formatted_yesterday)
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(5)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select"))
    dropdown_select.select_by_visible_text('Activity Unit')
    time.sleep(5)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select"))
    dropdown_select.select_by_visible_text('Prasad all activity errors yesterday')
    time.sleep(5)
    datepicker_link=driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date")
    datepicker_link.clear()
    datepicker_link.send_keys(formatted_yesterday)
    time.sleep(3)
    execute_link=driver.find_element(By.XPATH, '//button[text()="Execute"]')
    execute_link.click()
    time.sleep(50)
    # Export to Excel
    exportcsv_link=driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel")
    exportcsv_link.click()
    time.sleep(5)
    # Recompute
    recompute_element=driver.find_element(By.XPATH,"/html/body/div[4]/div/ul/li[21]/a")
    recompute_element.click()   
    time.sleep(5)
    button_ok=driver.find_element(By.CLASS_NAME,"ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")
    button_ok.click()
    time.sleep(60)

def add_alias_workers(formatted_yesterday):
    driver=login(formatted_yesterday)
    workers=['ASHMA-UPADHYAY']
    for worker in workers:
        print(worker)
        # ---- add alias (manual work required) --- #
        if worker.find('-')!=0:
            if worker.split('-')[1].isnumeric(): 
                first_name=worker.split('-')[1] 
                last_name=worker.split('-')[2] 
            else:
                first_name=worker.split('-')[0] 
                last_name=worker.split('-')[1] 
        else:
            last_name=worker.split(' ')[1]
        driver.find_element(By.LINK_TEXT,"Search").click()
        time.sleep(2)
        Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Worker')
        time.sleep(2)
        Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[2]/select")).select_by_visible_text('Prasad Find Worker') 
        driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[3]/div[5]/input").clear() 
        driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[4]/div[5]/input").clear() 
        driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[3]/div[5]/input").send_keys(first_name) #first name
        driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[4]/div[5]/input").send_keys(last_name) 
        driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[2]/div/button").click()
        time.sleep(6)
        #Open worker
        pyautogui.click(x=306,y=730,button='left')
        #pyautogui.click(x=266,y=587,button='left') # monitor
        # pyautogui.click(x=353,y=730,button='left') # laptop new
        # pyautogui.click(x=339,y=734,button='left') # laptop old
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div/ul/li[3]/a").click() #Edit
        # get current login value
        #print(driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[3]/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input").text)
        #login_field_text=login_field.text
        #login_field_attribute_value=login_field('value')
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/input").clear() #clear old aliases
        driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/input").send_keys(worker) #add alias
        driver.find_element(By.XPATH, "/html/body/div[5]/div/form/div[4]/button[1]").click()
        time.sleep(1)
    
def recompute_worker(formatted_yesterday):   
    driver=login(formatted_yesterday)
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(3)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Activity Unit')
    time.sleep(5)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select")).select_by_visible_text('Prasad Recompute Query2') #dropdown selec
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date").clear()
    # driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[3]/div[5]/input").clear()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date").send_keys(formatted_yesterday)
    # driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[2]/div[3]/div[5]/input").send_keys(worker)
    driver.find_element(By.XPATH, '//button[text()="Execute"]').click() #execute_link
    time.sleep(60)
    recompute_element=driver.find_element(By.XPATH,"/html/body/div[4]/div/ul/li[21]/a")
    recompute_element.click()   
    time.sleep(5)
    button_ok=driver.find_element(By.XPATH,"/html/body/div[10]/div[11]/div/button[1]")
    button_ok.click()
    time.sleep(5)

   
    
# disabled ---- 
def recompute_week():
    end_date = date.today() - timedelta(days=1)
    start_date = date.today() - timedelta(days=7)
    date_range=pandas.date_range(start_date,end_date).to_list()
    for date1 in date_range:
        print("processing Date:  ",date1)
        #recompute_day(date1.strftime("%m/%d/%y"))
        #recompute_allactivities_day(date1.strftime("%m/%d/%y"))
        
        
def main():
    yesterday = date.today() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%m/%d/%Y")
    # ------------   Run the error report
    # run_error_report(formatted_yesterday)     #time.sleep(10)
    # run_error_report("2/16/2024")
    # ------------ Add Alias+Recompute Workers
    add_alias_workers(formatted_yesterday)
    # ------------Recompute worker
    # recompute_worker(formatted_yesterday)    


    # ------------ not used begin
    # ------------   Recompute for the yesterday
    # recompute_day(formatted_yesterday)     
    # ------------ Recompute all activities yesterday
    #recompute_allactivities_day(formatted_yesterday)
    
    # Close the driver when done
    #driver.quit()
    # os.startfile('C:/Users/9387758/Downloads')
    
    #Clear all Variables
    #for name in list(globals()):
    #    if not name.startswith('__'):
    #        del globals()[name]
    # ------------ not used end
    
if __name__ == '__main__':
    main()