# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:46:20 2024

@author: 9387758
"""

import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service1 = Service(executable_path=r'C:\edgedriver_win64\msedgedriver.exe')
options1 = webdriver.EdgeOptions()
driver = webdriver.Edge()
driver.get("https://www.txdpsscheduler.com/")
time.sleep(10)
driver.quit()