# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:08:36 2024

@author: 9387758
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(r'C:\Users\9387758\OneDrive - MyFedEx\Documents\Python')

df_orig = pd.read_csv('foodhub_order.csv')
df=df_orig
sns.set_theme(style="dark")

'''sns.relplot(df,
                x='cost_of_the_order',
                y='delivery_time',
                col='day_of_the_week',
                size='cost_of_the_order',
                sizes=(20, 200), 
                hue='cuisine_type'
                )'''

#Q7. df.value_counts("restaurant_name", ascending=False)[:5]
#Q8. df.loc[df['day_of_the_week']=='Weekend'].value_counts("cuisine_type", ascending=False)[:1].index.tolist()[0]
#Q9. 100.00*len(df.loc[df['cost_of_the_order']>20].value_counts("order_id").index)/len(df.index)
#Q10. df['delivery_time'].mean(axis=0,numeric_only=True)
#Q11. df.value_counts('customer_id',ascending=False)[:3]
# df.value_counts("restaurant_name", ascending=False)[:5]
# df.loc[df['day_of_the_week']=='Weekend'].value_counts("cuisine_type", ascending=False)[:1].index.tolist()[0]
# 100.00*len(df.loc[df['cost_of_the_order']>20].value_counts("order_id").index)/len(df.index)
# df['delivery_time'].mean(axis=0,numeric_only=True)
# df.value_counts('customer_id',ascending=False)[:3]
#13# 
'''
cond1=df['cost_of_the_order']>20
cond2=df['cost_of_the_order']<=20 
cond3=df['cost_of_the_order']>5
cond4=df['cost_of_the_order']<=5

A=df[cond1]['cost_of_the_order'].sum()*1.25
B=df[cond2 & cond3]['cost_of_the_order'].sum()*1.15
C=df[cond4]['cost_of_the_order'].sum()*1.00

A+B+C
'''

'''
def factor(cost_of_the_order):
    if cost_of_the_order>20:
        return(cost_of_the_order*1.25)
    elif cost_of_the_order>5:
        return(cost_of_the_order*1.15)
    else:
        return(cost_of_the_order*1.00)
    
df['cost_of_the_order'].apply(factor).sum()
'''
    
#15# df['total_time_deliver_food']=df['food_preparation_time']+df['delivery_time']
#    100*df[df['total_time_deliver_food']>60]['order_id'].count()/df['order_id'].count()
#16# 
# df[df['day_of_the_week']=='Weekend']['delivery_time'].mean()
# df[df['day_of_the_week']=='Weekday']['delivery_time'].mean()

