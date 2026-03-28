# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:06:21 2019

@author: pgaiton

Python Web Scraping Tute
"""

"""
import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

path = 'K:\Projects\Python programming\WebScrapes'
os.chdir(path)
url = "http://web.mta.info/developers/turnstile.html"

query="hackernoon How To Scrape Google With Python"
query = query.replace(' ','+')
url = r"https://google.com/search?q={query}"

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent" : MOBILE_USER_AGENT}

response = requests.get(url, headers=headers)
response

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')
soup.findAll('div')

results = []
for g in soup.find_all('div', {"class" : "r"}):
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        title = g.find('h3').text
        item={
                "title":title,
                "link":link
        }
        results.append(item)
print(results)
        

min = 36
max = len(soup.findAll('a'))+1

for i in range(41,max):
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    
    download_url = 'http://web.mta.info/developers/'+ link
    
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

    # Last but not least, we should include this line of code so that we can pause our      code for a second so that we are not spamming the website with requests. This helps us avoid getting flagged as a spammer.
    print("I am on line =", i ,  " \n ")
    time.sleep(1)

"""

import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datascientists.simple_get import simple_get

path = 'K:\Projects\Python programming'
os.chdir(path)

raw_html = simple_get('https://realpython.com/blog/')
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
        
        
        
        
