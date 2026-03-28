# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:32:14 2020

@author: pgaiton
"""

import sspyrs
link = 'http://ftwssrs1/Reportserver/?%2fInHouse/AllStaffProjectMonthlyTimeDatasummary'
myusername = 'WT\pgaiton'
password = 'T@k3 goat hotel chapatis'
myrpt = sspyrs.report(link,myusername,password)
myrpt = sspyrs.report('http://ftwssrs1/Reportserver/?%2fInHouse/AllStaffProjectMonthlyTimeDatasummary',myusername,password)
