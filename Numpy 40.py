#!/usr/bin/env python
# coding: utf-8

# In[ ]:


40. How to convert a float (32 bits) array into an integer (32 bits) in place


# In[3]:


import numpy as np

a=np.array([1.,2.,3.,4.,5.,9.,6.,7.,8.],dtype=np.int32)
print(a.dtype)

