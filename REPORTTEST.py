# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:52:21 2020

@author: pgaiton
"""
import os
#import pyodbc
import pandas as pd
from selenium import webdriver

path=r'''K:\Projects\Maconomy\Mac2p4p4\Requirements Documents'''
os.chdir(path)

#conn = pyodbc.connect('Driver={SQL Server};'
#                      'server=DEVDB2\REPORTTEST;'
#                      'database=LearningPlans;'
#                      'Trusted_Connection=Yes;')

#cursor = conn.cursor()

file=r'''2.4.4 Test Scripts Checklist'''; ext='.xlsx'; sheet=r'''SRS Report Testing'''
excelfile=pd.ExcelFile(file+ext)
dfExcel=pd.read_excel(excelfile,sheet,na_values=['NA'],skiprows=3,header=0,usecols=[0, 1])

dfExcel=dfExcel.astype('str')

driver = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")

#driver.get("http://ftwssrs1/Reports/Pages/Folder.aspx")
driver.get("http://ftwssrs1/Reportserver?%2fInHouse&rs:Command=ListChildren")
dfExcel=dfExcel.replace('Home','InHouseReports')

#Folder_Link = driver.find_element_by_link_text("InHouse")

row1 = dfExcel.iloc[0] 

#elems = driver.find_elements_by_xpath("//a[@href]")
#for elem in elems:
#    print(elem.get_attribute("href"))
    
# search box method
'''
Search_Box = driver.find_element_by_id("S_searchTextBoxID")
Search_Box.clear()
Search_Box.click()
Search_Box.send_keys(row1['SRS Report Name'])
#Search_Send = driver.find_element_by_id("S_searchButtonID")
Search_Box.send_keys(u'\ue007')
result = driver.find_elements_by_class_name('class="msrs-itemName"') 
result.find_element_by_xpath("./div/h3/a").click() #click its href
# driver.find_element_by_xpath('//div[@id="pagn"]/span[@class="pagnLink"]/a[text()="2"]')
'''

links = driver.find_elements_by_partial_link_text(row1['SRS Report Name'])
for link in links:
    print(link.get_attribute("href"))

driver.get(link.get_attribute("href"))

#href="http://ftwssrs1/Reports/Pages/Report.aspx?ItemPath=%2fInHouse%2fARWriteOffsByPartner&SelectedTabId=PropertiesTab&SelectedSubTabId=GenericPropertiesTab&Export=true"

for folder, report in row1.iterrows():
    print(folder, report)


elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))

