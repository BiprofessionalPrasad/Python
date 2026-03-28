# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:40:18 2024

@author: Prasad Gaitonde
@Objective: WebpageAutomation Run Labor Summary query between dates provided, export, build 7 files.
@NextStep: Run combine csv.py to create All.csv. 
"""

#pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import date, timedelta
import os
import pandas as pd
import datetime

def clean_downloads():
    # Clean Downloads folder
   os.chdir("C:/Users/9387758/Downloads")
   for f in os.listdir("."):
       if not f.endswith(".csv"):
           continue
       else:
           os.remove(os.path.join("", f))
           
def remove_file1_thru_file7():           
   try:
       os.remove("c:/Import_Export/file1.csv")
       os.remove("c:/Import_Export/file2.csv")
       os.remove("c:/Import_Export/file3.csv")
       os.remove("c:/Import_Export/file4.csv")
       os.remove("c:/Import_Export/file5.csv")
       os.remove("c:/Import_Export/file6.csv")
       os.remove("c:/Import_Export/file7.csv")
   except OSError:
       pass

def rename_file1_thru_file7():
    try:
        os.rename("c:/Users/9387758/Downloads/excel.csv", "c:/Import_Export/file1.csv")
        os.rename("c:/Users/9387758/Downloads/excel (1).csv", "c:/Import_Export/file2.csv")
        os.rename("c:/Users/9387758/Downloads/excel (2).csv", "c:/Import_Export/file3.csv")
        os.rename("c:/Users/9387758/Downloads/excel (3).csv", "c:/Import_Export/file4.csv")
        os.rename("c:/Users/9387758/Downloads/excel (4).csv", "c:/Import_Export/file5.csv")
        os.rename("c:/Users/9387758/Downloads/excel (5).csv", "c:/Import_Export/file6.csv")
        os.rename("c:/Users/9387758/Downloads/excel (6).csv", "c:/Import_Export/file7.csv")
    except OSError:
        pass

def generate_date_list():
    # end_date = (date.today()-timedelta(days=2)).strftime("%m/%d/%y")
    # start_date = (date.today()-timedelta(days=8)).strftime("%m/%d/%y")
    end_date=datetime.date(2025, 4, 5).strftime("%m/%d/%y")
    start_date=datetime.date(2025, 3, 30).strftime("%m/%d/%y")
    date_list=pd.date_range(start_date,end_date).to_list()
    #return(date_list)
    print("Starting date: "+start_date+" Ending Date: "+end_date)
    dates=[]
    for date1 in date_list:
        dates.append(date1.strftime("%m/%d/%y"))
    print(dates)
    return(dates)
    
def main():
    # Initialize Chrome driver instance
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    # Clean Downloads folder
    clean_downloads()
    # Delete existing files
    remove_file1_thru_file7()
    # Generate date range list
    date_list=generate_date_list()
    
    # Navigate 
    driver.get('https://genco.nextviewcloud.com/Pages/P.aspx?tpl=Dashboard')
    time.sleep(3)
    driver.maximize_window() 
        
    #---------------------------
    # Login
    #---------------------------
    username=driver.find_element(By.ID,"txtUsername")
    password=driver.find_element(By.ID,"txtPassword")
    username.send_keys("pgaitond")
    password.send_keys("Export-hit-file-recent1!")
    driver.find_element(By.NAME, "btnLogin").click()
    time.sleep(3)
    # Run Labor Summary Query
    search_tab=driver.find_element(By.LINK_TEXT,"Search")
    search_tab.click()
    time.sleep(3)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select"))
    dropdown_select.select_by_visible_text('Labor Summary')
    time.sleep(3)
    dropdown_select=Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select"))
    dropdown_select.select_by_visible_text('Prasad Data Dump')
    time.sleep(3)
    
    # Loop thru Dates
    for date1 in date_list:
        print(date1)
        datepicker_link=driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date")
        datepicker_link.clear()
        datepicker_link.send_keys(date1)
        time.sleep(5)
        execute_link=driver.find_element(By.XPATH, '//button[text()="Execute"]')
        execute_link.click()
        time.sleep(60)
        exportcsv_link=driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel")
        exportcsv_link.click()
        time.sleep(10)
        
    
    # Close the driver when done
    driver.quit()
    # Rename csvs
    rename_file1_thru_file7()    
    # open folder
    os.startfile('C:/Import_Export/')
    print("please run the Combine CSVs python script")
    
    '''
    import time
    import datetime
    import pandas as pd
    from datetime import date, timedelta
    
    end_date = (date.today() - timedelta(days=1)).strftime("%m/%d/%y")
    start_date = (date.today() - timedelta(days=7)).strftime("%m/%d/%y")
    
    #print(start_date," ",end_date)
    
    
    date_list = pd.date_range(start_date, end_date).tolist()
    
    #dates=['11/10/2024','11/11/2024','11/12/2024','11/13/2024','11/14/2024','11/15/2024','11/16/2024']
    
    for date1 in date_list:
        print(date1)
        #dates.remove(date1)
        date_list
        time.sleep(1)
        
        '''
        
if __name__ == '__main__':
    main()