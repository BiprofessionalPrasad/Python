# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:44:14 2024

@author: 9387758
"""

import pandas as pd
import os

os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Nextview\Data Validation\Grading")

df = pd.read_excel('WFR Activity Display 5_9_2024 2nd shift.xls',
                   sheet_name='WFR Activity Display 5_9_2024 2',
                   index_col=0,
                   skipfooter=0)
#df = df[df["Next Repair Step"]=='5831101']
# df.query("(name=='john') or (country=='UK')")
df2=df[(df['Next Repair Step']=='TMO-LIQUIDATION-A')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-B')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-C')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-D')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-N')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-NEW')
   |(df['Next Repair Step']=='TMO-LIQUIDATION-NEWK')]

df3=df2.groupby(['Last Inserted By']).size()

output_excel = "WFR_Activity_592024_Grading_2ndShift.xls"

df3.to_excel(output_excel, index=True)