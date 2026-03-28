# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:09:28 2018

@author: pgaiton
"""

import re
S = input()
#S = '..12345678910111213141516171820212223'
S = re.sub(r'[\W]|[\_]',r'',S)
length = len(S)
hold = ()
flag = 0
for i in range(length):
    m = re.match(r'^(\d|\w)?', S[i:length])
    hold = hold + m.groups(1)
    
for i in range(len(hold)):
    if i >= 1:
        if hold[i] == hold[i-1]:
            print (hold[i])
            flag = 1
            break
if flag == 0:
    print ('-1')
        
    