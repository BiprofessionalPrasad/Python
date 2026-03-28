# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:29:31 2019

@author: pgaiton
"""

import sspyrs
myrpt = sspyrs.report('http://ftwssrs1/ReportServer/Pages/ReportViewer.aspx?%2fInHouse%2fPartner+Reports%2fMaconomyPartnerBillingRepor',
                       'dbReports',
                       'Reportingservicesacct')

"""
http://ftwssrs1/ReportServer/Pages/ReportViewer.aspx?%2fInHouse%2fPartner+Reports%2fMaconomyPartnerBillingReport&PartnerProjectBiller=ALL&StartDate=6/1/2018&EndDate=5/31/2019&loc=Austin%2CDallas%2CFort+Worth%2CHouston%2CLos+Angeles%2CMOJO%2CNew+York%2CSan+Antonio&PPReport=True&ShowDetailOnly=False&rs:Format=EXCEL  



http://ftwssrs1/ReportServer/Pages/ReportViewer.aspx?%2fInHouse%2fPartner+Reports%2fMaconomyPartnerBillingReport&StartDate=6/1/2018&EndDate=5/31/2019&PPReport=0&PartnerProjectBiller=ALL&ShowDetailOnly=1&rs:Format=EXCEL  
"""