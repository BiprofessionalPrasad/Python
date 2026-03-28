# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import pandas as pd
import numpy as np
import os
import pyodbc 
import win32com.client as win32

os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\SQL scripts")

# connect to sql server
'''
import psycopg2
def get_connection():
	try:
		return psycopg2.connect(
			database="Prasad",
			user="postgres",
			password="gaitonde",
			host="localhost",
			port=5432,
		)
	except:
		return False
conn = get_connection()
#if conn:
#	print("Connection to the PostgreSQL established successfully.")
#else:
#	print("Connection to the PostgreSQL encountered and error.")

with conn.connection as cursor:
    cursor.execute(open("schema.sql", "r").read())
    
# run sql file

# export to csv
'''

# attach to email
# send email     
os.chdir(r"C:\Import_Export")
# os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Administrative\Manager Communications")

def send_email(subject, body, recipient,cc):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = subject
    #mail.Body = body
    mail.HTMLBody= body
    mail.To = recipient
    mail.cc=cc
    #attachment1 = os.getcwd() +"\\Daily Productivity and Utilization.xlsx"
    attachment1 = os.getcwd() +"\\All.csv"
    #attachment2 = os.getcwd() +"\\rampup.csv"
    mail.Attachments.Add(attachment1)
    #mail.Attachments.Add(attachment2)
    # mail.Display(True)
    mail.Send()

subject="KPI files are attached" 
body="<p>&nbsp;</p>\
<p>Good Morning..&nbsp;</p>\
<p><br /> This is an automated email sent using Python!&nbsp;</p>\
<p><br /> Best, -Prasad</p>\
<p><strong>Prasad Gaitonde</strong> | Business Process Specialist | FedEx Supply Chain | mobile: 469.265.1049</p>\
<p>840 W Sandy Lake Rd. Coppell, TX&nbsp; 75019</p>\
<p><a>prasad.gaitonde@fedex.com</a></p>\ "
to="prasad.gaitonde@fedex.com"
cc="prasad.gaitonde@fedex.com"
#to="janet.berkenbile@fedex.com;silvia.perez@fedex.com"
#to="Emmanuel.Njie@fedex.com; naimo.mohamed@fedex.com; gregory.frenzel@fedex.com; Antonio.Zurria@fedex.com"
send_email(subject, body, to, cc)


