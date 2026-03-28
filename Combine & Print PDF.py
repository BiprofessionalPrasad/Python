# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:32:55 2019

@author: pgaiton
"""
import os
import PyPDF2

# basics
def get_text(fname):
	f = open(fname,'rb')
	pdfr = PyPDF2.PdfFileReader(f)
	pdfr.numPages
	page = pdfr.getPage(0)
	# print(page)
	txt=page.extractText()
	f.close()
	return txt
	# print(txt)

# combine PDFs
def combine_files(f1,f2,rf):
	pdf1 = open(f1,'rb')
	pdf2 = open(f2,'rb')
	pdfr1 = PyPDF2.PdfFileReader(pdf1)
	pdfr2 = PyPDF2.PdfFileReader(pdf2)
	pdfw = PyPDF2.PdfFileWriter()

	for pn in range(pdfr1.numPages):
		po=pdfr1.getPage(pn)
		pdfw.addPage(po)
	for pn in range(pdfr2.numPages):
		po=pdfr2.getPage(pn)
		pdfw.addPage(po)
		
	pdfo=open(rf,'wb')
	pdfw.write(pdfo)
	pdfo.close()
	pdf1.close()
	pdf2.close()

f = './combined.pdf'
combine_files('./pat.pdf','./pat.pdf',f)
print(get_text(f))