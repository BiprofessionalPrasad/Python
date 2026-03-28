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
os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Operations Dashboard")
# os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Administrative\Manager Communications")

def send_email(subject, body, recipient,cc):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = subject
#    mail.Body = body
    mail.HTMLBody= body
    mail.To = recipient
    mail.cc=cc
    #attachment1 = os.getcwd() +"\\Daily Productivity and Utilization.xlsx"
    #attachment1 = os.getcwd() +"\\All.csv"
    #attachment2 = os.getcwd() +"\\rampup.csv"
    attachment1 = os.getcwd() + "\\Master File.xlsx"
    mail.Attachments.Add(attachment1)
    #mail.Attachments.Add(attachment2)
    # mail.Display(True)
    mail.Send()

subject="Operations Dashboard" 
body="<p>Good Morning Team,</p>\
<p>Friendly reminder to update Master schedule for the Operations Dashboard.&nbsp;</p>\
<p>If already updated, please ignore this reminder.</p>\
<p>Data seems to be missing for a few latest dates, or intermediate dates.</p>\
<p>Attached: Lastest schedule from Teams.</p>\
<p>Thank you, -Prasad&nbsp;</p>\
<p><strong>Prasad Gaitonde</strong> | Business Process Specialist | FedEx Supply Chain | mobile: 469.265.1049</p>\
<p>840 W Sandy Lake Rd. Coppell, TX&nbsp; 75019</p>\
<p><a>prasad.gaitonde@fedex.com</a></p>\
         "
#to="prasad.gaitonde@fedex.com; "
to="april.l.jones@fedex.com;Durgesh.Subba@fedex.com"
cc="prasad.gaitonde@fedex.com;Steve.Diascro@fedex.com;melissa.martin@fedex.com"
#cc="prasad.gaitonde@fedex.com; "
#to="janet.berkenbile@fedex.com;silvia.perez@fedex.com"
#to="Emmanuel.Njie@fedex.com; naimo.mohamed@fedex.com; gregory.frenzel@fedex.com; Antonio.Zurria@fedex.com"
send_email(subject, body, to, cc)


