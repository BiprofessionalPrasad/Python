# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:40:18 2024

@author: Prasad Gaitonde
@Objective: WebpageAutomation finds Tms who didnt use kiosk
 or high Idle/NPT time.
@NextStep: Email export to Mgrs, Sups.
"""

#pip install webdriver-manager


import win32com.client as win32
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import date, timedelta
import os
import pandas as pd


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
    password.send_keys("Flood-kinder-halloween1!1")
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

def kiosk_notused(formatted_yesterday):
    driver=login(formatted_yesterday)
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(5)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Labor Summary')
    time.sleep(5)
    Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[2]/select")).select_by_visible_text('Prasad Kiosk not used teammates')
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/div/button").click()
    time.sleep(20)
    driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel").click()
    time.sleep(5)

def training(formatted_yesterday):
    driver=login(formatted_yesterday)
    driver.find_element(By.LINK_TEXT,"Search").click()
    time.sleep(5)
    Select(driver.find_element(By.CLASS_NAME,"nv-querybuilder-querytarget-select")).select_by_visible_text('Labor Summary')
    time.sleep(5)
    Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[2]/select")).select_by_visible_text('prasad trainings last week')
    driver.find_element(By.XPATH,"/html/body/div[5]/div/form/div[2]/div/button").click()
    time.sleep(20)
    driver.find_element(By.CLASS_NAME, "nv-toolbar-button.nv-icon-excel").click()
    time.sleep(5)
    
def convert_min_to_hrs(df):
    columns=['Idle Time','E360 NPT (Unplanned)','E360 NPT (Planned)']
    for column1 in columns:
        print(column1)
        df[column1]=df[column1].fillna(0)
        df[column1]=df[column1].astype(str)
        df[column1]=df[column1].str.replace(',','')
        df[column1]=pd.to_numeric(df[column1])
        df[column1]=df[column1].div(60)

def send_email(subject, body, recipient,cc):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = subject
    mail.HTMLBody= body
    mail.To = recipient
    mail.cc=cc
    attachment1 =  r'C:/Import_Export/IdleNPT.csv'
    mail.Attachments.Add(attachment1)
    #mail.Attachments.Add(attachment2)
    # mail.Display(True)
    mail.Send()
        
    
def main():
    yesterday = date.today() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%m/%d/%Y")    
    folder=r'C:/Users/9387758/Downloads'
    file=r'C:/Import_Export/IdleNPT.csv'
    #-------------------------------
    # Clean Downloads folder
    #-------------------------------
    clean_downloads()    
    #-------------------------------
    # Run Kiosk not used
    # Run trainings last week
    # export
    #-------------------------------
    kiosk_notused(formatted_yesterday)     
    training(formatted_yesterday)   
    try:
        os.rename('excel.csv',file)       
    except:
        os.replace('excel.csv',file)       
    #os.startfile(folder)
    #-------------------------------
    # Import Kiosk not used & Process csv
    #-------------------------------
    df = pd.read_csv(file,skipfooter=1,engine='python')
    convert_min_to_hrs(df)
    #-------------------------------
    # Calc Total, sort, filter & export
    #-------------------------------
    df['Total']=df['Idle Time']+df['E360 NPT (Unplanned)']+df['E360 NPT (Planned)']
    selected_columns=['From Date','To Date','Supervisor','Worker','Total']
    df2=df[selected_columns].copy()
    df2=df2.sort_values(by='Total',ascending=False)
    df2=df2[df2['Total']>=(40/6)]
    df2.to_csv(file, mode='w', index=False)
    #-------------------------------
    # Email
    #-------------------------------
    subject="Weekly Idle NPT Hours" 
    body="<p>Please see atached&nbsp;</p>"
    to="prasad.gaitonde@fedex.com"
    cc=""
    send_email(subject, body, to, cc)
        
if __name__ == '__main__':
    main()