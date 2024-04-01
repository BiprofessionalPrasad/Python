# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:23:30 2024

@author: 9387758
"""
'''
Multiple Time chart for supervisors using catplot barplot
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

All = pd.read_csv(r'C:\Users\9387758\Downloads\SupsData.csv')
# To leverage the use of seaborn's FacetGrid (which is used by catplot) you need to transform you dataframe from "wide" to "long"
All2 = All.melt(id_vars=['Supervisor'], var_name='features')

# Apply the default theme
sns.set_theme()
All2['color'] = 'y'

# Create a visualization
my_plot=sns.catplot(
    data=All2, 
    kind="bar",
    x="value",
    y="Supervisor",
    col="features",
    #col_wrap=5,
    hue="color",
    palette="dark",
    height=10, aspect=.3
)

