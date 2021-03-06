#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt 
dataset.plot(kind='scatter', x='Adj Close', y='Volume')
plt.show()

import matplotlib.pyplot as plt 
dataset.plot(kind='bar',x='Adj Close',y='Volume') 
plt.show()

import matplotlib.pyplot as plt 
ax = plt.gca() 
dataset.plot(kind='line',x='Adj Close',y='Volume',ax=ax) 
dataset.plot(kind='line',x='Adj Close',y='Volume', color='red', ax=ax) 
plt.show() 

import matplotlib.pyplot as plt 
ax = plt.gca() 
dataset.plot(kind='line',x='High',y='Low',ax=ax) 
dataset.plot(kind='line',x='High',y='Low', color='blue', ax=ax) 
plt.show() 

