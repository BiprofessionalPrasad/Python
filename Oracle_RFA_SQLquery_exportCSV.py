# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:55:00 2024

@author: 9387758
"""


import getpass
import oracledb as cx_Oracle
import pandas as pd
import numpy as np
import seaborn 
import os
from datetime import date

os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\SQL scripts\Oracle PBI-OpsDash")

un='reporting_read'
pw='UzKmKZaLTh9sJIbBHXqzmjwIY'
cs='vxtmobproddb02.genco.com:1561/STARPRD'

'''with cx_Oracle.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)'''
            
con = cx_Oracle.connect(user=un, password=pw, dsn=cs)            
cur = con.cursor()
# query="SELECT calendardate,    day,    holiday,    tunneldevicequantity,    tunnelmaxaged,    palletcount,    clearshotlvl1count,    clearshotlvl2count,    clearshotlvl1pass,    clearshotlvl2pass,    devicesreceived,    hsireceived,    watchesreceived,    accessoriesreceived,    totalreceived,    receiptexceptions,    idexceptions,    clearexceptions \
#     FROM starreporting.opsdash_receiving";

fd = open('RFA V4_oraclesql.sql', 'r')
sqlFile = fd.read()
fd.close()

cur.execute(sqlFile)
rows = cur.fetchall()
columns=[col[0] for col in cur.description]

df=pd.DataFrame(rows,columns=columns)
cur.close()
con.close()

todaystr = date.today()
todaystr2 = todaystr.strftime("%Y_%m_%d")

file_name = 'RFAV4_oraclesql'+todaystr2+".csv"

os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\SQL scripts\Oracle PBI-OpsDash\Data Validation")
df.to_csv(file_name, sep=',', encoding='utf-8')

#file_name_parquet='WIPquery_Export'+todaystr2+".parquet"
#df.to_parquet(file_name_parquet)

