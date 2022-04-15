#!/usr/bin/env python
# coding: utf-8

# In[ ]:


16. Create a 8x8 matrix and fill it with a checkerboard pattern 


# In[1]:


import numpy as np
a=np.zeros((8,8))
a[::2,::2]=1
a[1::2,1::2]=1
print(a)

