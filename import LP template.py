# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:59:04 2019

@author: pgaiton

script is used to import LP template into db
"""

import os
import pyodbc
import pandas as pd
# import sqlalchemy 

#set LP template path. Make sure to empty & refill excel file TemplateForImport.xlsx
path=r'''K:\Projects\LearningPlan\ProcessFiles'''
#path=r'''C:\Users\pgaiton\OneDrive - WEAVER\K Drive\Projects\LearningPlan\ProcessFiles'''
os.chdir(path)

server='ftwdb2' #r'''devdb2\reporttest''' 
db='LearningPlans'
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'server=server;'
#                      'database=LearningPlans;'
#                      'Trusted_Connection=Yes;')

#conn = pyodbc.connect('DRIVER={SQL Server};host=server;DATABASE=LearningPlans')

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER='+server+';'
                      'DATABASE='+db+';'
                      'Trusted_Connection=Yes;')

######  ------------- step 1. truncate staging table ------------------ #######
cursor = conn.cursor()
sql = "TRUNCATE TABLE [LearningPlans].[dbo].[TemplateForUpload_py]"
cursor.execute(sql)
conn.commit()

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

#------------ 2d. remove index column from sql table ---------------------
'''sql = "ALTER TABLE [LearningPlans].[dbo].[TemplateForUpload_py] \
        DROP COLUMN [index]"
cursor.execute(sql)
conn.commit()
'''
#------------ 2e. update table , remove nan values -----------------------
sql = "UPDATE [LearningPlans].[dbo].[TemplateForUpload_py]  \
        SET [Delete Y = YES] = '' \
        WHERE [Delete Y = YES] = 'nan'"
cursor.execute(sql)
conn.commit()

# ------------------- step 2f. load stg table to work table after truncate -------
sql = "TRUNCATE TABLE [LearningPlans].[dbo].[TemplateForUploadALL$]"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO [LearningPlans].[dbo].[TemplateForUploadALL$] \
        ( \
        [DepartmentName], \
        [LevelDescription], \
        [CourseNumber], \
        [CourseName], \
        [StatusDescription], \
        [Delete _Y = YES] \
        ) \
         SELECT [Department Name], \
         [Level Description], \
         [Course Number], \
         [Course Name], \
         [Status Description], \
         [Delete Y = YES] \
         FROM [LearningPlans].[dbo].[TemplateForUpload_py]"
cursor.execute(sql)
conn.commit()
cursor.close()

# ---------------- Project FoolProofing ----------------------------- #
# ----------------- verify Levels , Status & course------------------ #
# Template has a level which is out of supported levels
# Template has a Status which is out of supported status
# Template has a Course Name which is out of supported Courses

cursor = conn.cursor()
sql = "DECLARE @errmsg nvarchar(max); \
       EXEC [LearningPlans].[dbo].[verify_levels_status_course] @errmsg = @errmsg OUTPUT  \
       SELECT @errmsg as error"
cursor.execute(sql)
error_message = cursor.fetchone()[0]
conn.commit()
if len(error_message)>1:
    print(error_message)

# if no error then proceed.

###### ------------ step 3. EXEC [dbo].[GetDepartmentLevelCourseStatus] ------- #######
cursor = conn.cursor()
sql = "EXEC [LearningPlans].[dbo].[GetDepartmentLevelCourseStatus]"
cursor.execute(sql)
conn.commit()


###### --- cleanup close cursor, sql connection ------- #########
cursor.close()
conn.close()


#for index, row in dfExcel.iterrows():
#    print (index, row['Course Name'])
    
    