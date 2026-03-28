# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:12:20 2021

@author: pgaiton
"""

import json
import praw
import requests

credentials = 'client-secrets.json'

with open(credentials) as f:
    creds = json.load(f)