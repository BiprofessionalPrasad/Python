# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:02:56 2019

@author: pgaiton

script is used to insert newly added course to exisitng ELP's:
1] figure out the newly inserted courses. 
   create an excel NewlyInsertedCourses_DeptandLevels.xlsx
2] course applies to "May be required", so we need to exec.   
   Proc InsertCoursesToExistingEmployeeLearningPlan . 
   This proc needs employee logins.
3] depending on levels & depts, gather emp logins.
4] run a cursor on each login. run the proc InsertCoursesToExistingEmployeeLearningPlan. 
    
"""


import os
import pyodbc
import pandas as pd
# import sqlalchemy 

#set LP template path. Make sure to empty & refill excel file TemplateForImport.xlsx
path=r'''K:\Projects\LearningPlan\ProcessFiles'''
os.chdir(path)

conn = pyodbc.connect('Driver={SQL Server};'
                      'server=FTWDB2;'
                      'database=LearningPlans;'
                      'Trusted_Connection=Yes;')

cursor = conn.cursor()

######  ------------- step 1. first create new excel, save dept & levels info ------------------ #######
file='NewlyInsertedCourses_DeptandLevels'; ext='.xlsx'; sheet='Sheet1'
excelfile=pd.ExcelFile(file+ext)
dfExcel=pd.read_excel(excelfile,sheet,na_values=['NA'])

dfExcel=dfExcel.astype('str')

######  ------------- step 2. Create and load NewlyInsertedCourses table ------------------ #######
sql = "Truncate Table [LearningPlans].[dbo].[NewlyInsertedCourses]"
cursor.execute(sql)
conn.commit()

for index, row in dfExcel.iterrows():
    sql="INSERT INTO [LearningPlans].[dbo].[NewlyInsertedCourses] \
    (\
    [Department Name], \
    [Level Description] \
    ) \
    VALUES(?,?)"
    values=(row['Department Name']
    ,row['Level Description'])
     
    cursor.execute(sql,(values))
conn.commit()

sql = " Update A \
        Set DepartmentId = d.DepartmentId, \
            LevelNumber = L.LevelNumber, \
            FiscalYear = '2020' \
        FROM [LearningPlans].[dbo].[NewlyInsertedCourses]  A \
		Join Department d on d.DepartmentName=A.[Department Name] \
		Join Level l on l.LevelDescription=A.[Level Description]"
        
cursor.execute(sql)
conn.commit()

######  ------------- step 3. Get empLogins & Exec Proc ------------------ #######
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
    
######  ------------- cleanup ------------------ #######

cursor.close()
conn.close()
