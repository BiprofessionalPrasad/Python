# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:23:00 2018

@author: pgaiton
"""
import string

def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase

    for i in range(size - 1, 0, -1): #i=3
        row = ["-"] * (size * 2 - 1) #9's
        for j in range(0, size - i): #j=0,1
            row[size - 1 - j] = alphabet[j + i] #4=d,3=e 
            row[size - 1 + j] = alphabet[j + i] #4=d,5=e
        print("-".join(row))

    for i in range(0, size):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alphabet[j + i]
            row[size - 1 + j] = alphabet[j + i]
        print("-".join(row))

    