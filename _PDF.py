# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:29:44 2020

@author: pgaiton
"""

import PyPDF2
import os

path = r'‪C:\Users\pgaiton\Downloads'
os.chdir(path.replace('\u202a',''))

pdfFileObj = open(r'automate2e_SampleCh7.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(0)
pageObj.extractText()

pdfFileObj.close()
  

import os
import subprocess

for top, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('lowriter --invisible --convert-to doc "{}"'
                            .format(abspath), shell=True)

# need to continue on this module, later.            