# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:58:47 2023

@author: Prasad
"""

import requests

response = requests.get("https://randomuser.me/api/")

response = requests.get("https://api.thecatapi.com/")

response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text
response.headers
response.request
request = response.request
request.url
request.path_url
request.method
request.headers


# mars rover pictures
import http.client

conn = http.client.HTTPSConnection("api.nasa.gov")
payload = ''
headers = {}
conn.request("GET", "/planetary/apod?api_key=608ObRjuxXQsTuh4Nec6NgBYhJYkcogjhOwglPTy", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))