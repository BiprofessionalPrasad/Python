# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:46:27 2024

@author: Prasad
"""

import pandas as pd
import numpy as np

# Generate example data (replace with your actual data)
np.random.seed(42)
transaction_amounts = np.random.normal(loc=100, scale=20, size=1000)

# Create a DataFrame
df = pd.DataFrame({'TransactionAmount': transaction_amounts})

# Calculate quartiles and IQR
Q1 = df['TransactionAmount'].quantile(0.25)
Q3 = df['TransactionAmount'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier thresholds
lower_threshold = Q1 - 1.5 * IQR
upper_threshold = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df['TransactionAmount'] < lower_threshold) | (df['TransactionAmount'] > upper_threshold)]

print("Detected outliers:")
print(outliers)
