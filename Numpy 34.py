#!/usr/bin/env python
# coding: utf-8

# In[ ]:


34. Consider two random array A and B, check if they are equal


# In[1]:


import numpy as np

a=np.random.randint(1,10,10)
b=np.random.randint(1,10,10)
np.allclose(a,b)

