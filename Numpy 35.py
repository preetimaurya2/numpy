#!/usr/bin/env python
# coding: utf-8

# In[ ]:


35. Make an array immutable (read-only)


# In[1]:


import numpy as np

a=np.zeros(10)
a.flags.writeable=False
a[0]=1
print(a)

