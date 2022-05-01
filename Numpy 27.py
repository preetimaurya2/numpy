#!/usr/bin/env python
# coding: utf-8

# In[ ]:


27. How to get all the dates corresponding to the month of July 2016? 


# In[2]:


import numpy as np

a=np.arange('2016-07','2016-08',dtype='datetime64[D]')
print(a)

