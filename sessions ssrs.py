# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:45:46 2020

@author: pgaiton
"""

import requests
from requests_ntlm import HttpNtlmAuth
import json

session = requests.Session()

uid='prasad.gaitonde@weaver.com'
pwd='T@k3 goat hotel chapatis'
reporturl='http://ftwssrs1/ReportServer/Pages/ReportViewer.aspx?%2fInHouse%2fFirm+Management%2frpt_OfficeLocationUpdate_CountOfEmployeesOnADay'
outputlocation='K:/temp/output'
session.auth = HttpNtlmAuth(uid,pwd)
#response = session.get(reporturl,stream=True)
response = session.get(reporturl)
print (response.status_code)

#for line in response.iter_lines():
#    # filter out keep-alive new lines
#    if line:
#        decoded_line = line.decode('utf-8')
#        print(json.loads(decoded_line))
#        
        
for chunk in response.iter_content(chunk_size=1024):
    print (chunk)
    
with open(outputlocation+'.xlsx','wb') as xls:
    for chunk in response.iter_content(chunk_size=1024):
        #if chunk:
        xls.write(chunk)
session.close()
