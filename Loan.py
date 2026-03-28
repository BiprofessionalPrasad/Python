# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:33:45 2024

@author: 9387758
"""

import pandas as pd
import os
import seaborn as sns
import numpy as np


os.chdir(r"C:\Users\9387758\OneDrive - MyFedEx\Documents\AIML")

df=pd.read_parquet("Loan_Modeling.parquet")

# 1. What is the distribution of mortgage attribute? 
# Are there any noticeable patterns or outliers in the distribution?
df.isnull().values.any()

sns.set_theme(style="ticks")

sns.pairplot(df,
             x_vars=["Income","ZIPCode","CCAvg","Mortgage","Personal_Loan"],
             y_vars=["Income","ZIPCode","CCAvg","Mortgage","Personal_Loan"],
             hue="Education")


median = np.median(df["Mortgage"],axis=0)

df.Mortgage.quantile([0.25,0.5,0.75])
# 0.25      0.0
# 0.50      0.0
# 0.75    101.0

# 2. How many customers have credit cards? 1470
df[df["CreditCard"]==1]["ID"].count()

# 3. What are the attributes that have a strong correlation with the target attribute 
# (personal loan)?

corr_matrix=df.corr()
target_correlations =corr_matrix["Personal_Loan"].sort_values(ascending=False)
print(target_correlations)

# Income                0.502462
# CCAvg                 0.366889
# CD_Account            0.316355
# Mortgage              0.142095
# Education             0.136722
# Family                0.061367
# Securities_Account    0.021954

# 4. How does a customer's interest in purchasing a loan vary with their age?
# Age 30-60 apply PLs , outside that window low likelihood.
df_count_age=df.groupby(["Age"])["Personal_Loan"].count()
sns.scatterplot(df_count_age)

# 5. How does a customer's interest in purchasing a loan vary with their education?
# 1: Undergrad; 2: Graduate;3: Advanced/Professional, 1 has higher population among Loan applicants.

df_count_education=df.groupby(["Education"])["Personal_Loan"].count()
print(df_count_education)

# missing values

missing_indices=np.where(pd.isnull(df))
missing_values=[df.iloc[i,j] for i,j in zip(*missing_indices)]

# Logistic Regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

X = df.drop(columns=['Personal_Loan'])
y = df['Personal_Loan']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scalar=StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

model=LogisticRegression(penalty='l2',solver='lbfgs')

model.fit(X_train_scaled, y_train)
y_pred=model.predict(X_test_scaled)

#Evaluate its performance on the testing data using metrics like accuracy, precision, recall, and F1-score.
print(classification_report(y_test,y_pred))

cm=confusion_matrix(y_test,y_pred)
conf_matrix=pd.DataFrame(data=cm,columns=['Predicted:0','Predicted:1'],index=['Actual:0','Actual:1'])
plt.figure(figsize = (8,5))
sns.heatmap(conf_matrix, annot=True,fmt='d',cmap="YlGnBu");

TN=cm[0,0]
TP=cm[1,1]
FN=cm[1,0]
FP=cm[0,1]
sensitivity=TP/float(TP+FN)
specificity=TN/float(TN+FP)

print('The accuracy of the model = TP+TN/(TP+TN+FP+FN) =       ',(TP+TN)/float(TP+TN+FP+FN),'\n',

'The Mis-Classification = 1-Accuracy =                  ',1-((TP+TN)/float(TP+TN+FP+FN)),'\n',

'Sensitivity or True Positive Rate = TP/(TP+FN) =       ',TP/float(TP+FN),'\n',

'Specificity or True Negative Rate = TN/(TN+FP) =       ',TN/float(TN+FP),'\n',

'Positive Predictive value = TP/(TP+FP) =               ',TP/float(TP+FP),'\n',

'Negative predictive Value = TN/(TN+FN) =               ',TN/float(TN+FN),'\n',

'Positive Likelihood Ratio = Sensitivity/(1-Specificity) = ',sensitivity/(1-specificity),'\n',

'Negative likelihood Ratio = (1-Sensitivity)/Specificity = ',(1-sensitivity)/specificity)


y_pred_prob=model.predict_proba(X_test_scaled)[:,:]
y_pred_prob_df=pd.DataFrame(data=y_pred_prob, columns=['Prob to Apply for Loan(1)','Prob of Not(0)'])
y_pred_prob_df.head()