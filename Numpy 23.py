#!/usr/bin/env python
# coding: utf-8

# In[ ]:


23. How to round away from zero a float array ? 


# In[1]:


import numpy as np
a=np.random.uniform(-10,10,10)
print(a)
c=np.copysign(np.ceil(np.abs(a)),a)
print(c)

