# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:05:59 2020

@author: pgaiton
"""

# import webbrowser

# webbrowser.open('https://getinline.dps.texas.gov/wa-services/txdpsservices/waweb/default.aspx?siteid=TXDPS141')  # Go to example.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ReemaPhoneNumber = '2144580154'
#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")
# lewisville
driver.get("https://getinline.dps.texas.gov/wa-services/txdpsservices/waweb/default.aspx?siteid=TXDPS141")
#driver.get("https://mail.google.com/")
#elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
#elem = driver.find_elements_by_xpath("//*[@type='next']"))
#print(elem.get_attribute("class"))
#driver.close()

#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08

# ---------------------------------------
# Select Language Screen 
language_button = driver.find_element_by_id('btnEnglish')

language_button.click()
# ---------------------------------------
# Phone number 
PhoneNumber_box = driver.find_element_by_id('txtPhone')

PhoneNumber_box.send_keys(ReemaPhoneNumber)

continue_button = driver.find_element_by_id('btnContinue')

continue_button.click()
# ---------------------------------------
# Do you have a Texas Driver License,Texas Permit or Texas ID Card?
LicenseQuestion_button=driver.find_element_by_id('btnHaveDLYes')

LicenseQuestion_button.click()
# ---------------------------------------
# Renew Replace Question
LicenseQuestion2_button=driver.find_element_by_id('btnsvcIDYes1')

LicenseQuestion2_button.click()
# ---------------------------------------
# Prepared Put in Line Question
Prepp_button=driver.find_element_by_id('btnYesGetInline')

Prepp_button.click()
# ---------------------------------------
# click on provided time slot
SubmitFinal_button=driver.find_element_by_id('btnSite1')

SubmitFinal_button.click()
