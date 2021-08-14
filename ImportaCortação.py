#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# vamos pegar cotação do Indice e de Petrobras

#indice
df = web.DataReader('^BVSP', data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
print(df)


# In[ ]:




