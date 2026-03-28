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

#ReemaPhoneNumber = '2144359868'
#driver = webdriver.Chrome()
for i in range(10):
driver = webdriver.Chrome(executable_path=r"C:\Users\pgaiton\AppData\Local\Continuum\anaconda3\DLLs\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=42pfAhm4JQQ")
play_button=driver.find_element_by_xpath('//button[@aria-label="Play"]')
play_button.click()
driver.minimize_window()


#play_button=driver.find_element_by_class_name('ytp-large-play-button ytp-button')

#driver.get("https://mail.google.com/")
#elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
#elem = driver.find_elements_by_xpath("//*[@type='next']"))
#print(elem.get_attribute("class"))
#driver.close()

#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
