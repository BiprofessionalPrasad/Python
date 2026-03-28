# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:12:42 2019

@author: pgaiton
"""

import pyodbc 
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ftwdb2;'
                      'Database=InHouseReports;'
                      'Trusted_Connection=yes;')

#cursor = conn.cursor()
#cursor.execute('SELECT Top 10 * FROM InHouseReports.dbo.ClientMonthlyDataMaconomy')

# sql = "Select * From InHouseReports.dbo.ClientMonthlyDataMaconomy Where CMGnum='1857' and CurrentMonthStartDate between '2018-04-01' and '2019-03-31'"
"""sql = "Select mci.[ParentClientNumber], Cltnum,Cltname,CltIDW,MPI.ProjectName,Datename(Month, [CurrentMonthStartDate]) As [Month],ProjectPartner, ProjectPartnerName, \
SUM([HrsMTDW]) AS [HrsMTDW],SUM([FeeMTDW]) AS [FeeMTDW],SUM([HoursBilledMTD]) AS [HoursBilledMTD],SUM([BilledMTDC]) AS [BilledMTDC] \
From InHouseReports.dbo.ClientMonthlyDataMaconomy CMDM \
LEFT JOIN [dbo].[MaconomyClientInformation] MCI ON MCI.ClientNumber = CMDM.Cltnum \
LEFT JOIN [dbo].[MaconomyProjectInformation] MPI ON MPI.ProjectNumber = convert(VARCHAR(10), CMDM.CltIDW)\
Where CMGnum='1857' and CurrentMonthStartDate between '2018-04-01' and '2019-04-01'\
Group By mci.[ParentClientNumber], Cltnum,Cltname,CltIDW,MPI.ProjectName,Datename(Month, [CurrentMonthStartDate]),ProjectPartner, ProjectPartnerName"
"""
"""
sql = "Select CMGnum,CMGLname, mci.[ParentClientNumber], ProjectPartnerName, \
SUM([HrsMTDW]) AS [Hours Worked],\
SUM([FeeMTDW]) AS [Amount Worked],\
SUM([ExpMTDC]) AS [Expenses Charged],\
SUM([WorkMTDW]) AS [Total Work Done],\
SUM([HoursBilledMTD]) AS [HoursBilledMTD],\
SUM([WorkMTDC]) AS [Work Cleared],\
SUM([BilledMTDC]) AS [Billed] \
From InHouseReports.dbo.ClientMonthlyDataMaconomy CMDM \
LEFT JOIN [dbo].[MaconomyClientInformation] MCI ON MCI.ClientNumber = CMDM.Cltnum \
LEFT JOIN [dbo].[MaconomyProjectInformation] MPI ON MPI.ProjectNumber = convert(VARCHAR(10), CMDM.CltIDW)\
Where CMGnum='1857' and CurrentMonthStartDate between '2018-04-01' and '2019-03-31'\
Group By CMGnum,CMGLname,mci.[ParentClientNumber], ProjectPartnerName"
"""

#this will pass params just has them hard coded for testing
"""
sql="exec InHouseReports.[dbo].[rpt_PartnerWorkInOtherLocationsTSBSMAC] @BeginDate='2018-04-01', @EndDate='2019-03-31',@PartnerEmployeeNumber='-1',@LocationId='-1'"
"""

sql = "exec [InHouseReports].[dbo].[rpt_PartnerBillingsbyIndustryGroup] @Partner='1413' \
                                      , @StartDate= '2018-06-01' \
                                      , @EndDate= '2019-05-31' "

#conn.execute()
#conn.commit()

#with parameters
""" df = pd.read_sql(('select "Timestamp","Value" from "MyTable" '
                     'where "Timestamp" BETWEEN %(dstart)s AND %(dfinish)s'),
                   conn,params={"dstart":datetime(2014,6,24,16,0),"dfinish":datetime(2014,6,24,17,0)},
                   index_col=['Timestamp'])
"""

data = pd.read_sql(sql,conn)

#cursor.close()
conn.close()

# group by the dataframe
dfout = data.groupby(['ProjectTypeName']).sum()
dfout2 = data.groupby(['IndustryDescription']).sum()
# drop projectnumber
dfout = dfout.drop(['ProjectNumber','Billed/WorkCLeared'], axis=1)
dfout2 = dfout2.drop(['ProjectNumber','Billed/WorkCLeared'], axis=1)
 
#data.to_csv('K:\Projects\AdministrationTeam\Adrienne Heetland\PartnerNominationMatrix_20190422\output_files\out.csv', sep='\t')

from pandas import ExcelWriter
writer = ExcelWriter(r'''K:\Projects\ITAS\Monica Loza\NehaPatelData_20190426\output_files\Neha_Patel.xlsx''')
data.to_excel(writer,'Details')
dfout.to_excel(writer,'ProjectTypeName')
dfout2.to_excel(writer,'IndustryDescription')
writer.save()

#for row in cursor:
#     print('row = %r' % (row,))A1



