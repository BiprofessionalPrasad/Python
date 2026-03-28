# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyodbc 
import pandas as pd
import os
import time
from os import listdir
from os.path import isfile, join
import re

def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       if not (re.search('Maconomy Views',dirpath) or re.search('logfiles',dirpath) or re.search('Security',dirpath)):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
           
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=devdb1;'
                      'Database=InHouseReports;'
                      'Trusted_Connection=yes;')

path = r'''K:\Projects\Maconomy\Mac2p4p4\Scripts\testing123''' #test
#path = r'''K:\Projects\Maconomy\Mac2p4p4\Scripts\Scripts macproddb1''' #PROD
           
os.chdir(path)

datetime=time.strftime('%Y%m%d%H%M%S')
logpath=path+'\log_'+datetime
#logpath
os.mkdir(logpath)

cursor = conn.cursor()

#for python you need a query, can not just run a file.

for sqlscriptfullpath in absoluteFilePaths(path): 
    print(sqlscriptfullpath)
    #cursor.execute(sql)
#    conn.execute(sql)
