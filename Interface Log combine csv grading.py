#=================================
# Grading April 22 Data Join Interf Log
#=================================
# begin
from os import listdir
from os.path import isfile, join
import pandas as pd
import os

mypath=r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Nextview\Data Validation\Grading\May1 Interface Files"
os.chdir(mypath)

#--- delete file so it does not join itself over and over
try:
    os.remove("May1Grading.csv")
except OSError:
    pass

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

combined_df = pd.DataFrame()

for file in onlyfiles:
    df = pd.read_csv(file,header=None,skipfooter=0)
    combined_df = pd.concat([combined_df,df], axis=0, ignore_index=True)

#-- column headers are set as the 1st row & the 1st row is dropped
combined_df.columns = combined_df.iloc[0]
combined_df = combined_df.drop([0], axis=0)

#-- filter for the user
# combined_df = combined_df[combined_df["Last Modified By"]=='SARMILA-RAI']

#-- convert date string to date
combined_df['Transaction Date2']=pd.to_datetime(combined_df['Transaction Date'], format='%Y%m%d%H%M%S')
combined_df['Transaction Date']=combined_df['Transaction Date2']
combined_df = combined_df.drop(['Transaction Date2'], axis=1)

output_csv = "May1Grading.csv"
combined_df.to_csv(output_csv, index=False)

# end
