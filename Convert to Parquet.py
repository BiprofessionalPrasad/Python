# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:49:44 2024

@author: 9387758
"""

import csv
import pandas as pd
import os

os.chdir(r"C:\Import_Export")

df = pd.read_csv('All.csv',skipfooter=1)
df.columns
#--------- cleanup
df = df.fillna(0)

df.Supervisor.unique()

df = df.drop(df[df.Supervisor=='Undefined'].index)
df = df.drop(df[df.Supervisor=='VAZQUEZ, MAYRA'].index)


#----------- transform
df.dtypes

df['From Date']=pd.to_datetime(df['From Date'])#, format='%d%b%Y')
df['To Date']=pd.to_datetime(df['To Date'])#, format='%d%b%Y')
df['E360 Productivity']=pd.to_numeric(df['E360 Productivity'], errors='coerce')
df['E360 Effectiveness']=pd.to_numeric(df['E360 Effectiveness'], errors='coerce')
df['Units']=pd.to_numeric(df['Units'], errors='coerce')
df['UPH']=pd.to_numeric(df['UPH'], errors='coerce')



#------------ load/write to Parquet
df.to_parquet("All.parquet")

