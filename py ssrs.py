# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:22:13 2020

@author: pgaiton
"""

import SSRS

Service='https://ftwssrs/Reportserver/ReportService2010.asmx?wsdl'  
# Service = 'http://localhost/ReportinServices/ReportService2010.asmx?wsdl'
Execution = 'http://ftwssrs/Reportserver/ReportExecution2005.asmx?wsdl'
user = 'WT\pgaiton'
password = 'T@k3 goat hotel chapatis'

RS = SSRS.SSRS(Service, Execution, user, password)

#RS = SSRS(Service, Execution, user, password)
result = RS.ServiceClient.service.ListChildren(dir, recursive)

for item in result.CatalogItem:
    print(item['Name'])