# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:29:49 2021

@author: pgaiton
"""

# Python API Tutorial: Getting Started with APIs
# In this Python API tutorial, we’ll learn how to retrieve data for data science projects. 
# There are millions of APIs online which provide access to data. 
# Websites like Reddit, Twitter, and Facebook all offer certain data through their APIs.

# pip install requests
# conda install requests

import requests
import pandas as pd

# response = requests.get('https://api.open-notify.org/this-api-doesnt-exist')
# response = requests.get('https://w3schools.com')
# print(response.status_code)

"""
200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
404: The resource you tried to access wasn’t found on the server.
503: The server is not ready to handle the request.

# https://www.reddit.com/r/{subreddit}/{listing}.json?limit={count}&t={timeframe}
response = requests.get("https://www.reddit.com/r/python/top.json?limit=100&t=week")
print(response.status_code)

print(response.json())

"""

subreddit = 'Home'
limit = 10
timeframe = 'day' #hour, day, week, month, year, all
listing = 'best' # controversial, best, hot, new, random, rising, top

def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

def get_post_titles(r):
    '''
    Get a List of post titles
    '''
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts

def get_results(r):
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments']}
    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df
 
if __name__ == '__main__':
    r = get_reddit(subreddit,listing,limit,timeframe)
    df = get_results(r)
    print(df)
