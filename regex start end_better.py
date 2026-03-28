# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:01:27 2018

@author: pgaiton
"""

def remove_dups(duplicate):
    final_tuple = ()
    for item in duplicate:
        if item not in final_tuple:
            final_tuple = final_tuple + (item,)
    return final_tuple
    
import re
# S = 'aabcdeffgabcdef'
# K = 'abcdef'
S = input()
K = input()
hold = ()
for i in range(len(S)):
    match = re.search(K, S[i:len(S)])
    if match:
        hold = hold + ((match.start()+i , match.start()+i+len(K)-1) ,)

if len(hold) >= 1:
    for ele in remove_dups(hold):
        print (ele)
else:
    print ((-1, -1))
    