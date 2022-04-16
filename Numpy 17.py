#!/usr/bin/env python
# coding: utf-8

# In[ ]:


17. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? 


# In[2]:


import numpy as np
a=np.unravel_index(99,(6,7,8))
print(a)

