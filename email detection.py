# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:07:25 2018

@author: pgaiton
"""

"""A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
"""

from email.utils import getaddresses
