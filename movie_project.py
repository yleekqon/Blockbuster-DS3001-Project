#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:22:35 2018

@author: khuyencao1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


df = pd.read_csv('movie_metadata.csv')
print df.isnull().sum().sort_values()
df.isnull().sum().sort_values().plot.bar()

missingValueColumns = df.columns[df.isnull().any()].tolist()
#msno.bar(df[missingValueColumns],\
            #figsize=(20,8),color="#34495e",fontsize=12,labels=True,)
msno.matrix(df[missingValueColumns],width_ratios=(10,1),\
            figsize=(20,8),color=(0,0, 0),fontsize=12,sparkline=True,labels=True)