# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:30:37 2018

@author: pgaiton
"""

import re
#S = input()
S = 'abaabaabaabaae'
S = re.sub(r'[\W]|[\_]',r'',S)
length = len(S)
hold = ()
flag = 0
vowels = re.findall(r'(?:\w{1})([aeiouAEIOU]{2,})(?:\w{1})', S)
    
if len(vowels) < 1:
    print (-1)
    
for vow in vowels:
    print (vow)
    