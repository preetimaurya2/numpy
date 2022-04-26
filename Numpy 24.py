#!/usr/bin/env python
# coding: utf-8

# In[ ]:


24. How to find common values between two arrays? 


# In[2]:


import numpy as np
a=np.random.randint(0,10,10)
b=np.random.randint(0,10,10)
print(a)
print(b)
c=np.intersect1d(a,b)
print(c)

