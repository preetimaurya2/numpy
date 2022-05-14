#!/usr/bin/env python
# coding: utf-8

# In[ ]:


37.Create random vector of size 10 and replace the maximum value by 0 


# In[1]:


import numpy as np

a=np.random.randint(1,10,10)
print(a)
a[a.argmax()]=0
print(a)

