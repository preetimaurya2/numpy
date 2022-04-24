#!/usr/bin/env python
# coding: utf-8

# In[ ]:


22. Given a 1D array, negate all elements which are between 3 and 8, in place.


# In[6]:


import numpy as np
a=np.arange(11)
b=np.arange(4,8)
c=np.delete(a,b)
print(c)

