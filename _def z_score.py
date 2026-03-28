# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:59:57 2021

@author: pgaiton
"""

import pandas as pd

def z_score(df: pd.DataFrame):
    close_mean = df['close'].mean()
    close_std = df['close'].std(ddof=0)
    df['zscore'] = df['close'].apply(lambda close: (close - close_mean) / close_std)
    
    