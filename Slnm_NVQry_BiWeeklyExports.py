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

def main():
    # Initialize Chrome driver instance
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    # Clean Downloads folder
    os.chdir("C:/Users/9387758/Downloads")
    for f in os.listdir("."):
        if not f.endswith(".csv"):
            continue
        else:
            os.remove(os.path.join("", f))
    
    try:
        os.remove("C:/Import_Export/file1.csv")
        os.remove("C:/Import_Export/file2.csv")
        os.remove("C:/Import_Export/file3.csv")
        os.remove("C:/Import_Export/file4.csv")
        os.remove("C:/Import_Export/file5.csv")
        os.remove("C:/Import_Export/file6.csv")
        os.remove("C:/Import_Export/file7.csv")
        os.remove("C:/Import_Export/file8.csv")
        os.remove("C:/Import_Export/file9.csv")
        os.remove("C:/Import_Export/file10.csv")
        os.remove("C:/Import_Export/file11.csv")
        os.remove("C:/Import_Export/file12.csv")
        os.remove("C:/Import_Export/file13.csv")
        os.remove("C:/Import_Export/file14.csv")
    except OSError:
        pass
    
    # Navigate 
    driver.get('https://genco.nextviewcloud.com/Pages/P.aspx?tpl=Dashboard')
    time.sleep(10)
    driver.maximize_window() 
    time.sleep(10)
    
    #--- dates logic
    end_date = (date.today() - timedelta(days=1)).strftime("%m/%d/%y")
    start_date = (date.today() - timedelta(days=14)).strftime("%m/%d/%y")
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
    # Run Labor Summary Query
    driver.find_element(By.LINK_TEXT,"Search").click() #search_tab
    time.sleep(10)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Labor Summary')
    time.sleep(10)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-queryview-select")).select_by_visible_text('Prasad Data Dump') #dropdown_select
    time.sleep(10)
    
    # Loop thru Dates
    for date1 in dates:
        driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date").clear() #datepicker_link
        driver.find_element(By.CLASS_NAME, "nv-textbox.nv-small.nv-textbox-datepicker.hasDatepicker.nv-val-date").send_keys(date1)
        time.sleep(5)
        driver.find_element(By.XPATH, '//button[text()="Execute"]').click() #execute_link
        time.sleep(50)
        driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel").click() #exportcsv_link
        time.sleep(10)
        #dates.remove(date1)
        
    # Close the driver when done
    driver.quit()
    
    # Rename csvs
        
    os.rename('excel.csv','C:/Import_Export/file1.csv')
    os.rename('excel (1).csv','C:/Import_Export/file2.csv')
    os.rename('excel (2).csv','C:/Import_Export/file3.csv')
    os.rename('excel (3).csv','C:/Import_Export/file4.csv')
    os.rename('excel (4).csv','C:/Import_Export/file5.csv')
    os.rename('excel (5).csv','C:/Import_Export/file6.csv')
    os.rename('excel (6).csv','C:/Import_Export/file7.csv')
    os.rename('excel (7).csv','C:/Import_Export/file8.csv')
    os.rename('excel (8).csv','C:/Import_Export/file9.csv')
    os.rename('excel (9).csv','C:/Import_Export/file10.csv')
    os.rename('excel (10).csv','C:/Import_Export/file11.csv')
    os.rename('excel (11).csv','C:/Import_Export/file12.csv')
    os.rename('excel (12).csv','C:/Import_Export/file13.csv')
    os.rename('excel (13).csv','C:/Import_Export/file14.csv')
    
    os.startfile('C:/Import_Export/')
    
    
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