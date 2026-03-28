import os
import pandas as pd
# ========================================================================
# Carousel files
#=========================================================================
# begin
os.chdir(r"C:\Join")
#os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Nextview\Data Validation\Presort\raw")

combined_df = pd.DataFrame()

file_list = os.listdir()

for file in file_list:
    df = pd.read_csv(file, sep="|")
#    df = df[df["ins_user_id"]=='5831101']
    combined_df=pd.concat([combined_df,df],axis=0,ignore_index=True)
    
output_csv = "Joined.csv"

combined_df.to_csv(output_csv, index=False)
# end
#=========================================================================