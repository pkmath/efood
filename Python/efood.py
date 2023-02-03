# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:15:39 2023

@author: Notis
"""

import os
import pandas as pd
import numpy as np


os.chdir('C:\\Users\\Notis\\Desktop\\efood2023')
data = pd.read_csv('orders.csv')
data.duplicated().sum()

pd.DataFrame([{'users': len(data['user_id'].unique()),    
               'cities': len(data['city'].unique()),
               'cuisine': len(data['cuisine'].unique()),  
              }], columns = ['users', 'cities', 'cuisine'], index = ['quantity'])

"""
There are 121943 unique users across 46 citites and 4 different cuisine types.
Total number of orders is 534,270 with no duplicates
"""

"""
Next, i will create some metrics which will help me to better understand users' segmentation'
"""

data['total_orders']= np.nan  #total orders per user

data['total_orders']= [len(data[data['user_id']==i]) for i in data.user_id[0:10]]

