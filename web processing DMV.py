# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:05:59 2020

@author: pgaiton
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ReemaPhoneNumber = '2144359868'
PrasadPhoneNumber = '2144580154'
GooglePhoneNumber = '4085073343'

driver1 = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")
driver2 = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")
driver3 = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")
# ===================================================
# lewisville
driver1.get("https://getinline.dps.texas.gov/wa-services/txdpsservices/waweb/default.aspx?siteid=TXDPS141")

#driver1.get("https://mail.google.com/")
#elem = driver1.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
#elem = driver1.find_elements_by_xpath("//*[@type='next']"))
#print(elem.get_attribute("class"))
#driver1.close()

#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08

# ---------------------------------------
# Select Language Screen 
language_button1 = driver1.find_element_by_id('btnEnglish')
language_button1.click()

# ===================================================
# Carrollton
driver2.get("https://getinline.dps.texas.gov/wa-services/txdpsservices/waweb/default.aspx?siteid=TXDPS108")

# ---------------------------------------
# Select Language Screen 
language_button2 = driver2.find_element_by_id('btnEnglish')
language_button2.click()

# ===================================================
# Dallas Mega Center
driver3.get("https://getinline.dps.texas.gov/wa-services/txdpsservices/waweb/default.aspx?siteid=TXDPS110")

# ---------------------------------------
# Select Language Screen 
language_button3 = driver3.find_element_by_id('btnEnglish')
language_button3.click()

# ---------------------------------------
# Phone number 
PhoneNumber_box1 = driver1.find_element_by_id('txtPhone')
PhoneNumber_box1.send_keys(ReemaPhoneNumber)
continue_button1 = driver1.find_element_by_id('btnContinue')
continue_button1.click()
# ---------------------------------------
# Phone number 
PhoneNumber_box2 = driver2.find_element_by_id('txtPhone')
PhoneNumber_box2.send_keys(PrasadPhoneNumber)
continue_button2 = driver2.find_element_by_id('btnContinue')
continue_button2.click()
# ---------------------------------------
# Phone number 
PhoneNumber_box3 = driver3.find_element_by_id('txtPhone')
PhoneNumber_box3.send_keys(GooglePhoneNumber)
continue_button3 = driver3.find_element_by_id('btnContinue')
continue_button3.click()

# ---------------------------------------
# Do you have a Texas driver1 License,Texas Permit or Texas ID Card?
LicenseQuestion_button1=driver1.find_element_by_id('btnHaveDLYes')
LicenseQuestion_button1.click()
# ---------------------------------------
# Do you have a Texas driver1 License,Texas Permit or Texas ID Card?
LicenseQuestion_button2=driver2.find_element_by_id('btnHaveDLYes')
LicenseQuestion_button2.click()
# ---------------------------------------
# Do you have a Texas driver1 License,Texas Permit or Texas ID Card?
LicenseQuestion_button3=driver3.find_element_by_id('btnHaveDLYes')
LicenseQuestion_button3.click()

# ---------------------------------------
# Renew Replace Question
LicenseQuestion2_button1=driver1.find_element_by_id('btnsvcIDYes1')
LicenseQuestion2_button1.click()
# ---------------------------------------
# Renew Replace Question
LicenseQuestion2_button2=driver2.find_element_by_id('btnsvcIDYes1')
LicenseQuestion2_button2.click()
# ---------------------------------------
# Renew Replace Question
LicenseQuestion2_button3=driver3.find_element_by_id('btnsvcIDYes1')
LicenseQuestion2_button3.click()

# ---------------------------------------
# Prepared Put in Line Question
Prepp_button1=driver1.find_element_by_id('btnYesGetInline')
Prepp_button1.click()
# ---------------------------------------
# Prepared Put in Line Question
Prepp_button2=driver2.find_element_by_id('btnYesGetInline')
Prepp_button2.click()
# ---------------------------------------
# Prepared Put in Line Question
Prepp_button3=driver3.find_element_by_id('btnYesGetInline')
Prepp_button3.click()