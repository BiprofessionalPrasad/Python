# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:15:01 2018

@author: Prasad
"""

string = 'BANANA'
vowels = ['A','E','I','O','U']
stu_ans = {}
kev_ans = {}

for char in string:
    if char not in vowels:
        stu_ans[char] = 1
    elif char in vowels and char not in kev_ans:
        kev_ans[char] = 1
    else:
        kev_ans[char] += 1