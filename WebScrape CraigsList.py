import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

path = 'K:\Projects\Python programming'
os.chdir(path)

raw_html = simple_get('https://dallas.craigslist.org/')
len(raw_html)

no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
no_html is None

html = BeautifulSoup(raw_html, "html.parser")
html.findAll('a')

list=html.select('p')

for p in list[0:10]:
    #if p['id'] == '<a>' or '</a>':
    if p['id'] == 'a':
        print (p.text)
        
        