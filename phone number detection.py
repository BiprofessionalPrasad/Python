# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:05:43 2018

@author: pgaiton
"""

import re
N = int(input()) 
ans = []
for i in range(0,N,1):
    input_string = input()
    match = re.search('^[7-9]\d{9}$',input_string)
    if match:
        ans.append('YES')
    else:
        ans.append('NO')
    
for chars in ans:
    print (chars)
    
#8F54698745
#9898959398
#879546242    