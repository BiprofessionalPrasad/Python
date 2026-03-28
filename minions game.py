# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:25:15 2018

@author: pgaiton
"""

Vowels=['a','e','i','o','u','A','E','I','O','U']

word='Gabber'
Stuart = 0
Kevin = 0
# word = string
for i in range(len(word)):
    if word[i] in Vowels:
        Kevin += (len(word)-i)
    else:
        Stuart += (len(word)-i)

if Stuart > Kevin:
    print ('Stuart ', Stuart)
elif Kevin > Stuart:
    print ('Kevin', Kevin)
else:
    print ('Draw')