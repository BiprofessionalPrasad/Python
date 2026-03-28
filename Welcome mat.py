# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:11:58 2018

@author: Prasad
"""

def welcome_mat():
    k = list( map(int, input().split()) )
    N, M = k 
    filler='-'
    str='.|.'
    width = int(M)
    mid = int((N+1)/2)

    for i in range(1, mid):
        print ((((2*i)-1)*str).center(width, filler))

    print (('WELCOME').center(width, filler))

    for i in range(mid-1, 0, -1):
        print ((((2*i)-1)*str).center(width, filler))

if __name__ == "__main__":
    welcome_mat()