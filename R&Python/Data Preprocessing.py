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

#takign care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#encoding categorical data (country)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # these two are classes of lib
labelencoder_X=LabelEncoder()   #object of class LabelEncoder #_X for country #object is created
X[:,0] = labelencoder_X.fit_transform(X[:,0]) #Fit label encoder and return encoded labels
onehotencoder = OneHotEncoder(categorical_features=[0])  #object of class OneHotEncoder
X=onehotencoder.fit_transform(X).toarray() #Fit OneHotEncoder to X, then transform X.

#encoding categorical data (Purchased)
labelencoder_Y=LabelEncoder()   #object of class LabelEncoder #_X for country #object is created
Y = labelencoder_Y.fit_transform(Y) #Fit label encoder and return encoded labels

#splitting dat into training and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

