# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import pandas as pd
import numpy as np
import os
import pyodbc 

os.chdir(r"C:\Raw data")

df = pd.read_csv('all.csv',header=0)
df = df[:-1]


df_shiftstartup=df[df['Activity']=='AWRE - Shift Startup']

df_shiftstartup[df_shiftstartup['Actual Time']>20]