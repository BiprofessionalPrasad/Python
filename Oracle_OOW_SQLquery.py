# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:55:00 2024

@author: 9387758
"""
# DO NOT USE
import getpass
import oracledb as cx_Oracle
import pandas as pd
import numpy as np
import seaborn 
import os
from datetime import date

os.chdir(r"//copdwv-fshare11.atcwan.com/Fulfillment/Reporting/Scott Dashboard Files/Queries/DC45 OW Priority Aging DOD")

un='STARREPORTING' #un='reporting_read'
pw='report'#pw='UzKmKZaLTh9sJIbBHXqzmjwIY'
cs='vxtmobstgdb01.genco.com:1561/starstg'

'''with cx_Oracle.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)'''
            
con = cx_Oracle.connect(user=un, password=pw, dsn=cs)            
cur = con.cursor()
# query="SELECT calendardate,    day,    holiday,    tunneldevicequantity,    tunnelmaxaged,    palletcount,    clearshotlvl1count,    clearshotlvl2count,    clearshotlvl1pass,    clearshotlvl2pass,    devicesreceived,    hsireceived,    watchesreceived,    accessoriesreceived,    totalreceived,    receiptexceptions,    idexceptions,    clearexceptions \
#     FROM starreporting.opsdash_receiving";

for file1 in ['Run1.sql','Run2.sql','Run3.sql']:
    fd = open(file1, 'r')
    sqlFile = fd.read()
    fd.close()
    cur.execute(sqlFile) 
    
#### ORA-00942: table or view does not exist
#### Help: https://docs.oracle.com/error-help/db/ora-00942/
#rows = cur.fetchall()
#columns=[col[0] for col in cur.description]

#df=pd.DataFrame(rows,columns=columns)
cur.close()
con.close()

#todaystr = date.today()
#todaystr2 = todaystr.strftime("%Y_%m_%d")

#file_name = 'WIPquery_Export'+todaystr2+".csv"

#os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\SQL scripts\Oracle PBI-OpsDash\Data Validation")
#df.to_csv(file_name, sep=',', encoding='utf-8')

#file_name_parquet='WIPquery_Export'+todaystr2+".parquet"
#df.to_parquet(file_name_parquet)

