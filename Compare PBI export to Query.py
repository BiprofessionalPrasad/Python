# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:52:56 2024

@author: 9387758
"""

# program to import csv from query (April) vs power bi (Export)
# compare and contrast

import pandas as pd
import os

os.chdir(r"C:\Temp\Comparison")
#file='Auction Picklist 10.22.24 7AM.xlsx'
file='MDMHOLD WIP 20241022.xlsx'
df_query = pd.read_excel(file,skipfooter=0)
df_PBI = pd.read_excel('MDM Lock MDMHOLD WIP.xlsx',header=0)

df_query.dtypes
df_PBI.dtypes 

#df_query['piece_identifier'] = df_query['piece_identifier'].astype(str)

df_PBI = df_PBI.rename(columns={'DTLNUM': 'dtlnum'})#, 'STORAGE_LOCATION': 'storage_location', 'CASE_IDENTIFIER': 'case_identifier', 'LOAD': 'load'})

'''comparisons
A) #of rows
B) IMEI exists in one vs another
C) check stoloc for matching IMEIs
D) check case id for matching IMEIs
E) check load for matching IMEIs
'''
# ---- A) #of rows
len_df_query=len(df_query)
len_PBI_query=len(df_PBI)
#-- 370 vs 376

# ----- B) IMEI exists in one vs another
merged_df=pd.merge(df_query, df_PBI, how ='left', on ='dtlnum')
IMEI_missingfrom_PBI=merged_df[merged_df['RCVDTE'].isnull()]  # 0 records
IMEI_missingfrom_PBI_length=len(IMEI_missingfrom_PBI)
100*IMEI_missingfrom_PBI_length/len_df_query #0%

merged_df=pd.merge(df_query, df_PBI, how ='right', on ='dtlnum')
IMEI_missingfrom_Query=merged_df[merged_df['rcvdte'].isnull()]  # 8110 records
IMEI_missingfrom_Query_length=len(IMEI_missingfrom_Query)
100*IMEI_missingfrom_Query_length/len_df_query #1.6%

# ----- C) check rcvdte for matching IMEIs
# ----- D) check trknum for matching IMEIs
# ----- E-I) check make, model, prtnum, mdmlock, stoloc for matching IMEIs

merged_df=pd.merge(df_query, df_PBI, how ='inner', on ='dtlnum')
merged_df.to_excel("output.xlsx")

#rcvdte_mismatch = merged_df[merged_df['rcvdte']!=merged_df['RCVDTE']] #0 records


#100*len(Stolock_mismatch)/len_df_query #6.5%
