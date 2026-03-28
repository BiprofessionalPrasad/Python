import pandas as pd
import os
# ========================================================================
# ADIJAT-OTENIYA-RAJI
# begin
os.chdir(r"C:\Import_Export\file")

combined_df = pd.DataFrame()

file_list = os.listdir()

for file in file_list:
    df = pd.read_csv(file)
    #df = df[df["mod_usr_id"]=='AMITA-KASPAL']
    combined_df=pd.concat([combined_df,df],axis=0,ignore_index=True)
    
output_csv = "interface_log.csv"

combined_df.to_csv(output_csv, index=False)
#end
