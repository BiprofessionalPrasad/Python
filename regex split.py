# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:51:00 2018

@author: pgaiton
"""

import re
N = int(input())
ans = []
for i in range(N):
    str = input()
    match = re.search(r'^[+-]?\d*?\.{1}\d+$', str)
    if match:
        ans.append('True')
    else:
        ans.append('False')

for item in ans:
    print (item)
    