import csv
import pandas as pd
import numpy as np
import os
import pyodbc 
'''with open('intf5_STARPRD_WFR_ACTIVITY_DISPLAY_Sep-06-2023-14-58-12.csv',newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))'''
os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Python")
df1 = pd.read_csv('intf5_STARPRD_WFR_ACTIVITY_DISPLAY_Sep-06-2023-14-58-12.csv')
df2 = pd.read_csv('intf5_FedExSC_Carousel_Hourly_20231003170000.dat')
result=df2.head(10)
print(df1.info())
print(df2.info())
#print(result)