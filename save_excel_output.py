# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:05:43 2020

@author: pgaiton
"""

import pyodbc 
import pandas as pd
import os

path = 'K:/Projects/TSBS/Sean/output_files'
os.chdir(path)


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ftwdb2;'
                      'Database=InHouseReports;'
                      'Trusted_Connection=yes;')
#cursor = conn.cursor()
sql = "exec [InHouseReports].[dbo].[rpt_YearlybyWeek_ProductivityMaconomy_TSBS]"
#cursor.execute(sql)

data = pd.read_sql(sql,conn)

from pandas import ExcelWriter
writer = ExcelWriter(r'''K:\Projects\TSBS\Sean\output_files\Output_20200512.xlsx''')
data.to_excel(writer,'Details')
writer.save()




conn.close()
