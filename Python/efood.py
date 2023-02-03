# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:15:39 2023

@author: Notis
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import collections
import plotly.express as px
from sklearn import preprocessing

data = pd.read_csv('orders.csv')
data1 = pd.read_csv('orders.csv')

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
Next, i will create some metrics which will help me to better understand users
"""

#total orders per user
data['total_orders'] = data.groupby('user_id')['user_id'].transform('count')

#total orders splitted to break/non break orders
data['total_break_orders'] = (data.assign(user_id = data['user_id'].where(data['cuisine'] == 'Breakfast'))
                          .groupby('user_id')['user_id']
                          .transform('count'))

data['total_break_orders'] = data.groupby(['user_id'])['total_break_orders'].ffill()


data=data.fillna(0)

data['total_non_break_orders'] = data['total_orders'] - data['total_break_orders']


#avg amount per order, break & non-break
data['avg_tot_amount'] = data.groupby(['user_id'])['amount'].transform('mean')

data['avg_break_amount'] = (data.assign(user_id = data['user_id'].where(data['cuisine'] == 'Breakfast'))
                          .groupby('user_id')['amount']
                          .transform('mean'))

data['avg_break_amount'] = data.groupby(['user_id'])['avg_break_amount'].ffill()
data['avg_break_amount'] = data.groupby(['user_id'])['avg_break_amount'].bfill()


data['avg_non_break_amount'] = (data.assign(user_id = data['user_id'].where(data['cuisine'] != 'Breakfast'))
                          .groupby('user_id')['amount']
                          .transform('mean'))

data['avg_non_break_amount'] = data.groupby(['user_id'])['avg_non_break_amount'].ffill()
data['avg_non_break_amount'] = data.groupby(['user_id'])['avg_non_break_amount'].bfill()

data=data.fillna(0)


###Drop duplicated users
data.drop_duplicates(subset='user_id', inplace=True)


###### metrics on users

#Share of users with more than 10 breakfast orders
str(round((len(data[data.total_break_orders > 1]) / len(data))*100,2))+"%"

str(round((len(data[(data.total_break_orders > 5) & (data.total_non_break_orders > 10)]) / len(data))*100,2))+"%"

share1=[round((len(data[data.total_break_orders > i]) / len(data))*100,2) for i in range(0,20)]

share2=[round((len(data[(data.total_break_orders > 0) & (data.total_non_break_orders > i)]) / len(data))*100,2) for i in range(0,20)]

##### PLOTS
##### correlations 

ax = sns.lmplot(x="total_break_orders", y="total_non_break_orders", data=data)
ax.set(xlabel='Total breakfast orders', ylabel='Total Non-Breakfast orders', title='Breakfast / Non-Breakfast Correlation')
plt.show()




len(data[data.total_break_orders!=0])
len(data[data.total_break_orders==0])



### PIE CHARTS

labels = list(data1.cuisine.unique())
sizes = list(collections.Counter(data1.cuisine).values())
explode = (0.1, 0, 0, 0)
#add colors
colors = ['olivedrab','darkviolet','tomato','beige']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.title("Cuisine share across all orders")
plt.show()

#######################


labels = ['Breakfast','Non-breakfast']
sizes = [len(data[data.total_break_orders!=0]), len(data[data.total_break_orders==0])]

explode = (0.1, 0)
#add colors
colors = ['olivedrab','tomato']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.title("Breakfast / Non-breakfast users")

plt.show()

### Histogram plots 

plt.hist(data.total_break_orders, density=True, bins=150)
plt.xlim([0, 30])
plt.title("Total Breakfast orders' Density")
plt.show() 


plt.hist(data.total_non_break_orders, density=True, bins=50)
plt.xlim([0, 30])
plt.title("Total Non-Breakfast orders' Density")
plt.show() 


plt.hist(data.avg_break_amount, density=True, bins=150)
plt.xlim([0, 20])
plt.title("Average Breakfast amount Density")
plt.show() 


plt.hist(data.avg_non_break_amount, density=True, bins=150)
plt.xlim([0, 50])
plt.title("Average Non-Breakfast amount Density")
plt.show() 

#### line plots

plt.plot(range(0,20),share1)
plt.title("Breakfast users over number of Breakfast orders")
plt.xlabel("Breakfast orders")
plt.ylabel("Users' Share")
plt.show()



plt.plot(range(0,20),share2)
plt.title("Breakfast users over number of Non-Breakfast orders")
plt.xlabel("Non-Breakfast orders")
plt.ylabel("Users' Share")
plt.show()


