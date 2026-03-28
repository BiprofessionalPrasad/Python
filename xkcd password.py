# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:23:05 2020

@author: pgaiton
"""

from xkcdpass import xkcd_password as xp

# create a wordlist from the default wordfile
# use words between 5 and 8 letters long
wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=3, max_length=8)

# --count=5 --acrostic='chaos' --delimiter='|' --min=5 --max=6 --valid-chars='[a-z]'

# create a password with the acrostic "face"
print(xp.generate_xkcdpassword(mywords, acrostic="weaver"))
print(xp.generate_xkcdpassword(mywords, acrostic="xkcd"))