# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:36:00 2020

@author: pgaiton

join PDF files
"""
from PyPDF2 import PdfFileMerger
path = r'‪C:\Users\pgaiton\Downloads'
os.chdir(path.replace('\u202a',''))

pdfs = ['automate2e_SampleCh7.pdf', 'fy2020_Monthly Client Activity -Partner Maconomy_Excel.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
