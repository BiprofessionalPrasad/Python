# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:04:21 2018

@author: pgaiton
"""

import re

S = 'jjhv'
K = 'z'
#S = input()
#K = input()
prS = S
seS = S
hold = ()
st1 = 0
en1 = 0
for i in range(len(seS)):
    m = re.search(K,S)
    if m:
        st = m.start()
        en = m.end()
        prS = S[st:en]
        if len(seS) == len(S):
            st1 = st
            en1 = st+len(K)
            hold = hold + ((st1,en1-1),)
        else:
            st1 += (st+1)
            en1 = st1+len(K)
            hold = hold + ((st1,en1-1),)
#        print(prS)
        S = S[st+1:]
    else:
        break

if len(hold) >= 1:
    for ele in hold:
        print (ele)
else:
    print ('(-1, -1)')
