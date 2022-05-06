#!/usr/bin/env python
# coding: utf-8

# In[ ]:


31.  Create a vector of size 10 with values ranging from 0 to 1, both excluded


# In[1]:


import numpy as np

a=np.linspace(0,1,11,endpoint=False)[1:]
print(a)

