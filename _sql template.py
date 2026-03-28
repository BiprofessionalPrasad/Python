# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:12:42 2019

@author: pgaiton
"""


import pyodbc 
import pandas as pd
import os

path = 'K:/Projects/ITAS/Monica Loza/NehaPatelData_20190426/'
os.chdir(path)


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ftwdb2;'
                      'Database=InHouseReports;'
                      'Trusted_Connection=yes;')

#cursor = conn.cursor()
#sql="SELECT top 100 percent * \
#FROM [LearningPlans].[dbo].[uvw_rpt_DLHDdetails]"
#cursor.execute(sql)
#records = cursor.fetchall()
#for i in records:
#    print (i)
#conn.commit()
#cursor.close()
#conn.close()

#conn.commit()
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

######  ------------- step 2. Import Excel File -----------------------########

# ----------- 2a. read excel into py ------------------
file='TemplateForImport'; ext='.xlsx'; sheet='All'
excelfile=pd.ExcelFile(file+ext)
dfExcel=pd.read_excel(excelfile,sheet,na_values=['NA'])

# ----------- 2b. df change datatype ------------------
dfExcel=dfExcel.astype('str')
# dfExcel.dtypes

''' ----- sql alchemy (does not work) ------
#sqlalchemy engine connection
engine = sqlalchemy.create_engine("mssql+pyodbc://ftwdb2/LearningPlans?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes")
#2b. write py df to sql
# this part is failing....
dfExcel.to_sql(name='TemplateForUpload_py',con=engine,schema='dbo',if_exists='append')
#df.to_sql(name='new_table',con=engine,if_exists='append')
#check data inserted
engine.execute("SELECT * FROM [LearningPlans].[dbo].[TemplateForUpload_py]").fetchall()

result=engine.execute("SELECT * FROM [LearningPlans].[dbo].[TemplateForUpload_py]")
for row in result:
    print(row[:])
    
    
    session.close()
result.close()
'''

#-------------- 2c. write py df to sql ------------------- 

for index, row in dfExcel.iterrows():
    cursor.execute("INSERT INTO [LearningPlans].[dbo].[TemplateForUpload_py] \
    (\
    [Department Name], \
    [Level Description], \
    [Course Number], \
    [Course Name], \
    [Status Description], \
    [Delete Y = YES] \
    ) \
    VALUES(?,?,?,?,?,?)"
    ,row['Department Name']
    ,row['Level Description']
    ,row['Course Number']
    ,row['Course Name']
    ,row['Status Description']
    ,row['Delete Y = YES']
    )
    conn.commit()

#-------------- exec proc w/ params ------------------- 

sql = "select EmployeeLogin, '2020' as FiscalYear \
        from Employee e \
        join Department d on e.DepartmentId=d.DepartmentId \
        join NewlyInsertedCourses n on n.DepartmentId=d.DepartmentId \
        and n.LevelNumber=e.LevelNumber "

df_Emplogins = pd.read_sql(sql,conn)

for index, row in df_Emplogins.iterrows():   
    sql ="EXEC [LearningPlans].[dbo].InsertCoursesToExistingEmployeeLearningPlan \
                   ?, ?"
    values = (row['EmployeeLogin'],row['FiscalYear'])
    cursor.execute(sql, (values))

conn.commit()    
    
#----------------------------------------------------
    
from pandas import ExcelWriter

writer = ExcelWriter(r'''K:\Projects\ITAS\Reema\IT Audit assit_20190520\output_files\ITAS_stuff.xlsx''', engine='xlsxwriter')

dfdata.to_excel(writer, sheet_name='Details', startrow=1, header=False, index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Details']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})

# Write the column headers with the defined format.
for col_num, value in enumerate(dfdata.columns.values):
    worksheet.write(0, col_num , value, header_format)
	
	