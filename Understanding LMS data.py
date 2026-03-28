# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:24:53 2024

@author: 9387758
"""

import pandas as pd
import os

os.chdir(r'C:\Import_Export')

## by Activity
df_PastWeekLMSdataByActivity=pd.read_csv('PastWeekLMSdataByActivity.csv')
df_PastWeekLMSdataByActivity=df_PastWeekLMSdataByActivity.dropna(subset='Activity')

# print(df.dtypes)
df2_PastWeekLMSdataByActivity=df_PastWeekLMSdataByActivity[(df_PastWeekLMSdataByActivity['Earned Time']>0) & (df_PastWeekLMSdataByActivity['E360 Productivity']<101)].sort_values(by='Actual Time',ascending=False)

#print out
out_PastWeekLMSdataByActivity=df2_PastWeekLMSdataByActivity[df2_PastWeekLMSdataByActivity['Activity']=='PRE-SORT AT THE TRACK - RECEIVING'].iloc[:,:6]
out2_PastWeekLMSdataByActivity=df2_PastWeekLMSdataByActivity[df2_PastWeekLMSdataByActivity['Activity']=='DTB - PUTAWAY TO L-RACK'].iloc[:,:6]
out3_PastWeekLMSdataByActivity=df2_PastWeekLMSdataByActivity[df2_PastWeekLMSdataByActivity['Activity']=='CAROUSEL - PUTAWAY']


## by Teammate
df_PastWeekLMSdataByTM=pd.read_csv('PastWeekLMSdataByTM.csv',usecols=['From Date','To Date','Worker','E360 Utilization','E360 Direct Time','E360 NPT (Planned)','E360 NPT (Unplanned)'])
df_PastWeekLMSdataByTM.fillna(value=0,inplace=True)
df_PastWeekLMSdataByTM['Total NPT']=df_PastWeekLMSdataByTM['E360 NPT (Planned)']+df_PastWeekLMSdataByTM['E360 NPT (Unplanned)']

df_PastWeekLMSdataByTM=df_PastWeekLMSdataByTM.dropna(subset='Worker')
#print(df_PastWeekLMSdataByTM.dtypes)
df_PastWeekLMSdataByTM=df_PastWeekLMSdataByTM.sort_values(by='Worker')

df2_PastWeekLMSdataByTM=df_PastWeekLMSdataByTM[(df_PastWeekLMSdataByTM['E360 Utilization']>0) & (df_PastWeekLMSdataByTM['E360 Productivity']<101)].sort_values(by='Actual Time',ascending=False)

df2_PastWeekLMSdataByTM.to_csv(r'C:\Users\9387758\Downloads\PastWeekLMSdataByTM.csv', sep=',', encoding='utf-8')
