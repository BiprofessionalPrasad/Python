# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:27:22 2017

@author: pgaiton
"""

import numpy as np                   ## math functions 
import matplotlib.pyplot as plt
import pandas as pd                  ## import data
import os

#set working directory
os.chdir('K:\Projects\Machine Learning\Data_Preprocessing')

#import a dataset
dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values        #take all rows,take all columns-1
Y=dataset.iloc[:,3].values          #take all rows,last column (0-3)
