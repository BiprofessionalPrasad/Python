# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:04:29 2018

@author: Prasad
"""

from itertools import product

A = list( map(int, input().split()) )
B = list( map(int, input().split()) )
T = list((product(A,B)))
print(' '.join(map(str, T)))