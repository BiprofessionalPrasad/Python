# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:55:22 2024

@author: 9387758
"""

import re

phoneNumRE = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRE.search('My number is 214-458-0154 blah blah blah.... 2334-. ... 384- etc')
print(mo.group(1))

areaCode, number= mo.groups()
print(areaCode)
print(number)

print(mo.groups())