# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:16:21 2024

@author: 9387758
"""

import pandas as pd
import os
import glob

# path = r"C:\Import_Export\file"
path=r"c:\Temp\wfr"
os.chdir(path)
results = pd.DataFrame()
total_len=0

# headers1=['Repair Action ID','Transaction Date','Repair Number','Flow Section','Piece Identifier','Repair Group','Repair Step','Next Repair Step','Item Number','Item Client ID','Warehouse ID','Area','Storage Location','Device Code','Step Begin Date','Old Date','Last Inserted By','Date Last Modified','Last Modified By','Repair Batch','Make','Model']

# for counter, current_file in enumerate(glob.glob("*.dat")):
for counter, current_file in enumerate(glob.glob("*.csv")):
    # namedf = pd.read_csv(current_file, header='infer',  sep="|") #header=None
    # namedf=pd.read_csv(current_file,names=headers1,header=None,sep=",")
    namedf=pd.read_csv(current_file,header=None,sep=",",skipfooter=0,engine='python')
    #print(namedf)
    # print(current_file, "            ", len(namedf.index),"          ",counter,"             ",total_len)
    total_len=total_len+len(namedf.index)
    results = pd.concat([results, namedf])

# drop empty columns
results.dropna(how='all', axis=1, inplace=True)

#convert type
# results['E360 Productivity']=results['E360 Productivity'].str.replace(',','',regex=False).astype(float)

#remove / filter
# results2=results.loc[results['E360 Productivity']>0]
# results3=results2.loc[results2[6]!='NEW-REPAIR']

#Sort
#results_sorted=results.sort_values(by=['Worker','From Date'])

#export to csv
results.to_csv('Combined.csv', index=False, sep=",") #header=0
#results_sorted.to_csv('Combined.csv', index=False, sep=",")