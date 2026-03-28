# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:46:13 2018

@author: pgaiton
"""
import re

N = int(input())
y = ''
for i in range(1,N+1,1):
    x = input()
    y = y + (re.sub("\s([&]{2})(?=\s)", " and", (re.sub("\s([|]{2})(?=\s)"," or",x)))) + "\n"

print (y)

# ------------------------------------------------------------------

import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment

# ------------------------------------------------------------------

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
