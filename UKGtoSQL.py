# This script needs UKG QuickFind exported to CSV placed at xyz location
# It then loads SQL server & you can refresh the BI dashboard (Excel)

import csv
import pandas as pd
import numpy as np
import os
import pyodbc 
'''with open('intf5_STARPRD_WFR_ACTIVITY_DISPLAY_Sep-06-2023-14-58-12.csv',newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))'''
os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Nextview\Kronos Employees\ImportFile")

       
df1 = pd.read_csv('QuickFind.csv',header=1)
df1.iloc[1:, :]
#df2 = pd.read_csv('intf5_FedExSC_Carousel_Hourly_20231003170000.dat')
#result=df1.head(10)
#print(df1.info())
#print(df2.info())
#print(result)

df1=df1.rename(columns={'ADP | Dept':'ADP_Dept','Department | Name':'Department_Name','FedEx or Temp':'FedExorTemp','Location':'Location','Teammate | Name':'Teammate_Name','Person ID':'Person_ID','Assigned | Supervisor':'Assigned_Supervisor','Hire Date':'Hire_Date','Schedule | Group':'Schedule_Group'})

df1.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)
df1 = df1.fillna(0)

#print(df1.info())

#-------SQL----------#
def truncate_table(table_ref, dbc):
    try:
        with dbc.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {table_ref}')
            cursor.commit()
    except Exception as err:
        dbc.rollback()
        raise err
        
con=pyodbc.connect('Driver={SQL Server};Server=''localhost\SQLExpress'';Database=Nextview;Trusted_connection=yes')
truncate_table('Employees', con)

cursor = con.cursor()


for index, row in df1.iterrows():
     cursor.execute("INSERT INTO dbo.Employees([ADP_Dept]   ,[Department_Name],[FedEx_or_Temp],[Location],[Teammate_Name]      ,[Person_ID],[Assigned_Supervisor],[Hire_Date]      ,[Schedule_Group]) values(?,?,?,?,?,?,?,?,?)", row.ADP_Dept,row.Department_Name,row.FedExorTemp,row.Location,row.Teammate_Name,row.Person_ID,row.Assigned_Supervisor,row.Hire_Date,row.Schedule_Group)
     
'''for index, row in df1.iterrows():
    cursor.execute("INSERT INTO dbo.Employees([Schedule_Group]) values(?)",row.Schedule_Group)'''
    
con.commit()

#-------Email-------#
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

filename = 'QuickFind.csv'
SourcePathName  = 'C:/Users/9387758/OneDrive - MyFedEx/Documents/Nextview/Kronos Employees/ImportFile/' + filename 
msg = MIMEMultipart()
msg['From'] = 'prasad.gaitonde@fedex.com'
msg['To'] = 'prasad.gaitonde@domain.com'
msg['Subject'] = 'UKG as of Today'
body = 'Testing'
msg.attach(MIMEText(body, 'plain'))

attachment = open(SourcePathName, 'rb')
part = MIMEBase('application', "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

'''does not work
server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
server.ehlo()
server.starttls()
server.ehlo()
#server.login('from@domain.com', 'password_here')  ### if applicable
server.send_message(msg)
server.quit()'''

